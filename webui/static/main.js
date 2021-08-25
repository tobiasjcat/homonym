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

function check_correct_ajax(inchoice){
  var xhttp = new XMLHttpRequest();
  xhttp.onreadystatechange = function() {
    if (this.readyState == 4 && this.status == 200) {
      if (this.responseText == "True") {
        return true;
      }
      return false;
    }
  };
  xhttp.open("POST", "/api/check_answer/", true);
  xhttp.send(inchoice);
}

function check_correct(inwa) {
  var this_button = document.getElementById("button_answer_" + inwa);
  var current_score = document.getElementById("score_element");
  var all_buttons = document.getElementsByTagName("button");
  var high_score = document.getElementById("high_score");

  if (check_correct_ajax(inwa)){
    this_button.innerHTML = "CORRECT";
    var new_score = Number(current_score) + 1;
    current_score.innerHTML = new_score;
    if (new_score > Number(high_score.innerHTML)){
      high_score.innerHTML = new_score;
    }
  } else {
    this_button.innerHTML = "WRONG";
    current_score.innerHTML = "0";
  }
  this_button.disabled = true;
  this_button.style.fontSize = "xx-large";
  // var youshouldnotseethis = setInterval()
  for (var i = 0; i < all_buttons.length; i++) {
    all_buttons[i].disabled = true;
  }
  setTimeout(stupid_function,1500);
}
