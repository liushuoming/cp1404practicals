

from project import Project
from datetime import datetime


def load_projects(filename):
    projects = []
    with open(filename, "r") as file:
        next(file)  # skip header
        for line in file:
            parts = line.strip().split("\t")
            if len(parts) == 5:
                project = Project(*parts)
                projects.append(project)
    return projects


def save_projects(projects, filename):
    with open(filename, "w") as file:
        print("Name\tStart Date\tPriority\tCost Estimate\tCompletion Percentage", file=file)
        for p in projects:
            print(f"{p.name}\t{p.start_date.strftime('%d/%m/%Y')}\t{p.priority}\t{p.cost_estimate}\t{p.completion_percentage}", file=file)


def display_projects(projects):
    incomplete = sorted([p for p in projects if not p.is_complete()])
    complete = sorted([p for p in projects if p.is_complete()])
    print("Incomplete projects:")
    for p in incomplete:
        print(f"  {p}")
    print("Completed projects:")
    for p in complete:
        print(f"  {p}")


def filter_projects_by_date(projects):
    date_str = input("Show projects that start after date (dd/mm/yyyy): ")
    try:
        date = datetime.strptime(date_str, "%d/%m/%Y").date()
        filtered = sorted([p for p in projects if p.start_date > date], key=lambda p: p.start_date)
        for p in filtered:
            print(p)
    except ValueError:
        print("Invalid date format.")


def add_new_project():
    name = input("Name: ")
    start_date = input("Start date (dd/mm/yyyy): ")
    priority = int(input("Priority: "))
    cost_estimate = float(input("Cost estimate: "))
    completion_percentage = int(input("Percent complete: "))
    return Project(name, start_date, priority, cost_estimate, completion_percentage)


def update_project(projects):
    for i, p in enumerate(projects):
        print(f"{i} - {p}")
    try:
        index = int(input("Project choice: "))
        project = projects[index]
        new_percentage = input("New percentage (leave blank to keep current): ")
        new_priority = input("New priority (leave blank to keep current): ")

        if new_percentage:
            project.completion_percentage = int(new_percentage)
        if new_priority:
            project.priority = int(new_priority)
    except (ValueError, IndexError):
        print("Invalid selection.")


def main():
    FILENAME = "projects.txt"
    projects = load_projects(FILENAME)
    MENU = """\nMenu:
L - Load projects  
S - Save projects  
D - Display projects  
F - Filter projects by date  
A - Add new project  
U - Update project  
Q - Quit"""
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "L":
            filename = input("Filename: ")
            projects = load_projects(filename)
        elif choice == "S":
            filename = input("Filename: ")
            save_projects(projects, filename)
        elif choice == "D":
            display_projects(projects)
        elif choice == "F":
            filter_projects_by_date(projects)
        elif choice == "A":
            project = add_new_project()
            projects.append(project)
        elif choice == "U":
            update_project(projects)
        else:
            print("Invalid choice.")
        print(MENU)
        choice = input(">>> ").upper()

    save = input("Would you like to save to the default file? (Y/N): ").upper()
    if save == "Y":
        save_projects(projects, FILENAME)
        print("Projects saved.")


if __name__ == "__main__":
    main()
