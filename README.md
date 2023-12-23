## Question-Answering bot using LLM, based on the content of a document using Langchain framework

**Problem Statement :** 
Create API Question-Answering bot that leverages LLM, able to answer questions based on the content of a document. Demonstrate usage of Langchain framework.

**Implementation**

1. The application uses
```
- Python 3.x
- LangChain (Python)
- OpenAI (gpt-3.5-turbo model)
- VectorDB
```

2. Deployment Steps 

```
1. Clone the repo
2. update .env with openAI key
3. Run
   $ pip3 install -r requirements.txt
   $ python app/app.py
```

3. API for testing

```
Import the attached collection with file named "APIs.postman_collection.json"

Request : 
curl --location --request POST 'http://localhost:5000/upload' \
--form 'doc_file=@"/home/archit/Documents/workspace/llm/qa-bot-llm/app/data/sample.json"' \
--form 'question_file=@"/home/archit/Documents/workspace/llm/qa-bot-llm/app/data/questions.json"'

Response :
{
    "Is personal information transmitted, processed, stored, or disclosed to or retained by third parties": "Based on the given context, there is no specific information provided regarding the transmission, processing, storage, disclosure, or retention of personal information by third parties. Therefore, I don't have enough information to answer this question.",
    "Which cloud providers do you rely on,?": "I don't have enough information to answer that question.",
    "does customer has network diagram?": "Yes, the company has a Network Diagram showing firewalls in place to separate networks."
} 
```


4. Explanation of basic concepts used in the application
```

Load: Document loaders provide a "load" method for loading data as documents from a configured source.
It loads data from a source as Document based on type of document. Have used langchain's document_loaders.

Split: Text splitters break large Documents into smaller chunks. This is useful both for indexing data and for passing it in to a model, since large chunks are harder to search over and won’t fit in a model’s finite context window. Have used langchain's RecursiveCharacterTextSplitter

Store: Require store and index our splits, so that they can later be searched over. Langchain's vectorstores is used

Embeddings : Designed for interfacing with text embedding models. In this case openAI is being used.

SystemMessagePromptTemplate : Provides initial instructions, context, or data for the AI model.
 
HumanMessagePromptTemplate :  Provides messages from the user that the AI model responds to. 
```

5. Explanation of code flow structure 
```
In this problem overall flow and operations remains the same, example, loading, splitting, storing and calling openAI.
We may want to change the implementation depends on various condition.
As of know I have created interface which has 3 abstract method for performing loading, splitting and storing in vectorDb
Which has 2 implementation based on filetype (json and pdf) we can change logic of implementation as well as can extend for any other file types
After above preparation we can call the API's of openAI. It contains SystemMessagePromptTemplate, HumanMessagePromptTemplate
```

6. Directory and file structure
```
views :
    qa_apis.py : contains API contract and basic validation

models :
    file_processor.py : common interface for processing of documents
    json_file_processor.py : implementation to perform load, split and store for json documents
    pdf_file_processor.py : implementation to perform load, split and store for pdf documents

service : 
    qa_apis_service.py : creates the object based on the implementation and executes the steps
     
common :
    openapi.py : contains setting of template and call to openAI.
    
data : 
    contains sample data files
    uploads : api saves file in this folder and then processes it. 
```