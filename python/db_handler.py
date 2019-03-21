# This is a current workaround to import ManageDB using an absolute path.
# It seems a bit excessive
# but everyone at https://stackoverflow.com/questions/67631/how-to-import-a-module-given-the-full-path
# seems to like it.
import importlib.util
spec = importlib.util.spec_from_file_location("manage_db", "/users/orionriitters/Documents/school/spring_2019/software_projects_2903/lift/python/db/manage_db.py")
manage_db = importlib.util.module_from_spec(spec)
spec.loader.exec_module(manage_db)
ManageDB = manage_db.ManageDB


class DBHandler():
    """
    This class will contain the business logic for the Lift app. Template names will be used as arguments to
    selector(), which will in turn call other methods. Methods being called on by selector() will call on
    DBManager methods to query the database.
    """

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
        Python implementation of switch statement.
        """
        dict = {
            'start_workout': '',
        }

        if template in dict.keys():
            method = getattr(self, dict.get(template))
            method()


    def selector(self, template):
        """
        This method will call other instance methods using template and switch(). Template is the name of the template that this
        class will load information for.
        """
        return None


    def query_all_rows(self, table):
        """
        Queries every row in a given table.
        """
        rowid = 1
        rows = []
        while True:
            row = getattr(ManageDB, 'query_' + table)
            print(row)
            if row:
                rows.append(row)
            rowid += 1
            else:
                break
