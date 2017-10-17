import  requests
from requests.auth import HTTPBasicAuth
url_link="http://35.196.109.69/wp-json/wp/v2/posts/"

data = {'title':'new title', "content": "new content"}
r = requests.post(url_link, data=data, auth=('admin', 'bitnami'))
print (r.status_code)
print (r.headers['content-type'])
print (r.json)
