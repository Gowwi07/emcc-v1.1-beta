from flask import Flask, request, jsonify
from flask_cors import CORS
from llm.phi3_llm import stream_phi3

app = Flask(__name__)
CORS(app)

@app.route('/api/chat', methods=['POST'])
def chat():
    data = request.json
    user_message = data.get("message")
    mode = data.get("mode", "full")

    # Build prompt based on mode
    if mode == "short":
        prompt = f"Answer briefly (1 to 3 lines): {user_message}"
    elif mode == "paragraph":
        prompt = f"Answer as a short paragraph: {user_message}"
    else:
        prompt = user_message

    full_response = []

    def collect_response(part):
        full_response.append(part)

    stream_phi3(prompt, collect_response)

    final_response = ''.join(full_response)
    
    return jsonify({"response": final_response})


if __name__ == '__main__':
    app.run(debug=True)
