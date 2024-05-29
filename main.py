from llama_index.llms.ollama import Ollama  #type: ignore
from llama_parse import LlamaParse #type: ignore
from llama_index.core import VectorStoreIndex, SimpleDirectoryReader, PromptTemplate #type: ignore
from llama_index.core.embeddings import resolve_embed_model # type: ignore
from dotenv import load_dotenv
load_dotenv()
llm = Ollama(model="phi3",request_timeout=300.0)

pdfparser = LlamaParse(result_type="markdown")
file_extractor = {".pdf":pdfparser }
documents = SimpleDirectoryReader("./resume", file_extractor=file_extractor).load_data()
embed_model = resolve_embed_model("local:BAAI/bge-m3")
vector_index = VectorStoreIndex.from_documents(documents, embed_model=embed_model)
query_engine = vector_index.as_query_engine(llm=llm)
result = query_engine.query("Print out all the lines in the achievements section, then for each line, divide the line into action verb, the task/project and the results/metric and show which part of line falls in which category, dont add any words")
print(result)