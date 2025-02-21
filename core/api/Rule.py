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

    def __init__(self,response_valid:work, Ticket: Ticket, Problem: Problem):
        self.Ticket = Ticket
        self.Problem = Problem
        self.response_valid = response_valid
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
        if response_valid.response.type == 'problem':
            self.Problem.id = int(response_valid.response.ticket_id)


    def find_users(self):
        user = self.response_valid
        return 184

    def Task_1(self,response_valid):
        self.Ticket.Ticket_User.type = 2
        self.Ticket.Ticket_User.users_id = 38 # Тех.под.юр
        self.Ticket.itilcategories_id = 3 # Директум/Диадок

    def Task_2(self,response_valid):
        self.Problem.status = 1 # Новая
        self.Problem.content = ''
        self.Problem.Problem_User.users_id = self.find_users()
        self.Problem.Problem_User.type = 2
        self.Ticket.Ticket_User.type = 2
        print('Дошёл до таска 2 в руле')

        pass
