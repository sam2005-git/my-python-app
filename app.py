from flask import Flask

app = Flask(__name__)  # Corrected _name_ to __name__

@app.route('/')
def hello_world():
    return 'Hello, Jenkins!'  # Added a space after the comma for better readability

if __name__ == '__main__':  # Corrected if_name_ to __name__
    app.run(host='0.0.0.0', port=5000)  # Corrected host value to '0.0.0.0'
