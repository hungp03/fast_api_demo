import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from contextlib import contextmanager
from sqlalchemy.exc import OperationalError

load_dotenv()
Base = declarative_base()


class DBConfig:
    def __init__(self):
        self.database_url = os.getenv("DATABASE_URL")
        if not self.database_url:
            raise ValueError("DATABASE_URL không được cấu hình trong file .env")
        try:
            self.engine = create_engine(self.database_url, echo=True)
            self.engine.connect()
            print("Kết nối cơ sở dữ liệu thành công!")
        except OperationalError as e:
            print("Kết nối cơ sở dữ liệu thất bại:", e)
            raise

        # Tạo session để giao tiếp với cơ sở dữ liệu
        self.SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=self.engine)

    def create_session(self):
        # Tạo một phiên làm việc (session) với cơ sở dữ liệu
        return self.SessionLocal()

    def create_tables(self):
        # Tạo các bảng trong cơ sở dữ liệu (nếu chưa có)
        Base.metadata.create_all(bind=self.engine)

    def drop_tables(self):
        # Xóa các bảng trong cơ sở dữ liệu
        Base.metadata.drop_all(bind=self.engine)

    @contextmanager
    def session_scope(self):
        session = self.create_session()
        try:
            yield session
            session.commit()
        except Exception as e:
            session.rollback()
            raise e
        finally:
            session.close()
