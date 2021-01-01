@ECHO OFF
sleep 1s

ECHO
ECHO
ECHO 'Installing the requirements'
pip install -r requirements.txt
sleep 2s

ECHO
ECHO
ECHO 'Initializing the database'
python db_init.py
sleep 2s


ECHO
ECHO
ECHO 'Creating a dump server'
uvicorn main:app --reload