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
