from script.utils import load_projects
from script.constants import NAME
from script.matching import matching_finance_tool

if __name__ == "__main__":
    list_project = load_projects()
    for project in list_project:
        finance_tool = matching_finance_tool(project)
        print(f'Per il progetto {project[NAME]} è stato scelto il piano {finance_tool}')
