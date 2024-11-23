from flask import Flask, request
import test

app = Flask(__name__)


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
        response_message = test.run_all(input_message)
    except Exception as e:
        return {"error": f"Failed to process message: {str(e)}"}, 500

    # Return the response
    return {"response": response_message}


if __name__ == "__main__":
    app.run(debug=True)