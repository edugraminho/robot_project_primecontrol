import requests
import csv
import os

import urllib.parse


header = {
    'Accept': 'application/json',
    'Authorization': 'Bearer ...'
}

response = requests.get('https://api.clashroyale.com/v1/locations/57000038/rankings/clans', headers=header)

if 200 >= response.status_code <= 299:
    print("OK")
else:
    print("Aconteceu algo de errado")


def search_clan():
    """Faz a busca em uma lista de clan retornando somente o clan requerido: The resistance """
    json = response.json()
    list_all_clans = json["items"]

    return [clan for clan in list_all_clans 
            if "The resistance" == clan['name']]



id_clan_encoding = urllib.parse.quote(search_clan()[0]['tag'])
"""Faz o tratamento da URL para URL-encoded"""


response_clan = requests.get(f'https://api.clashroyale.com/v1/clans/{id_clan_encoding}', headers=header)
""" Faz a requisicao para encontrar o clan"""

def get_member_clan():
    """ 
    Transforma a requisicao em um json/dict, listando todos os membros do clan,
    e enfim criando um csv: data/members_clan 
    """
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
    print(search_clan())
    get_member_clan()
