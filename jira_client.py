#!/usr/bin/env python3

import os

from jira import JIRA

class JiraClient():
    def __init__(self, endpoint, user, api):
        self.endpoint = endpoint
        self.options = {'server':self.endpoint}
        self.user = user
        self._api = api
        self.conn = JIRA(self.options, basic_auth=(self.user, self._api))

    def get_ticket_summary(self, ticket):
        """
        Retrieve ticket's summary field

        Args:
            ticket <str> - ticket number
        """
        issue = self.conn.issue(ticket)
        return issue.fields.summary

    def __str__(self):
        return ("Endpoint: {} User: {}".format(self.endpoint, self.user))


if __name__ == '__main__':
    api = os.environ['JIRA_API']
    user = os.environ['JIRA_USER']
    endpoint = os.environ['JIRA_ENDPOINT']
    jira = JiraClient(endpoint, user, api)
    ticket = 'CW-24'
    sum = jira.get_ticket_summary(ticket)
    print(sum)
