from app.config.env import settings
import psycopg2
from psycopg2.extras import RealDictCursor
import pymysql

class Database:
    def __init__(self):
        self.driver = settings.DB_DRIVER
        self.conn = None
        self.connect()  # ⬅️ WAJIB

    def connect(self):
        try:
            if self.driver == "postgres":
                self.conn = psycopg2.connect(
                    host=settings.DB_HOST,
                    port=settings.DB_PORT,
                    dbname=settings.DB_NAME,
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
                    cursorclass=pymysql.cursors.DictCursor,
                    autocommit=False
                )

            else:
                raise ValueError("Unsupported database driver")

        except Exception as e:
            print("DB CONNECTION ERROR:", e)
            raise

    def execute(self, query, params=None, fetchOne=False):
        if not self.conn:
            raise RuntimeError("Database connection is not initialized")

        # PostgreSQL
        if self.driver == "postgres":
            with self.conn.cursor(cursor_factory=RealDictCursor) as cur:
                cur.execute(query, params)
                self.conn.commit()

                if fetchOne:
                    return cur.fetchone()
                return cur.fetchall()

        # MySQL
        elif self.driver == "mysql":
            with self.conn.cursor() as cur:
                cur.execute(query, params)
                self.conn.commit()

                if fetchOne:
                    return cur.fetchone()
                return cur.fetchall()
