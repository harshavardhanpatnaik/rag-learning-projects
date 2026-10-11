🚀 RAG Projects — From Basic RAG to Conversational Memory

A hands-on Python project exploring document-based question answering, interactive RAG, query rewriting, and session-based chat history.

📌 Table of Contents

📖 About the Project
🎯 Project Objectives
🧰 Technologies Used
✨ Project Features
📂 Project Structure
🏗️ Project Architecture
🧩 The Four Implementations
⚙️ Installation and Setup
▶️ How to Run
💬 Example Interaction
🧠 Understanding the Concepts
⚠️ Current Limitations
🔮 Future Improvements
👨‍💻 Author

📖 About the Project
This repository contains four Python implementations developed while learning Retrieval-Augmented Generation (RAG) and conversational applications using LangChain and Ollama.
The project starts with a basic document-question-answering pipeline and gradually explores additional capabilities, including interactive question answering, query rewriting using conversation history, and session-based chat history management.
Instead of relying entirely on a language model's existing knowledge, the RAG implementations retrieve relevant text chunks from a PDF document and provide that content as context to the model.
The session-history implementation explores how messages can be maintained separately for different conversation sessions.
💡 What does this project do?

📄 Loads content from a PDF document.
✂️ Splits document content into smaller text chunks.
🧬 Generates embeddings for document chunks.
🗄️ Stores document representations in a Chroma vector store.
🔍 Retrieves relevant document chunks for a question.
🤖 Uses an Ollama language model to generate a response.
🔄 Supports repeated question answering in an interactive program.
🧠 Experiments with rewriting questions using conversation history.
💬 Demonstrates session-based message history.

🎯 Project Objectives
The primary objective is to understand how individual RAG components work together and how additional functionality can be built on top of a basic retrieval pipeline.

Objective
Description

📄 Document loading
Read PDF content using a document loader.

✂️ Text splitting
Divide documents into smaller chunks for retrieval.

🧬 Embeddings
Convert text into vector representations.

🗄️ Vector storage
Store and retrieve document representations using Chroma.

🔍 Retrieval
Find relevant chunks for a user's question.

🤖 Answer generation
Generate responses using retrieved context.

🔄 Interactive RAG
Ask multiple questions in one running program.

📝 Query rewriting
Rewrite a follow-up question using previous conversation messages.

💬 Session history
Maintain separate in-memory message histories by session ID.

🧰 Technologies Used
The following technologies and libraries are used in the implementations.

Technology
Purpose in this project

Python
Implements the application logic and connects the RAG components.

LangChain
Connects document loaders, text splitters, prompts, models, retrievers, and chains.

PyPDFLoader
Loads document content from PDF files.

RecursiveCharacterTextSplitter
Splits the loaded content into smaller text chunks.

OllamaEmbeddings
Generates embeddings for document text using an Ollama embedding model.

Chroma
Stores vector representations and supports similarity-based retrieval.

ChatOllama
Connects the application to chat models served through Ollama.

ChatPromptTemplate
Defines prompts for answering questions and rewriting queries.

StrOutputParser
Converts model output into a string representation.

MessagesPlaceholder
Provides a place for conversation messages inside a chat prompt.

InMemoryChatMessageHistory
Stores chat messages in memory for a conversation session.

RunnableWithMessageHistory
Wraps a runnable chain with session-based message-history handling in the current implementation.

🤖 Models used
The code includes the following model names:

nomic-embed-text — used for document embeddings in the RAG implementations.
qwen2.5-coder:3b — used as a chat model in the RAG implementations.
gpt-oss:120b-cloud — configured as the chat model in the session-history implementation.

Model availability and execution depend on the Ollama environment and the model tags configured in the code.

✨ Project Features
📄 1. PDF-Based Question Answering
Load a PDF document and ask questions about its contents. The application retrieves relevant chunks and provides them to the language model as context.
🔍 2. Semantic Retrieval
Document chunks are converted into embeddings and stored in Chroma. The retriever searches for relevant chunks instead of passing the entire document to the language model for every question.
🔄 3. Interactive Question Answering
The interactive implementation uses a loop to accept multiple questions until the user chooses to exit.
📝 4. Query Rewriting
The query-rewriting implementation uses previous conversation messages and a new question to generate a standalone question before retrieval.
💬 5. Session-Based Chat History
The session-history implementation maintains a separate in-memory message history for each session ID, allowing messages to be associated with a particular conversation.

📂 Project Structure
The recommended organization of the four Python files is:
RAG/
│
├── projects/
│ │
│ ├── basic_rag.py
│ ├── basic_rag_interactive.py
│ ├── rag_with_query_rewriting.py
│ └── session_chat_history.py
│
├── README.md
└── requirements.txt

Note: The Python filenames above are the recommended names for the four existing programs. Rename the files accordingly if you have not already done so. Keep README.md and requirements.txt in the repository root if that matches your actual repository layout.

📁 File descriptions

File
Purpose

basic_rag.py
Implements a basic PDF-based RAG pipeline for answering a question.

basic_rag_interactive.py
Extends the basic implementation with an interactive question loop.

rag_with_query_rewriting.py
Uses conversation history to rewrite a question before retrieving relevant document chunks.

session_chat_history.py
Demonstrates session-based chat history using in-memory message storage.

README.md
Documents the project, setup, features, and usage.

requirements.txt
Lists the Python dependencies required to run the project.

🏗️ Project Architecture
🔹 Basic RAG workflow
flowchart TD
A["📄 PDF Document"] --> B["PyPDFLoader"]
B --> C["✂️ Text Splitter"]
C --> D["🧬 Ollama Embeddings"]
D --> E["🗄️ Chroma Vector Store"]
F["❓ User Question"] --> G["🔍 Retriever"]
E --> G
G --> H["📚 Retrieved Context"]
H --> I["📝 Prompt Template"]
F --> I
I --> J["🤖 ChatOllama"]
J --> K["💬 Generated Answer"]

    classDef input fill:#dbeafe,stroke:#2563eb,color:#111827
    classDef process fill:#dcfce7,stroke:#16a34a,color:#111827
    classDef output fill:#f3e8ff,stroke:#9333ea,color:#111827

    class A,F input
    class B,C,D,E,G,H,I,J process
    class K output

🔹 Query rewriting workflow
flowchart TD
A["💬 Previous Conversation Messages"] --> C["📝 Query Rewriting Prompt"]
B["❓ New User Question"] --> C
C --> D["🤖 Chat Model"]
D --> E["🔄 Standalone Question"]
E --> F["🔍 Retriever"]
G["🗄️ Chroma Vector Store"] --> F
F --> H["📚 Retrieved Context"]
E --> I["📝 Answer Prompt"]
H --> I
I --> J["🤖 Chat Model"]
J --> K["💬 Final Answer"]

    classDef input fill:#dbeafe,stroke:#2563eb,color:#111827
    classDef process fill:#dcfce7,stroke:#16a34a,color:#111827
    classDef output fill:#f3e8ff,stroke:#9333ea,color:#111827

    class A,B input
    class C,D,E,F,G,H,I,J process
    class K output

Important distinction: In the query-rewriting implementation, conversation history is used to rewrite the question before retrieval. The final answer prompt receives the standalone question and retrieved context; the entire conversation history is not directly passed into that final answer prompt.
🔹 Session-history workflow
flowchart TD
A["👤 User"] --> B["🆔 Session ID"]
B --> C["📚 Retrieve or Create Session History"]
C --> D["📝 Chat Prompt + History + New Question"]
D --> E["🤖 Chat Model"]
E --> F["💬 Response"]
F --> G["💾 Update In-Memory History"]
G --> H["🔁 Continue Conversation"]

    classDef input fill:#dbeafe,stroke:#2563eb,color:#111827
    classDef process fill:#dcfce7,stroke:#16a34a,color:#111827
    classDef output fill:#f3e8ff,stroke:#9333ea,color:#111827

    class A,B input
    class C,D,E,G,H process
    class F output

The session-history program stores conversation messages in memory. It does not implement permanent database-backed conversation storage.

🧩 The Four Implementations
1️⃣ Basic RAG — basic_rag.py
Purpose: Understand the fundamental Retrieval-Augmented Generation workflow.
The program loads a PDF, splits its content into chunks, creates embeddings, stores them in Chroma, retrieves relevant chunks, and passes the retrieved context to a chat model.
Workflow:

Load the PDF with PyPDFLoader.
Split its content with RecursiveCharacterTextSplitter.
Generate embeddings using OllamaEmbeddings.
Add the document chunks to Chroma.
Retrieve the most relevant chunks for a question.
Combine the retrieved text into a context.
Pass the context and question to the prompt template.
Generate and display the answer using ChatOllama.

Current configuration in the code:

Chunk size: 200
Chunk overlap: 20
Number of retrieved chunks (k): 3
Embedding model: nomic-embed-text
Chat model: qwen2.5-coder:3b

These values describe the current implementation and can be changed in the Python file.
2️⃣ Interactive RAG — basic_rag_interactive.py
Purpose: Ask multiple questions without restarting the application after every question.
This implementation adds a loop around the RAG question-answering process.
Workflow:

Initialize the PDF retrieval pipeline.
Display the available menu options.
Accept a question from the user.
Retrieve relevant chunks.
Generate an answer using the model.
Continue accepting questions until the user selects the exit option.

What it demonstrates:

Python while loops.
User input handling.
Repeated retrieval and answer generation.
Basic command-line interaction.

The current implementation does not automatically make the previous questions part of the next question's context.
3️⃣ RAG with Query Rewriting — rag_with_query_rewriting.py
Purpose: Improve retrieval for follow-up questions that depend on previous conversation messages.
A follow-up question can be difficult to retrieve against a document when it contains references such as “What about its advantages?” or “Explain that in more detail.”
Query rewriting uses the previous messages and the new question to create a more self-contained question before retrieval.
Workflow:

Maintain a list of conversation messages.
Receive a new user question.
Pass the previous messages and the new question to a rewriting prompt.
Generate a standalone question.
Retrieve document chunks using the rewritten question.
Pass the retrieved context and standalone question to the answer prompt.
Generate the answer.
Append the new question and answer to the conversation history.

What it demonstrates:

Conversation-aware question rewriting.
Using history to improve the retrieval query.
Separating query rewriting from answer generation.
Maintaining a simple conversation history with Python data structures.

Current limitation: The conversation history is a Python list of tuples and exists only while the program is running. This implementation does not use the session-history wrapper from the fourth program.
4️⃣ Session-Based Chat History — session_chat_history.py
Purpose: Understand how a chat chain can load and update message history for a specific session.
This program uses InMemoryChatMessageHistory and RunnableWithMessageHistory to associate conversation messages with a session ID.
Workflow:

Receive a session ID.
Check whether a history object already exists for that session.
Create an in-memory history object if the session is new.
Invoke the chat chain with the user's question and session configuration.
Load the appropriate message history.
Generate the response.
Update the history with the conversation messages.
Allow the user to continue the session or open another session.

Important components:

Component
Role

InMemoryChatMessageHistory
Holds messages in RAM.

RunnableWithMessageHistory
Connects the chain to session-specific message history.

MessagesPlaceholder
Inserts existing messages into the chat prompt.

session_id
Identifies the conversation whose history should be used.

history_messages_key="history"
Matches the history key used by the prompt placeholder.

input_messages_key="question"
Identifies the input question in the chain's input dictionary.

Current limitation: Session histories are not saved permanently. They disappear when the Python process terminates. The current code also uses LangChain APIs that may emit deprecation warnings in newer installed versions.

⚙️ Installation and Setup
Prerequisites
Before running the programs, make sure you have:

Python installed.
Ollama installed and running.
The embedding and chat models required by the selected script available in your Ollama environment.
The PDF document you want to process.
The Python dependencies installed in your environment.

Step 1: Clone the repository
Replace the URL below with your actual GitHub repository URL.
git clone <YOUR_GITHUB_REPOSITORY_URL>

Navigate to the project directory:
cd <YOUR_PROJECT_DIRECTORY>

Step 2: Create a virtual environment (recommended)
python -m venv .venv

Activate it on Windows Command Prompt:
.venv\Scripts\activate

For Windows PowerShell:
.\.venv\Scripts\Activate.ps1

Step 3: Install the dependencies
If the repository contains a correctly prepared requirements.txt, run:
python -m pip install -r requirements.txt

Make sure the file lists the packages imported by your actual code. Do not add unrelated dependencies.
Step 4: Prepare the PDF
The RAG scripts currently rely on a PDF file path supplied in the code.
Update the path to the location of your own PDF document before running the program.
For example:
pdf_path = r"C:\path\to\your\document.pdf"

Use the variable name that already exists in the relevant script.
Step 5: Prepare the Ollama models
The code uses Ollama for embeddings and chat generation. Ensure that the required models and model tags are available in your environment.
For example, the embedding model referenced by the RAG programs is:
ollama pull nomic-embed-text

The chat models and their availability depend on the model tags used by the individual scripts. Verify those tags in your code and Ollama environment before running the programs.

▶️ How to Run
Run the Python files from the directory that contains them.
Run the basic RAG program
python basic_rag.py

Run the interactive RAG program
python basic_rag_interactive.py

Run RAG with query rewriting
python rag_with_query_rewriting.py

Run the session-history program
python session_chat_history.py

If your files have not been renamed, use their actual current filenames instead.

💬 Example Interaction
The following is an illustrative example of how a document-based RAG application can behave. The answer will depend on the PDF content and the model's response.
========================================
📚 PDF QUESTION ANSWERING
========================================

Enter your question:
What is machine learning?

🔍 Retrieving relevant document chunks...

🤖 Generating answer...

Answer:
Machine learning is a field of artificial intelligence
that enables systems to learn patterns from data.

========================================

For the query-rewriting implementation, a conversation could look like this:
User: What is machine learning?

Assistant: [Answer based on the retrieved PDF content]

User: What are its applications?

Query rewriting:
"What are the applications of machine learning?"

Retriever:
Searches for relevant document chunks using the rewritten question.

Assistant:
[Answer based on the retrieved PDF content]

The output shown above is illustrative, not a claim that every PDF will produce those exact answers.

🧠 Understanding the Concepts
What is RAG?
Retrieval-Augmented Generation combines information retrieval with language-model generation.
Instead of asking the language model to answer using only its existing knowledge, the application retrieves relevant information from a supplied document and includes it in the prompt.
What are embeddings?
Embeddings are numerical representations of text. They allow text chunks and user questions to be compared in vector space to identify relevant content.
What is a vector store?
A vector store holds vector representations and associated information. In this project, Chroma is used to store document representations and retrieve relevant chunks.
What is a retriever?
A retriever searches for relevant document chunks in response to a query. The basic RAG implementations configure the retriever to return three chunks.
What is query rewriting?
Query rewriting converts a new question into a more self-contained question, using earlier conversation messages when available. The rewritten question is then used for retrieval.
What is session-based chat history?
Session-based chat history associates messages with a particular conversation session. The session ID identifies which history should be loaded for the next interaction.
In the current implementation, this history is held in memory rather than stored permanently.

⚠️ Current Limitations
This section describes the limitations of the existing implementations rather than claiming features that have not yet been built.

PDF path configuration: The RAG scripts require a valid PDF path in the code.
Document scope: The RAG implementations work with the PDF documents loaded by the scripts.
In-memory history: The query-rewriting and session-history implementations do not provide permanent conversation storage.
Session persistence: Session histories disappear when the session-history Python process terminates.
Query rewriting: Rewriting a question does not guarantee that the rewritten question will always improve retrieval.
Model availability: Execution depends on the models and model tags configured in the Ollama environment.
Deprecation warnings: The session-history implementation uses LangChain components that may be deprecated in newer versions. Check the installed version's documentation before upgrading.
Error handling: The current programs should not be assumed to handle every invalid path, model failure, or retrieval error.
Interactive RAG: Repeated question input does not, by itself, provide conversational memory.

🔮 Future Improvements
The following are possible future improvements, not features claimed to be implemented in this repository.

[ ] Improve error handling for missing PDF files and model failures.
[ ] Move repeated initialization outside the interactive question loop.
[ ] Make file paths configurable rather than hardcoded.
[ ] Review LangChain deprecation warnings and update the session-history implementation.
[ ] Add persistent storage for conversation history.
[ ] Add tests for document loading, retrieval, and question answering.
[ ] Compare retrieval results with different chunk sizes and retrieval settings.
[ ] Add clear logging for retrieval and model execution.

These improvements can be introduced incrementally as the project evolves.

👨‍💻 Author
Harsha Vardhan Patnaik
This repository documents hands-on learning and implementation of RAG concepts using Python, LangChain, Chroma, and Ollama.
The focus is on understanding how the components work together by implementing the code and experimenting with progressively more advanced RAG-related concepts.

⭐ Project Summary
Four Python programs. One learning journey.
📄 Basic RAG
↓
🔄 Interactive RAG
↓
📝 RAG with Query Rewriting
↓
💬 Session-Based Chat History

The project demonstrates the progression from document-based question answering to query rewriting and session-specific conversational history.

🚀 Learning by building, testing, and improving.
