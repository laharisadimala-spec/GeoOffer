// STORE LOCATION (center of geofence)
const storeLat = 17.348692
const storeLon = 78.339537

// Geofence radius in meters
const geofenceRadius = 500

let userMarker
let entered = false


// Create map
var map = L.map('map').setView([storeLat, storeLon],15)


// Map tiles
L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png',{
attribution:'© OpenStreetMap'
}).addTo(map)


// Store marker
L.marker([storeLat,storeLon])
.addTo(map)
.bindPopup("Store Location")


// Geofence circle
L.circle([storeLat,storeLon],{

radius: geofenceRadius,
color:'green'

}).addTo(map)




// Track user location
navigator.geolocation.watchPosition(function(position){

let userLat = position.coords.latitude
let userLon = position.coords.longitude

console.log("User Lat:",userLat)
console.log("User Lon:",userLon)


// Update marker
if(userMarker){
map.removeLayer(userMarker)
}

userMarker = L.marker([userLat,userLon])
.addTo(map)
.bindPopup("You are here")


// Calculate distance
let distance = calculateDistance(
userLat,
userLon,
storeLat,
storeLon
)

console.log("Distance:",distance)


// Check geofence
if(distance <= geofenceRadius){

document.getElementById("status").innerText =
"You are near the store! Offer unlocked 🎉"

if(!entered){

entered = true

callBackend(userLat, userLon)

}

}else{

document.getElementById("status").innerText =
"You are outside store area"

}

})




// Distance formula
function calculateDistance(lat1,lon1,lat2,lon2){

const R = 6371000

let dLat = (lat2-lat1)*Math.PI/180
let dLon = (lon2-lon1)*Math.PI/180

let a =
Math.sin(dLat/2)*Math.sin(dLat/2) +
Math.cos(lat1*Math.PI/180) *
Math.cos(lat2*Math.PI/180) *
Math.sin(dLon/2) *
Math.sin(dLon/2)

let c = 2*Math.atan2(Math.sqrt(a),Math.sqrt(1-a))

return Math.round(R*c)

}
function callBackend(userLat, userLon) {

fetch(`http://10.231.32.247:5001/retail-ai-offer-system/us-central1/detectLocation?lat=${userLat}&lon=${userLon}`)
.then(response => response.json())
.then(data => {
console.log("Nearby stores:", data);
})
.catch(error => {
console.error("Error:", error);
});

}