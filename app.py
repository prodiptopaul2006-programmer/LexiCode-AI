import os
from flask import Flask, render_template, request, jsonify
import google.generativeai as genai

app = Flask(__name__)

# Configure Gemini API key
genai.configure(api_key=os.environ.get("GEMINI_API_KEY", "YOUR_API_KEY_HERE"))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    data = request.get_json()
    code_snippet = data.get('code', '')

    if not code_snippet:
        return jsonify({'error': 'No code provided'}), 400

    try:
        model = genai.GenerativeModel('gemini-1.5-flash')
        prompt = f"Analyze this code snippet and provide professional documentation, a plain-English explanation, and a breakdown of its logic:\n\n{code_snippet}"

        response = model.generate_content(prompt)
        return jsonify({'documentation': response.text})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
