$(function () {
  const url = 'https://swapi-api.hbtn.io/api/films/?format=json';
  $.get(url, function (data) {
    const objects = data.results;
    objects.forEach((title) => {
      $('UL#list_movies').append(`<li>${title.title}</li>`);
    });
  });
});
