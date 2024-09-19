import base64
import json
import zlib

from item import set_gems, get_item_text, get_slot, get_slots
from passive_encode import get_passive_tree_url
from schema import Character

import xml.etree.ElementTree as ET
from data import coordinate_to_jewel_hash, ascendancy_class_to_base_class, base_class_to_class_id, ascendancy_class_to_ascendancy_class_id


with open("character.json", "r") as file:
    character: Character = json.load(file)


def create_pob_string(character: Character) -> str:
    if character["class"] in ascendancy_class_to_base_class:
        base_class = ascendancy_class_to_base_class[character["class"]]
        ascendant_class = character["class"]
        class_id = base_class_to_class_id[base_class]
        ascendancy_class_id = ascendancy_class_to_ascendancy_class_id[ascendant_class]
    else:
        base_class = character["class"]
        ascendant_class = "nil"
        class_id = base_class_to_class_id
        ascendancy_class_id = "nil"

    root = ET.Element("PathOfBuilding")
    build = ET.SubElement(
        root,
        "Build",
        level=str(character["level"]),
        targetVersion="3_0",
        pantheonMajorGod=character["passives"]["pantheon_major"],
        pantheonMinorGod=character["passives"]["pantheon_minor"],
        bandit=character["passives"]["bandit_choice"],
        className=base_class,
        ascendClassName=ascendant_class,
        characterLevelAutoMode="false",
        mainSocketGroup="1",
        viewMode="IMPORT",
    )
    ET.SubElement(
        build, "TimelessData",
        devotionVariant2="1",
        searchListFallback="",
        searchList="",
        devotionVariant1="1"
    )
    tree = ET.SubElement(root, "Tree", activeSpec="1")

    spec = ET.SubElement(
        tree,
        "Spec",
        masteryEffects=",".join(
            [f"{{{k},{v}}}" for k, v in character["passives"]["mastery_effects"].items()]),
        nodes=",".join([str(x) for x in character["passives"]["hashes"]]),
        classId=class_id,
        ascendClassId=ascendancy_class_id,
        secondaryAscendClassId="nil",
        treeVersion="_".join(character["metadata"]["version"].split(".")[:2]),
    )
    ET.SubElement(spec, "URL").text = get_passive_tree_url(int(class_id), int(ascendancy_class_id),
                                                           character["passives"]["hashes"], character["passives"]["mastery_effects"])

    jewel_sockets = ET.SubElement(spec, "Sockets")
    items = ET.SubElement(root, "Items", activeItemSet="1",
                          showStatDifferences="true", useSecondWeaponSet="nil")
    item_set = ET.SubElement(
        items, "ItemSet", useSecondWeaponSet="nil", id="1")

    item_slots = get_slots()
    item_id = 1
    for jewel in character["jewels"]:
        node_id = coordinate_to_jewel_hash[jewel["x"]]
        ET.SubElement(items, "Item", id=str(item_id)
                      ).text = get_item_text(jewel)
        ET.SubElement(jewel_sockets, "Socket",
                      nodeId=node_id, itemId=str(item_id))
        ET.SubElement(item_set, "SocketIdURL",
                      nodeId=node_id, name=f"Jewel {node_id}")
        item_id += 1

    skills = ET.SubElement(root, "Skills", sortGemsByDPSField="CombinedDPS",
                           activeSkillSet="1", sortGemsByDPS="true", defaultGemQuality="0", defaultGemLevel="normalMaximum", showSupportGemTypes="ALL", showAltQualityGems="false")
    skillset = ET.SubElement(skills, "SkillSet", id="1")

    for item in character["equipment"]:
        if item["inventoryId"] in ["Weapon2", "Offhand2"]:
            continue

        set_gems(item, skillset)
        ET.SubElement(items, "Item", id=str(item_id)
                      ).text = get_item_text(item)
        item_slots[get_slot(item)] = str(item_id)
        item_id += 1

    for slot, item_id in item_slots.items():
        ET.SubElement(item_set, "Slot", name=slot, itemId=item_id)

    ET.SubElement(root, "TreeView", searchStr="",
                  zoomY="0", zoomLevel="3", showStatDifferences="true", zoomX="0")
    pob_string = base64.urlsafe_b64encode(
        zlib.compress(ET.tostring(root))).decode('utf-8')
    return pob_string


create_pob_string(character)
