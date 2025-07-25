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

@app.route('/todo')
def todo_form():
    return render_template('todo.html')



if __name__ == '__main__':
    app.run(debug=True)
