import requests
import json
from notion_client import Client

NOTION_TOKEN = "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"  # seu token de integração
PARENT_PAGE_ID = "22bca1d11970807291dff116f720bd6c"  # ID da página onde a tabela será criada

notion = Client(auth=NOTION_TOKEN)

notion.pages.create(
    parent={"database_id": "22cca1d1197081a282c5ccb25277cb68"},
    properties=
        {
        "Local": {
            "title": [
                {"text": {"content": "Seu texto aqui"}}
            ]
        },
        "Data da print": {
            "date": {
                'start': '2025-07-17'
            }
        },
        # "Cameras com problema": {
        #     "select": {"name": "Ativo"}
        # }
        }
    
)
