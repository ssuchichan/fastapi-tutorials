from fastapi import FastAPI

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
async def get_book(id: int):
    return {"id": id, "message": f"这是第{id}本书"}


@app.get("/user/{id}")
async def get_user(id: int):
    return {"id": id, "message": f"普通用户{id}"}





















































