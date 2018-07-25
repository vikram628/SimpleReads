function printDefintion() {
  var printContent = document.getElementById("define").innerHTML;
  var originalContent = document.body.innerHTML;

     document.body.innerHTML = printContent;

     window.print();

     document.body.innerHTML = originalContent;
}

console.log("hey")
var hardDiv = document.querySelector('#divHiddenBox')
var hardWords = document.getElementsByClassName('wordsHard')
//var hardWords = document.querySelectorAll('.wordsHard')
var cars = ['Mary Grace'];
for(var i = 0; i < hardWords.length; i++) {
  cars.push(hardWords[i].innerText)
}
// hardWords.forEach(function(hardWordItem) {
//   cars.push(hardWordItem)
//   console.log('param2',hardWords)
// })
console.log('param3',hardWords)
var text = "";
var i;

for (i = 0; i < cars.length; i++) {
text += "<div class = \"tabs\" >"  + (1+i ) + ". " + cars[i] + "</div> ";
}
document.getElementById("demo").innerHTML = text;

function printDefintion() {
  var printContent = document.getElementById("define").innerHTML;
  var originalContent = document.body.innerHTML;

     document.body.innerHTML = printContent;

     window.print();

     document.body.innerHTML = originalContent;
}
