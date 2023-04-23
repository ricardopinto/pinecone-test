from langchain.document_loaders import TextLoader
loader = TextLoader('/datasets/state_of_the_union.txt')

from langchain.embeddings import LlamaCppEmbeddings
from langchain.text_splitter import CharacterTextSplitter

documents = loader.load()
from langchain.text_splitter import CharacterTextSplitter
text_splitter = CharacterTextSplitter(chunk_size=450, chunk_overlap=0)
texts = text_splitter.split_documents(documents)

embeddings = LlamaCppEmbeddings(model_path="/models/ggml-vicuna-13b-1.1-q4_3.bin")

# pinecone
import pinecone
from langchain.vectorstores import Pinecone

# initialize pinecone
pinecone.init(
    api_key="<redacted>",  # find at app.pinecone.io
    environment="asia-northeast1-gcp"  # next to api key in console
)

index_name = "test" # this index was created with P1 pod type, has 5120 dimensions and uses euclidean distance

docsearch = Pinecone.from_documents(texts, embeddings, index_name=index_name) # <-- error here
