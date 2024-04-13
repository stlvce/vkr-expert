from shapely.geometry import Polygon
from .schemas import BuildingInfo


class Building(Polygon):
    """
    Class for all buildings
    """

    def __new__(cls, x: int, y: int, width: int, length: int, **kwargs):
        second_point = (x + width, y)
        third_point = (x + width, y - length)
        fourth_point = (x, y - length)
        return super().__new__(cls, [(x, y), second_point, third_point, fourth_point], **kwargs)


def calculate_distance(obj1_info: BuildingInfo, obj2_info: BuildingInfo) -> float:
    """ Расчет расстояния между двумя строениями """

    building1 = Building(obj1_info["x"], obj1_info["y"], obj1_info["width"], obj1_info["length"])
    building2 = Building(obj2_info["x"], obj2_info["y"], obj2_info["width"], obj2_info["length"])

    return building1.distance(building2)
