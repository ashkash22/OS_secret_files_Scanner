class BasePlugin:
    def __init__(self):
        self.output = None
        self.result = {'check': 'base_check',
                       'vulnerable': False, 'patterns_found': None}
        self.run()
        self.check_output()

    def run(self):
        return False

    def check_output(self):
        return False
