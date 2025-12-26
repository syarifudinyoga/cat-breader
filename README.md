mkdir cat_breader
cd cat_breader

conda deactivate (keluar dari conda)

python3 -m venv venv
source venv/bin/activate

pip install fastapi uvicorn python-dotenv

<!-- Initial App -->
mkdir app
touch app/main.py
touch .env

<!-- Config Database -->
mkdir -p app/config
touch app/config/env.py
touch app/config/database.py

pip install psycopg2-binary pymysql


<!-- RUN APP -->
uvicorn app.main:app --reload