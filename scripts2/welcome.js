var images=['../images/mainpic.jpg','../images/cloudwater.jpg','../images/ocean.jpg','../images/flowerfield.jpg','../images/greenfield.jpg','../images/middlelake.jpg']

function updateBackgroundImage(imageIndex){
  setBodyImage(images[imageIndex])
  setTimeout(function(){
    var nextIndex= imageIndex+1
    nextIndex=nextIndex%images.length
    updateBackgroundImage(nextIndex)
  }, 5000)
}

function setBodyImage(image){
  document.body.style.backgroundImage= "url('"+ image +"')"
}

updateBackgroundImage(0)
