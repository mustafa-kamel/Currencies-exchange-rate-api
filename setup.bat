@ECHO OFF
ECHO 'Starting the installation'
sleep 1s

ECHO 'Creating a virtual environment'
python -m venv env
sleep 2s

ECHO 'Activating the virtual environment'
env\Scripts\activate.bat