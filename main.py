from fastapi import FastAPI
from pydantic import BaseModel
from function_embedding_store import retrieve_best_function
from code_generator import generate_code

app = FastAPI()

class UserRequest(BaseModel):
    prompt: str

@app.get("/")
def read_root():
    return {"message": "Welcome to the LLM + RAG API!"}

@app.post("/execute")
def execute_function(request: UserRequest):
    function_name = retrieve_best_function(request.prompt)

    if not function_name:
        return {"error": "No matching function found"}

    code_snippet = generate_code(function_name)
    return {
        "function": function_name,
        "code": code_snippet
    }

# Run the API: uvicorn main:app --reload

