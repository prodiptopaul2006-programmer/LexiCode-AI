import os
import logging
from flask import Flask, render_template, request, jsonify
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from groq import Groq

# Configure secure server-side logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

app = Flask(__name__)

# Initialize Flask-Limiter to protect endpoints from abuse/DoS
limiter = Limiter(
    get_remote_address,
    app=app,
    default_limits=["200 per day", "50 per hour"],
    storage_uri="memory://"
)

# Initialize Groq client
client = Groq(api_key=os.environ.get("GROQ_API_KEY", "YOUR_API_KEY_HERE"))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
@limiter.limit("10 per minute")  # Restricts each IP address to 10 requests per minute
def generate():
    data = request.get_json()
    if not data:
        return jsonify({'error': 'Invalid JSON payload'}), 400
        
    code_snippet = data.get('code', '')
    
    if not code_snippet.strip():
        return jsonify({'error': 'No code provided'}), 400

    # 1. Input Validation & Length Constraint (mitigates memory exhaustion & token abuse)
    MAX_LENGTH = 5000
    if len(code_snippet) > MAX_LENGTH:
        return jsonify({'error': f'Code snippet too large. Maximum allowed length is {MAX_LENGTH} characters.'}), 400

    try:
        prompt = f"Analyze this code snippet and provide professional documentation, a plain-English explanation, and a breakdown of its logic:\n\n{code_snippet}"
        
        chat_completion = client.chat.completions.create(
            messages=[
                {
                    "role": "user",
                    "content": prompt,
                }
            ],
            model="openai/gpt-oss-120b",
        )
        
        doc_text = chat_completion.choices[0].message.content
        return jsonify({'documentation': doc_text})
        
    except Exception as e:
        # 2. Generic Error Response & Secure Server-Side Logging
        logger.exception("An unhandled exception occurred during documentation generation:")
        return jsonify({'error': 'An internal server error occurred while processing your request. Please try again later.'}), 500

if __name__ == '__main__':
    # Keep debug=False for production-level testing to prevent stack trace leaks
    app.run(debug=False)
