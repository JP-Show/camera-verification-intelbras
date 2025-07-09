import requests
from requests.auth import HTTPDigestAuth

from PIL import Image
import numpy as np

print("Running")

def fetching_image(camera_channel):
    r = requests.get(f'http://192.168.12.40/cgi-bin/snapshot.cgi?channel={camera_channel}&type=0', auth=HTTPDigestAuth('admin', 'V0xd0br4s1l'))
    with open("snapshot.jpg", "wb") as f:
        f.write(r.content)
    

def is_full_black(image_path):
    img = Image.open(image_path).convert('L') # converting for gray scale
    arr = np.array(img)
    std = np.std(arr) # desvio
    return std <= 10

for i in range(18):
    if i == 0:
        continue
    fetching_image(i)
    print(f'{i} - {is_full_black('./snapshot.jpg')}')

# fetching_image()

print("Finishing")