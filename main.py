from src.schemas import DataForExpert
from src.calculate import calculate_distance
from src.explanation import receive_tip
from typing import List


def expert(data: DataForExpert) -> List[str]:
    modified_building = data["modified_building"]
    result_tips = []

    for building in data["other_buildings"]:
        distance = calculate_distance(modified_building, building)
        sorted_types = sorted([modified_building["type"], building["type"]])
        relationship = "-".join(sorted_types)
        tip = receive_tip(relationship, distance)

        if tip is not None:
            result_tips.append(tip)

    return result_tips


data_from_client = {
    "modified_building": {"id": 1, "x": 1, "y": 4, "width": 1, "length": 1, "type": "house"},
    "other_buildings": [
        {"id": 2, "x": 3, "y": 2, "width": 2, "length": 2, "type": "garage"},
        {"id": 3, "x": 4, "y": 2, "width": 1, "length": 2, "type": "baths"}
    ]
}

expert(data_from_client)
