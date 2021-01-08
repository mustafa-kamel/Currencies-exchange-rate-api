from fastapi import HTTPException
import requests
import ratedbhandle

url = "https://api.frankfurter.app"


# Get the rate from the database if it's found
def find_indb(from_currency, to_currency, date):
    # Check if the rate is found in the database
    select_query = "SELECT * FROM rates WHERE from_currency = %s AND to_currency = %s AND request_date = %s"
    # Execute the select query and return the result
    return ratedbhandle.execute_select(select_query, (from_currency, to_currency, date))


# Check if the currencies are provided by the api
def check_currencies_existence(from_currency, to_currency):
    currencies_response = requests.get(F"{url}/currencies")
    # Parse the json response data
    currencies = currencies_response.json()
    if not from_currency in currencies:
        raise HTTPException(status_code=404, detail=F"The passed currency {from_currency} is not available")
    elif not to_currency in currencies:
        raise HTTPException(status_code=404, detail=F"The passed currency {to_currency} is not available")


# Make a request to get the rate from the api, save it in the database then return it to the user
def get_and_save_rate(from_currency, to_currency, date):
    response = requests.get(F"{url}/{date}?from={from_currency}&to={to_currency}")
    data = response.json()

    # Save the response data in the database
    insert_query = "INSERT INTO rates (from_currency, to_currency, request_date, exchange_rate) VALUES (%s, %s, %s, %s)"
    row_count = ratedbhandle.execute_insert(
        insert_query, (from_currency, to_currency, date, data['rates'][to_currency]))

    # Return the data to the client if the insert query succeeded
    if row_count:
        return {'from_currency': from_currency, 'to_currency': to_currency, 'date': date, 'exchange_rate': data['rates'][to_currency]}
    # Return HTTP response error if the database failed to save the data
    else:
        raise HTTPException(status_code=500, detail="Internal Server Error")
