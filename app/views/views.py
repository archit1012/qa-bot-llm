# Importing flask module in the project is mandatory
# An object of Flask class is our WSGI application.
from flask import Flask, request, jsonify, Blueprint
from dotenv import load_dotenv
from service.llm_service import process_request
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.chat_models import ChatOpenAI

# app_views = Blueprint('views', __name__)

load_dotenv()

# Global variable
embeddings = OpenAIEmbeddings()
chat = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0.2)

# Flask constructor takes the name of
# current module (__name__) as argument.
# app = Flask(__name__)


# The route() function of the Flask class is a decorator,
# which tells the application which URL should call
# the associated function.
# @app.route('/')
# @app_views.route('/')
# ‘/’ URL is bound with hello_world() function.
def hello_world():
    return 'Hello World'


# @app.route('/upload', methods=['POST'])
# @app_views.route('/upload', methods=['POST'])
def upload_files():
    try:
        # Check if the POST request has file parts
        if 'doc_file' not in request.files or 'question_file' not in request.files:
            return jsonify({'error': 'Both files must be provided'})
        response = process_request(request,embeddings,chat)
        return jsonify(response)
    except Exception as e:
        print("Internal Server Error", e)
    return jsonify("Internal Server Error")

    # # main driver function
# if __name__ == '__main__':
#     # run() method of Flask class runs the application
#     # on the local development server.
#     # app.run(debug=False, host='0.0.0.0')
#     app.run()