from typing import TypedDict, List


class BuildingInfo(TypedDict):
    id: int
    x: int
    y: int
    width: int
    length: int
    type: str


class Tips(TypedDict):
    id: int
    list: List[str]


class DataForExpert(TypedDict):
    modified_building: BuildingInfo
    other_buildings: List[BuildingInfo]
