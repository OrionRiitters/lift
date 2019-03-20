#from .db.manage_db import *

import importlib.util
spec = importlib.util.spec_from_file_location("manage_db", "/users/orionriitters/Documents/school/spring_2019/software_projects_2903/lift/python/db/manage_db.py")
manage_db = importlib.util.module_from_spec(spec)
spec.loader.exec_module(manage_db)


class DBHandler():

    instance = None

    @staticmethod
    def get_instance():
        if DBHandler.instance:
            return DBHandler.instance
        else:
            DBHandler.instance = DBHandler()
            return DBHandler.instance

    def switch(self, ui, user_input):
        """
        This function acts like a switch statement that you would find in java or another
        similar language.
        """
        dict = {
            'start_workout': '',
        }

        if template in dict.keys():
            method = getattr(self, dict.get(template))
            method()


    def selector(self, template):
        return None
