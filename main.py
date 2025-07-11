import json
from typing import Any, Dict

from searchCamera import fetching_image, is_full_black

def getJSON(json_path):
    dados = None
    try:
        with open(json_path, "r", encoding="utf-8") as f:
            dados = json.load(f)
    except Exception as e:
        raise Exception("Erro ao pegar o arquivo JSON: ", e)
    return dados
    
def formating_dict_to_arr(dict):
    dvr_arr = []
    for key, value in dict.items():
        is_standard = value.get("standard")
        if is_standard:
            for dvr_name, ip in value.items():
                if dvr_name == "standard":
                    continue
                dvr_arr.append([key, dvr_name, ip])
        else:
            for dvr_name, dvr_info in value.items():
                if dvr_name == "standard":
                    continue
                dvr_arr.append([key, dvr_name, dvr_info['ip'], dvr_info['user'], dvr_info['password']])
    return dvr_arr

dvr_arr = formating_dict_to_arr(getJSON("./dvrs.json"))
for dvrs in dvr_arr:
    fetching_image(dvr_arr[2], )
    
