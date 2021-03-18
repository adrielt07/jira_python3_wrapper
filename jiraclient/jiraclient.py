#!/usr/bin/env python3

import os

from jira import JIRA

class JiraClient():
    def __init__(self, endpoint, user, apitoken):
        """
        Args:
            endpoint <str>: jira url endpoint
            user     <str>: user account use for authentication
            apitoken <str>: user's API token generated from JiRA
        """
        self.endpoint = endpoint
        self.options = {"server": self.endpoint}
        self.user = user
        self._api = apitoken
        self.conn = JIRA(self.options, basic_auth=(self.user, self._api))


    def get_ticket_summary(self, ticket):
        """
        Retrieve ticket's summary field

        Args:
            ticket <str>: ticket number
        """
        issue = self.conn.issue(ticket)
        return issue.fields.summary


    def new_issue(self, project, summary, description, issuetype):
        """ Creates a new ticket in Jira

        Args:
            project <str>: name of the jira project (Ex. REQ, SRE)
            summary <str>: summary of the ticket
            description <str>: description of what the ticket is about
            issuetype <dict>: the type of issue (Ex. {'name': 'Lead'})

        Return:
            returns a jira ticket object which has more information about
                the ticket, such as the ticket number, assignee, etc.
        """
        new_issue = self.conn.create_issue(
            project=project,
            summary=summary,
            description=description,
            issuetype=issuetype
            )
        return new_issue


    def __str__(self):
        """ Prints the endpoint and user """
        return ("Endpoint: {} User: {}".format(self.endpoint, self.user))
