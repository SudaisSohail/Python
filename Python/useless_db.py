import sqlite3 as sq

class My_database:

    def __init__(self, name):

        self.name = name

        print(name)

    def create_table(self, database_name, name_of_table, *column_and_datatype):

        try:
            conn = sq.connect(self.database_name)
            c = conn.cursor()
            
            c.execute("CREATE TABLE {} ({})".format(self.name_of_table, self.column_and_datatype))
            
            conn.commit()
            conn.close()
        
        except AttributeError as e:
            
            print(e)
            print("Method is not present")
        except Exception as f:
            print(e)
            print("Again something went wrong")

test = My_database("testing.db")

test.create_table("testing.db", "my_test", ("first_test text"))
