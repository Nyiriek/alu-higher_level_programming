$.getJSON('https://swapi-api.alx-tools.com/api/films/?format=json', function(data) {
	$.each(data.results, (index, value) => {
		$('<li>' + value.title + '</li>').appendTo('UL#list_movies');
	});
});
