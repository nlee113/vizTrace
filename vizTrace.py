from flask import Flask, render_template, request, jsonify
import subprocess
import re

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/trace', methods=['POST'])
def trace():
    hostname = request.form['hostname']
    print("Received hostname:", hostname)
    output = run_traceroute(hostname)
    print(output)  # Print traceroute output in terminal
    ip_addresses = parse_traceroute_output(output)
    return jsonify({'ip_addresses': ip_addresses})

def run_traceroute(hostname):
    try:
        # Execute traceroute command and capture the output
        output = subprocess.check_output(["traceroute", hostname]).decode("utf-8")
        return output
    except subprocess.CalledProcessError as e:
        # Handle traceroute command error
        return f"Error: {e}"

def parse_traceroute_output(output):
    # Extract IP addresses from the output
    ip_addresses = re.findall(r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})', output)
    return ip_addresses

if __name__ == '__main__':
    app.run(debug=True)


