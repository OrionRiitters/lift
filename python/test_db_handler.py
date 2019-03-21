#from db_handler import DBHandler

import importlib.util
spec = importlib.util.spec_from_file_location("db_handler", "/users/orionriitters/Documents/school/spring_2019/software_projects_2903/lift/python/db_handler.py")
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
DBHandler = module.DBHandler()

DBHandler.query_all_rows('lifts')
