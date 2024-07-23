import pandas as pd
import requests

token = 'CC585E1F8B3EC9212A45B258CFFD5E9E'
apiUrl = 'https://ncov.medsci.ox.ac.uk/api/'

data = {
    'token': token,
    'content': 'metadata',
    'format': 'json',
    'returnFormat': 'json'
}
r = requests.post(apiUrl,data=data)
print('HTTP Status: ' + str(r.status_code))
db1 = pd.DataFrame(r.json())

data = {
    'token': token,
    'content': 'record',
    'action': 'export',
    'format': 'json',
    'type': 'flat',
    'csvDelimiter': '',
    'rawOrLabel': 'raw',
    'rawOrLabelHeaders': 'raw',
    'exportCheckboxLabel': 'false',
    'exportSurveyFields': 'false',
    'exportDataAccessGroups': 'false',
    'returnFormat': 'json'
}
r = requests.post(apiUrl,data=data)
print('HTTP Status: ' + str(r.status_code))
db2 = pd.DataFrame(r.json())

print(db1)
print(db2)