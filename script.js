/* eslint-disable no-undef */
/**
 * great-circle
 */

// config map
let config = {
  minZoom: 2,
  maxZomm: 18,
};
// magnification with which the map will start
const zoom = 10;
// co-ordinates ICMC
const lat = -22.007198923101388;
const lng = -47.89478480815888;

// calling map
const map = L.map("map", config).setView([lat, lng], zoom);

// Used to load and display tile layers on the map
// Most tile servers require attribution, which you can set under `Layer`
L.tileLayer("https://tile.openstreetmap.org/{z}/{x}/{y}.png", {
  attribution:
    '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors',
}).addTo(map);

// Debug
map.on("click", (e) => {
  console.log(e.latlng);
});

const icon = L.icon({
  iconUrl: "http://grzegorztomicki.pl/serwisy/pin.png",
  iconSize: [50, 58], // size of the icon
  iconAnchor: [20, 58], // changed marker icon position
  popupAnchor: [0, -60], // changed popup position
});
// icmc coordinate (starting point)
const center = [lat, lng];
L.marker(center, { icon: icon })
  .bindPopup(`<strong>ICMC USP - São Carlos</strong>`)
  .addTo(map);
const start = turf.point(center.reverse());

let featureGroups = [];
function getRandomInRange(from, to, fixed) {
  return (Math.random() * (to - from) + from).toFixed(fixed) * 1;
}

function get_info(student_data) {
  info = ''
  for (const [key, value] of Object.entries(student_data)) {
    info += `<strong>${key}</strong>: ${value}<br>`
  }
  return info
}

data.map((student_data) => {
  // Generating random coordinates
  if (Math.round(Math.random()) > 0.5)
    city = [getRandomInRange(-5, 5, 3)+lat, getRandomInRange(-5, 5, 3)+lng]
  else 
    city = [getRandomInRange(-90, 90, 3), getRandomInRange(-90, 90, 3)]
  const marker = L.marker(city).bindPopup(get_info(student_data)).addTo(map);

  featureGroups.push(marker);

  // distance between two points
  const end = turf.point(city.reverse());
  const greatCircle = turf.greatCircle(start, end);

  L.geoJSON(greatCircle).addTo(map);
});


// add array to featureGroup
let group = new L.featureGroup(featureGroups);

// set map view to featureGroup
map.fitBounds(group.getBounds(), {
  padding: [50, 50], // adding padding to map
});
