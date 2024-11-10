"""CP1404 Practical 7 - Guitar"""
"""Estimated = 60m
Actual = 40m"""

class Guitar:
    """Identify the age and vintage status of a guitar"""
    def __init__(self, name="", year=int(), cost=float()):
        """Initialize a guitar instance"""
        self.name = name
        self.year = year
        self.cost = cost

    def get_age(self):
        """Get the age of a guitar"""
        age = 2024 - self.year
        return age

    def is_vintage(self):
        """Determine if the guitar is vintage"""
        if self.year <= 1976:
            return "(vintage)"
        else:
            return ""
    def __lt__(self):
        """This method will sort guitars by year"""

    def __str__(self):
        """Return a string with guitar names, year and cost"""
        return f"{self.name}, {self.year}, {self.cost}"