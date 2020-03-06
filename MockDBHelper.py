class MockDBHelper:
    def connect(self, database='crimemap'):
        pass

    def get_all_inputs(self):
        return []

    def add_input(self, data):
        pass

    def clear_all(self):
        pass

    def add_crime(self, category, date, description):
        pass

    def get_all_crimes(self):
        return [{
            'date': "2020-03-05",
            'category': "mugging",
            "description": "mock description"
        }]

