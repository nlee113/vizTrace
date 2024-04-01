from flask import Flask, render_template, request
import requests

app = Flask(__name__)

def get_route(hostname):
    try:
        response = requests.get(f"https://ipinfo.io/{hostname}/json")
        if response.status_code == 200:
            data = response.json()
            route = [hop.split()[0] for hop in data.get('trace', '').split('\n') if hop]
            return route
        else:
            print("Error: Unexpected status code:", response.status_code)
            return []
    except Exception as e:
        print("Error:", e)
        return []

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/trace', methods=['POST'])
def trace():
    hostname = request.form['hostname']  # Extract hostname 
    print("Received hostname:", hostname) 
    route = get_route(hostname)
    return {'route': route}


if __name__ == '__main__':
    app.run(debug=True)


