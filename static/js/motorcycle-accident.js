// Initialize all of the LayerGroups we'll be using
var layers = {
  MALE: new L.LayerGroup(),
  FEMALE: new L.LayerGroup()
};

var myMap = L.map("map", {
  center: [51.5074, -0.1278],
  zoom: 13,
  layers: [
    layers.MALE,
    layers.FEMALE
  ]
});

// Adding tile layer
L.tileLayer("https://api.mapbox.com/styles/v1/{id}/tiles/{z}/{x}/{y}?access_token={accessToken}", {
  attribution: "© <a href='https://www.mapbox.com/about/maps/'>Mapbox</a> © <a href='http://www.openstreetmap.org/copyright'>OpenStreetMap</a> <strong><a href='https://www.mapbox.com/map-feedback/' target='_blank'>Improve this map</a></strong>",
  tileSize: 512,
  maxZoom: 18,
  zoomOffset: -1,
  id: "mapbox/streets-v11",
  accessToken: API_KEY
}).addTo(myMap);




// Create an overlays object to add to the layer control
var overlays = {
  "Males": layers.MALE,
  "Females": layers.FEMALE
};

// Create a control for our layers, add our overlay layers to it
L.control.layers(null, overlays).addTo(myMap);



// var AgeRange = ["Under 18", "18 to 25", "26 to 35", "36 to 45", "46 to 55", "Over 55"]
// var GenderRange = ["Male", "Female"]
// var YearRange = ["2010", "2011", "2012", "2013", "2014"]

var AgeRange = ["Under 18"]
var GenderRange = ["Male"]
var YearRange = ["2013"]

// slider = L.control.slider(function(value) {console.log(value)}, {id:slider, 'vertical'});

var newtry = "/all500"
//var newtry = "../static/resources/motorcycle_accident_400.json"
//var newtry = "/fltrdgrps/"+YearRange+"/"+GenderRange+"/"+AgeRange;
console.log("dabase location: " + newtry)

d3.json(newtry, function(response) {

  // console.log("-------");
  // console.log(response);
  // console.log("-------");

  var count = Object.keys(response).length;
  console.log(count);
  console.log("-------");


  for (var i = 0; i < count; i++) {
    var location = response[i];
    // console.log(i);
    // console.log(location.Longitude, location.Latitude);
    // console.log("-------");
    let LatLng = [location.Latitude, location.Longitude];
    let Gender = [location.Sex_of_Casualty];
    var newMarker = L.marker(LatLng);

    if (Gender == "Female") {
      newMarker.addTo(layers["FEMALE"]);
    }
    else if (Gender == "Male") {
      newMarker.addTo(layers["MALE"]);
    }

    // console.log(LatLng)
    // console.log("-------");
      // L.marker(LatLng).addTo(myMap);
  }

});
