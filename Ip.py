import argparse
import requests
import json
import sys
import os
from sys import argv

parser = argparse.ArgumentParser()

parser.add_argument ("-h", help= "target/host IP address", type=str, dest='target', required=True )

args = parser.parse_args()


ip = args.target

api = "http://ip-api.com/json/"

try:
        data = requests.get(api+ip).json()
        sys.stdout.flush()
        a = lgreen+bold+"[$]"
        b = cyan+bold+"[$]"
        print (a, " <Victim:", data['query'])
        print(red+"[>]——————-————-–———[<]"+red)
        print (b, " <ISP:", data['isp'])
        print(red+"[>]——————-————-–———[<]"+red)
        print (a, " <Organisation:", data['org'])
        print(red+"[>]———-———————-–———[<]"+red)
        print (b, " <City:", data['city'])
        print(red+"[>]——————-—————————[<]"+red)
        print (a, " <Region:", data['region'])
        print(red+"[>]——-–————————-———[<]"+red)
        print (a, " <Latitude:", data['lat'])
        print(red+"[>]————————————-–——[<]"+red)
        print (b, " <Longitude:", data['lon'])
        print(red+"[>]——————-————-–———[<]"+red)
        print (b, " <Time zone:", data['timezone'])
        print(red+"[>]———-–-———–———-——[<]"+red)
        print (a, " <Zip code:", data['zip'])
        print (" "+yellow)

except KeyboardInterrupt:
        print ('Quiting Utility! Bye Bye, Have a nice day!'+lgreen)
        sys.exit(0)
except requests.exceptions.ConnectionError as e:
        print (red+"[-]"+" Please check your internet connection!"+clear)
sys.exit(1)