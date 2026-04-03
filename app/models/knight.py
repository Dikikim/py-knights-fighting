class Knight:
    def __init__(self, config: dict) -> None:
        self.name: str = config["name"]

        # Base stats
        base_hp = config.get("hp", 0)
        base_power = config.get("power", 0)
        base_protection = 0

        armour_protection = sum(
            part.get("protection", 0) for part in config.get("armour", [])
        )

        weapon_power = 0
        if "weapon" in config and config["weapon"]:
            weapon_power = config["weapon"].get("power", 0)

        potion_hp, potion_power, potion_protection = 0, 0, 0
        potion = config.get("potion")

        if potion and "effect" in potion:
            effect = potion["effect"]
            potion_hp = effect.get("hp", 0)
            potion_power = effect.get("power", 0)
            potion_protection = effect.get("protection", 0)

        self.hp = base_hp + potion_hp
        self.power = base_power + weapon_power + potion_power

        self.protection = base_protection + armour_protection
        self.protection += potion_protection

    def take_damage(self, damage: int) -> None:
        self.hp -= damage
        if self.hp < 0:
            self.hp = 0
