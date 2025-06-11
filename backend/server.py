from flask import Flask, request, jsonify
from flask_cors import CORS
import threading

# Import your existing autocorrect + LLM modules
from llm.phi3_llm import stream_phi3
from llm.phi3_llm_autocorrect import autocorrect_input

app = Flask(__name__)
CORS(app)

# Main API endpoint
@app.route('/api/chat', methods=['POST'])
def chat():
    data = request.json
    user_message = data.get("message")

    # Step 1: Autocorrect
    corrected_text = autocorrect_input(user_message)

    # Step 2: LLM Call (using streaming but collecting output fully)
    full_response = []

    def collect_response(part):
        full_response.append(part)

    stream_phi3(corrected_text, collect_response)

    final_response = ''.join(full_response)
    
    return jsonify({"response": final_response})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
