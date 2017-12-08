import mysql.connector

class Database:
    HOST = "localhost"
    USER = "root"
    PASSWD = "root"
    NAME = "animal_shelter"

    USER_TABLE = "`user`"
    USER_ID = "id"
    USER_USERNAME = "username"
    USER_PASSWORD = "password"
    CREATE_USER_TABLE = "CREATE TABLE " + USER_TABLE + " ( " + \
        USER_ID + " INTEGER NOT NULL AUTO_INCREMENT, " + \
        USER_USERNAME + " varchar(50) NOT NULL UNIQUE, " + \
        USER_PASSWORD + " varchar(50) NOT NULL, " + \
        "PRIMARY KEY (" + USER_ID + "));"
    DROP_USER_TABLE = "DROP TABLE IF EXISTS " + USER_TABLE + ";"

    @staticmethod
    def connect():
        return mysql.connector.connect(user=Database.USER,
                password=Database.PASSWD, database=Database.NAME,
                host=Database.HOST)

    @staticmethod
    def create_user_table():
        cnx = Database.connect()
        cursor = cnx.cursor()
        cursor.execute(Database.CREATE_USER_TABLE)
        # Create default user: admin/admin
        cursor.execute("INSERT INTO " + Database.USER_TABLE + " ({}, {}, {}) ".format(
                Database.USER_ID, Database.USER_USERNAME, Database.USER_PASSWORD) + \
                "VALUES ({}, '{}', '{}');".format(1, "admin", "admin")) 
        cnx.commit()

    @staticmethod
    def drop_user_table():
        cnx = Database.connect()
        cursor = cnx.cursor()
        cursor.execute(Database.DROP_USER_TABLE)

    @staticmethod
    def valid(username, password):
        cnx = Database.connect()
        cursor = cnx.cursor()
        cursor.execute(
                "SELECT {} FROM {} WHERE {} = %s AND {} = %s".format(
                    Database.USER_ID, Database.USER_TABLE,
                    Database.USER_USERNAME, Database.USER_PASSWORD),
            (username, password))
        data = cursor.fetchone()
        return data



Database.drop_user_table()
Database.create_user_table()
