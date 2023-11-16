#########################################################
##                                                     ##
##  A database library for managing a sqlite database. ##
##                                                     ##
#########################################################
##      run : python3 database.py help                 ##
##          for more details                           ##
#########################################################



import sqlite3, sys, os, time


default_db = "accounts.db"      ## The default name of the database


class Database:
    """ 
    A class to manage the functions of a sqlite database.

    Parameters
    -------
    name : str
        The filename of the database.
    
    testing : bool, optional
        When testing mode is enabled, it will print out the commands sent as sql queries. (Default is False)

    Attributes
    ----------
    name : str
        The filename of the database.
    table : dict of dict of str
        A dictionary of tables, in which tables are a dictionary of strings representing the columns of the table.
    primary_keys : dict of str
        A dictionary of the primary keys of each table.
    is_testing : bool
        Whether or not to have testing mode enabled.

    Methods
    -------
    create(table, primary_key):
        Creates a new row to the given table with the supplied primary key.

    fetch_all(table):
        Returns a list of all the data in every row of the given table.

    get_tables():
        Returns a list of the names of every table in the database.

    get_columns(table):
        Returns a list of the names of all the columns in the given table.

    load():
        Initalizes every table of the database. (Run this at startup before any other database code.)

    update(table, where, cells, data):
        Updates a given value or values of a particular row in a given table.


    """

    def __init__(self, name, testing = False):
        """Constructs the database class."""

        self.name = name
        self.table = {}

        self.primary_keys = {}

        self.is_test = testing

        ## ADD NEW TABLES HERE
        self.table["accounts"] = {}
        self.table["jobs"] = {}

        ## CREATE NEW METHOD TO FILL NEW TABLE IN FORMAT SHOWN BELOW
        self.init_accounts()
        self.init_jobs()


    def init_accounts(self):
        self.table["accounts"]["username"] = "TEXT PRIMARY KEY"         # data 0
        self.table["accounts"]["password"] = "TEXT"                     # data 1
        self.table["accounts"]["firstname"] = "TEXT"                    # data 2
        self.table["accounts"]["lastname"] = "TEXT"                     # data 3
        self.table["accounts"]["emailAd"] = "INTEGER"                   # data 4
        self.table["accounts"]["smsAd"] = "INTEGER"                     # data 5
        self.table["accounts"]["targetAd"] = "INTEGER"                  # data 6
        self.table["accounts"]["language"] = "TEXT"                     # data 7
        self.table["accounts"]["friend_requests"] = "TEXT"              # data 8
        self.table["accounts"]["active_requests"] = "TEXT"              # data 9
        self.table["accounts"]["friends"] = "TEXT"                      # data 10
        self.table["accounts"]["has_profile"] = "INTEGER"               # data 11
        self.table["accounts"]["title"] = "TEXT"                        # data 12
        self.table["accounts"]["major"] = "TEXT"                        # data 13
        self.table["accounts"]["university"] = "TEXT"                   # data 14
        self.table["accounts"]["info"] = "TEXT"                         # data 15
        self.table["accounts"]["experience"] = "TEXT"                   # data 16
        self.table["accounts"]["education"] = "TEXT"                    # data 17
        self.table["accounts"]["postings"] = "TEXT"                     # data 18
        self.table["accounts"]["applied"] = "TEXT"                      # data 19
        self.table["accounts"]["saved"] = "TEXT"                        # data 20
        self.table["accounts"]["is_plus"] = "INTEGER"                   # data 21
        self.table["accounts"]["inbox"] = "TEXT"                        # data 22
        self.table["accounts"]["new_job"] = "TEXT"                      # data 23

    def init_jobs(self):
        self.table["jobs"]["id"] = "INTEGER PRIMARY KEY"                # data 0
        self.table["jobs"]["title"] = "TEXT"                            # data 1
        self.table["jobs"]["desc"] = "TEXT"                             # data 2
        self.table["jobs"]["employer"] = "TEXT"                         # data 3
        self.table["jobs"]["location"] = "TEXT"                         # data 4
        self.table["jobs"]["salary"] = "TEXT"                           # data 5
        self.table["jobs"]["firstname"] = "TEXT"                        # data 6
        self.table["jobs"]["lastname"] = "TEXT"                         # data 7
        self.table["jobs"]["applications"] = "TEXT"                     # data 8

    def create(self, table, primary_key):
        """
        Creates a new row to the given table with the supplied primary key.

        All other values in the table will be initalized as '' for TEXT,
        0 for INTEGER, 0.0 for REAL, or NULL for NULL. BLOB currently not supported.

        Parameters
        ----------
        table : str
            The name of the table you want to add a new row too.

        primary_key : str or int or float or None
            Primary key of table to be set during creation.
        """

        connection = sqlite3.connect(self.name)
        cursor = connection.cursor()

        cmd = """INSERT INTO """+table+""" ("""
        cmd_cells = """"""
        cmd_values = """"""
        for k,v in self.table[table].items():
            cmd_cells = cmd_cells+k+""", """

            if self.primary_keys[table] == k:
                data = "'"+str(primary_key)+"'"
            elif v == "TEXT":
                data = "''"
            elif v == "INTEGER":
                data = "0"
            elif v == "REAL":
                data = "0.0"
            #elif data == "BLOB":
            #    data = "b''"
            else:
                data = "NULL"


            cmd_values = cmd_values+data+""", """

        cmd_cells = cmd_cells[0:-2]
        cmd_values = cmd_values[0:-2]
        cmd = cmd+cmd_cells+""") VALUES ("""
        cmd = cmd+cmd_values+""") """

        cursor.execute(cmd)

        connection.commit()
        connection.close()

        if self.is_test:
            print(cmd+"\n")

        
    def fetch_all(self, table):
        """
        Returns a list of all the data in every row of the given table.

        Parameters
        ----------
        table : str
            The name of the table you want to fetch the data from.

        Returns
        -------
        data : list of list of str
            a list of each row of the table containing a list of all the data in each row.
        """
    
        connection = sqlite3.connect(self.name)
        cursor = connection.cursor()

        cursor.execute("SELECT * FROM "+table)
        data =  cursor.fetchall()
        connection.close()
        return data

    def get_tables(self):
        """
        Returns a list of the names of every table in the database.

        Returns
        -------
        data : list of str
            a list containing the names of each table in the database.
        """
        connection = sqlite3.connect(self.name)
        cursor = connection.cursor()
        cursor.execute("""SELECT name FROM sqlite_master WHERE type='table';""")
        data = [description[0] for description in cursor.fetchall()]
        connection.close()
        return data


    def get_columns(self, table):
        """
        Returns a list of the names of all the columns in the given table.

        Parameters
        ----------
        table : str
            The name of the table you want to get the names of columns from.

        Returns
        -------
        data : list of str
            a list containing the names of each columns in the given table.
        """
        connection = sqlite3.connect(self.name)
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM "+table)
        data = [description[0] for description in cursor.description]
        connection.close()
        return data


    def load(self):
        """
        Initalizes every table of the database. (Run this at startup before any other database code.)
        It also retrieves the primary keys for each table.
        """

        connection = sqlite3.connect(self.name)
        cursor = connection.cursor()

        for k,v in self.table.items():
            table = k
            cells = v

            cmd = """CREATE TABLE IF NOT EXISTS """+table+""" (
"""    

            for k,v in cells.items():

                if "PRIMARY" in v.split(" "):
                    self.primary_keys[table] = k


                cmd = cmd+k+""" """+v+""",
"""

            cmd = cmd[0:-2]+"""
"""
            cmd = cmd+""")"""

            cursor.execute(cmd)


        connection.commit()
        connection.close()

        if self.is_test:
            print(cmd+"\n")


    def update(self, table, where, cells, data):
        """
        Updates a given value or values of a particular row in a given table.

        The cells and data parimeter can be a list or a single value, but both need to be the same size list.

        Parameters
        ----------
        table : str
            The name of the table you want to change a value in.

        where : str or int or float or None
            The value of the data in the primary key column of the paticular row you want to modify.
            It's specifically the value itself, not the name of the column.

        cells : str
            the name or names of the column(s) you want to modify in the particular row of the given table.

        data : (str or int or float or None) OR a list of (str or int or float or None)
            The value or values to set to the corresponding cell or cells.
        """

        connection = sqlite3.connect(self.name)
        cursor = connection.cursor()
        
        if type(cells) is not list: cells = [cells]
        if type(data) is not list: data = [data]


        if len(cells) != len(data):
            print("cells and data must be a list of the same size!")

        cmd = "UPDATE "+table+" SET "
        for cell in range(len(cells)):
            if "TEXT" in self.table[table][cells[cell]].split(" "):
               cmd = cmd + cells[cell] + " = " + "'"+data[cell]+"', " 
            else:
                cmd = cmd + cells[cell] + " = " + str(data[cell])+", "


        cmd = cmd[0:-2]+" "
        cmd = cmd + "WHERE "+self.primary_keys[table]+" = "+"'"+str(where)+"'"
        
        cursor.execute(cmd)

        connection.commit()
        connection.close()


        if self.is_test:
            print(cmd+"\n")


    def delete(self, table, where):
        """
        Deletes a particular row in a given table.

        Parameters
        ----------
        table : str
            The name of the table you want to delete the row from.

        where : str or int or float or None
            The value of the data in the primary key column of the paticular row you want to delete.
            It's specifically the value itself, not the name of the column.

        """
        connection = sqlite3.connect(self.name)
        cursor = connection.cursor()
        
        cmd = "DELETE from "+table+" WHERE "+self.primary_keys[table]+" = "+"'"+str(where)+"'"

        cursor.execute(cmd)

        connection.commit()
        connection.close()



def update_database():
    """
        (Hasn't really been tested.)
        "Should" update a database to the newer format whenever you make a change to the database script.
        Creates a time-stamped back-up of the previous database.

        run using : python3 database.py update

    """
    old_db = Database(default_db)

    new_db = Database("new.db")
    new_db.load()

    tables = old_db.get_tables()
    for table in tables:
        columns = old_db.get_columns(table)
        rows = old_db.fetch_all(table)
        index = 0
        if columns: index = columns[0].index(new_db.primary_keys[table])

        ##print(rows)
        ##print(columns)
        ##print("")

        for i in range(len(rows)):
            #print(rows[i])
            new_db.create(table, rows[i][index])

            for j in range(len(columns)):

                if j != index:
                    new_db.update(table, rows[i][index], columns[j], rows[i][j])

    
    t = str(time.time())
    t = t.split(".")
    t = "-".join(t)

    try:
        os.rename(default_db, default_db[0:-3]+"_old_"+t+".db")
    except FileNotFoundError:
        pass
    
    try:
        os.rename("new.db", default_db)
    except FileNotFoundError:
        pass
    
        



def delete_database(name=default_db):
    """
        Deletes the default database

        run using : python3 database.py delete
        or
        run using : python3 database.py delete (name of database)

        Parameters
        ----------
        name : str
            The name of the database you want to delete. (Default is default_db)
    """
    try:
        os.remove(name)
    except OSError:
        print(name+" doesn't exist!")


def test_database():
    """
        A simple test to check the capabilities of the database.
    
        run using : python3 database.py test

    """

    db = Database("test.db", testing=True)
    db.load()
    db.create("accounts", "good")
    db.update("accounts", "good", "password", "12345")
    db.update("accounts", "good", "username", "test")
    db.update("accounts", "test", "language", "English")
    db.update("accounts", "test", "has_profile", "1")


def clear_table_in_database(table):
    """
        Clears all the rows from a given table in the default database.
    
        run using : python3 database.py clear (table name)

    """
    db = Database(default_db)
    db.load()

    tables = db.get_tables()

    if table in tables:
        connection = sqlite3.connect(default_db)
        cursor = connection.cursor()

        cmd = "DELETE from "+table

        cursor.execute(cmd)

        connection.commit()
        connection.close()
    
    else:
        print(table+" table does not exist!")



def main():
    args = sys.argv[1:]

    if "update" in args:
        update_database()

    elif "delete" in args:
        if len(args) > 1 and args[1]:
            delete_database(args[1])
        else:
           delete_database()

    elif "clear" in args:
        if len(args) > 1 and args[1]:
            clear_table_in_database(args[1])
        else:
            print("Missing! Name of table to clear!")
    
    elif "test" in args:
        test_database()

    elif "help" in args:
        help(Database)
        print("")
        help(update_database)
        print("")
        help(delete_database)
        print("")
        help(test_database)
        print("")
        help(clear_table_in_database)
        print("")
    
    else:
        if len(args) > 0:
            print(args[0]+" is not a valid command!")



if __name__ == "__main__":
    main()
