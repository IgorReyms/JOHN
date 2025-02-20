from pydoc import classify_class_attrs

from core.api.Ticket import Ticket
from core.api.Problem import Problem
from core.api.Validation import work
#from core.api.Gear import Gear


class Update:

    def __init__(self):
        pass

class Add:

    def __init__(self):
        pass

class Rule:

    def __init__(self,response_valid:work,Ticket: Ticket,Problem: Problem):
        self.Ticket = Ticket
        self.Problem = Problem
        self.__config(response_valid)


    def __config(self,response_valid):
        self.rule_number = response_valid.response.tasks.category
        method_name = f"{self.rule_number}"  # Формируем имя метода
        print(method_name)
        try:
            method_to_call = getattr(self, method_name)
            method_to_call(response_valid)
        except AttributeError:
            print(f"Error: Task method '{method_name}' not found.")
            # Или можно вызвать метод по умолчанию, поднять исключение, и т.д.
        if response_valid.response.type == 'ticket':
            self.Ticket.id = int(response_valid.response.ticket_id)

    def Task_1(self,response_valid):
        self.Object.Ticket_User.type = 2
        self.Object.Ticket_User.users_id = 38 # Тех.под.юр
        self.Object.itilcategories_id = 3 # Директум/Диадок

    def Task_2(self,response_valid):
        #self.Object.content = f'Здарова! Сделал {self.rule_number}'
        self.Object.status = 1 # Новая
        self.Object.content = ''
        user = response_valid.response.tasks.user
        ## Надо сделать перевод юзера в его ID. Прилетает User: str, А надо user: int
        if user == 'John':
            fuck = 184
        print(fuck)
        self.Problem.Problem_User.users_id = fuck
        print(self.Problem.Problem_User.users_id)
        self.Problem.Problem_User.type = 2
        print('Дошёл до таска 2 в руле')

        pass
