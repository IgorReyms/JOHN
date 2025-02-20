import requests
from glpi_api import GLPI, GLPIError, _glpi_error, _unknown_error
import glpi_api
from core.api.Rule import Rule
from core.api.Ticket import FirstAccessDescriptor_Ticket
from core.api.Ticket_User import FirstAccessDescriptor_Ticket_User
from core.api.Problem import FirstAccessDescriptor_Problem
from core.api.Problem_User import FirstAccessDescriptor_Problem_User

from logging import Logger
class GLPICustom(GLPI):

    def _init_session(self, apptoken, auth, use_headers=True):

        from base64 import b64encode
        self.session = requests.Session()
        self.session.verify = False
        init_headers = {
            'Content-Type': 'application/json',
            'App-Token': apptoken
        }
        params = {}

        if isinstance(auth, (list, tuple)):
            if len(auth) > 2:
                raise GLPIError("invalid 'auth' parameter (should contains "
                                'username and password)')
            if use_headers:
                authorization = 'Basic {:s}'.format(b64encode(':'.join(auth).encode()).decode())
                init_headers.update(Authorization=authorization)
            else:
                params.update(login=auth[0], password=auth[1])
        else:
            if use_headers:
                init_headers.update(Authorization='user_token {:s}'.format(auth))
            else:
                params.update(user_token=auth)

        response = self.session.get(url=self._set_method('initSession'),
                                    headers=init_headers,
                                    params=params)

        return {
            200: lambda r: r.json()['session_token'],
            400: _glpi_error,
            401: _glpi_error
        }.get(response.status_code, _unknown_error)(response)

class Connector:
    def __init__(self,Rule,endpopint):
        self.endpopint = endpopint
        self.glpi_url = "https://raccoon.npss.loc/helpdesk/apirest.php"
        self.api_token = "ayn83esajCpe0ii31l7gcETlgTEHGoGpwdrPSPJl"
        self.user_token = "Jnn8ZslaVYDS0HIcCmko6uNpWwa2UCHmAy4jJsA1"
        self.config(Rule)
        #self.__add_JOHN(1)

    def config(self,Rule):
        if self.endpopint == 'ticket':
            self.slovarik = FirstAccessDescriptor_Ticket.Ticket_body
            self.slovarik_User = FirstAccessDescriptor_Ticket_User.Ticket_User_body
        if self.endpopint == 'problem':
            self.slovarik = FirstAccessDescriptor_Problem.Problem_body
            self.slovarik_User = FirstAccessDescriptor_Problem_User.Problem_User_body
        method_name = f"work_{Rule.rule_number}"  # Формируем имя метода
        try:
            method_to_call = getattr(self, method_name)
            method_to_call(Rule)
        except AttributeError:
            print(f"Error: Task method '{method_name}' not found.")
            # Или можно вызвать метод по умолчанию, поднять исключение, и т.д.

    def work_Task_1(self, Rule):
        glp = GLPICustom(self.glpi_url, self.api_token, self.user_token)
        response_api_get = glp.get_sub_items('Ticket',Rule.Object.id,'Ticket_User')
        Separator_API(Rule,endpoint = self.endpopint,type_glpi= 'get_sub_items',response = response_api_get)
        glp.update_sub_items('Ticket', Rule.Object.id, 'Ticket_User',self.slovarik_User)
        glp.update('Ticket',self.slovarik)
        Rule.Object.content = f'Здарова! Сделал {Rule.rule_number}'
        glp.add('ITILFollowup',{'itemtype':'Ticket','items_id': Rule.Object.id,'content': Rule.Object.content,"users_id": 184})
        return print(f'Доставлено! Выполнена {Rule.rule_number}')

    def work_Task_2(self,Rule):
        glp = GLPICustom(self.glpi_url, self.api_token, self.user_token)
        response_api_get = glp.get_item('Ticket',Rule.Object.id)
        Separator_API(Rule,endpoint = self.endpopint,type_glpi= 'get_item',response= response_api_get)
        response = glp.add('Problem',self.slovarik)
        Separator_API(Rule, endpoint=self.endpopint, type_glpi='add', response=response)
        glp.add_sub_items('Problem',Rule.Object.id,'Problem_User',{'problems_id':Rule.Object.id,'type':Rule.Object.Problem_User.type,'users_id':Rule.Object.Problem_User.users_id})
        print('До сюда дошёл, бля ура')

    def __add_JOHN(self,Rule):
        glp = GLPICustom(self.glpi_url, self.api_token, self.user_token)
        #response = glp.add('Problem',{'content':'Say Hello BANANAS','status':1,'name': 'Просто говнище','itilcategories_id': 2,'time_to_resolve':'2025-02-14 13:02'})
        #response = glp.add('ITILFollowup',{'itemtype':'Problem','items_id': 12,'content': 'fucking she'})
        #response = glp.add_sub_items('Problem', 15,'Problem_User',{'problems_id':15,'type':2,'users_id': 184})
        #response = glp.update('Problem', {'id': 15, 'name': 'Просто говнище','itilcategories_id': 2,'time_to_resolve':'2025-02-14 13:02'})

        #response = glp.update('Ticket',3777,{'id':3777,'status':3})

        response = glp.get_sub_items('Problem',12,'Problem_User')

        #response = glp.get_item('Problem',18)
        #response = glp.add_sub_items("Ticket", 607, "TicketValidation",{"id": 61, "users_id": 61, 'tickets_id': 607, "status": 2})

        #response = glp.add("TicketFollowup",{"tickets_id": 607, "users_id": 2, "content": "fucking shet", "is_private": 0, "status": 2})
        print(response)


class Separator_API:
    def __init__(self,Rule,endpoint,type_glpi,response):
        self.response = response
        self.config(Rule,endpoint,type_glpi)

    def config(self,Rule,endpoint,type_glpi):
        method_name = f"separator_{endpoint}_{type_glpi}"  # Формируем имя метода
        try:
            method_to_call = getattr(self, method_name)
            method_to_call(Rule,self.response)
        except AttributeError:
            print(f"Error: Task method '{method_name}' not found.")
            # Или можно вызвать метод по умолчанию, поднять исключение, и т.д.

    def separator_ticket_get_sub_items(self,Rule,response):
        for item in response:
            if item['type'] == Rule.Object.Ticket_User.type:
                Rule.Object.Ticket_User.id = (item['id'])

    def separator_ticket_get_item(self,Rule,response):
        for item in response:
            Rule.Problem.name = item['name']
            Rule.Problem.content = item['content']
            Rule.Problem.itilcategories_id = item['itilcategories_id']
            Rule.Problem.time_to_resolve = item['time_to_resolve']

    def separator_ticket_add(self,Rule,response):
        for item in response:
            Rule.Problem.id = item['id']





#a = Connector(1,1)