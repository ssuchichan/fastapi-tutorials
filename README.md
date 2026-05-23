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

### 参数

- 路径参数
    - 位置：URL路径的一部分，`/book/{id}`
    - 作用：指向唯一的、特定的资源
    - 方法：GET
- 查询参数
    - 位置：URL?之后，`k1=v1&k2=v2`
    - 作用：对资源集合进行过滤、排序、分页等操作
    - 方法：GET
- 请求体
    - 位置：HTTP请求的消息体(body)中
    - 作用：创建、更新资源，携带大量数，据如：JSON
    - 方法：POST、PUT等

### 请求体参数

在HTTP协议中，一个完整的请求体由三部分组成：

- 请求行：包含方法、URL、协议版本
- 请求头：元数据信息（Content-Type、Authorization）等
- 请求体：实际要发送的数据内容

使用请求体参数：

- 定义类型
- 类型注解











































































