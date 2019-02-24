function magnifyFigure(idstub) {
  var modal = document.getElementById("modal-frame");
  modal.style.display = "block";
  var modalObject = document.getElementById("modal01");
  var object = document.getElementById(idstub.concat("-figure"));
  modalObject.innerHTML = object.innerHTML;
  var caption = document.getElementById(idstub.concat("-caption"));
  var captionText = document.getElementById("modal-caption");
  captionText.innerHTML = caption.innerHTML;
}

function closeMagnify() {
  var modal = document.getElementById("modal-frame");
  modal.style.display = "none";
}
