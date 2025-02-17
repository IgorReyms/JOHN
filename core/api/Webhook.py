import requests
from glpi_api import GLPI, GLPIError, _glpi_error, _unknown_error
import glpi_api

# headers = {
#     'Content-Type': 'application/json',
#     'App-Token': api_token,
#     'Authorization': f"user_token {user_token}"
# }
# params = {"id": 123}
#
# def get_session_token():
#     response = requests.get(f"{glpi_url}/initSession", headers=headers)
#     if response.status_code == 200:
#         return response.json()['session_token']
#     else:
#         raise Exception("Не удалось получить сессионный токен")
class GLPICustom(GLPI):

    def _init_session(self, apptoken, auth, use_headers=True):

        from base64 import b64encode
        self.session = requests.Session()
        self.session.verify = False
        # self.session.cert = ("star_npss.crt", "private.key")
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

class ticket_update:
    def __init__(self):
        self.glpi_url = "https://raccoon.npss.loc/helpdesk/apirest.php"
        self.api_token = "ayn83esajCpe0ii31l7gcETlgTEHGoGpwdrPSPJl"
        self.user_token = "Jnn8ZslaVYDS0HIcCmko6uNpWwa2UCHmAy4jJsA1"
        #self.__session_lol()
        # self.__validation()
        self.zapusk()
    def __session(self):
            glp = GLPICustom(self.glpi_url, self.api_token, self.user_token)



            glp.session = requests.Session()
            glp.session.cert = ("C:/PycharmProject/JOHN/star_npss.crt", "C:/PycharmProject/JOHN/private.key")

            response = glp.add('Ticket', {"name": "john_tester",
                                           "content": "i have no ideas",
                                           "itilcategories_id": 1,
                                           "entities_id": 0,
                                           "type": 2,
                                           "urgency": 3,
                                           "impact": 1,
                                           "priority": 1,
                                           "status": 1,
                                           "users_id_recipient": 144,
                                           })
            print(response)

    def __session_status(self):
        with glpi_api.connect(self.glpi_url, self.api_token, self.user_token) as glpi:
            response = glpi.update("Ticket", {"id": 3714, "status": 4})
            print(response)

    def __session_lol(self):
        glp = GLPICustom(self.glpi_url, self.api_token, self.user_token)
        response = glp.add("TicketFollowup", {"tickets_id": 607, "users_id": 2, "content": "fucking shet","is_private":0, "status": 2})
        print(response)

    def __validation(self):
        glp = GLPICustom(self.glpi_url, self.api_token, self.user_token)
        response = glp.add_sub_items("Ticket",3683,"TicketValidation",{"id":61,"users_id": 1,'tickets_id': 3683,"status": 2})
        print(response)

    def zapusk(self):
        glp = GLPICustom(self.glpi_url, self.api_token, self.user_token)
        response = glp.get_item('TicketFollowup',4587)
        print(response)

    def zapusk2(self):
        glp = GLPICustom(self.glpi_url, self.api_token, self.user_token)
        # glp.update("Ticket", {"id": 3758, "status": 1})
        response = glp.add('QueuedNotification',{
    "itemtype": "Ticket",          # Тип объекта (например, Ticket, Change, Problem и т.д.)
    "items_id": 3713,               # ID объекта (например, ID тикета)
    "notificationtemplates_id": 74, # ID шаблона уведомления
    "entities_id": 0,              # ID сущности (0 для корневой сущности)
    "is_deleted": 0,               # 0 — уведомление активно, 1 — удалено
    "sent_try": 0,                 # Количество попыток отправки (0 для новой очереди)
    "mode": "mail",                # Режим отправки (mail, sms и т.д.)
    "recipient": "ireymers@npssnab.ru", # Получатель (например, email)
    "name": "Test Queued Notification", # Название уведомления
    "body": '&#60;p class=MsoNormal&#62;Добрый день, добавьте, пожалуйста, новых контрагентов (Поставщик) :&#60;/p&#62;', # Текст уведомления
    "headers": "From: no-reply@example.com", # Заголовки (например, для email)
    "create_time": "2023-10-01 12:00:00", # Время создания (необязательно)
    "send_time": "2023-10-01 12:05:00"    # Время отправки (необязательно)
  })
  # #       response = glp.get_item('Notification', 83)
        # response = glp.get_sub_items('Ticket', 3683,'TicketValidation')
        # response = glp.get_item('Ticket', 3758)
        print(response)
