"""CP1404 Practical 6 - programming language class"""
"""Estimated time = 45m 9:20am
Actual time = """

class ProgrammingLanguage:
    """"""
    def __init__(self, field="", typing="", reflection=False, year=0):
        """Initialize a Programming Language instance"""
        self.field = field
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def is_dynamic(self):
        """Determine if a language is dynamic"""
        if self.typing == "Dynamic":

    def __str__(self):
      """Return a string with programming language name, typing, reflection and year"""
      return f"{self.field}, {self.typing} Typing, reflection={self.reflection}, First appeared in {self.year}"
