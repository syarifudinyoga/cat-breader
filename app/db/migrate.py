import os
from app.config.database import Database

MIGRATION_TABLE = """
CREATE TABLE IF NOT EXISTS schema_migrations (
    version VARCHAR(50) PRIMARY KEY,
    filename VARCHAR(255),
    executed_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
"""

class Migrator:
    def __init__(self):
        self.db = Database()

    def prepare(self):
        self.db.execute(MIGRATION_TABLE)

    def applied_versions(self):
        rows = self.db.execute(
            "SELECT version FROM schema_migrations;", 
            fetchAll=True
        )
        return {row['version'] if isinstance(row, dict) else row[0] for row in rows}
    
    def run(self):
        self.prepare()

        applied = self.applied_versions()
        migration_path = "app/db/migrations"

        files = sorted(os.listdir(migration_path))

        for file in files:
            if not file.endswith(".sql"):
                continue

            version = file.split("_")[0]

            if version in applied:
                continue

            with open(f"{migration_path}/{file}", "r") as f:
                sql = f.read()

            self.db.execute(sql)
            self.db.execute(
                "INSERT INTO schema_migrations (version, filename) VALUES (%s, %s);",
                (version, file)
            )