#!/usr/bin/node
/**
 * Function to print all characters of a Start Wars Movie
 * The first positional argument passed is the Movie ID
 * Display one character name per line
 *
 */

const util = require('util');
const request = util.promisify(require('request'));
const filmID = process.argv[2];

async function starwarsCharacters (filmId) {
  const endpoint = `https://swapi.dev/api/films/${filmId}`;

  try {
    let response = await request(endpoint);
    response = JSON.parse(response.body);
    const characters = response.characters;

    for (const url of characters) {
      const characterResponse = await request(url);
      const character = JSON.parse(characterResponse.body);
      console.log(character.name);
    }
  } catch (error) {
    console.error(`Error fetching data: ${error}`);
  }
}

if (!filmID) {
  console.log('Usage: node 0-starwars_characters.js <Movie ID>');
} else {
  starwarsCharacters(filmID);
}
