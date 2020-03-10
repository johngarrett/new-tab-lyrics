import re
import lyricsgenius
from pymongo import MongoClient

genius = lyricsgenius.Genius('BoMYF5d1k91V9us_tIHpO4RSFlfeMHVdnvFXnWe-16UU1-Kx7edlj_rj21q7dDhx', verbose=True)
client = MongoClient()
db = client.test
genius.remove_section_headers = True 

def search_artist(name):
    artist = genius.search_artist(name, max_songs=1, sort='popularity')
    sanatized_name = artist.name.lower()
    for banned_char in [",", " ", "'", '(', ')']:
        sanatized_name = sanatized_name.replace(banned_char, '')
    print(f'sanaized name: {sanatized_name}')
    artist_entry = db[sanatized_name]

    for song in artist.songs:
        for line in song.lyrics.splitlines():
            if len(line.strip()) == 0:
                continue
            line = line.replace(".", "%2E") # .'s can't exist in bson keys
            data = {
                 line: {
                     'rating': 0,
                     'song': song.title,
                 }
                }
            artist_entry.insert_one(data)


if __name__ == '__main__':
    search_artist(input("Enter artist name: "))

