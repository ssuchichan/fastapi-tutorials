from fastapi import FastAPI, Path, Query
from pydantic import BaseModel, Field

# 创建FastAPI实例
app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}


@app.get("/hello")
async def say_hello():
    return {"message": "你好，FastAPI"}


@app.get("/user/hello")
async def say_hello():
    return {"message": "我正在学习FastAPI"}


@app.get("/book/{id}")
async def get_book(id: int = Path(...,gt=0, lt=101, description="书籍的ID,取之范围1-100")):
    return {"id": id, "title": f"这是第{id}本书"}

@app.get("/author/{name}")
async def get_book(name: str = Path(..., max_length=10, min_length=2, description="书的作者，长度2-10字符")):
    return {"msg": f"这是{name}的信息"}


@app.get("/user/{id}")
async def get_user(id: int):
    return {"id": id, "message": f"普通用户{id}"}


@app.get("/news/news_list")
async def get_news_list(
        skip: int = Query(0, lt=100, description="跳过的记录数"),
        limit: int = Query(10, description="返回的记录数")
):
    return {"skip": skip, "limit": limit}


# 定义类型
class User(BaseModel):
    username: str = Field(default="王德发", min_length=2, max_length=10, description="用户名，长度为2-10各字符")
    password: str = Field(min_length=6, max_length=32)
    email: str = Field(...)

@app.post("/register")
async def register(user: User):
    return {"username": user.username, "password": user.password, "email": user.email}



















































































