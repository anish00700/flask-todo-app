from flask import request
from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client.todo_db
todo_collection = db.todos

@app.route('/submittodoitem', methods=['POST'])
def submit_todo_item():
    item_name = request.form.get('itemName')
    item_description = request.form.get('itemDescription')

    if item_name and item_description:
        todo_collection.insert_one({
            "itemName": item_name,
            "itemDescription": item_description
        })
        return "To-Do item submitted successfully!"
    else:
        return "Invalid input", 400
