import sqlalchemy
from typing import AsyncGenerator
from uuid import UUID as UUIDTYPE
from datetime import datetime

from uuid6 import uuid7
from sqlalchemy import DateTime
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.dialects.postgresql import UUID as UUIDCOLUMN

from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker
from sqlalchemy.ext.declarative import declarative_base

from src.config import Config

SQLALCHEMY_DATABASE_URL = f"postgresql+asyncpg://{Config.DB_USER}:{Config.DB_PASS}@{Config.DB_HOST}:{Config.DB_PORT}/{Config.DB_NAME}"

engine = create_async_engine(SQLALCHEMY_DATABASE_URL)
async_session_maker = async_sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)


async def get_async_session() -> AsyncGenerator[AsyncSession, None]:
    async with async_session_maker() as session:
        yield session

Base = declarative_base()


async def create_db() -> None:
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


async def drop_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)


class UuidMixin:
    id: Mapped[UUIDTYPE] = mapped_column(
        "id",
        UUIDCOLUMN(as_uuid=True),
        primary_key=True,
        default=uuid7,
        unique=True,
        index=True,
        nullable=False,
    )


class utcnow(sqlalchemy.FunctionElement):
    type = DateTime()
    inherit_cache = True


class TimestampMixin:
    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        nullable=False,
        server_default=utcnow(),
        sort_order=9999,
    )
    updated_at: Mapped[datetime] = mapped_column(
        DateTime,
        nullable=True,
        index=True,
        server_default=utcnow(),
        server_onupdate=utcnow(),
        sort_order=10000,
    )