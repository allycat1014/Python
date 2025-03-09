class Crash_type_to_damage:
    def __init__(self, crash_type):
        self.crash_type = crash_type
        self.total_damage = 0
        def __repr__(self):
            return repr((self.crash_type))

