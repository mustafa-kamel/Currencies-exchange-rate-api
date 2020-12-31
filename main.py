from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import datetime
import requests
import mydbhandle


class Rate(BaseModel):
    from_currency: str
    to_currency: str
    date: datetime.date


app = FastAPI()


@app.get('/rate')
async def get_rate(from_currency: str, to_currency: str, date: datetime.date):
    # check if the rate is found in the database
    select_query = "SELECT * FROM rates WHERE from_currency = %s AND to_currency = %s AND request_date = %s"
    result = mydbhandle.execute_select(
        select_query, (from_currency, to_currency, date))
    # if the rate is found return it
    if result:
        return {'from_currency': result[1], 'to_currency': result[2], 'date': result[4], 'exchange_rate': result[3]}
    # else make a request then save it and return it
    response = requests.get(
        F"https://api.frankfurter.app/{date}?from={from_currency}&to={to_currency}")
    data = response.json()
    insert_query = "INSERT INTO rates (from_currency, to_currency, request_date, exchange_rate) VALUES (%s, %s, %s, %s)"
    row_count = mydbhandle.execute_insert(
        insert_query, (from_currency, to_currency, date, data['rates'][to_currency]))
    if row_count:
        return {'from_currency': from_currency, 'to_currency': to_currency, 'date': date, 'exchange_rate': data['rates'][to_currency]}
    else:
        raise HTTPException(status_code=500, detail="Internal Server Error")
