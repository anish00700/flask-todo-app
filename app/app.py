from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello from Flask!"

@app.route('/api')
def api():
    return jsonify({
        "message": "API updated!",
        "author": "Anish Patil",
        "course": "DevOps"
    })


if __name__ == '__main__':
    app.run(debug=True)
