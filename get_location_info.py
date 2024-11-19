import ipinfo
import sys

#def get_location_info(ip_adress):
# get the ip address from the command line
try:
    ip_address = sys.argv[1]
except IndexError:
    ip_address = None
# access token for ipinfo.io
access_token = 'da7560f6b600fe'
# create a client object with the access token
handler = ipinfo.getHandler(access_token)
# get the ip info
details = handler.getDetails(ip_address)
#stores the region and city
region_from_ip = details.region
city_from_ip = details.city
lat_from_ip = details.latitude
lon_from_ip = details.longitude
#print the city and region
#print(city,", ",region)
#return city, region
#print(lat_from_ip, lon_from_ip)
