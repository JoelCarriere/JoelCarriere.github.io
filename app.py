import os
from hugchat import hugchat
from hugchat.login import Login

# Read environment variables for email and password
EMAIL = os.getenv('HUGGINGFACE_EMAIL')
PASSWD = os.getenv('HUGGINGFACE_PASSWD')

# Log in to HuggingFace and grant authorization to HuggingChat
cookie_path_dir = "./cookies/" # NOTE: trailing slash (/) is required to avoid errors
sign = Login(EMAIL, PASSWD)
cookies = sign.login(save_cookies=False)  # Do not save cookies to a directory

# Create your ChatBot
chatbot = hugchat.ChatBot(cookies=cookies.get_dict())

# Non-stream response
query_result = chatbot.chat("Hi!")
print(query_result)  # or query_result.text or query_result["text"]

# Stream response
for resp in chatbot.query("Hello", stream=True):
    print(resp)

# Web search (new feature)
query_result = chatbot.query("Hi!", web_search=True)
print(query_result)
for source in query_result.web_search_sources:
    print(source.link)
    print(source.title)
    print(source.hostname)

# Create a new conversation
chatbot.new_conversation(switch_to=True)  # Switch to the new conversation

# Get conversations on the server that are not from the current session (all your conversations in HuggingChat)
conversation_list = chatbot.get_remote_conversations(replace_conversation_list=True)
# Get conversation list (local)
conversation_list = chatbot.get_conversation_list()

# Get the available models (not hardcore)
models = chatbot.get_available_llm_models()

# Switch model with given index
chatbot.switch_llm(0)  # Switch to the first model
chatbot.switch_llm(1)  # Switch to the second model

# Get information about the current conversation
info = chatbot.get_conversation_info()
print(info.id, info.title, info.model, info.system_prompt, info.history)

# Assistant
assistant = chatbot.search_assistant(assistant_name="ChatGpt")  # Assistant name list in https://huggingface.co/chat/assistants
assistant_list = chatbot.get_assistant_list_by_page(page=0)
chatbot.new_conversation(assistant=assistant, switch_to=True)  # Create a new conversation with assistant

# [DANGER] Delete all the conversations for the logged-in user
chatbot.delete_all_conversations()
