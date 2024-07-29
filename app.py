from flask import Flask, jsonify, request
from mock_data import get_flight_data
from notification import send_notification

app = Flask(__name__)

@app.route('/flight_status', methods=['GET'])
def flight_status():
    flight_id = request.args.get('flight_id')
    flight_data = get_flight_data(flight_id)
    return jsonify(flight_data)

@app.route('/update_flight_status', methods=['POST'])
def update_flight_status():
    flight_id = request.json['flight_id']
    status = request.json['status']
    gate = request.json['gate']
    delay = request.json['delay']
    
    # Update the flight data in the mock database
    # Code to update the mock data

    # Send notification
    send_notification(flight_id, status, gate, delay)
    return jsonify({'message': 'Flight status updated and notification sent'})

if __name__ == '__main__':
    app.run(debug=True)
