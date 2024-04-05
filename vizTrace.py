from flask import Flask, render_template, request
import subprocess

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/trace', methods=['POST'])
def trace():
    hostname = request.form['hostname']  # Extract hostname 
    print("Received hostname:", hostname)
    output = run_traceroute(hostname)
    print(output)  # Print traceroute output in terminal
    return {'output': output}

def run_traceroute(hostname):
    try:
        # Execute traceroute command and capture the output
        output = subprocess.check_output(["traceroute", hostname]).decode("utf-8")
        return output
    except subprocess.CalledProcessError as e:
        # Handle traceroute command error
        return f"Error: {e}"

if __name__ == '__main__':
    app.run(debug=True)


