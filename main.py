from amadeus import Client, ResponseError

amadeus = Client(
    client_id='y9iqdSqYOxJkdW6fNyHhl3u5UfB5OvLH',
    client_secret='zZgV2V5oMwwgmr2C'
)
origin = input('Give your origin airpot (3-letter code): ').upper()
destination = input('Give your destination airport (3-letter code): ').upper()
dep_date = input('Give your date of departure (YYYY-MM-DD): ')

try:
    response = amadeus.shopping.flight_offers_search.get(
        originLocationCode=origin,
        destinationLocationCode=destination,
        departureDate=dep_date,
        adults=1
    )

    print(response.data[0]['price']['total'])

except ResponseError as error:
    print(error)