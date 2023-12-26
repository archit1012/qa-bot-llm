import pytest
import os

from application import *

# Fixture to create a test client and set up the app for testing
TESTS_DIRECTORY = os.path.dirname(os.path.abspath(__file__))

def test_hello_world(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b'Hello, World!' in response.data



# Test Hello World Endpoint
def test_hello_world(client):
    response = client.get('/')
    assert response.status_code == 200
    assert response.json() == {"message": "Hello, World!"}

# Test Upload Files Endpoint
@pytest.mark.parametrize('doc_file_name, question_file_name', [
    ('./sample.json', './questions.json', ),
])
def test_upload_files(client, doc_file_name, question_file_name):
    # Prepare sample files for testing
    # doc_file_path = "path/to/sample.json"
    # question_file_path = "path/to/questions.json"

    doc_file = os.path.join(TESTS_DIRECTORY, 'data', doc_file_name)
    question_file = os.path.join(TESTS_DIRECTORY, 'data', question_file_name)



    response = client.post('/upload', data={'doc_file': doc_file, 'question_file': question_file})

    assert response.status_code == 200
    assert "Is personal information transmitted" in response.json()

# Test Exception Handling
def test_upload_files_exception_handling(client, monkeypatch):
    # Mocking an exception to test exception handling
    monkeypatch.setattr(views, 'process_request', lambda x, y, z: 1/0)

    doc_file = open("path/to/sample.json", "rb")
    question_file = open("path/to/questions.json", "rb")

    response = client.post('/upload', data={'doc_file': doc_file, 'question_file': question_file})

    assert response.status_code == 500
    assert response.json() == "Internal Server Error"

# Test Missing Files Handling
def test_upload_files_missing_files(client):
    response = client.post('/upload')
    assert response.status_code == 400
    assert response.json() == {'error': 'Both files must be provided'}
