import requests
from bs4 import BeautifulSoup

# Log in to the website
try:
    session = requests.Session()
    login_data = {
        'username': 'a.joseph.192@westcliff.edu',
        'password': '$DMiS.qm&yY=Z3C'
    }
    response = session.post('https://example.com/login', data=login_data)

    if response.status_code != 200:
        raise Exception('Login failed. Check login credentials.')
except Exception as e:
    print(f'Error during login: {e}')
    exit(1)

# Scrape the website for video links
url = 'https://members.codewithmosh.com/courses/enrolled/240431'
response = session.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
video_links = []

for link in soup.find_all('a'):
    href = link.get('href')
    if href.endswith('.mp4'):
        video_links.append(href)

# Download the videos
for link in video_links:
    try:
        response = requests.get(link, stream=True)

        if response.headers['Content-Type'] != 'video/mp4':
            continue

        total_size = int(response.headers['Content-Length'])
        downloaded_size = 0

        with open(link.split('/')[-1], 'wb') as f:
            for chunk in response.iter_content(chunk_size=1024):
                downloaded_size += len(chunk)
                f.write(chunk)

                progress = int(downloaded_size / total_size * 100)
                print(f'Downloading {link} - {progress}% complete')

    except Exception as e:
        print(f'Error downloading video {link}: {e}')
