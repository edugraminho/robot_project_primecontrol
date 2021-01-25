import requests
import csv
import os

import urllib.parse


header = {
    'Accept': 'application/json',
    'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiIsImtpZCI6IjI4YTMxOGY3LTAwMDAtYTFlYi03ZmExLTJjNzQzM2M2Y2NhNSJ9.eyJpc3MiOiJzdXBlcmNlbGwiLCJhdWQiOiJzdXBlcmNlbGw6Z2FtZWFwaSIsImp0aSI6ImYxNDM1NWRjLWRlNjUtNDFhOC05NTI5LTYxNDU4OTgyMjgwMSIsImlhdCI6MTYxMTU4MjIwOSwic3ViIjoiZGV2ZWxvcGVyLzYzZDczNWI3LWI5ZWYtMTliNC1hNTcyLWIzYTUwOGM2YzVjMCIsInNjb3BlcyI6WyJyb3lhbGUiXSwibGltaXRzIjpbeyJ0aWVyIjoiZGV2ZWxvcGVyL3NpbHZlciIsInR5cGUiOiJ0aHJvdHRsaW5nIn0seyJjaWRycyI6WyIxNzcuOTYuMTUuMTAzIl0sInR5cGUiOiJjbGllbnQifV19.yB8KKtWhZ4vqJkSF2giQidOArHRcgOC56vLbQTw3p-dfYV9YqFg9YA3tw_CQaxDb6LviUoqw-AsTQU0lIQN9LQ'
}

response = requests.get('https://api.clashroyale.com/v1/locations/57000038/rankings/clans', headers=header)

if 200 >= response.status_code <= 299:
    print("OK")
else:
    print("Aconteceu algo de errado")


def search_clan():
    json = response.json()
    list_all_clans = json["items"]

    return [clan for clan in list_all_clans 
            if "The resistance" == clan['name']]

print(search_clan())



id_clan_encoding = urllib.parse.quote(search_clan()[0]['tag'])
print(id_clan_encoding)

response_clan = requests.get(f'https://api.clashroyale.com/v1/clans/{id_clan_encoding}', headers=header)


def get_member_clan():
    json = response_clan.json()
    list_all_members = json["memberList"]


    fieldname = ["nome", "level", "trofeus", "papel"]

    with open("data/members_clan.csv", "a", encoding="utf-8", newline='') as f:
        writer = csv.DictWriter(f, fieldnames=fieldname)

        if (os.stat("data/members_clan.csv").st_size == 0):
            writer.writeheader()

        for member in list_all_members:

            writer.writerow({
                "nome": member["name"],
                "level": member["expLevel"], 
                "trofeus": member["trophies"], 
                "papel": member["role"]})


if __name__ == "__main__":
    get_member_clan()
        
