from langchain_core.chat_history import InMemoryChatMessageHistory

from langchain_core.runnables.history import RunnableWithMessageHistory

from langchain_ollama import ChatOllama

from langchain_core.output_parsers import StrOutputParser


from langchain_core.prompts import ChatPromptTemplate,MessagesPlaceholder

priority1 = "gpt-oss:120b-cloud"
priority2 = "qwen2.5-coder:3b"

model = ChatOllama(model=priority1)

parser = StrOutputParser()

prompt = ChatPromptTemplate([
    ('system','You are a helpful assistant.'),
    MessagesPlaceholder(variable_name="history"),
    ('user','{question}')
])


model_chain = prompt | model | parser

session = {}

def session_id_manager(session_id):
    if session_id not in session:
        session[session_id] = InMemoryChatMessageHistory();
    return session[session_id]
    
history_chain = RunnableWithMessageHistory(
    model_chain,
    session_id_manager,
    input_messages_key="question",
    history_messages_key="history"
)
def llm(question,session_id):
    response = history_chain.invoke(
        {"question": question},
        config={
        "configurable": {
            "session_id": session_id
        }
        },
            )
    return response
    
    
def chat_session(session_id):
    while(True):
        print("1. Ask queston ")
        print("2. print conversation history ")
        print("3. exit ...")
        
        choice = int(input("Enter Your choice : "))
        
        if choice == 1:
            question = input("Enter Your question :").strip()
            
            answer = llm(question,session_id)
            print(f"{'---'*20}")
            print()
            print(answer)
            print()
            print(f"{'---'*20}")
            
        elif choice == 2:
            id = input("Enter Session id :").strip().lower()
            if id in session:
                hist = session_id_manager(id)
                print(f"{'---'*20}")
                for i in hist.messages:
                    print(f"{i.type}  {i.content}")
                print()
                print(f"{'---'*20}")
            else :
                print("User not found ")
                
        else:
            print("Exiting ... ")
            break
    
    
while(True):
    print("1.new user ")
    print("2.old user ")
    print("3. Exit ")
    
    choice = int(input("Enter Choice : "))
    
    if choice == 1:
        id = input("Enter User Id : ").strip().lower()
        if id in session:
            print("User Already Exists ..")
            continue
        
        session_id_manager(id)
        print("New session created")
        chat_session(id)

    elif choice == 2:
        id = input("Enter User Id : ").strip().lower()
        
        if id in session:
            print("User Found ..")
            chat_session(id)
        else:
            print("User Not Found")

    elif choice == 3:
        print("Exit")
        break
    
    else: 
        print("Invalid choice.....")
    
