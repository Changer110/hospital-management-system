


function getfile(event) {
    var imageFile = event.target.files[0];
    var imagePreview = document.getElementById('picfile');

    var reader = new FileReader();
    reader.onload = function(e) {
        imagePreview.src = e.target.result;
    };
    reader.readAsDataURL(imageFile);
}

function show_datetime(event){
  var input = event.target.closest('input');
  input.type = 'text';
  var new_value = input.value;
  input.value = (new_value.trim() !== '') ? new_value : old_value;
}

function insert_datetime(event){
  var input = event.target.closest('input');
  old_value = input.value;
  input.type = (input.id === 'date') ? 'date' : 'time';
}
