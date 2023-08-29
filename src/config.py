import os

APP_NAME = " MTG AI アシスタント(β)"
SPLIT_SECONDS = 600
OUTPUT_DIR = "/tmp/data/"
QDRANT_PATH = "/tmp/local_qdrant"
COLLECTION_NAME = "my_collection_2"
QDRANT_HOST = os.environ.get("QDRANT_HOST", "localhost")
QDRANT_PORT = os.environ.get("QDRANT_PORT", 6333)
