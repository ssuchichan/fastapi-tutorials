# FastAPI Tutorials

## Run

```
uvicorn main:app --reload
```

## 基础

### 路由

URL地址和处理函数之间的映射关系

```python
@app.get("/hello")
async def say_hello():
    return {"message": "你好，FastAPI"}
```


