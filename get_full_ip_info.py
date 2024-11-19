import ipinfo
import sys

def get_full_ip_info(ip_address=0):
    # access token for ipinfo.io
    access_token = 'da7560f6b600fe'
    # create a client object with the access token
    handler = ipinfo.getHandler(access_token)
    # get the ip info
    details = handler.getDetails(ip_address)
    #stores the region and city
    # print the ip info
    for key, value in details.all.items():
        print(f"{key}: {value}")
    return details.city, details.region

if __name__ == "__main__":
    # get the ip address from the command line
# get the ip address from the command line
    try:
        ip_address = sys.argv[1]
    except IndexError:
        ip_address = None
    
    city, region = get_full_ip_info(ip_address)
