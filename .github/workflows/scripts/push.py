import json
import os
from base64 import b64encode, b64decode
import requests

new_file = '''# webstore-demo-gitops

This repo demonstrates how an OTS (off-the-shelf) helm chart can be retrieved and pinned to a specific helm sem version from an upstream helm repository, and customized using a custom values.yaml in the private git repository.

More information can be found at <https://github.com/argoproj/argocd-example-apps/tree/master/helm-dependency>

We referenced a chart from [openinsight-proj/openinsight-helm-charts](https://github.com/openinsight-proj/openinsight-helm-charts/tree/main/charts/opentelemetry-demo)，which create an application named `webstore`.

this is a test line， changed by a python script 2 by github'''

headers = {"Content-Type": "application/json", "charset": "UTF-8"}
files_sha ='https://gitee.com/api/v5/repos/Frapschen/webstore-demo-gitops/contents/%2F?access_token=d1bdbe6cd0b2f92b7edd1f0b79e0d937&ref=main'
gitee_token = os.getenv("GITEE_TOKEN")
response = requests.get(files_sha, headers=headers)
print(response.status_code)
m = json.loads(response.text)
for value in m:
    if value['path'] == 'README.md' and value['name'] == 'README.md':
        sha = value['sha']
        break
print(sha)

code = new_file.encode(encoding='utf-8')
code = b64encode(code)
code = bytes.decode(code)
headers = {
    'Content-Type': 'application/json;charset=UTF-8',
}

json_data = {
    'access_token': 'd1bdbe6cd0b2f92b7edd1f0b79e0d937',
    'content': code,
    'sha': sha,
    'message': 'test-api',
    'branch': 'main',
}

response = requests.put(
    'https://gitee.com/api/v5/repos/Frapschen/webstore-demo-gitops/contents/README.md',
    headers=headers,
    json=json_data,
)
print(response.status_code)


