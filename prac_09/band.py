from prac_09.musician import Musician
class Band:
    """Band class"""
    def __init__(self, name):
        """Initialize and instance of band"""
        self.name = name
        self.musicians = []

    def add(self, musician):
        """Add musicians to band"""
        self.musicians.append(musician)

    def play(self):
        """"""
        return "\n".join(musician.play() for musician in self.musicians)

    def __str__(self):
        """Returns a string of musicians and there instruments"""
        musicians_formatted = ", ".join(str(musician) for musician in self.musicians)
        return f"{self.name} {musicians_formatted}"