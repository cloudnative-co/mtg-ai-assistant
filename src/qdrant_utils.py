import os
import shutil
from langchain.embeddings.openai import OpenAIEmbeddings
from qdrant_client import QdrantClient
from qdrant_client.models import Distance, VectorParams
from langchain.vectorstores import Qdrant
from config import QDRANT_HOST, QDRANT_PATH, COLLECTION_NAME


def load_qdrant():
    client = QdrantClient(host=QDRANT_HOST, port=6333)

    collections = client.get_collections().collections
    collection_names = [collection.name for collection in collections]

    if COLLECTION_NAME not in collection_names:
        client.create_collection(
            collection_name=COLLECTION_NAME,
            vectors_config=VectorParams(size=1536, distance=Distance.COSINE),
        )
        print('collection created')

    return Qdrant(
        client=client,
        collection_name=COLLECTION_NAME,
        embeddings=OpenAIEmbeddings()
    )


def recreate_qdrant():
    client = QdrantClient(host=QDRANT_HOST, port=6333)
    client.recreate_collection(
        collection_name=COLLECTION_NAME,
        vectors_config=VectorParams(size=1536, distance=Distance.COSINE),
    )
    print('collection recreated')


def build_vector_store(vtt_text):
    recreate_qdrant()

    Qdrant.from_texts(
        vtt_text,
        OpenAIEmbeddings(),
        url=QDRANT_HOST,
        collection_name=COLLECTION_NAME,
    )
