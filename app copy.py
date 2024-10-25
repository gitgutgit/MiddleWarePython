from fastapi import FastAPI, Request, Form, Depends, HTTPException
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel

app = FastAPI()

# template directory 
templates = Jinja2Templates(directory="templates")

# users_db (for testing)
# it could be replaced by real db
users_db = {
    "testuser": {
        "username": "testuser",
        "password": "1234",
        "birthday": "1990-01-01",
        "gender": "Male",
        "phone": "+1-202-555-0183"
    },
    "anotheruser": {
        "username": "anotheruser",
        "password": "1234",
        "birthday": "1985-05-12",
        "gender": "Female",
        "phone": "+1-303-555-0144"
    }
}


# Login Form model
class LoginForm(BaseModel):
    username: str
    password: str

# Authenticate user
def authenticate_user(username: str, password: str):
    user = users_db.get(username)
    if user and user["password"] == password:
        return user
    return None

# Middleware: check login status
@app.middleware("http")
async def check_login(request: Request, call_next):
    if request.url.path not in ["/login", "/"]:
        if "username" not in request.cookies:
            return RedirectResponse(url="/login", status_code=302)
    
    response = await call_next(request)
    return response

# Login page
@app.get("/login", response_class=HTMLResponse)
async def login_form(request: Request):
    return templates.TemplateResponse("loginpage.html", {"request": request})

# login api
@app.post("/login", response_class=HTMLResponse)
async def login(request: Request, username: str = Form(...), password: str = Form(...)):
    user = authenticate_user(username, password)
    if user:
        response = RedirectResponse(url="/", status_code=302)
        response.set_cookie(key="username", value=user["username"])  # 쿠키로 로그인 상태 유지
        return response
    else:
        return templates.TemplateResponse("loginpage.html", {"request": request, "error": "Invalid credentials"})

@app.get("/logout")
async def logout():
    response = RedirectResponse(url="/")
    response.delete_cookie("username")  # delete cookie
    return response


# Main page
@app.get("/", response_class=HTMLResponse)
async def homepage(request: Request):
    username = request.cookies.get("username")
    if username:
        return templates.TemplateResponse("index.html", {"request": request, "username": username})
    else:
        return templates.TemplateResponse("guest_index.html", {"request": request})


# Mypage Api
@app.get("/mypage", response_class=HTMLResponse)
async def mypage(request: Request):
    username = request.cookies.get("username")
    if username:
        user = users_db.get(username)
        return templates.TemplateResponse("mypage.html", {"request": request, "user": user})
    raise HTTPException(status_code=403, detail="Not authorized")
