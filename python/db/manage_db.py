

import sqlite3
"""
These functions are used to query and modify the lift database
using sqlite3.
"""

DATABASE = 'lift.db'

def open_close_connection(func):
    """
    A decorator to pull the opening and closing of connections outside of each function.
    """
    def decorated_function(*args):
        try:
            db = sqlite3.connect(DATABASE)
            db.row_factory = sqlite3.Row # Allows access to column names in query results

            cur = db.cursor()
            cur.execute('PRAGMA foreign_keys = ON')

            returnable = func(db, cur, *args)

            db.commit()

            if returnable: # Returns query results if decorated function is a query
                return returnable

        except sqlite3.Error:
            raise sqlite3.Error
        finally:
            db.close()
    return decorated_function


@open_close_connection
def create_workouts_table(db, cur):
    """
    Creates workouts table.
    """
    with db:
        cur.execute("""
        CREATE TABLE IF NOT EXISTS workouts (
          rowid   INTEGER    NOT NULL   PRIMARY KEY,
          name    TEXT       NOT NULL
        );
        """)

@open_close_connection
def create_lifts_table(db, cur):
    """
    Creates lifts table.
    """
    with db:
        cur.execute("""
        CREATE TABLE IF NOT EXISTS lifts (
          rowid   INTEGER    NOT NULL   PRIMARY KEY,
          name    TEXT       NOT NULL,
          sets    INTEGER    NOT NULL,
          reps    INTEGER    NOT NULL
        );
        """)

@open_close_connection
def create_days_table(db, cur):
    """
    Creates days table.
    """
    with db:
        cur.execute("""
        CREATE TABLE IF NOT EXISTS days (
          rowid      INTEGER    NOT NULL   PRIMARY KEY,
          name       TEXT       NOT NULL,
          workout_id INTEGER    NOT NULL,
          FOREIGN KEY(workout_id) REFERENCES workouts(rowid)
        );
        """)

@open_close_connection
def create_lifts_days_association_table(db, cur):
    """
    Creates an association table for the lifts table and days table.
    """
    with db:
        cur.execute("""
        CREATE TABLE IF NOT EXISTS lifts_days_association (
          rowid     INTEGER    NOT NULL   PRIMARY KEY,
          lift_id   INTEGER    NOT NULL,
          day_id    INTEGER    NOT NULL,
          FOREIGN KEY(lift_id) REFERENCES lifts(rowid),
          FOREIGN KEY(day_id)  REFERENCES days(rowid)
        );
        """)

@open_close_connection
def add_workout(db, cur, values):
    """
    Adds a row to the workouts table.
    """
    print(values['name'])
    with db:
        cur.execute("""
        INSERT INTO workouts
          (name)
        VALUES
          (?);
        """,
        ([values['name']])
        )

@open_close_connection
def add_day(db, cur, values):
    """
    Adds a row to the days table.
    """
    with db:
        cur.execute("""
        INSERT INTO days
          (name, workout_id)
        VALUES
          (?, ?)
        """,
        (values['name'], values['workoutID'])
        )

@open_close_connection
def add_lift(db, cur, values):
    """
    Adds a row to the lifts table.
    """
    with db:
        cur.execute("""
        INSERT INTO lifts
          (name, sets, reps)
        VALUES
          (?, ?, ?)
        """,
        (values['name'], values['sets'], values['reps'])
    )

@open_close_connection
def add_lifts_days_association(db, cur, values):
    """
    Adds a row to the lifts_days_association table
    """
    with db:
        cur.execute("""
        INSERT INTO lifts_days_association
          (lift_id, day_id)
        VALUES
          (?, ?)
        """,
        (values['liftID'], values['dayID'])
        )

@open_close_connection
def query_workouts(db, cur, values):
    """
    Queries a row from programs table
    """
    with db:
        cur.execute("""
        SELECT * FROM workouts
        WHERE rowid = (?)
        """,
        ([values['rowid']])
        )

    row = cur.fetchone()
    if row:
        return row['name']
    else:
        return None

@open_close_connection
def query_lifts(db, cur, values):
    """
    Queries a row from lifts table
    """
    with db:
        cur.execute("""
        SELECT * FROM lifts
        WHERE rowid = (?)
        """,
        ([values['rowid']])
        )

    row = cur.fetchone()
    if row:
        return row['name']
    else:
        return None

@open_close_connection
def query_days(db, cur, values):
    """
    Queries a row from days table
    """
    with db:
        cur.execute("""
        SELECT * FROM days
        WHERE rowid = (?)
        """,
        ([values['rowid']])
        )

    row = cur.fetchone()
    if row:
        return row['name']
    else:
        return None
