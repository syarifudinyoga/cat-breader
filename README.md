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

<!-- migrasi db -->
mkdir -p app/db/migrations
touch app/db/migrate.py

<!-- User Core -->
mkdir -p app/utils app/repositories app/services app/models
touch app/utils/password.py
touch app/models/user.py
touch app/repositories/user_repo.py
touch app/services/auth_service.py

pip install "passlib[bcrypt]"

<!-- JWT -->
pip install "python-jose[cryptography]"

touch app/utils/jwt.py

<!-- RUN APP -->
uvicorn app.main:app --reload