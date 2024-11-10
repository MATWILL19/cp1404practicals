"""CP1404 Prac 07 Project Management"""
"""Estimated time: 120min"""
"""Actual time: min"""

from prac_07.project import Project

MAIN_MENU = """(L)oad project
(S)ave project
(D)isplay project
(F)ilter projects by date
(A)dd new project
(U)pdate project
(Q)uit"""
FILENAME = 'projects.txt'

def main():
    """Display, filter, modify or add projects to a file"""
    print(MAIN_MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "L":
            projects = load_projects()
        # elif choice == "S":
        #
        # elif choice == "D":
        #
        # elif choice == "F":
        #
        # elif choice == "A":
        #
        # elif choice == "U":







def load_projects():
    """Load projects from csv file"""
    projects = []
    in_file = open(FILENAME, "r")
    for line in in_file:
        line.strip()


def display_projects():
    """Display projects"""

def filter_projects():
    """Filter projects by user inputted date"""

def add_project():
    """Add new project"""

def update_project():
    """Update project"""



main()