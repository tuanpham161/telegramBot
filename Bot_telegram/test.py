import requests
import pprint
from virustotal_python import Virustotal
import json

proxy = { 'https':'https://10.57.10.34:3128'}

hash="47c5bdd321376806fe88956b81d48fb3cb4429423862d34ebe03f022e1a5c5db"
url = 'https://www.virustotal.com/gui/file/file/behaviour/47c5bdd321376806fe88956b81d48fb3cb4429423862d34ebe03f022e1a5c5db"/detection'

# response=requests.get(url,proxies=proxy)
# response.raise_for_status()
# print(response.json())



vtotal = Virustotal(
    API_KEY="09744d1da7500cdda4087790c576309aef2a2a3e54a43fe9aba5758d646546a3",
    API_VERSION="v3",
    PROXIES={'https':'http://10.57.10.34:3128'},
    TIMEOUT=5.0)



hash="54f6bd17b04a946eaf0620a7833e9a0f9f42d797330d0d4d6c84d01d827a1b43"
response=vtotal.request(f"files/{hash}")
y=json.dumps(response.data,indent=4, sort_keys=True)
print(y)