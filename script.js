import { getLyrics, getSong } from 'genius-lyrics-api';

const options = {
	apiKey: 'XXXXXXXXXXXXXXXXXXXXXXX',
	title: 'Blinding Lights',
	artist: 'The Weeknd',
	optimizeQuery: true
};

getLyrics(options).then((lyrics) => console.log(lyrics));

getSong(options).then((song) =>
	console.log(`
	${song.id}
	${song.url}
	${song.albumArt}
	${song.lyrics}`)
);
