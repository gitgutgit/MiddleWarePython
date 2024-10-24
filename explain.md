# 0. Setting

(middleware_learn can be replace with any name)
conda create -n middleware_learn
conda activate middleware_learn

conda install fastapi uvicorn pydantic (or pip)
conda install python-multipart
conda install jinja2

# 2. explain code

why middleware?
Middleware definition:
middleware is a function that is called before the request is processed

# 3. How to test

1. uvicorn app:app --reload
2. 127.0.0.1:8000 or localhost:8000 on browser

# minor tips

how to kill port instead of killing terminals
lsof -i :8000
kill -9 PID ex kill -9 1234
