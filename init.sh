echo 'Installing the requirements'
env/bin/pip install -r requirements.txt

echo 'Initializing the database'
/usr/bin/python3 db_init.py

echo 'Creating a dump server'
uvicorn main:app --reload