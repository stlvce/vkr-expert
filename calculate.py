from shapely.geometry import Polygon
from typing import TypedDict, Union


# TODO использовать pydantic
class BuildingInfo(TypedDict):
    id: int
    x: int
    y: int
    width: int
    height: int
    type: str


class Building(Polygon):
    """
    Class for all buildings
    """

    def __new__(cls, x: int, y: int, width: int, height: int, **kwargs):
        second_point = (x + width, y)
        third_point = (x + width, y - height)
        fourth_point = (x, y - height)
        return super().__new__(cls, [(x, y), second_point, third_point, fourth_point], **kwargs)


def receive_tip(distance: Union[int, float]) -> str:
    pass


def calculate_distance(obj1_info: BuildingInfo, obj2_info: BuildingInfo) -> ValueError or str:
    building1 = Building(obj1_info["x"], obj1_info["y"], obj1_info["width"], obj1_info["height"])
    building2 = Building(obj2_info["x"], obj2_info["y"], obj2_info["width"], obj2_info["height"])
    distance = building1.distance(building2)

    if distance == 0.0:
        raise ValueError("Строения пересекаются")

    # TODO call expert class
    return "12 метров"


obj1 = {"id": 1, "x": 1, "y": 4, "width": 1, "height": 1, "type": "house"}
obj2 = {"id": 2, "x": 3, "y": 2, "width": 2, "height": 2, "type": "house"}
obj3 = {"id": 3, "x": 4, "y": 2, "width": 1, "height": 2, "type": "house"}

print(calculate_distance(obj1, obj3))
