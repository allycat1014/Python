class Crash_type_to_damage:
    def __init__(self, first_crash_type):
        self.first_crash_type = first_crash_type
        self.total_damage = 0

    def parseDamage(self, damage):
        if 'OVER' in damage:
            damage = damage.split("$")
            damage = damage[1].split(",")
            damage = int(damage[0] + damage[1])
        elif "OR LESS" in damage:
            damage = damage.split("O")
            damage = damage[0].split("$")
            damage = int(damage[1])
        elif "-" in damage:
            damage = damage.split("-")
            less = damage[0].split("$")
            more = damage[1].split("$")
            more1 = more[1].split(",")
            more1 = more1[0] + more1[1]
            average = (int(less[1]) + int(more1))
            average = average / 2
            damage = average
        return damage

    def add_to_total_damage(self, damage):
        damage = self.parseDamage(damage)
        self.total_damage = self.total_damage + damage


    def __repr__(self):
        return repr((self.first_crash_type, self.total_damage))

