import requests
from requests.auth import HTTPDigestAuth

from pickJSON import MakeDVRList

from PIL import Image
import numpy as np

print("Running")

dvr_list = MakeDVRList()
print(dvr_list)


def fetching_image(ip_dvr, camera_channel):
    try:
        r = requests.get(f'http://{ip_dvr}/cgi-bin/snapshot.cgi?channel={camera_channel}&type=0', 
                         auth=HTTPDigestAuth('admin', 'V0xd0br4s1l'), timeout = 3)
        r.raise_for_status()
        
        with open("snapshot.jpg", "wb") as f:
            f.write(r.content)
    except requests.exceptions.Timeout as errt:
        print(f"Timeout error: {errt}")
        raise
    except:
        raise Exception("DVR fora do ar ou sem camera")

def is_full_black(image_path):
    img = Image.open(image_path).convert('L') # converting for gray scale
    arr = np.array(img)
    std = np.std(arr) # desvio
    return std <= 25
dvr_index = 0
camera_channel = 1


while True:
    try:
        fetching_image(dvr_list[dvr_index], camera_channel)
        is_full_black('./snapshot.jpg')
        print(f'{camera_channel} do dvr {dvr_list[dvr_index]} - {is_full_black('./snapshot.jpg')}')
        camera_channel += 1
    except Exception as e:
        camera_channel = 1
        dvr_index += 1
        if len(dvr_list) - 1 == dvr_index:
            break

# fetching_image()

print("Finishing")