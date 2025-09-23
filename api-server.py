from flask import Flask, jsonify, request

app = Flask(__name__)

# Using sample data to test
data = [
    {"id": 1, "type": "new", "category": "members"},
    {"id": 2, "type": "existing", "category": "subscribers"},
    {"id": 3, "type": "churned", "category": "fans"}
]


@app.route('/api/items', methods=['GET'])
def get_items():
    return jsonify(data)


@app.route('/api/items/<int:item_id>', methods=['GET'])
def get_item(item_id):
    item = next((item for item in data if item["id"] == item_id), None)
    if item:
        return jsonify(item)
    else:
        return jsonify({"error": "Item not found"}), 404


@app.route('/api/items', methods=['POST'])
def add_item():
    new_item = request.get_json()
    data.append(new_item)
    return jsonify(new_item), 201

if __name__ == '__main__':
    app.run(debug=True)
