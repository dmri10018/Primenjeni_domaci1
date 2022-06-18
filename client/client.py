import requests
from requests.structures import CaseInsensitiveDict
import os

url = "http://localhost:8081/users"

headers = CaseInsensitiveDict()
headers["Accept"] = "application/json"
headers["Content-Type"] = "application/json"

data = """
{
	"ime": "David",
	"prezime": "Malesevic",
	"smer": "RI",
	"predmeti": [
		{
			"ime": "matematicka_analiza",
			"espb": 8
		}
	]
}
"""

resp = requests.post(url, headers=headers, data=data)

print(resp.status_code)