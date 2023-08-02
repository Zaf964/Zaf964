import os
from datetime import datetime, timedelta
import requests
import json
import config
id_2 = config.TS
class Match:
    def __init__(self):
        self.tod = datetime.today()
        self.today = self.tod.strftime('%Y-%m-%d')
        self.tom = self.tod + timedelta(days=1)
        self.tomorrow = self.tom.strftime('%Y-%m-%d')
        self.folder_path = "./src/"

    def get_today_matches(self):
        self.delete_files_in_folder(self.folder_path)
        url = f"https://app.footystats.org/app-todays-matches{id_2}{self.today}"

        headers = {
            'user-agent': 'Dart/2.19 (dart:io)',
            'accept-encoding': 'gzip',
            'host': 'app.footystats.org'
            }
        response = requests.get(url, headers=headers, proxies=None)
        data = response.json()['data']
        matches = []
        for match in data:
            for m in match['matches']:
                match_info = {
                    "id": m['id'],
                    "heure": datetime.fromtimestamp(m['date_unix']).strftime('%H:%M:%S'),
                    "league": match['title'],
                    "pays": match['country'],
                    "team_a": m['home_name'],
                    "team_b": m['away_name'],
                    "hid": m['homeID'],
                    "aid": m['awayID']
                }
                matches.append(match_info)
        matches.sort(key=lambda x: x['heure'])
        with open("./src/today_matches.json", "w", encoding='utf-8') as file:
            json.dump(matches, file, indent=4, ensure_ascii=False)

    def get_tomorrow_matches(self):
        self.delete_files_in_folder(self.folder_path)
        url = f"https://app.footystats.org/app-todays-matches{id_2}{self.tomorrow}"

        headers = {
            'user-agent': 'Dart/2.19 (dart:io)',
            'accept-encoding': 'gzip',
            'host': 'app.footystats.org'
            }
        response = requests.get(url, headers=headers, proxies=None)
        data = response.json()['data']
        matches = []
        for match in data:
            for m in match['matches']:
                match_info = {
                    "id": m['id'],
                    "heure": datetime.fromtimestamp(m['date_unix']).strftime('%H:%M:%S'),
                    "league": match['title'],
                    "pays": match['country'],
                    "team_a": m['home_name'],
                    "team_b": m['away_name'],
                    "hid": m['homeID'],
                    "aid": m['awayID']
                }
                matches.append(match_info)
        matches.sort(key=lambda x: x['heure'])
        with open("./src/tomorrow_matches.json", "w", encoding='utf-8') as file:
            json.dump(matches, file, indent=4, ensure_ascii=False)

    @staticmethod
    def delete_files_in_folder(folder_path):
        for file_name in os.listdir(folder_path):
            file_path = os.path.join(folder_path, file_name)
            if os.path.isfile(file_path):
                os.remove(file_path)
                print(f"{file_path} a été supprimé.")
