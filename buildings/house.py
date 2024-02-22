from experta import Fact, KnowledgeEngine, Rule, AS, L, P


class BuildingLocationRules(KnowledgeEngine):
    @Rule(Fact(building="bathhouse", distance=P(lambda x: x < 8)))
    def rule_bathhouse(self):
        print("Расстояние между домом и баней должно быть больше 8 метров")

    @Rule(AS.variant << Fact(building=L('red_border') | L('well'), distance=P(lambda x: x < 5)))
    def rule_outbuildings(self, variant):
        print("Расстояние между домом и баней должно быть больше 5 метров", variant["building"])


engine = BuildingLocationRules()


def call_expert(building: str, distance: int):
    engine.reset()
    engine.declare(Fact(building=building, distance=distance))
    engine.run()


call_expert("bathhouse", 5)
print(engine.get_rules())
