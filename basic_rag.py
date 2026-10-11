from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_ollama import OllamaEmbeddings, ChatOllama
from langchain_chroma import Chroma
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

loader = PyPDFLoader(
    r"C:\Users\vardhan\OneDrive\Documents\Project\Projects\AMAZON_HACKTHON\Langchain\NSRIT ML LAB R23.docx.pdf"
)

documents = loader.load()

text_splitter = RecursiveCharacterTextSplitter(chunk_size=200, chunk_overlap=20)

chunks = text_splitter.split_documents(documents)

embeddings = OllamaEmbeddings(model="nomic-embed-text")

vectorstore = Chroma(collection_name="My_Collection", embedding_function=embeddings)

batch_size = 10

for i in range(0, len(chunks), batch_size):
    batch = chunks[i : i + batch_size]
    vectorstore.add_documents(batch)

retriever = vectorstore.as_retriever(search_kwargs={"k": 3})

question = input("Enter your question: ").strip()

docs = retriever.invoke(question)

context = "\n\n".join(doc.page_content for doc in docs)

prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            """
            Answer the question properly using only the provided context.
            If the answer is not available in the context,
            say that the answer is not available in the provided document.
            """,
        ),
        (
            "human",
            """
            Context:
            {context}

            Question:
            {question}
            """,
        ),
    ]
)

model = ChatOllama(model="qwen2.5-coder:3b")

parser = StrOutputParser()

chain = prompt | model | parser

answer = chain.invoke({"context": context, "question": question})

print("\nAnswer:")
print(answer)
