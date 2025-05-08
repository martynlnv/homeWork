import pytest

empty_dict = {}

football_stats = {
    "Число стран": 48,
    "Страна": "Катар",
    "Участники": ["Австралия", "Англия", "Аргентина", "Бельгия", "еще 42 страны", "Эквадор", "Япония"],
    "Награды": {
        "Золотой мяч": "Лионель Месси",
        "Серебряный мая": "Килиан Мбаппе",
        "Золотая бутса": "Килиан Мбаппе",
        "Серебряная бутса": "Килиан Мбаппе",
        "Золотой мая": "Лионель Месси",
        "Больше всего голов": {
            "Игрок": "Килиан Мбаппе - капитан команды",
            "Количество мячей": 8
        },
    }
}

def test_empty_dict():
    assert len(empty_dict) == 0

# Читаем словарь
def test_read_value():
    count = football_stats.get('Число стран')
    assert count == 48

# Прямое чтение
def test_read_value():
    country = football_stats['Страна']
    assert country == 'Катар'

# Записать значение
def test_write_read_value():
    football_stats['Число стран'] = 50
    count = football_stats.get('Число стран')
    assert count == 50

# Тест на новое значение
def test_write_new_value():
    football_stats['Победитель'] = 'Аргентина'
    winner = football_stats['Победитель']
    assert winner == 'Аргентина'

# Сложные тесты
def test_read_list():
    participants = football_stats['Участники']
# participants = ["Австралия", "Англия", "Аргентина", "Бельгия", "ещё 42 страны", "Эквадор", "Япония"]
    england = football_stats["Участники"][1]

    assert len(participants) > 0
    assert participants[0] == "Австралия"
    assert england == "Англия"

# Запрос списки в списке
def test_read_dict():
    awards = football_stats['Награды']['Золотая бутса']
    assert awards == 'Килиан Мбаппе'

def test_read_dict():
    total_goals = football_stats['Награды']['Больше всего голов']['Количество мячей']
    assert total_goals == 8

# Вычленение словаря в переменную
def test_save_dict():
    awards = football_stats['Награды']
    player = awards['Больше всего голов']['Игрок']
    assert player == 'Килиан Мбаппе - капитан команды'

# Вводим Pytest, import, error ; прямое чтение из словаря
def test_read_error():
    with pytest.raises(KeyError):
        empty_dict['key'] #None

# Чтение из словаря при помощи метода get (мягче)
def test_get_empty():
    value = test_empty_dict('key')
    assert value == None

# Метод get вернет значение, если ничего нет. Пригодится, когда  нужные добавлять в программу новые значения
def test_get_empty_or_default():
    value = empty_dict.get('key', 'abc123')
    assert  value == 'abc123'

