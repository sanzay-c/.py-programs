from geopy.geocoders import Nominatim
import time

def get_current_location_coordinate():
    # initialize nominatim 
    geolocator = Nominatim(user_agent='Nepal')

    try:
        # Provide a specific query, such as a city name
        location = geolocator.geocode('Tinkune, Kathmandu, Nepal')

        if location:
            latitude = location.latitude
            longitude = location.longitude
            return latitude, longitude
        else:
            print('Location not found.')
            return None
    
    except Exception as e:
        print('Error: ', e)
        return None

time.sleep(1) # add a delay between request to avoid rate limiting

coordinates = get_current_location_coordinate()
if coordinates:
    print('latitude: ', coordinates[0])
    print('longitude: ', coordinates[1])
else:
    print('Failed to retrieve current location.')
    