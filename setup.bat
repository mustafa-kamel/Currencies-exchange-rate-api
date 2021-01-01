echo 'Starting the installation'
echo '.....'

echo 'Creating the a virtual environment...'
python -m venv env

sleep 3s

echo 'Activating the virtual environment...'
env\Scripts\activate.bat

echo 'Installing the requirements...'
pip install -r requirements.txt

echo 'Initializing db_init.py'
python db_init.py

echo 'Installation process completed.'

echo 'Creating a dump server'
uvicorn main:app --reload

echo 'Now visit http://localhost:8000/rate?from_currency=usd&to_currency=eur&date=2021-01-01 to test the server'