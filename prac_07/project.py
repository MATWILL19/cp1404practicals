"""CP1404 Prac 07 Project Management"""

class Project:
    """"""
    def __init__(self, name, start_date, priority, cost_estimate, completion):
        self.name = name
        self.start_date = start_date
        self.priority = priority
        self.cost_estimate = cost_estimate
        self.completion = completion

    def is_complete(self):
        return self.completion == 100

    def __lt__(self, other):
        """This method will sort projects by priority"""
        return self.priority < other.priority

    def filter_date(self, filter_date):
        """This method will sort projects by date"""
        return self.start_date > filter_date

    def __str__(self):
        """Return a string with name, date, priority, cost and completion"""
        return f"{self.name}, {self.start_date}, {self.priority}, {self.cost_estimate}, {self.completion}"
