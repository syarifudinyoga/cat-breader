from app.config.env import settings
import psycopg2
import pymysql

class Database:
    def __init__(self):
        self.driver = settings.DB_DRIVER
        self.conn = None

    def connect(self):
        if self.driver == "postgres":
            self.conn = psycopg2.connect(
                host=settings.DB_HOST,
                port=settings.DB_PORT,
                database=settings.DB_NAME,
                user=settings.DB_USER,
                password=settings.DB_PASSWORD
            )
        elif self.driver == "mysql":
            self.conn = pymysql.connect(
                host=settings.DB_HOST,
                port=settings.DB_PORT,
                database=settings.DB_NAME,
                user=settings.DB_USER,
                password=settings.DB_PASSWORD,
                cursorclass=pymysql.cursors.DictCursor
            )
        else:
            raise ValueError("Unsupported database driver")
    
    def execute(self, query, params=None, fetchOne=False, fetchAll=False):
        if not self.conn:
            self.connect()
        
        with self.conn.cursor() as cursor:
            cursor.execute(query, params or [])

            if fetchOne:
                return cursor.fetchone()
            
            if fetchAll:
                return cursor.fetchall()
            
            self.conn.commit()