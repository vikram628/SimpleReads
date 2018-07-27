function printDefintion() {
  var printContent = document.getElementById("define").innerHTML;
  var originalContent = document.body.innerHTML;

     document.body.innerHTML = printContent;

     window.print();

     document.body.innerHTML = originalContent;
}
function hilightWord(word) {
  console.log(word);
  var list = document.querySelectorAll(".tabs")
  for (var i = 0; i < list.length; i++) {
    if (list[i].dataset.word == word) {
      list[i].classList.add("hilightWord")
    }
  }
}
function dehilightWord(word) {
  console.log(word);
  var list = document.querySelectorAll(".tabs")
  for (var i = 0; i < list.length; i++) {
    if (list[i].dataset.word == word) {
      list[i].classList.remove("hilightWord")
    }
  }
}
console.log("hey")
var hardDiv = document.querySelector('#divHiddenBox')
var hardWords = document.getElementsByClassName('wordsHard')
//var hardWords = document.querySelectorAll('.wordsHard')
var cars = [];
for(var i = 0; i < hardWords.length; i++) {
  cars.push({'content': hardWords[i].innerText, 'word' : hardWords[i].dataset.word})
}
// hardWords.forEach(function(hardWordItem) {
//   cars.push(hardWordItem)
//   console.log('param2',hardWords)
// })
console.log('param3',hardWords)
var text = "";
var i;

for (i = 0; i < cars.length; i++) {
text += "<div data-word = \"" + cars[i].word + "\" class = \"tabs\" >"  + (1+i ) + ". " + cars[i].content + "</div> ";
}
document.getElementById("demo").innerHTML = text;

function printDefintion() {
  var printContent = document.getElementById("define").innerHTML;
  var originalContent = document.body.innerHTML;

     document.body.innerHTML = printContent;

     window.print();

     document.body.innerHTML = originalContent;
}
