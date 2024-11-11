"""CP1404 Prac 07 Project Management"""
from sys import intern

from Tools.scripts.dutree import display

"""Estimated time: 150min"""
"""Actual time: 190min"""

from prac_07.project import Project
import datetime
MAIN_MENU = """- (L)oad project
- (S)ave project
- (D)isplay project
- (F)ilter projects by date
- (A)dd new project
- (U)pdate project
- (Q)uit"""

def main():
    """Display, filter, modify or add projects to a file"""
    print("Welcome to Pythonic Project Management")
    filename = "projects.txt"
    projects = load_projects(filename)
    number_of_projects = len(projects)
    print(f"Loaded {number_of_projects} projects from {filename}")
    print(MAIN_MENU)
    choice = input(">>> ").upper()
    projects = load_projects(filename)
    while choice != "Q":
        if choice == "L":
            print("Please enter filename")
            filename = input(">>> ")
            projects = load_projects(filename)
            print("")
            print(MAIN_MENU)
            choice = input(">>> ").upper()
        elif choice == "S":
            save_projects(projects, filename)
            print("")
            print(MAIN_MENU)
            choice = input(">>> ").upper()
        elif choice == "D":
            display_projects(projects)
            print("")
            print(MAIN_MENU)
            choice = input(">>> ").upper()
        elif choice == "F":
            filter_projects(projects)
            print("")
            print(MAIN_MENU)
            choice = input(">>> ").upper()
        elif choice == "A":
            add_project(projects)
            print("")
            print(MAIN_MENU)
            choice = input(">>> ").upper()
        elif choice == "U":
            update_project(projects)
            print("")
            print(MAIN_MENU)
            choice = input(">>> ").upper()
        else:
            print("Invalid input")
            print(MAIN_MENU)
            choice = input(">>> ").upper()
    save_choice = input(f"Would you like to save {filename}? ").upper()
    if save_choice == "Y":
        save_projects(projects, filename)
        print()
    else:
        print("Thank you for using custom-built project management software.")

def load_projects(filename):
    """Load projects from csv file"""
    projects = []
    in_file = open(filename, "r")
    next(in_file)
    for line in in_file:
        parts = line.strip().split("\t")
        start_date = datetime.datetime.strptime(parts[1], "%d/%m/%Y").date()
        project_details = Project(parts[0], start_date, int(parts[2]), float(parts[3]), int(parts[4]))
        projects.append(project_details)
    in_file.close()
    return projects

def save_projects(projects, filename):
    """Save projects to file"""
    save_file_projects = []
    for project in projects:
        parts_0 = [project.name, str(project.start_date), str(project.priority), str(project.cost_estimate),
                   str(project.completion)]
        parts_1 = " ".join(parts_0)
        save_file_projects.append(parts_1)
    for project in save_file_projects:
        print(project)
    with open(f"{filename}", "w") as out_file:
        for project in save_file_projects:
            out_file.write(project + "\n")
    return

def display_projects(projects):
    """Display loaded projects"""
    uncompleted_projects = [project for project in projects if not project.is_complete()]
    uncompleted_projects.sort()
    completed_projects = [project for project in projects if project.is_complete()]
    completed_projects.sort()
    print("Incomplete projects:")
    for project in uncompleted_projects:
        print(f"  {project.name}, {project.start_date.strftime('%d/%m/%Y')}, priority {project.priority}"
              f", estimate: ${project.cost_estimate}, completion: {project.completion}%")
    print("Completed projects:")
    for project in completed_projects:
        print(f"  {project.name}, {project.start_date.strftime('%d/%m/%Y')}, priority {project.priority}"
              f", estimate: ${project.cost_estimate}, completion: {project.completion}%")
    return



main()