import pytest
from sqlalchemy import create_engine

db_connection_string = \
    "postgresql://myuser:mypassword@localhost:5432/mydatabase"

db = create_engine(db_connection_string)


@pytest.fixture()
def db_connection():
    db = create_engine(db_connection_string)
    conn = db.connect()
    transaction = conn.begin()   # Начало транзакции
    yield conn
    transaction.rollback()    # Откат изменений
    conn.close()


def test_insert_and_delete_and_update(db_connection):
    repo = StudentTable()
    initial_count = repo.get_count(db_connection)
    student_name = "Test User"
    new_student_name = "Updated Test User"

    # Добавление
    repo.insert_student(db_connection, student_name)
    assert repo.get_count(db_connection) == initial_count + 1

    # Получение ID добавленного студента
    student_id = repo.find_student_by_name(db_connection, student_name)
    assert student_id is not None

    # Изменение
    repo.update_student_name(db_connection, student_id, new_student_name)
    update_student = repo.get_student_by_id(db_connection, student_id)
    assert update_student. name == new_student_name

    # Удаление
    repo.delete_student(db_connection, new_student_name)
    assert repo.get_count(db_connection) == initial_count
