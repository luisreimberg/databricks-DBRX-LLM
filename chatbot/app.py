import chainlit as cl
import os
from langchain.embeddings import DatabricksEmbeddings
from langchain_pinecone import PineconeVectorStore
from langchain.chat_models import ChatDatabricks
from langchain.chains.question_answering import load_qa_chain

os.environ["PINECONE_API_KEY"] = "Chave API"
os.environ["PINECONE_INDEX_NAME"] = "Nome do index"

databricks_token = "Host Databricks"
databricks_host = "Token Databricks"


model_embeddings = DatabricksEmbeddings(host = databricks_host, api_token = databricks_token,
                           endpoint = "databricks-bge-large-en")

vectorstore = PineconeVectorStore(embedding=model_embeddings)

llm = ChatDatabricks(host = databricks_host , max_tokens=500, api_token = databricks_token,
                           endpoint = "databricks-dbrx-instruct")

chain = load_qa_chain(llm, chain_type="stuff")

@cl.on_message
async def main(message: cl.Message):
    # Your custom logic goes here...
    query = message.content
    docs = vectorstore.similarity_search(query)
    answer = chain.run(input_documents=docs, question=query)
    # Send a response back to the user
    await cl.Message(
        content=answer,
    ).send()
