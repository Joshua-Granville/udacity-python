import json
from urllib.request import urlopen

url = "http://api.wunderground.com/api/d18f045be0ae40cb/conditions/q/MA/Wakefield.json"
conn = urlopen(url)
json_string = conn.read()
parsed_json = json.loads(json_string)
#location = parsed_json['location']['city']
#temp_f = parsed_json['current_observation']['temp_f']
#print ("Current temperature in %s is: %s") % (location, temp_f)

print (parsed_json)

f.close()


#key d18f045be0ae40cb
