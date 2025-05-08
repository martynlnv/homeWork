import pytest
from sqlalchemy import create_engine

db_connection =  "postgresql://SpbLeven:qwaszx1234@localhost:5432/SpbLNV"

db = create_engine(db_connection)
@pytest.fixture()
def test_db_connection():
    db = create_engine(db_connection)
    try:
        yield db
    finally:
        db.close()

# Тест на добавление
def test_add_item(db):
   new_item = Item(name = "Test Item",
description = "This is a test item.")
   db.add(new_item)
   db.commit()

# Проверка, что предмет добавлен в базу
added_item = db.query(Item).filter(Item.name == "Test Item").first()
assert added_item.name == "Test Item"
assert added_item.description == "This is a test item."

# Проверить изменения


# Изменить данные предмета
def test_update(db):
    added_item.name = "Up test Item"
    added_item.description = "Up description"
    db.commit()

# Удалить предмет
def test_delete(db):
    db.delete(added_item.name)
    db.commit()



