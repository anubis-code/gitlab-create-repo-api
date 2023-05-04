import json
import requests
import urllib3

with open('./group.json', 'r') as f:
    jfm_dict = json.load(f)

for jfm in jfm_dict:
    print(jfm['path'])
    gitlab_url = "https://testserver/gitlab/api/v4/groups"
    headers = {'Content-type': 'application/json', 'PRIVATE-TOKEN': '<TOKEN>'}
    data = {'name': jfm['path'], 'path': jfm['path'], 'visibility': jfm['visibility']}
    urllib3.disable_warnings()
    r = requests.post(gitlab_url, data=json.dumps(data), headers=headers, verify=False)
    