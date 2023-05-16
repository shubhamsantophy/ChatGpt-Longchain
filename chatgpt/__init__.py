# import os
# from langchain.document_loaders import PyPDFLoader 
# from langchain.embeddings import OpenAIEmbeddings 
# from langchain.vectorstores import Chroma 
# from langchain.chains import ConversationalRetrievalChain
# from langchain.memory import ConversationBufferMemory
# from langchain.llms import OpenAI

# os.environ['OPENAI_API_KEY'] = "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"


# pdf_path = "/home/sip/Downloads/python-interview-questions-answers.pdf"
# loader = PyPDFLoader(pdf_path)
# pages = loader.load_and_split()

# embeddings = OpenAIEmbeddings(chunk_size=1)

# vectordb = Chroma.from_documents(pages, embedding=embeddings, 
#                                  persist_directory=".")
# vectordb.persist()

# memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)
# pdf_qa = ConversationalRetrievalChain.from_llm(OpenAI(temperature=0.9) , 
#                                                vectordb.as_retriever(), memory=memory)

# # query = "What is pickling and unpickling?"
# query = "What is Python? What are the benefits of using Python?"
# result = pdf_qa({"question": query})
# print(result['chat_history'])
