import pytest
from sqlalchemy import create_engine, text


db_connection_string = \
    "postgresql://myuser:mypassword@localhost:5432/mydatabase"

db = create_engine(db_connection_string)


@pytest.fixture()
def test_db_connection():
    db = create_engine(db_connection_string)
    try:
        yield db
    finally:
        db.close()


# Получить список таблиц
def test_db_connection():
    title= db.table_name()


# Добавить новое значение в колонку
def test_insert():
    sql = text("insert into db.table_name(\"name\") values (:new_name)")


# Изменить новое значение
def test_update():
    sql = text("update db.table_name set name = :changed_new_name")


# Удалить значение
def test_delete():
    sql = text("delete from db.table_name where name = :changed_new_name")
