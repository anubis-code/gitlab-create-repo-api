import json
import requests
import urllib3

with open('./repo.json', 'r') as f:
    jfm_dict = json.load(f)

for jfm in jfm_dict:
    print(jfm['name'])
    gitlab_url = "http://gitlab.example.com:1337/api/v4/projects"
    headers = {'Content-type': 'application/json', 'PRIVATE-TOKEN': '<TOKEN>'}
    data = {'name': jfm['name'], 'namespace_id': jfm['namespace_id'], 'visibility': jfm['visibility']}
    urllib3.disable_warnings()
    r = requests.post(gitlab_url, data=json.dumps(data), headers=headers, verify=False)
    