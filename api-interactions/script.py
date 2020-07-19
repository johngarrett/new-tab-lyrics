import re
import json
import lyricsgenius

genius = lyricsgenius.Genius('BoMYF5d1k91V9us_tIHpO4RSFlfeMHVdnvFXnWe-16UU1-Kx7edlj_rj21q7dDhx', verbose=True)
genius.remove_section_headers = True 

def search_artist(name):
    artist = genius.search_artist(name, max_songs=1, sort='popularity')
    sanatized_name = artist.name.lower()
    for banned_char in [",", " ", "'", '(', ')']:
        sanatized_name = sanatized_name.replace(banned_char, '')
    print(f'sanaized name: {sanatized_name}')

    data = {}
    for song in artist.songs:
        data[song.title] = []
        for line in song.lyrics.splitlines():
            if len(line.strip()) == 0:
                continue
            data[song.title].append({
                line: {
                    'rating': 0,
                    'song': song.title,
                }
            })
    return data


if __name__ == '__main__':
    source = open('artists.txt', 'r')
    artists = source.readlines()
    for artist in artists:
        data = search_artist(artist)
        with open(f'{artist}.json', 'w') as outfile:
            json.dump(data, outfile)
            



