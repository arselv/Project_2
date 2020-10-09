var myMap = L.map("map", {
  center: [51.358227, -0.054993],
  zoom: 13
});

L.tileLayer("https://api.mapbox.com/styles/v1/{id}/tiles/{z}/{x}/{y}?access_token={accessToken}", {
  attribution: "© <a href='https://www.mapbox.com/about/maps/'>Mapbox</a> © <a href='http://www.openstreetmap.org/copyright'>OpenStreetMap</a> <strong><a href='https://www.mapbox.com/map-feedback/' target='_blank'>Improve this map</a></strong>",
  tileSize: 512,
  maxZoom: 18,
  zoomOffset: -1,
  id: "mapbox/streets-v11",
  accessToken: API_KEY
}).addTo(myMap);

// var AgeRange = ["Under 18", "18 to 25", "26 to 35", "36 to 45", "46 to 55", "Over 55"]
// var GenderRange = ["Male", "Female"]
// var YearRange = ["2010", "2011", "2012", "2013", "2014"]

var AgeRange = ["Under 18"]
var GenderRange = ["Male"]
var YearRange = ["2012"]

var newtry = "/fltrdgrps/"+YearRange+"/"+GenderRange+"/"+AgeRange;
console.log("dabase location: " + newtry)

d3.json(newtry, function(response) {

  console.log("-------");
  console.log(response);
  console.log("-------");

  var count = Object.keys(response).length;
  console.log(count);
  console.log("-------");

  var heatArray = [];

  for (var i = 0; i < count; i++) {
    var location = response[i];
    // console.log(i);
    // console.log(location.Longitude, location.Latitude);
    // console.log("-------");
    let LatLng = [location.Latitude, location.Longitude];
    // console.log(LatLng)
    // console.log("-------");
    heatArray.push(LatLng);

    // heatArray.push(location.Latitude, location.Longitude);
    // console.log(heatArray)
    // L.marker(LatLng).addTo(myMap);
    // L.heatLayer(heatArray, {
    //   radius: 20,
    //   blur: 30}).addTo(myMap);
  

  }
  console.log(heatArray)  
    L.heatLayer(heatArray, {
    radius: 75,
    blur: 45
  }).addTo(myMap);

});
