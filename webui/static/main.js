function load_next_question() {
  var xhttp = new XMLHttpRequest();
  xhttp.onreadystatechange = function() {
    if (this.readyState == 4 && this.status == 200) {
      // var resp_json = JSON.parse(this.responseText);
      // console.log(resp_json);
      var game_area_elem = document.getElementById("game_area");
      game_area_elem.innerHTML = this.responseText;
    }
  };
  xhttp.open("GET", "/api/next", true);
  xhttp.send();
}
function stupid_function(){
  load_next_question();
}
function check_correct(inwa) {
  var this_button = document.getElementById("button_answer_" + inwa);
  this_button.disabled = true;
  this_button.innerHTML = "WRONG";
  // var youshouldnotseethis = setInterval()
  setTimeout(stupid_function,1500);
}
