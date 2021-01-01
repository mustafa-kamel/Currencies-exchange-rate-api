echo 'Starting the installation'
sleep 1s

echo 'Creating a virtual environment...'
/usr/bin/python3 -m venv env
sleep 2s

echo 'Activating the virtual environment...'
env/bin/activate