from flask import Flask, request, jsonify

app = Flask(__name__)

# Set default AC state
ac_state = {"status": "OFF", "upper_limit": 30, "lower_limit": 20}
temperature = None

@app.route('/')
def my_default():
    return jsonify( {"Welcome Message Temperature ": temperature})


@app.route('/update_temperature', methods=['POST'])
def update_temperature():
    global ac_state, temperature
    data = request.get_json()
    
    if not data or "temperature" not in data:
        return jsonify({"error": "Invalid request"}), 400
    
    temperature = data["temperature"]

    # Determine AC state based on temperature
    if temperature > ac_state["upper_limit"]:
        ac_state["status"] = "ON"
    elif temperature < ac_state["lower_limit"]:
        ac_state["status"] = "OFF"

    return jsonify({"message": "Temperature updated", "ac_status": ac_state["status"], "Last Temperature": temperature})

@app.route('/get_ac_command', methods=['GET'])
def get_ac_command():
    return jsonify({"ac_status": ac_state["status"]})

if __name__ == '__main__':
    app.run(debug=True)
