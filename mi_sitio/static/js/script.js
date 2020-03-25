window.onload = function() {
  var btn = document.getElementById("btn");
  btn.addEventListener("click", saludar);

  function saludar() {
    var p = document.getElementById("parrafo");
    p.innerHTML = "<strong>Por fin lo pude hacer</strong>";
    p.style.color = "red";
  }
};
