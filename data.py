import json
from typing import TypedDict

import requests


def get_gem_dict():
    resp = requests.get(
        "https://raw.githubusercontent.com/lvlvllvlvllvlvl/RePoE/refs/heads/master/RePoE/data/gems.json")
    gem_dict = {}
    for gem_id, gem_data in resp.json().items():

        if "Royale" in gem_id or "Playtest" in gem_id or gem_data["display_name"] is None or "UNUSED" in gem_data["display_name"]:
            continue
        base_item = gem_data["base_item"]
        if not base_item:
            continue
        gem_dict[gem_data["display_name"]] = {
            "variantId": gem_id,
            "gemId": gem_data["base_item"]["id"]
        }

    with open("gems.json", "w") as file:
        file.write(json.dumps(gem_dict, separators=(',', ': ')))


def get_skilltree():
    resp = requests.get(
        "https://raw.githubusercontent.com/grindinggear/skilltree-export/master/data.json")
    with open("skilltree.json", "w") as file:
        file.write(json.dumps(resp.json(), separators=(',', ': ')))


coordinate_to_jewel_hash = [
    '26725', '36634', '33989', '41263', '60735', '61834', '31683', '28475', '6230', '48768', '34483', '7960',
    '46882', '55190', '61419', '2491', '54127', '32763', '26196', '33631', '21984', '29712', '48679', '9408',
    '12613', '16218', '2311', '22994', '40400', '46393', '61305', '12161', '3109', '49080', '17219', '44169',
    '24970', '36931', '14993', '10532', '23756', '46519', '23984', '51198', '61666', '6910', '49684', '33753',
    '18436', '11150', '22748', '64583', '61288', '13170', '9797', '41876', '59585',
]


class GemData(TypedDict):
    gemId: str
    variantId: str


with open("gems.json", "r") as file:
    gem_data: dict[str, GemData] = json.load(file)

with open("skilltree.json", "r") as file:
    skilltree = json.load(file)


base_class_to_class_id = {}
ascendancy_class_to_ascendancy_class_id = {}
ascendancy_class_to_base_class = {}

for class_id, base_class in enumerate(skilltree["classes"]):
    base_class_to_class_id[base_class["name"]] = str(class_id)
    for ascendancy_class_id, ascendancy_class in enumerate(base_class["ascendancies"]):
        ascendancy_class_to_ascendancy_class_id[ascendancy_class["name"]
                                                ] = str(ascendancy_class_id + 1)
        ascendancy_class_to_base_class[ascendancy_class["name"]
                                       ] = base_class["name"]

if __name__ == "__main__":
    get_gem_dict()
    get_skilltree()
