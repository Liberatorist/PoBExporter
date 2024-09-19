import xml.etree.ElementTree as ET

from schema import Item
from data import gem_data


def get_item_text(item: Item) -> str:
    quality = ""
    sockets = ""
    level_req = ""
    limit = ""
    radius = ""

    for property in item.get("properties", []):
        if property["name"] == "Quality":
            quality = property["values"][0][0].replace(
                "+", "").replace("%", "")
        if property["name"] == "LevelReq":
            level_req = property["values"][0][0]
        if property["name"] == "Limited to":
            limit = property["values"][0][0]
        if property["name"] == "Radius":
            radius = property["values"][0][0]
    socket_group = 0
    sockets = []
    for socket_group in {socket["group"] for socket in item.get("sockets", [])}:
        sockets.append("-".join([socket["sColour"][0]
                                 for socket in item.get("sockets", []) if socket["group"] == socket_group]))
    sockets = " ".join(sockets)

    item_text = []
    item_text.append(f"Rarity: {item['rarity'].upper()}")
    if item["name"]:
        item_text.append(item["name"])
    if item["typeLine"]:
        item_text.append(item["typeLine"])
    item_text.append(f"Unique ID: {item['id']}")
    item_text.append(f"Item Level: {item['ilvl']}")
    if quality:
        item_text.append(f"Quality: {quality}")
    if sockets:
        item_text.append(f"Sockets: {sockets}")
    if level_req:
        item_text.append(f"LevelReq: {level_req}")
    if limit:
        item_text.append(f"Limited to: {limit}")
    if radius:
        item_text.append(f"Radius: {radius}")
    item_text.append(
        f"Implicits: {len(item.get('implicitMods', []) + item.get('enchantMods', []))}")
    item_text.extend(item.get("implicitMods", []))
    item_text.extend(
        ["{crafted}" + mod for mod in item.get("enchantMods", [])])
    item_text.extend(
        ["{fractured}" + mod for mod in item.get("fracturedMods", [])])
    item_text.extend(item.get("explicitMods", []))
    item_text.extend(
        ["{crafted}" + mod for mod in item.get("craftedMods", [])])
    return "\n".join(item_text)


def set_gems(item: Item, skillset: ET.Element) -> None:
    sockets: list[list[int]] = []
    for socket_group in {socket["group"] for socket in item.get("sockets", [])}:
        group_ids = []
        for idx, socket in enumerate(item.get("sockets", [])):
            if socket["group"] == socket_group:
                group_ids.append(idx)
        sockets.append(group_ids)

    for socket_group in sockets:
        skill = ET.SubElement(skillset, "Skill", {
            "mainActiveSkillCalcs": "nil",
            "includeInFullDPS": "nil",
            "label": "",
            "enabled": "true",
            "slot": get_slot(item)
        })
        for socket_id in socket_group:
            if len(item.get("socketedItems", [])) > socket_id:
                gem = item["socketedItems"][socket_id]
                if "abyssJewel" in gem:
                    continue
                ET.SubElement(skill, "Gem", get_gem_stats(gem))


def get_gem_stats(gem: Item) -> dict:
    level = "1"
    quality = "0"
    for property in gem.get("properties", []):
        if property["name"] == "Quality":
            quality = property["values"][0][0].replace(
                "+", "").replace("%", "")
        if property["name"] == "Level":
            level = property["values"][0][0].replace(" (Max)", "")
    gem_info = gem_data.get(gem["baseType"], {})

    gemId = gem_info.get("gemId")
    variantId = gem_info.get("variantId")
    return {
        "level": level,
        "quality": quality,
        "gemId": gemId,
        "variantId": variantId,
        "qualityId": "Default",
        "enabled": "true",
        "count": "nil",
        "nameSpec": gem["baseType"]
    }


def get_slot(item: Item) -> str:
    if item["inventoryId"] == "Flask":
        return f"Flask {item['x'] + 1}"
    return {
        "Weapon": "Weapon 1",
        "Offhand": "Weapon 2",
        "BodyArmour": "Body Armour",
        "Helm": "Helmet",
        "Gloves": "Gloves",
        "Boots": "Boots",
        "Ring": "Ring 1",
        "Ring2": "Ring 2",
        "Amulet": "Amulet",
        "Belt": "Belt",
    }.get(item["inventoryId"], item["inventoryId"])


def get_slots():
    return {
        "Gloves": "0",
        "Weapon 1": "0",
        "Boots Abyssal Socket 5": "0",
        "Belt Abyssal Socket 2": "0",
        "Flask 3": "0",
        "Weapon 1 Swap Abyssal Socket 4": "0",
        "Weapon 1 Abyssal Socket 5": "0",
        "Weapon 2 Abyssal Socket 5": "0",
        "Weapon 1 Swap Abyssal Socket 6": "0",
        "Weapon 1 Abyssal Socket 6": "0",
        "Weapon 2 Abyssal Socket 6": "0",
        "Weapon 2 Swap Abyssal Socket 1": "0",
        "Boots Abyssal Socket 3": "0",
        "Weapon 1 Abyssal Socket 2": "0",
        "Weapon 2 Swap Abyssal Socket 4": "0",
        "Helmet Abyssal Socket 1": "0",
        "Belt Abyssal Socket 6": "0",
        "Helmet Abyssal Socket 2": "0",
        "Helmet": "0",
        "Helmet Abyssal Socket 3": "0",
        "Weapon 2 Swap Abyssal Socket 5": "0",
        "Weapon 1 Abyssal Socket 1": "0",
        "Weapon 2 Abyssal Socket 1": "0",
        "Weapon 1 Abyssal Socket 4": "0",
        "Belt": "0",
        "Weapon 1 Swap Abyssal Socket 2": "0",
        "Boots Abyssal Socket 4": "0",
        "Weapon 2 Abyssal Socket 2": "0",
        "Flask 5": "0",
        "Weapon 1 Swap Abyssal Socket 3": "0",
        "Boots Abyssal Socket 2": "0",
        "Belt Abyssal Socket 3": "0",
        "Body Armour Abyssal Socket 1": "0",
        "Gloves Abyssal Socket 1": "0",
        "Helmet Abyssal Socket 5": "0",
        "Helmet Abyssal Socket 6": "0",
        "Weapon 1 Swap Abyssal Socket 1": "0",
        "Weapon 2 Swap Abyssal Socket 2": "0",
        "Flask 1": "0",
        "Helmet Abyssal Socket 4": "0",
        "Gloves Abyssal Socket 5": "0",
        "Body Armour Abyssal Socket 2": "0",
        "Amulet": "0",
        "Weapon 1 Abyssal Socket 3": "0",
        "Weapon 2 Abyssal Socket 3": "0",
        "Belt Abyssal Socket 4": "0",
        "Belt Abyssal Socket 1": "0",
        "Body Armour Abyssal Socket 3": "0",
        "Weapon 2 Swap": "0",
        "Flask 4": "0",
        "Flask 2": "0",
        "Weapon 2": "0",
        "Belt Abyssal Socket 5": "0",
        "Boots Abyssal Socket 1": "0",
        "Body Armour Abyssal Socket 4": "0",
        "Weapon 2 Swap Abyssal Socket 6": "0",
        "Weapon 2 Swap Abyssal Socket 3": "0",
        "Weapon 1 Swap": "0",
        "Ring 2": "0",
        "Gloves Abyssal Socket 2": "0",
        "Body Armour Abyssal Socket 6": "0",
        "Weapon 1 Swap Abyssal Socket 5": "0",
        "Weapon 2 Abyssal Socket 4": "0",
        "Body Armour": "0",
        "Ring 1": "0",
        "Gloves Abyssal Socket 3": "0",
        "Body Armour Abyssal Socket 5": "0",
        "Gloves Abyssal Socket 4": "0",
        "Gloves Abyssal Socket 6": "0",
        "Boots": "0",
        "Boots Abyssal Socket 6": "0"
    }
