"""CP1404 Practical 6 - programming language class"""
"""Estimated time = 45m 9:20am
Actual time = """

class ProgrammingLanguage:
    """Identify if a language is dynamic"""
    def __init__(self, name="", typing="", reflection=False, year=0):
        """Initialize a Programming Language instance"""
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def is_dynamic(self):
        """Determine if a language is dynamic"""
        if self.typing == "Dynamic":
            return True

    def __str__(self):
      """Return a string with programming language name, typing, reflection and year"""
      return f"{self.name}, {self.typing} Typing, reflection={self.reflection}, First appeared in {self.year}"
