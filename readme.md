`pip3 install lyricsgenius`
https://github.com/johnwmillr/LyricsGenius

#### newtab lyrics
enter a set of artist names and everytime you open a new tab, their lyrics will appear

#### scrap ideas
- can't use node.js as I wanted to
- might just switch to a flask REST API and have a website point to it
    - have to store a local cookie to keep track of artists and already seen lyrics
- have a thumbs up and thumbs down
- when a user inputs an artist's name, download 100 songs to the server to speed up retrevial in the future
- store each lyric with a rating next to it


#### database structure
~~|-ArtistName1~~
~~|-ArtistName2~~
~~|-ArtistName3~~
~~| |-song1~~
~~| |-song2~~
~~| | |-line1~~
~~| | |-line2~~

```ascii
|-ArtistName1
|-ArtistName2
|-ArtistName3
| |-line1
| | |-songName
| | |-rating
| |-line2
```

line fields
- raiting
    - 0 - 1 
    - ratio of positive to negative
- ~~songName~~ song
    - the song it came from
- ~~explicit~~
    - boolean
- ~~id~~~ this is auto added via mongo (i think)
    - ID to recall the lyric


#### todo
- remove duplicate lyrics
- search database for songs first
-
