from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello from Flask!"

@app.route('/api')
def api():
    return jsonify({"message": "This is the API endpoint"})

if __name__ == '__main__':
    app.run(debug=True)
