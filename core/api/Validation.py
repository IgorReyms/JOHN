from pydantic import BaseModel, ValidationError
from datetime import datetime
import re, json
from uuid import uuid4

class Task(BaseModel):
    date: datetime
    author: str
    description: str
    category: str

class Ticket_task(BaseModel):
    type: str
    id: str
    ticket_id: str
    time: datetime
    category: str
    tasks: Task

class Problem_task(BaseModel):
    type: str
    id: str
    problem_id: str
    tasks: Task

class work:
    def __init__(self,response,endpoint):
        message = self.__decode_glpi_message(response)
        print(message)
        tasks = self.__parse_glpi_message(message,endpoint)
        try:
            if endpoint == 'ticket':
                self.response_valid = Ticket_task(**tasks)
            if endpoint == 'problem':
                self.response_valid = Problem_task(**tasks)
            print(self.response_valid)
        except ValueError as error:
            print(error.json())

    def __decode_glpi_message(self,encoded_message):
        try:
            decoded_message = encoded_message.decode('utf-8')
            return decoded_message
        except UnicodeDecodeError as e:
            print(f"Ошибка декодирования UTF-8: {e}")
            return None

    def __parse_glpi_message(self,decoded_message,endpoint):
        try:
            # Извлекаем номер заявки
            id_match = re.search(r'ID (\d+)', decoded_message)
            if not id_match:
                print("Не удалось извлечь ID заявки.")
                return None
            ticket_id = id_match.group(1)

            # Извлекаем время до решения
            time_to_resolve = re.search(r'Время до решения ([\d\-: ]+)', decoded_message)
            if not time_to_resolve:
                print("Не удалось извлечь время до решения.")
                time_to_resolve = None
            else:
                due_date_str = time_to_resolve.group(1).strip()
                try:
                    time_to_resolve = datetime.strptime(due_date_str, '%Y-%m-%d %H:%M')
                except ValueError:
                    print(f"Неправильный формат даты: {due_date_str}")
                    time_to_resolve = None
            # Извлекаем категорию тикета
            category_match = re.search(r'Категория:(.*)', decoded_message)  # Захватываем значение
            if not category_match:
                print("Не удалось извлечь категорию.")
                ticket_category = None
            else:
                ticket_category = category_match.group(1).strip()  # Получаем значение категории

            # Находим начало описания первой задачи (предполагаем, что задачи идут после категории)
            task_start_match = re.search(r"\[\d{4}-\d{2}-\d{2} \d{2}:\d{2}\]", decoded_message)  # Ищем начало задачи
            if not task_start_match:
                print("Не найдено начало задач.")
                task_records_str = ""
            else:

                # Извлекаем записи задач, начиная с места, где начинается первая задача
                task_records_str = decoded_message[task_start_match.start():].strip()

            # Разделяем записи задач. Используем более простое разделение.
            task_records = re.split(r'\n\n\n', task_records_str)
            tasks = []
            for record in task_records:
                if not record.strip():
                    continue

                task = {}
                lines = record.splitlines()

                task['date'] = lines[0].strip().replace('[', '').replace(']', '') if len(lines) > 0 else None

                author_line = next((line for line in lines if "Автор" in line), None)
                task['author'] = author_line.split('Автор')[1].strip() if author_line else None

                description_line = next((line for line in lines if "Описание" in line), None)
                task['description'] = description_line.split('<p>')[1].split('</p>')[0].replace('Описание',
                                                                                                '').strip() if description_line else None

                category_line = next((line for line in lines if "Категория" in line), None)
                task['category'] = category_line.split('Категория')[1].strip() if category_line else None
                tasks.append(task)

            result = {
                'type': endpoint,
                'id': str(uuid4()),
                f'{endpoint}_id': ticket_id,
                'time': time_to_resolve,
                'category': ticket_category,
                'tasks': tasks[-1]
            }
        except Exception as e:
            print(f"Ошибка при разборе сообщения: {e}")
            return None
        return result

    def __to_json(self,data):
        try:
            json_string = json.dumps(data, indent=5, ensure_ascii=False)  # indent для читаемости
            return json_string
        except Exception as e:
            print(f"Ошибка при создании JSON: {e}")
            return None