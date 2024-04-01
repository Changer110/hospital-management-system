


function getfile(event) {
    var imageFile = event.target.files[0];
    var imagePreview = document.getElementById('picfile');

    var reader = new FileReader();
    reader.onload = function(e) {
        imagePreview.src = e.target.result;
    };
    reader.readAsDataURL(imageFile);
}

function show_date(event){
  var input = event.target.closest('input');
  input.type = 'text';
  var new_date = input.value;
  input.value = (new_date.trim() !== '') ? new_date : old_value;
}

function insert_date(event){
  var input = event.target.closest('input');
  old_value = input.value;
  input.type = 'date';
}