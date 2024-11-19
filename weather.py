from get_location_info import city_from_ip, lon_from_ip, lat_from_ip
import time
#from get_location_info import city

# import required modules
import requests, json
 
#section for day icon weather description
def get_day_weather_icon(description):
    match description:
        case "clear sky":
            return "󰖙"
        case "few clouds":
            return ""
        case "scattered clouds":
            return "☁️"
        case "broken clouds":
            return "☁️"
        case "shower rain":
            return "🌧️"
        case "rain":
            return "🌧️"
        case "thunderstorm":
            return "⛈️"
        case "snow":
            return "🌨️"
        case "mist":
            return "🌫️"
        case _:
            return "❓"
 
#section for night icon weather description
def get_night_weather_icon(description):
    match description:
        case "clear sky":
            return ""
        case "few clouds":
            return ""
        case "scattered clouds":
            return "☁️"
        case "broken clouds":
            return "☁️"
        case "shower rain":
            return ""
        case "rain":
            return "🌧️"
        case "thunderstorm":
            return "⛈️"
        case "snow":
            return "🌨️"
        case "mist":
            return "🌫️"
        case _:
            return "❓"
 
#case statement for moonpases
def moon_phase_icon(moon_phase):
    match moon_phase:
        case "0.00":
            return ""
        case "0.25":
            return ""
        case "0.50":
            return ""
        case "0.75":
            return ""
        case "1.00":
            return ""

# create a range to map a specific rounded number for the moonphase
def moon_phase_mapped(moon_phase):
    try:
        phase = float(moon_phase)
        ranges = {
            (0.00, 0.20): 0.00,
            (0.20, 0.30): 0.25,
            (0.30, 0.60): 0.50,
            (0.60, 0.80): 0.75,
            (0.80, 1.00): 1.00
        }
        for (low, high), mapped_value in ranges.items():
            if low <= phase <= high:
                return str(mapped_value)
        return "0.00"  # default value if not in any range
    except (ValueError, TypeError):
        return "0.00"  # default value if conversion fails

# Enter your API key here
api_key = "dc790c7357097803a290acfcc4d277c7"
 
# base_url variable to store url
base_url = "https://api.openweathermap.org/data/3.0/onecall?"
 
# Give city name
city_name = (city_from_ip)
# set lat and lon
lon = lon_from_ip
lat = lat_from_ip

# complete_url variable to store
# complete url address
complete_url = base_url + "lat=" + lat_from_ip + "&lon=" + lon_from_ip + "&appid=" + api_key
#print(complete_url) 
# get method of requests module
# return response object
response = requests.get(complete_url)
 
# json method of response object 
# convert json format data into
# python format data
x = response.json()
 
# Now x contains list of nested dictionaries
# Check the value of "cod" key is equal to
# "404", means city is found otherwise,
# city is not found
#if x["cod"] != "404":
 
# store the value of "current"
# key in variable y
y = x["current"]

# store the value of daily
#key in the varriable z
d = x["daily"]

# store the value corresponding
# to the "temp" key of y
current_temperature = y["temp"]
current_temp_fahrenheit = ((current_temperature - 273.15) * 1.8 + 32)
# store the value corresponding
# to the "pressure" key of y
current_pressure = y["pressure"]

# store the value corresponding
# to the "humidity" key of y
current_humidity = y["humidity"]

#stores the time of day for if statement
current_time = y["dt"]
sunrise = y["sunrise"]
sunset = y["sunset"]

#moonphase variable
moon_phase_value = d[0]["moon_phase"]  # Access first day's moon phase from daily forecast
mapped_phase = moon_phase_mapped(moon_phase_value)
current_moon_phase = moon_phase_icon(mapped_phase)
# store the value of "weather"
# key in variable z
z = y["weather"]

# store the value corresponding 
# to the "description" key at 
# the 0th index of z
weather_description = z[0]["description"]

if current_time >= sunset:
    weather_icon = get_night_weather_icon(weather_description)
else:
    weather_icon = get_day_weather_icon(weather_description)

# Print moon phase
print("Moon phase:" + str(current_moon_phase))

# print following values
print(" Current weather in " + 
                str(city_name) +
      "\n Temperature = " +
                str(round(current_temp_fahrenheit)) + "󰔅" +
      "\n atmospheric pressure (in hPa unit) = " +
                str(current_pressure) +
      "\n humidity (in percentage) = " +
                str(current_humidity) +
      "\n description = " +
                str(weather_icon))


