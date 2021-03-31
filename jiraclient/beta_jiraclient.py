import requests
from requests.auth import HTTPBasicAuth


class BetaJiraClient():

    def __init__(self, base_url, user, api_token, api_version=2):
        """ Instantiate an instance

        base_url    <str>: jira base url (example: 'https://example.atlassian.net/')
        username    <str>: email address
        api_token   <str>: user's api token from jira 
                        (https://id.atlassian.com/manage-profile/security/api-tokens)
        """
        self.base_url = '{}/rest/api/{}/'.format(base_url, api_version)
        self.auth = HTTPBasicAuth(user, api_token)
        self.try_connection()
        pass

    def try_connection(self):
        test_url = '{}project'.format(self.base_url)
        req = requests.get(test_url, auth=self.auth)
        if req.status_code != 200:
            print("Unable to connect: {}".format(req.status_code))
        else:
            self.conn = requests.Session()
            self.conn.auth = self.auth

    def get_all_projects(self):
        """ Retrieve all projects 
        
        return:
            <list>: of <dict> about the project and its metadata 
        """
        projects = self.conn.get('{}project'.format(self.base_url))
        return projects.json()
