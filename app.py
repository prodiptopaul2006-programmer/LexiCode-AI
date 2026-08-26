import os
from flask import Flask, render_template, request, jsonify
from groq import Groq

app = Flask(__name__)

# Initialize Groq client
client = Groq(api_key=os.environ.get("GROQ_API_KEY", "YOUR_API_KEY_HERE"))

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
        prompt = f"Analyze this code snippet and provide professional documentation, a plain-English explanation, and a breakdown of its logic:\n\n{code_snippet}"
        
        chat_completion = client.chat.completions.create(
            messages=[
                {
                    "role": "user",
                    "content": prompt,
                }
            ],
            model="llama-3.3-70b-versatile",
        )
        
        doc_text = chat_completion.choices[0].message.content
        return jsonify({'documentation': doc_text})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
