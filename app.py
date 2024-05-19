from hugchat import hugchat
from flask import Flask, request, jsonify

app = Flask(__name__)

# Initialize the chatbot
chatbot = hugchat.ChatBot()

# Create a new conversation
id = chatbot.new_conversation()
chatbot.change_conversation(id)

@app.route('/chat', methods=['POST'])
def chat():
    data = request.json
    user_input = data['prompt']
    response = chatbot.chat(user_input)
    return jsonify({"response": response})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
