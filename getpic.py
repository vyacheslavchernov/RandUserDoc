import vk_api
import requests
import time
import os
import sys
import random 

phone = ''
password = ''

vk_session = vk_api.VkApi(phone, password)
vk_session.auth()
vk = vk_session.get_api()

search_type = ".jpg"
search = vk.docs.search(q=search_type, count= 1000)

rnd = random.randint(0, len(search['items'])-1)
dir = "vk_photos\\"

photo = search["items"][rnd]

photo_title = "id"+str(photo["owner_id"])+"_"+str(photo["id"])+"-"+str(time.time())
r = requests.get(photo["url"])
        
file_name = ""
file_name = dir+photo_title
file_name = file_name.replace(' ', '_')

with open(file_name, "wb") as code:
        code.write(r.content)
        code.close()

print(file_name)
    
