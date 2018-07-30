# guide-TP
# /admin user: sadmin p455w0rd

var infowindow = new google.maps.InfoWindow({
              content: contentString
            });

            var contentString = '<div id="container">'
              + '<h1>{{place.name}}</h1>'
              + '<img src="{{place.img.url}}" alt=""/>'
              + '<b>Typ:</b> {{place.type}}<br/>'
              + '<b>Godziny otwarcia:</b> {{place.open_hours}}<br/>'
              + '</div>';

            var latlng = {lat: {{place.gps_x}}, lng: {{place.gps_y}}}
            var marker = new google.maps.Marker({
              position: latlng,
              map: map
            });

            marker.addListener('click', function() {
              infowindow.open(map, marker);
            });