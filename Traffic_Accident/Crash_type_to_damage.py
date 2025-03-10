class Crash_type_to_damage:
    def __init__(self, first_crash_type):
        self.first_crash_type = first_crash_type
        self.total_damage = 0
        def __repr__(self):
            return repr((self.first_crash_type))

