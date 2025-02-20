import requests
from glpi_api import GLPI, GLPIError, _glpi_error, _unknown_error
import glpi_api


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

class ticket_update:
    def __init__(self):
        self.glpi_url = "https://raccoon.npss.loc/helpdesk/apirest.php"
        self.api_token = "ayn83esajCpe0ii31l7gcETlgTEHGoGpwdrPSPJl"
        self.user_token = "Jnn8ZslaVYDS0HIcCmko6uNpWwa2UCHmAy4jJsA1"
        self.__add_JOHN()

    def get_type(self):

        return Rule
        pass

    def __add_JOHN(self):
        glp = GLPICustom(self.glpi_url, self.api_token, self.user_token)
        glp.delete_sub_items
        # response = glp.get_item('Problem', 4)
        #response = glp.add('TicketFollowup',{'rel':'Problem','tickets_id': 607,'content': 'fucking she'})
        # response = glp.get_sub_items('Ticket', 607,'ITILFollowup')
        #response = glp.update('Problem',{'id': 12,"status": 4})
        #response = glp.add_sub_items('Problem',4,'ProblemTask',[{"id": 61, "users_id": 61, 'tickets_id': 4, "status": 1}])
        # response = glp.add_sub_items("Ticket", 607, "TicketValidation",{"id": 61, "users_id": 61, 'tickets_id': 607, "status": 2})


        # response = glp.add_sub_items("Ticket",607,'TicketTask', {"tickets_id": 607, "content": "Followup contents"})
        # response = glp.add_sub_items("Problem",12,'ProblemTask', {"problems_id": 12, "content": "Followup contents", "status": 2})
        # response = glp.add_sub_items("Problem", 12, "ITILFollowup", {"items_id": 12, "itemtype":"Problem","content":"Идинахуй"})

        print(response)

a = ticket_update()