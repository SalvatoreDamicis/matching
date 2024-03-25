import pandas as pd
from script.constants import DATA_FOLDER
import os
from typing import List, Dict, Any


def load_data(path_excel: str) -> pd.DataFrame:
    """ This function read an excel file and return a pandas dataframe"""
    path = os.path.join(DATA_FOLDER, path_excel)
    return pd.read_excel(path)


def load_projects() -> List[Dict[str, Any]]:
    """ This function load the project and return a list of projects objects"""
    df_projects = load_data('projects_data.xlsx')
    list_projects = df_projects.to_dict(orient='records')
    return list_projects
