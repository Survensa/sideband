import os
import sched
import time
import requests

# Token used for authentication
token = '<TOKEN>'

# Release URL
url = 'https://api.github.com/repos/graniteriverlabs/SideBand_App/releases/latest'

# Scheduled to run every 10 min
scheduler = sched.scheduler(time.time, time.sleep)


def check_for_releases():
    headers = {
        'Authorization': 'token ' + token,
        'Accept': 'application/vnd.github.v3+json',
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        for asset in data['assets']:
            filename = asset['name']
            if filename.endswith('.msi'):
                if os.path.exists(filename):
                    print("No work to do")
                else:
                    download_url = asset['browser_download_url']
                    r = requests.get(download_url, allow_redirects=True)
                    with open(filename, 'wb') as f:
                        f.write(r.content)
                    print(filename + " downloaded successfully!")
    else:
        print("Failed to get repo data: " + 'response.status_code')


# Schedule the function
scheduler.enter(10, 1, check_for_releases, (scheduler,))
scheduler.run()
