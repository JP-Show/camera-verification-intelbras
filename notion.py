import requests
import json

NOTION_TOKEN = "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"  # seu token de integração
PARENT_PAGE_ID = "sua_page_id"  # ID da página onde a tabela será criada

headers = {
    "Authorization": f"Bearer {NOTION_TOKEN}",
    "Content-Type": "application/json",
    "Notion-Version": "2022-06-28"
}

data = {
    "parent": { "type": "page_id", "page_id": PARENT_PAGE_ID },
    "title": [{
        "type": "text",
        "text": {
            "content": "Minha Tabela"
        }
    }],
    "properties": {
        "Nome": {
            "title": {}
        },
        "Idade": {
            "number": {
                "format": "number"
            }
        },
        "Ativo": {
            "checkbox": {}
        }
    }
}

response = requests.post("https://api.notion.com/v1/databases", headers=headers, data=json.dumps(data))

print(response.status_code)
print(response.json())
