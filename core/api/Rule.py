
from core.api.Ticket import Ticket
from core.api.Validation import work

class Rule:

    def __init__(self,response_valid:work):
        self.__BR_1(response_valid)

    def __BR_1(self,response_valid):
        self.type = 'ticketfollowup'
        self.user_id = 184
        self.ticket_id = int(response_valid.response_valid.ticket_id)
        print(self.ticket_id)
        pass