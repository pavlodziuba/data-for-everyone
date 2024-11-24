from flask import Flask, request
from flask_cors import CORS  # Import the CORS extension
import logic

app = Flask(__name__)

# Enable CORS with custom configuration:
CORS(app, resources={r"/process": {"origins": "http://localhost:3000"}})


def select_last_result(response_message):
    # Find the last occurrence of "THIS OUTPUT MESSAGE "
    marker = "THIS OUTPUT MESSAGE "
    last_index = response_message.rfind(marker)

    # If the marker is not found, return an empty string or appropriate message
    if last_index == -1:
        return response_message

    # Extract and return the text after the last occurrence of the marker
    return response_message[last_index + len(marker):]


@app.route("/process", methods=["POST"])
def process_message():
    # Get the message from the POST request
    data = request.json
    if not data or "message" not in data:
        return {"error": "Missing 'message' in request"}, 400

    input_message = data["message"]

    # Process the message using test.run_all
    try:
        print(input_message)
        response_message = logic.run_all(input_message)
    except Exception as e:
        return {"error": f"Failed to process message: {str(e)}"}, 500
    response_message = select_last_result(response_message)
    # Return the response
    return {"response": response_message}

if __name__ == "__main__":
    app.run(debug=True)