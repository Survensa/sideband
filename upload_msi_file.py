import os
import requests

# get the access token
token = '<access_token>'

# get the last modified msi file
files = os.listdir('path/to/directory/')
msi_files = [f for f in files if f.endswith('.msi')]
last_modified_file = max(msi_files, key=os.path.getctime)

# set the file name and path
file_name = last_modified_file
file_path = 'path/to/{}'.format(file_name)

# set the upload endpoint URL
upload_endpoint = 'URL'

# set the headers
headers = {
    'Authorization': 'Bearer {}'.format(token),
    'Content-Type': 'application/octet-stream'
}

# read the file content
with open(file_path, 'rb') as f:
    content = f.read()

# make the upload request
response = requests.put(upload_endpoint, data=content, headers=headers)

# check the response
if response.status_code == 200:
    print('File successfully uploaded!')
else:
    print('There was an error uploading the file: {}'.format(response.text))
