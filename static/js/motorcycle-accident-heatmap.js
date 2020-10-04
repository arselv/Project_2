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

var url = "../motorcycle_accident_full.json";
console.log("dabase location: " + url)

d3.json(url, function(response) {

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
    radius: 40,
    blur: 35
  }).addTo(myMap);

});
