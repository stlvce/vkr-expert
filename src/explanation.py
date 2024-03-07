from typing import Union

db = [{"id": 1, "relationship": "garage-house", "distance": 3,
       "tip_text": "Расстояние между домом и гаражом должно быть больше 3 метров"},
      {"id": 2, "relationship": "baths-house", "distance": 8,
       "tip_text": "Расстояние между домом и баней должно быть больше 8 метров"}]


def receive_tip(relationship: str, distance: float) -> Union[str, None]:
    # Поиск в бд по отношению
    # Если нет, то возвращать None

    # Сравнение дистанций и возвращение совета
    # Если все нормально возращать None
    return None
