# 0. Setting

(middleware_learn can be replace with any name)
conda create -n middleware_learn
conda activate middleware_learn

conda install fastapi uvicorn pydantic (or pip)
conda install python-multipart
conda install jinja2

# 2. explain code

# 2.1 Middleware Definition

Middleware is software that sits between an operating system and the applications running on it. Acting as a hidden translation layer, middleware enables communication and data management for distributed applications. It facilitates the connection between different services such as web servers, databases, and cloud systems, allowing them to interact seamlessly.

## 2.2 Why Middleware?

Middleware is used for various purposes, but in this example, it is primarily used for two reasons:

Maintaining and Checking Login Status:
After a user logs in via the login API, the middleware continuously checks the login status when navigating through different pages like mypage. It ensures that the user remains logged in without requiring repeated login attempts or redirection to the login page. Middleware intercepts each request to verify that the user is authenticated, allowing only authorized access to specific pages.

Blocking Access After Logout:
When a user logs out, the middleware automatically prevents access to private pages like mypage or any other restricted areas. It redirects the user to the guest page or login page, ensuring that logged-out users cannot access protected information. This mechanism enhances security by ensuring that once a user logs out, they cannot access previously available resources.

# 3. How to test

1. uvicorn app:app --reload
2. 127.0.0.1:8000 or localhost:8000 on browser

# minor tips

how to kill port instead of killing terminals
lsof -i :8000
kill -9 PID ex kill -9 1234
