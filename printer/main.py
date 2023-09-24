import os
from glob import glob
import random
import json
from urllib.request import urlopen
import time

# Replace it with your server URL
url = "http://127.0.0.1:9693/get_json?print=false"

def random_print():
    file_list = glob('*.png') + glob('*.PNG') + glob('*.pdf') + glob('*.PDF') + glob('*.jpg') + glob('*.JPG')
    file_count = len(file_list)
    print("Supported file list:", file_list)
    print("Count:", file_count)

    rnd_num = random.randint(0, file_count-1)
    print("Random number:", rnd_num)

    file_selected = file_list[rnd_num]
    print("The selected file is", file_selected)
    # Replace it with your CUPS printer
    os.system("lp -d HP_Deskjet_2050_J510_series -o landscape -o fit-to-page -o media=A5 %s" % file_selected)

while True: 
    try: 
        j_str = urlopen(url).read()
        # print(j_str)
        j_dict = json.loads(j_str)
        print(j_dict)
        #j_dict = json.loads('{"print" : "true"}')
        if j_dict['print'] == "true":
            print("Start printing!")
            random_print()
    except Exception as e:
        print('Error occurred.', e)
    except KeyboardInterrupt:
        break
    
    time.sleep(1)

