import * as mod from "/main.py"
function myFunction() {
    let x = document.getElementById("search").value;
    let text;

    text = mod.search("btc");
    window.alert(text);
    document.getElementById("demo").innerHTML = text;
    
    /*
    if (isNaN(x) || x < 1 || x > 10) {
      text = "Input not valid";
    } else {
      text = "Input OK";
    }
    document.getElementById("demo").innerHTML = text;
    */
  }