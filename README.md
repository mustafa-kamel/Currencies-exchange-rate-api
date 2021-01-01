Currencies Exchange Rate Api
===========================
This is a simple service built by FastAPI that provides the exchange rate between the two passed currencies on the passed date


Requirements
------------
> You should have the following requirements installed
* Python 3
* PostgreSQL 13


Installation
------------
1. Clone the project `git clone https://github.com/Mustafa-Kamel/Currencies-exchange-rate-api`
2. Change the active directory to the project directory `cd Currencies-exchange-rate-api`
3. You can simply setup the project using `setup.bat` for Windows users or `setup.sh` for Linux users
4. Open `ratedbhandle.py` file in any text editor and edit the database `username` and `password` to your database `username` and `password`
5. Now visit the [API] (http://localhost:8000/rate?from_currency=usd&to_currency=eur&date=2021-01-01)

> To setup it manually go on with the next setps

### Windows

4. Create a virual environment `python -m venv env`
5. Activate the virtual environment `env\Scripts\activate.bat`
6. Install the requirements `pip install -r requirements.txt`
7. Initialize `db_init.py` `3 db_init.py` you will be asked to enter the credentials for the PostgreSQL server (i.e. `username` and `password`)
8. Open `ratedbhandle.py` file in any text editor and edit the database `username` and `password` to your database `username` and `password`
9. Return to cmd and create a dump server `uvicorn main:app --reload`
10. Now visit the [API] (http://localhost:8000/rate?from_currency=usd&to_currency=eur&date=2021-01-01)

### Linux
4. Create a virual environment `/usr/bin/python3 -m venv env`
5. Activate the virtual environment `env/bin/activate`
6. Install the requirements `env/bin/pip install -r requirements.txt`
7. Initialize `db_init.py` `/usr/bin/python3 db_init.py` you will be asked to enter the credentials for the PostgreSQL server (i.e. `username` and `password`)
8. Open `ratedbhandle.py` file in any text editor and edit the database `username` and `password` to your database `username` and `password`
9. Return to the terminal and create a dump server `uvicorn main:app --reload`
10. Now visit the [API] (http://localhost:8000/rate?from_currency=usd&to_currency=eur&date=2021-01-01)


Usage
-----
> You can see the api documentaion on [http://localhost:8000/docs] (http://localhost:8000/docs)

The API receives a `GET` request at `/rate/` and expects 3 required parameters to return the exchange rate of the first currency `from_currency` against the second currency `to_currency` on the specefied `date`

### Request
- `from_currency` > `[string]` of 3 characters
- `to_currency` > `[string]` of 3 characters
- `date` > `[date]`: The date of the exchange rate

**Request Example:**
> */rate?from_currency=usd&to_currency=eur&date=2021-01-01*

### Response
The API returns a json object consists of four parameters if both of the currencies are available
- `from_currency` > *`[string]`* of 3 characters
- `to_currency` > *`[string]`* of 3 characters
- `date` > `[date]`: The date of the exchange rate
- `exchange_rate` > *`[float]`*

**Response Example:**
*`{"from_currency":"CNY","to_currency":"ZAR","date":"2019-04-05","exchange_rate":2.0949}`*


License
=======

This software is licensed under the `MIT License`. See the ``LICENSE``
file in the top distribution directory for the full license text.
