# jira_python3_wrapper
A simple wrapper class for jira API

### How to install using ssh

1) Make sure you have ssh setup in github

2) Run pip3

`pip3 install git+ssh://git@github.com/adrielt07/jira_python3_wrapper.git`

### Quick Test and how to use
Run python3 terminal

```
>>> from jiraclient import JiraClient
>>> dir(JiraClient)
['__class__', ... 'get_ticket_summary', 'new_issue']
```

Tested on:

Mac 10.13.6
raspberry pi 4.19.97
Python3.8
