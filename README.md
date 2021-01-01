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
3. Run setup using `setup.bat` for Windows users or `setup.sh` for Linux users

### Windows

4. Install the requirements `pip install -r requirements.txt`
5. Initialize the database `python db_init.py` you will be asked to enter the credentials for the PostgreSQL server (i.e. `username` and `password`)
6. Open `ratedbhandle.py` file in any text editor and edit the database `username` and `password` to your database `username` and `password`
7. Return to cmd and create a dump server `uvicorn main:app --reload`
8.  Now visit the [API] (http://localhost:8000/rate?from_currency=usd&to_currency=eur&date=2021-01-01)

### Linux
4. Install the requirements `env/bin/pip install -r requirements.txt`
5. Initialize the database `/usr/bin/python3 db_init.py` you will be asked to enter the credentials for the PostgreSQL server (i.e. `username` and `password`)
6. Open `ratedbhandle.py` file in any text editor and edit the database `username` and `password` to your database `username` and `password`
7. Return to the terminal and create a dump server `uvicorn main:app --reload`
8.  Now visit the [API] (http://localhost:8000/rate?from_currency=usd&to_currency=eur&date=2021-01-01)


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

If any of the passed currencies isn't available you will receive a 404 error message telling you that this currency isn't available
> {"detail":"The passed currency NY is not available"}

And if any other error happened you will get an informatic message telling you what happened


License
=======

This software is licensed under the `GNU GPL v3.0`. See the ``LICENSE``
file in the top distribution directory for the full license text.
