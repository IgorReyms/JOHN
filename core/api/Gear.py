from fastapi import FastAPI, Request



from core.api.Validation import work, Ticket_task
from core.api.Rule import Rule
from core.api.Connector import ticket_update
class Gear:

    def __init__(self, response, endpoint):
        self.response_valid = work(response,endpoint)
        test = Rule(self.response_valid)
        if test.type == 'ticketfollowup':
            ticket_update(test)
        else:
            pass


    def separator(self):

        pass
