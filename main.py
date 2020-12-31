from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import datetime
import requests
import mydbhandle

url = "https://api.frankfurter.app"

# Defining a class for the Rate model
class Rate(BaseModel):
    from_currency: str
    to_currency: str
    date: datetime.date

# Create a new app instance
app = FastAPI()

# Initialize the get_rate funcion when a getting a GET request on /rate
@app.get('/rate')
async def get_rate(from_currency: str, to_currency: str, date: datetime.date):
    # Converting the passed currencies to upper case before using them
    from_currency = from_currency.upper()
    to_currency = to_currency.upper()

    # Check if the passed curriencies is available
    currencies_response = requests.get(F"{url}/currencies")

    # Parse the json response data
    currencies = currencies_response.json()
    if not from_currency in currencies:
        raise HTTPException(status_code=404, detail=F"The passed currency {from_currency} is not available")
    elif not to_currency in currencies:
        raise HTTPException(status_code=404, detail=F"The passed currency {to_currency} is not available")

    # Check if the rate is found in the database
    select_query = "SELECT * FROM rates WHERE from_currency = %s AND to_currency = %s AND request_date = %s"
    # Execute the select query
    result = mydbhandle.execute_select(
        select_query, (from_currency, to_currency, date))

    # If the rate is found return it
    if result:
        return {'from_currency': result[1], 'to_currency': result[2], 'date': result[3], 'exchange_rate': result[4]}

    # Otherwise make a request to get the rate from the API then save it in the database and return it to the client
    response = requests.get(F"{url}/{date}?from={from_currency}&to={to_currency}")

    # Parse the json response data
    data = response.json()

    # Save the response data in the database
    insert_query = "INSERT INTO rates (from_currency, to_currency, request_date, exchange_rate) VALUES (%s, %s, %s, %s)"
    row_count = mydbhandle.execute_insert(
        insert_query, (from_currency, to_currency, date, data['rates'][to_currency]))

    # Return the data to the client if the insert query succeeded
    if row_count:
        return {'from_currency': from_currency, 'to_currency': to_currency, 'date': date, 'exchange_rate': data['rates'][to_currency]}

    # Return HTTP response error if the database failed to save the data
    else:
        raise HTTPException(status_code=500, detail="Internal Server Error")
