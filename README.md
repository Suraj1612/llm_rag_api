"# llm_rag_api" 

==================================================================================================

AUTOMATION_FUNCTION.py
Defines a set of automation functions (e.g., opening Chrome, launching the calculator, checking CPU usage, executing shell commands).
Stores these functions in a dictionary (FUNCTIONS).

CODE_GENERATOR.py
Generates Python scripts dynamically to execute selected functions.

FUNCTION_EMBEDDING_STORE.py
Uses sentence-transformers and FAISS to embed function descriptions.
Retrieves the most relevant function based on user input.

MAIN.py
Implements a FastAPI service.
Accepts user input, retrieves the best-matching function, and returns the generated code snippet.

Possible Improvements:

Function Execution:
Your current API only generates code but doesn’t execute it. You might need an execution layer.

Security Concerns:
Running shell commands (run_shell_command) can be risky. You might want to add validation or a sandboxed environment.

Enhancing Retrieval:
More function descriptions could improve retrieval accuracy. You could also consider using cosine similarity instead of L2 distance in FAISS.
