import json

with open("dvrs.json", "r", encoding="utf-8") as f:
    dados = json.load(f)

def MakeDVRList():
    dvr_list = []
    for key, value in dados.items(): # pecorre todos os condominios
        is_standard = False
        if value["standard"] == True:
            for key1, value1 in value.items():
                if isinstance(value1, bool):
                    pass
                else:
                    dvr_list.append(value1)
    return dvr_list
        
    # for key1, value1 in value.items():
    #     print(key1)
