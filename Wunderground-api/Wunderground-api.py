import json
from urllib.request import urlopen

url = "http://api.wunderground.com/api/d18f045be0ae40cb/conditions/q/MA/Wakefield.json"
conn = urlopen(url)
json_string = conn.read()
parsed_json = json.loads(json_string)

#display a bunch of data
for x in parsed_json:
    print (x)
    for y in parsed_json[x]:
        print (y,':',parsed_json[x][y])
    
conn.close()


#key d18f045be0ae40cb
