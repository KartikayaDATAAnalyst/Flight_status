# Mock data for flights
flights = {
    'AA123': {'status': 'On Time', 'gate': 'A1', 'delay': '0 mins'},
    'BB456': {'status': 'Delayed', 'gate': 'B2', 'delay': '30 mins'}
}

def get_flight_data(flight_id):
    return flights.get(flight_id, {'error': 'Flight not found'})

def update_flight_data(flight_id, status, gate, delay):
    if flight_id in flights:
        flights[flight_id]['status'] = status
        flights[flight_id]['gate'] = gate
        flights[flight_id]['delay'] = delay
