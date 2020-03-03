import lyricsgenius
genius = lyricsgenius.Genius('BoMYF5d1k91V9us_tIHpO4RSFlfeMHVdnvFXnWe-16UU1-Kx7edlj_rj21q7dDhx', verbose=True)
genius.remove_section_headers = True # Remove section headers (e.g. [Chorus]) from lyrics when searching

def search_artist(name):
    artist = genius.search_artist(name, max_songs=3, sort='popularity')
    for song in artist.songs:
        print(song.lyrics)
        song.to_json(filename=f'{song.title}-{artist.name}.json')

if __name__ == '__main__':
    search_artist(input("Enter artist name: "))

