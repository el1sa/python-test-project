import urllib.request
import json
from typing import Dict

JSON_URL = 'https://raw.githubusercontent.com/theikkila/postinumerot/master/postcode_map_light.json'


def get_postal_data() -> Dict[str, str]:
    with urllib.request.urlopen(JSON_URL) as response:
        data = response.read()
    return json.loads(data)
