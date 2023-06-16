$.getJSON('https://swapi-api.alx-tools.com/api/films/?format=json', function() {
	json.results.forEach(title) {
		$('ul#list_movies').appendTo(`<li>${title}</li>`);
	});
});
