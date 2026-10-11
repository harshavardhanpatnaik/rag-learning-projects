from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_ollama import OllamaEmbeddings, ChatOllama
from langchain_chroma import Chroma
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
path = input("Enter pdf path : ").strip()

loader = PyPDFLoader(path)

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

model = ChatOllama(model="qwen2.5-coder:3b")

parser = StrOutputParser()


rewrite_prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            """ 
    Given the conversation history and the latest question,
            rewrite the latest question as a standalone question.

            If the latest question is already clear and standalone,
            return it unchanged.

            Do not answer the question.
            Only return the rewritten question.
    """,
        ),
        (
            "user",
            """
        'chat_history':{chat_history},
        'new_question':{new_question}
        
        """,
        ),
    ]
)

rewrite_chain = rewrite_prompt | model | parser


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


chain = prompt | model | parser
chat_history = []


while True:
    print("\n1. Ask Question")
    print("2.Exit")

    choice = int(input("Enter Your Choice : "))

    if choice == 1:

        new_question = input("Enter your question: ").strip()

        standalone_question = rewrite_chain.invoke(
            {"chat_history": chat_history, "new_question": new_question}
        )

        docs = retriever.invoke(standalone_question)

        context = "\n\n".join(doc.page_content for doc in docs)

        answer = chain.invoke({"context": context, "question": standalone_question})

        chat_history.append(("user", new_question))
        chat_history.append(("assistant", answer))

        print("\nAnswer:")
        print(answer)

    elif choice == 2:
        print("Exiting .....")
        break

    else:
        print("Invalid choice .")
