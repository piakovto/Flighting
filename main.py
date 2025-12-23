from amadeus import Client, ResponseError

amadeus = Client(
    client_id='y9iqdSqYOxJkdW6fNyHhl3u5UfB5OvLH',
    client_secret='zZgV2V5oMwwgmr2C'
)
origin = input('Give your origin airpot (3-letter code): ').upper()
destination = input('Give your destination airport (3-letter code): ').upper()
dep_date = input('Give your date of departure (YYYY-MM-DD): ')
ret_date = input('Give your return date (YYYY-MM-DD): ')

def get_prices(frm, to,date):
    try:
        response = amadeus.shopping.flight_offers_search.get(
            originLocationCode=frm,
            destinationLocationCode=to,
            departureDate=date,
            adults=1,
            max=1 
        )
        if response.data:
            return float(response.data[0]['priATHce']['total'])
        return None
    except ResponseError as error:
        print(error)
        return None
    
outbound_price = get_prices(origin, destination, dep_date)
return_price = get_prices(destination, origin,ret_date)

if outbound_price and return_price:
    total = outbound_price + return_price
    print(f"Outbound flight: ${outbound_price:.2f}")
    print(f"Return flight: ${return_price:.2f}")
    print(f"--------------------")
    print(f"Total Prince: ${total:.2f}")
else:
    print("Could not find one or both fligths.")