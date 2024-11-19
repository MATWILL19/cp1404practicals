"""CP1404 Prac 07 Project Management"""

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
        elif choice == "S":
            save_projects(projects, filename)
        elif choice == "D":
            display_projects(projects)
        elif choice == "F":
            filter_projects(projects)
        elif choice == "A":
            add_project(projects)
        elif choice == "U":
            update_project(projects)
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
    """Sorts and Displays loaded projects"""
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

def filter_projects(projects):
    """Filter projects by user inputted date"""
    date_string = input("Date (d/m/yyyy): ")
    filter_date = datetime.datetime.strptime(date_string, "%d/%m/%Y").date()
    filtered_projects = [project for project in projects if project.filter_date(filter_date)]
    for project in filtered_projects:
        print(f"  {project.name}, {project.start_date.strftime('%d/%m/%Y')}, priority {project.priority}"
              f", estimate: ${project.cost_estimate}, completion: {project.completion}%")
    return

def add_project(projects):
    """Add new project from user input"""
    print("Lets add a new project")
    print("Project name")
    name = input(">>> ")
    print("Project start date (dd/mm/yyyy)")
    start_date = error_check_date_input()
    print("Priority")
    priority = error_check_integer_input()
    print("Cost estimate")
    cost_estimate = error_check_float_input()
    print("Completion")
    completion = error_check_integer_input()
    project_details = Project(name, start_date, priority, cost_estimate, completion)
    projects.append(project_details)
    return projects

def update_project(projects):
    """Update project from user input"""
    for i, project in enumerate(projects):
        print(f"{i} {project.name}, {project.start_date.strftime('%d/%m/%Y')}, priority {project.priority}"
              f", estimate: ${project.cost_estimate}, completion: {project.completion}%")
    project_choice = int(input("Project choice: "))
    selected_project = projects[project_choice]
    print(f"{selected_project.name}, {selected_project.start_date.strftime('%d/%m/%Y')}, priority {selected_project.priority}"
          f", estimate: ${selected_project.cost_estimate}, completion: {selected_project.completion}%")
    print("New completion: ")
    completion = error_check_integer_input()
    print("New priority: ")
    priority = error_check_integer_input()
    if completion == "":
        completion = selected_project.completion
    if priority == "":
        priority = selected_project.priority
    projects[project_choice] = Project(selected_project.name, selected_project.start_date, priority, selected_project.cost_estimate, completion)
    return projects

def error_check_integer_input():
    """Error check integer inputs"""
    while True:
        try:
            integer_input = int(input(">>> "))
            while integer_input < 0 or integer_input > 100:
                print("Number must be >= 0 or <=100")
                integer_input = int(input(">>> "))
            return integer_input
        except ValueError:
            print("Invalid input; enter a valid number")

def error_check_float_input():
    """Error check float inputs"""
    while True:
        try:
            float_input = float(input(">>> "))
            while float_input < 0:
                print("Number must be >= 0")
                float_input = float(input(">>> "))
            return float_input
        except ValueError:
            print("Invalid input; enter a valid number")

def error_check_date_input():
    """Error check date inputs"""
    while True:
        try:
            date_input = input(">>> ")
            start_date = datetime.datetime.strptime(date_input, "%d/%m/%Y").date()
            return start_date
        except ValueError:
            print("Invalid input; enter a date using dd/mm/yyyy format")

main()