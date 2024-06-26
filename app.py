from flask import Flask, request, jsonify
import openai

app = Flask(__name__)

openai.api_key = 'sk-proj-z07pLdYT03vfVnyLnMthT3BlbkFJiX4Mi8f7Z8w8v6MJql8R'

@app.route('/ask', methods=['POST'])
def ask():
    data = request.json
    question = data['question']
    
    try:
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=question,
            max_tokens=150,
            n=1,
            stop=None,
            temperature=0.7
        )
        answer = response.choices[0].text.strip()
        return jsonify({'answer': answer})
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True
