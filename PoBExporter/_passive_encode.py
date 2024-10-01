import base64

from PoBExporter._fetch import skilltree


def get_passive_tree_url(classId: int, ascendClassId: int, allocNodes: list[int], masterySelections: dict[str, int]) -> str:
    data = [0, 0, 0, 6, classId,  ascendClassId]
    node_count = 0
    cluster_count = 0
    mastery_count = 0

    cluster_node_ids = []
    mastery_node_ids = []
    nodes = []

    for id in allocNodes:
        node = skilltree["nodes"][str(id)]
        if "classStartIndex" in node or "isAscendancyStart" in node:
            continue
        if id < 65536 and node_count < 255:
            nodes.append(id // 256)
            nodes.append(id % 256)
            node_count += 1
            if id in masterySelections:
                effect_id = int(masterySelections[id])
                mastery_node_ids.append(effect_id // 256)
                mastery_node_ids.append(effect_id % 256)
                mastery_node_ids.append(id // 256)
                mastery_node_ids.append(id % 256)
                mastery_count += 1
        elif id >= 65536:
            cluster_id = id - 65536
            cluster_node_ids.append(cluster_id // 256)
            cluster_node_ids.append(cluster_id % 256)
            cluster_count += 1

    data.append(node_count)
    data.extend(nodes)

    data.append(cluster_count)
    data.extend(cluster_node_ids)

    data.append(mastery_count)
    data.extend(mastery_node_ids)
    encoded_data = base64.urlsafe_b64encode(bytes(data)).decode('utf-8')
    final_data = encoded_data.replace("+", "-").replace("/", "_")
    return "https://www.pathofexile.com/passive-skill-tree/" + final_data
