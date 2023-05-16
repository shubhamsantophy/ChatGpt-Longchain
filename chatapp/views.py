import os
from langchain.document_loaders import PyPDFLoader 
from langchain.embeddings import OpenAIEmbeddings 
from langchain.vectorstores import Chroma 
from langchain.chains import ConversationalRetrievalChain
from langchain.memory import ConversationBufferMemory
from langchain.llms import OpenAI
from django.views.generic import TemplateView
from django.core.files.storage import FileSystemStorage
from django.shortcuts import render


class UploadPdfView(TemplateView):
	template_name = 'pdf_page.html' 

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		return context


	def post(self, request):
		os.environ['OPENAI_API_KEY'] = "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"


		# ---------below commented line for static path of pdf file ---------#
		# pdf_path = "/home/sip/Downloads/python-interview-questions-answers.pdf"

		if request.FILES['myfile']:
			myfile = request.FILES['myfile']
			fs = FileSystemStorage()
			filename = fs.save(myfile.name, myfile)
			uploaded_file_path = fs.path(filename)

			loader = PyPDFLoader(uploaded_file_path)
			pages = loader.load_and_split()

			embeddings = OpenAIEmbeddings(chunk_size=1)

			vectordb = Chroma.from_documents(pages, embedding=embeddings, 
			                                 persist_directory=".")
			vectordb.persist()

			memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)
			pdf_qa = ConversationalRetrievalChain.from_llm(OpenAI(temperature=0.9) , 
                                               vectordb.as_retriever(), memory=memory)


			# ---------below line where you can write question which you want answer from selected PDF---------#
			# query = "How Python is interpreted?"
			query = "What is Python? What are the benefits of using Python?"

			result = pdf_qa({"question": query})
			print(result['chat_history'])
		return render(request, 'pdf_page.html', {'question':query, 'result':result['answer']})






