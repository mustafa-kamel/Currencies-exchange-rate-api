@ECHO OFF

ECHO Installing the requirements
pip install -r requirements.txt

ECHO Initializing the database
python db_init.py

ECHO Creating a dump server
uvicorn main:app --reload