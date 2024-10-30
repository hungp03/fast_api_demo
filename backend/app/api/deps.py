from collections.abc import Generator
from typing import Annotated
from core.dbconfig import DBConfig
from fastapi import Depends
from sqlalchemy.orm import Session

cfg = DBConfig()
engine = cfg.engine

def get_db() -> Generator[Session, None, None]:
    with Session(engine) as session:
        yield session


SessionDep = Annotated[Session, Depends(get_db)]