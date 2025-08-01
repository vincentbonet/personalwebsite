from flask import Flask, request, jsonify
from flask_cors import CORS
from utils import send_email, log_submission

app = Flask(__name__)
CORS(app)

@app.route('/contact', methods=['POST'])
def contact():
    data = request.form
    name = data.get('name', '')
    email = data.get('email', '')
    message = data.get('message', '')

    if not name or not email or not message:
        return jsonify({'error': 'Missing fields'}), 400

    try:
        send_email(name, email, message)
        log_submission(name, email, message)
        return jsonify({'success': 'Message sent'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)


@app.route("/")
def index():
    return "Flask backend is running. This is the API root."

