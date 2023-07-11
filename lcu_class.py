import base64
import requests
import json
import webbrowser


# Class for LCU API 

class LCU:
    def __init__(self):
        self.region = None
        self.app_port = None
        self.remoting_auth = None
        self.riot_app_port = None
        self.riot_token = None
        self.LCU_url = None
        self.LCU_auth_token = None
        self.LCU_headers = None
        self.riot_url = None
        self.riot_auth_token = None
        self.riot_headers = None

    def set_region(self, region):
        self.region = region

    def set_credentials(self, app_port, remoting_auth, riot_app_port, riot_token):
        self.app_port = app_port
        self.remoting_auth = remoting_auth
        self.riot_app_port = riot_app_port
        self.riot_token = riot_token

    def initialize_LCU(self):
        self.LCU_url = "https://127.0.0.1:" + self.app_port
        LCU_token = f"riot:{self.remoting_auth}"
        self.LCU_auth_token = base64.b64encode(LCU_token.encode("utf-8")).decode("utf-8")
        self.LCU_headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json',
            'Authorization': 'Basic ' + self.LCU_auth_token
        }

    def initialize_riot(self):
        self.riot_url = "https://127.0.0.1:" + self.riot_app_port
        riot_token = f"riot:{self.riot_token}"
        self.riot_auth_token = base64.b64encode(riot_token.encode("utf-8")).decode("utf-8")
        self.riot_headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json',
            'User-Agent': 'LeagueOfLegendsClient',
            'Authorization': 'Basic ' + self.riot_auth_token
        }
    
    def get_current_summoner(self):
        current_summoner = self.LCU_url + '/lol-summoner/v1/current-summoner'
        r = requests.get(current_summoner, headers=self.LCU_headers, verify=False)
        r = json.loads(r.text)
        summoner = r['displayName']
        return summoner

    def get_gameflow_phase(self):
        gameflow_phase = self.LCU_url + "/lol-gameflow/v1/gameflow-phase"
        r = requests.get(gameflow_phase, headers=self.LCU_headers, verify=False)
        r = json.loads(r.text)
        return r 

    def start_matchmaking(self):
        matchmaking_start = self.LCU_url + '/lol-lobby/v2/lobby/matchmaking/search'
        r = requests.post(matchmaking_start, headers=self.LCU_headers, verify=False)
        return r
    
    def play_again(self):
        play_again = self.LCU_url + '/lol-lobby/v2/play-again'
        r = requests.post(play_again, headers=self.LCU_headers, verify=False)
        return r
    
    def get_champ_select_participants(self):
        champ_select_participants = self.riot_url + '/chat/v5/participants/champ-select'
        r = requests.get(champ_select_participants, headers=self.riot_headers, verify=False)
        r = json.loads(r.text)
        game_names = [participant['game_name'] for participant in r['participants']]
        name_list = []
        for name in game_names:
            name_list.append(name)
        return name_list

    def accept_queue(self):
        accept_q = self.LCU_url + '/lol-lobby-team-builder/v1/ready-check/accept'
        r = requests.post(accept_q, headers=self.LCU_headers, verify=False)
        return r
    
    def get_summoner_stats(self,name_list,summoner):
        summoners = [name for name in name_list if name != summoner]
        summoner_list = ', '.join(summoners)
        url = f"https://u.gg/multisearch?summoners={summoner_list}&region={self.region}"
        webbrowser.open(url)

