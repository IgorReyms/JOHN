from fastapi import FastAPI, Request



from core.api.Validation import work, Ticket_task
from core.api.Rule import Rule
from core.api.Connector import Connector
from core.api.Ticket import Ticket
from core.api.Problem import Problem
class Gear:

    def __init__(self, response, endpoint):
        self.response_valid = work(response,endpoint)
        self.Ticket = Ticket()
        self.Problem = Problem()
        rule = Rule(self.response_valid, self.Ticket, self.Problem)
        Connector(rule,endpoint)

    def separator(self):

        pass