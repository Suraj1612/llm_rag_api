import faiss
import numpy as np
from sentence_transformers import SentenceTransformer

# Load an embedding model
embedding_model = SentenceTransformer("all-MiniLM-L6-v2")

# Function descriptions
function_descriptions = {
    "open_chrome": "Launch Google Chrome",
    "open_calculator": "Start the calculator",
    "get_cpu_usage": "Check CPU usage",
    "run_shell_command": "Execute shell commands"
}

# Convert descriptions to vector embeddings
descriptions = list(function_descriptions.values())
function_names = list(function_descriptions.keys())
embeddings = embedding_model.encode(descriptions)

# Store in FAISS index
dimension = embeddings.shape[1]
faiss_index = faiss.IndexFlatL2(dimension)
faiss_index.add(np.array(embeddings))

# Store function mapping
function_mapping = {i: name for i, name in enumerate(function_names)}

def retrieve_best_function(query):
    """Finds the best-matching function for a given query."""
    query_embedding = embedding_model.encode([query])
    _, index = faiss_index.search(query_embedding, 1)
    return function_mapping.get(index[0][0], None)
