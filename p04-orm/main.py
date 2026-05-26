from datetime import datetime
from fastapi import FastAPI, Depends
from sqlalchemy import DateTime, func, String, Float, select
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

app = FastAPI()

# 创建异步引擎
ASYNC_DB_URL = "mysql+aiomysql://root:csq123456@localhost:3306/fastapi_test?charset=utf8"
async_engine = create_async_engine(
    ASYNC_DB_URL,
    echo=True, # 可选，输出SQL日志
    pool_size=10, # 连接池活跃的连接数
    max_overflow=10, # 允许额外的连接数
)

# 定义模型类：基类 + 表对应的模型类
# 基类： 创建时间、更新时间
# 书籍表： id、书名、作者、价格、出版社

class Base(DeclarativeBase):
    create_time: Mapped[datetime] = mapped_column(DateTime, insert_default=func.now(), default=func.now, comment="创建时间")
    update_time: Mapped[datetime] = mapped_column(DateTime, insert_default=func.now(), default=func.now, comment="修改时间")


class Book(Base):
    __tablename__ = "book"
    id: Mapped[int] = mapped_column(primary_key=True, comment="书籍ID")
    name: Mapped[str] = mapped_column(String(255), comment="书名")
    author: Mapped[str] = mapped_column(String(255), comment="作者")
    price: Mapped[float] = mapped_column(Float, comment="价格")
    publisher: Mapped[str] = mapped_column(String(255), comment="出版社")

class User(Base):
    __tablename__ = "user"
    id: Mapped[int] = mapped_column(primary_key=True, comment="ID")
    username: Mapped[str] = mapped_column(String(255), comment="用户名")
    password: Mapped[str] = mapped_column(String(255), comment="密码")


# 建表：FastAPI启动时调用建表的函数
async def create_tables():
    async with async_engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


@app.on_event("startup")
async def startup():
    await create_tables()


@app.get("/")
async def root():
    return {"message": "Hello World"}



AsyncSessionLocal = async_sessionmaker(
    bind=async_engine, # 绑定数据库引擎
    class_=AsyncSession, # 制定会话类
    expire_on_commit=False, # 提交后会话不过期，不会重新查询数据库
)

async def get_database():
    async with AsyncSessionLocal() as session:
        try:
            yield session # 返回数据库会话给路由处理函数
            await session.commit() # 提交事务
        except Exception:
            await session.rollback() # 有异常，回滚
            raise
        finally:
            await session.close() # 关闭会话


@app.get("/book/books")
async def get_book_list(
    db: AsyncSession = Depends(get_database)
):
    result = await db.execute(select(Book))
    book = result.scalars().all()
    return book







































