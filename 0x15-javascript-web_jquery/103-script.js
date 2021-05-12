const url = 'https://www.fourtonfish.com/hellosalut/';
function Translate (str) {
  $.get(`${url}?lang=${str}`, function (data, textStatus) {
    if (textStatus === 'success') {
      $('#hello').text(data.hello);
    }
  });
}

$(document).ready(function () {
  $('#btn_translate').click(() => {
    const str = $('#language_code').val();
    Translate(str);
  });
});

$(document).ready(function () {
  $('#language_code').keypress(function (event) {
    const code = (event.keyCode ? event.keyCode : event.wich);
    if (code === 13) {
      const str = $('#language_code').val();
      Translate(str);
    }
  });
});
