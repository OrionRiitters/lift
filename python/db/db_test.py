import importlib.util
spec = importlib.util.spec_from_file_location("manage_db", "/users/orionriitters/Documents/school/spring_2019/software_projects_2903/lift/python/db/manage_db.py")
manage_db = importlib.util.module_from_spec(spec)
spec.loader.exec_module(manage_db)
manage_db = manage_db.ManageDB()

#print(manage_db.query_days({'rowid': 1}))

manage_db.create_workouts_table()
