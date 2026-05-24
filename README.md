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

### 响应类型

默认情况下，FastAPI会自动将路径操作函数返回的Python对象（字典、列表、Pydantic模型等），经由jsonable_encoder转换为JSON兼容格式，并包装
JSONResponse返回。这省去了手动序列化的步骤，让开发者能更专注于业务逻辑。如果需要返回非JSON数据（如HTML、文件流），FastAPI提供了丰富的响应
了类型来返回不同数据。

| 响应类型              | 用途            | 示例                                |
|-------------------|---------------|-----------------------------------|
| JSONResponse      | 默认响应，返回JSON数据 | return {"key":"value"}            |
| HTMLResponse      | 返回HTML内容      | return HTMLResponse(html_content) |
| PlainTextResponse | 返回纯文本         | return PlainTextResponse("text")  |
| FileResponse      | 返回文件下载        | return FileResponse(path)         |
| StreamingResponse | 流式响应          | 生成器函数返回数据                         |
| RedirectResponse  | 重定向           | return RedirectResponse(url)      |

### 中间件

中间件（Middleware）是一个在每次请求进入FastAPI应用时都会被执行的函数。它在请求到达实际的路径操作（路由处理函数）之前运行，并且在响应返回给
客户端之前再运行一次。中间件可以为每个请求前后添加统一的处理逻辑

### 依赖注入

使用依赖注入系统来共享通用逻辑，避免代码重复。

- 依赖项：可重用的组件（函数/类），负责提供某种功能或数据。
- 注入：FastAPI自动帮你调用依赖项，并将结果“注入”到路径操作函数中。














































































































































