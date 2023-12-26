from flask import Flask
from views import qa_apis  # Import the views module

# Define the WSGI application object
app = Flask(__name__)

app.add_url_rule('/', view_func=qa_apis.hello_world)
app.add_url_rule('/upload', view_func=qa_apis.upload_files , methods=['POST'])

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)
