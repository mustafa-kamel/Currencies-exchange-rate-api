from fastapi import FastAPI
from pydantic import BaseModel
import datetime
import raterequesthandler


# Defining a class for the Rate model
class Rate(BaseModel):
    from_currency: str
    to_currency: str
    date: datetime.date


# Create a new app instance
app = FastAPI(title="Currencies Exchange Rate Api", description="This is a simple service built by FastAPI that provides the exchange rate between the two passed currencies on the passed date")

# Initialize the get_rate funcion when a getting a GET request on /rate
@app.get('/rate')
def get_rate(from_currency: str, to_currency: str, date: datetime.date):
    # Converting the passed currencies to upper case before using them
    from_currency, to_currency = from_currency.upper(), to_currency.upper()

    # Get the rate from the database if it's found
    result = raterequesthandler.find_indb(from_currency, to_currency, date)
    # If the rate is found return it
    if result:
        return {'from_currency': result[1], 'to_currency': result[2], 'date': result[3], 'exchange_rate': result[4]}

    # Make a request to check if the passed curriencies is available
    raterequesthandler.check_currencies_existence(from_currency, to_currency)

    # If the rate doesn't exist in the db make a request to get the rate from the API then save it in the database and return it to the client
    return raterequesthandler.get_and_save_rate(from_currency, to_currency, date)
