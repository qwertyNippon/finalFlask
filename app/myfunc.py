import requests


class Anime_all():
    url = 'https://api.jikan.moe/v4/anime/{id}/full'

    def request_data(self):
        response = requests.get(self.url)
        data = response.json()
        if not response.ok:
            print("error fetching url")
        data = data["anime"]
        return data

class Anime():

    def __init__(self, id):
        self.url = f'https://api.jikan.moe/v4/anime/{id}/full'
        self.id = id
        self.new_url = ''
        self.img = ''
        self.trail = ''
        self.engT = ''
        self.japT = ''
        self.rating = ''
        self.syn = ''

    def request(self):
        response = requests.get(self.url)
        data = response.json()
        if not response.ok:
            print("error fetching url")
            return [1, 2, 3, 4, 5]
        return data

    def get_deets(self):
        data = self.request()
        self.id = data["data"]["mal_id"]
        self.new_url = data["data"]["url"]
        self.img = data["data"]["images"]["jpg"]["image_url"]
        self.trail = data["data"]["trailer"]["url"]
        self.engT = data["data"]["titles"][2]
        self.japT = data["data"]["titles"][1]
        self.rating = data["data"]["rating"]
        self.syn = data["data"]["synopsis"]
        
        d = {}
        
        d["id"] = data["data"]["mal_id"]
        d["new_url"] = data["data"]["url"]
        d["img"] = data["data"]["images"]["jpg"]["image_url"]
        d["trail"] = data["data"]["trailer"]["url"]
        d["engT"] = data["data"]["titles"][2]
        d["japT"] = data["data"]["titles"][1]
        d["rating"] = data["data"]["rating"]
        d["syn"] = data["data"]["synopsis"]
        return d
    

