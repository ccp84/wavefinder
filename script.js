function getPosition() {

   return new Promise((res, rej) => {
  
     if (navigator.geolocation) {
       navigator.geolocation.getCurrentPosition(success, error);
     } else {
       console.log("Sorry, your browser does not support HTML5 geolocation.");
     }
 
     function success(position) {
       res({
         lat: position.coords.latitude,
         lng: position.coords.longitude
       })
       
     }
 
     function error(error) {
       console.log("Sorry, we can\'t retrieve your local weather without location permission.");
     }
 
   });
 
 };


 async function returnCoordinates() {
      return getPosition();
    };


let pos = await returnCoordinates();

console.log(pos)

// Google map
let map;

async function initMap() {
  const { Map } = await google.maps.importLibrary("maps");
  

  map = new Map(document.getElementById("map"), {
    center: pos,
    zoom: 8,
  });
  new google.maps.Marker({
    position: pos,
    map: map
  })
}


// getLocation();
initMap();

