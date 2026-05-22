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

