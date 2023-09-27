import os
import sys
import openai
from dotenv import load_dotenv
from langchain.vectorstores import Chroma
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.chat_models import ChatOpenAI
from langchain.chains import RetrievalQA
from langchain.prompts import PromptTemplate

sys.path.append("../..")

load_dotenv()
openai.api_key = os.environ["OPENAI_API_KEY"]
LLM = os.environ["TURBO"]

persist_directory = "vector-store/chroma/"
embedding = OpenAIEmbeddings()
vectordb = Chroma(persist_directory=persist_directory, embedding_function=embedding)

llm = ChatOpenAI(model_name=LLM, temperature=0)

template = """Use the following pieces of context to answer the question at the
end. Use three sentences maximum. Keep the answer as concise as possible, but
speak it with the personality of Chacha Chaudhary.
{context}
Question: {question}
Helpful Answer:"""
QA_CHAIN_PROMPT = PromptTemplate.from_template(template)
qa_chain = RetrievalQA.from_chain_type(
    llm,
    retriever=vectordb.as_retriever(),
    return_source_documents=True,
    chain_type_kwargs={"prompt": QA_CHAIN_PROMPT},
)


def get_response(question: str):
    result = qa_chain({"query": question})
    return result["result"]