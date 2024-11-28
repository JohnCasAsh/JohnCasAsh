from flask import Flask, request, jsonify, render_template
from collections import deque

app = Flask(__name__)

# Initialize a queue
user_queue = deque()

@app.route('/')
def home():
    # Serve the index.html file
    return render_template('index.html')

@app.route('/signup', methods=['POST'])
def sign_up():
    # Handle user sign-up
    data = request.get_json()
    username = data.get('username')
    if username:
        user_queue.append(username)
        return jsonify({"message": f"User '{username}' has signed up successfully!"}), 201
    return jsonify({"error": "Username is required"}), 400

@app.route('/process', methods=['POST'])
def process_user():
    # Process the first user in the queue
    if user_queue:
        next_user = user_queue.popleft()
        return jsonify({"message": f"Processing account for user: {next_user}"}), 200
    return jsonify({"error": "No users in the queue to process"}), 400

@app.route('/queue', methods=['GET'])
def get_queue():
    # Return the current queue as a list
    return jsonify({"queue": list(user_queue)}), 200

if __name__ == '__main__':
    app.run(debug=True)
