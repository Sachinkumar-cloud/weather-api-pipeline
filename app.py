from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route('/weather')
def get_weather():
    city = request.args.get("city", "London")
    url = f"https://wttr.in/{city}?format=j1"
    data = requests.get(url).json()
    current = data["current_condition"][0]
    return jsonify({
        "city": city,
        "temperature": current["temp_C"],
        "humidity": current["humidity"],
        "description": current["weatherDesc"][0]["value"]
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
