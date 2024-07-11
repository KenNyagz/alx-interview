#!/usr/bin/node
const request = require('request');

if (process.argv.length !== 3) process.exit(1);

const Swapi = 'https://swapi-api.alx-tools.com/api/films/' + process.argv[2];

function getSWCharacters (url) {
  request.get(url, (error, response, body) => {
    if (error) {
      console.log(error);
    } else if (response.statusCode !== 200) {
      console.log(response.statusCode);
    } else {
      const filmData = JSON.parse(body);
      const characters = filmData.characters;

      characters.forEach((characterUrl) => {
        request.get(characterUrl, (error, resp, bodyy) => {
          if (error) console.log(error);
          else if (resp.statusCode !== 200) console.log(resp.statusCode);
          const chr = JSON.parse(bodyy);
          const name = chr.name;
          console.log(name);
        });
      });
    }
  });
}

getSWCharacters(Swapi);
