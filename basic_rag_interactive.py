from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_ollama import OllamaEmbeddings, ChatOllama
from langchain_chroma import Chroma
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

loader = PyPDFLoader(
    r"C:\Users\vardhan\OneDrive\Documents\Project\Projects\AMAZON_HACKTHON\Langchain\NSRIT ML LAB R23.docx.pdf"
)


# step -1 load pdf

documents = loader.load()  # list of documents
text_splitter = RecursiveCharacterTextSplitter(chunk_size=200, chunk_overlap=20)
# Step - 2 divide into chunks
chunks = text_splitter.split_documents(documents)

# step - 3 convert chunks into embeddings and store it in vector db

embeddings = OllamaEmbeddings(model="nomic-embed-text")

vectorstore = Chroma(collection_name="My_Collection", embedding_function=embeddings)

batch_size = 10

for i in range(0, len(chunks), batch_size):
    batch = chunks[i : batch_size + i]
    vectorstore.add_documents(batch)

retriver = vectorstore.as_retriever(search_kwargs={"k": 3})

while True:
    print("\n1. Ask Question")
    print("2. Exit")
    j = int(input())
    if j == 1:
        question = input("Enter your question ").strip().lower()

        docs = retriver.invoke(question)

        context = "\n\n".join(doc.page_content for doc in docs)

        prompt = ChatPromptTemplate.from_messages(
            [
                (
                    "system",
                    """
    Answer the question properly and give answer from only context given 
    """,
                ),
                (
                    "user",
                    """
        context:{context}
        question:{question}
        """,
                ),
            ]
        )

        model = ChatOllama(model="qwen2.5-coder:3b")

        parser = StrOutputParser()

        chain = prompt | model | parser

        answer = chain.invoke({"context": context, "question": question})

        print(answer)
    elif j == 2:
        print("Exiting......")
        break
    else:
        print("Invalid Choice Lanja Kodaka ")
