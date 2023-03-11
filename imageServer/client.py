import requests
host =  'localhost:8000'
url=f'http://{host}/processData'
mp3_f = open('C:/Users/Wasay Rizwani/Desktop/Video Integration/test.mp4', 'rb')
files = {'videoFile': mp3_f,
         'id':'userWasay',
         'session_id':20}

req = requests.post(url, files=files)
print (req.status_code)
print (req.content)