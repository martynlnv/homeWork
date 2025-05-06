from sqlalchemy import create_engine

db_connection_string = "postgresql://qa:skyqa@5.101.50.27:5432/x_clients"

db = create_engine(db_connection_string)

# Подключиться к базе данных
def test_db_connection():
    db = create_engine(db_connection_string)
    names = db.table_names()
    assert names[0] == 'alembic_version'

# Получить список таблиц
def test_db_connection():
    names = db.table_names()
    assert names[1] == 'app_users'

# Получить строки из таблицы. select
def test_db_connection():
    names = db.table_names()
    assert names[1] == 'app_users'

# Получить строки из таблицы
def test_select():
    rows = db.execute("select * from company").fetchall()
    print(rows)
    row1 = rows[0]

    assert row1[0] == 1
    assert row1["name"] == "QA Студия 'ТестировщикЪ'"

# Получить строку по одному фильтру
from sqlalchemy import create_engine, text

db_connection_string = "postgresql://qa:skyqa@5.101.50.27:5432/x_clients"
db = create_engine(db_connection_string)

def test_select_1_row():
    sql_statement = text("select * from company where id = :company_id")
    rows = db.execute(sql_statement, company_id = 1).fetchall()

    assert len(rows) == 1
    assert rows[0]["name"] == "QA Студия 'ТестировщикЪ'"

# Получить строки по двум фильтрам
def test_select_1_row_with_two_filters():
    sql_statement = text("select * from company where \"is_active\" = :is_active and id >= :id")
    my_params = {
        'id': 65,
        'is_active': True
    }

    rows = db.execute(sql_statement, my_params).fetchall()

    assert len(rows) == 2

# Добавить компанию. insert
def test_insert():
    sql = text("insert into company(\"name\") values (:new_name)")
    rows = db.execute(sql, new_name = 'SkyPro')

# Обновить компанию. update
def test_update():
    sql = text("update company set description = :descr where id = :id")
    rows = db.execute(sql, descr = 'New descr', id = 10)

# Удалить компанию. delete
def test_delete():
    sql = text("delete from company where id = :id")
    rows = db.execute(sql, id = 10)
