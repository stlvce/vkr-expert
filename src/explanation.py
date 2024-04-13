from typing import Union

db = [{"id": 1, "relationship": "garage-house", "distance": 3,
       "tip_text": "Расстояние между домом и гаражом должно быть больше 3 метров"},
      {"id": 2, "relationship": "baths-house", "distance": 8,
       "tip_text": "Расстояние между домом и баней должно быть больше 8 метров"}]


def receive_tip(relationship: str, distance: float) -> Union[str, None]:
    """ Метод для получения совета """

    # Поиск в бд по отношению
    rule = {}

    # Если правило есть в базе знаний, то расстояние в нем и переданое сравнивается.
    if rule and distance < rule["distance"]:
        return rule["tip_text"]

    # Если нет правила или расстояние удовалетворяет норме возращать None
    return None
