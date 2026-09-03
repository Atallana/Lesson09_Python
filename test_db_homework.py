import pytest
from SubjectTable import SubjectTable


db_connection_string = "postgresql://postgres:1809@localhost:5432/QA"
db = SubjectTable(db_connection_string)

# Добавить сущность: insert
def test_insert():
    subject = "NEW_SUBJECT"
    
    # Если методы возвращают измененные данные или статус:
    result = db.insert_subject(subject)
    
    # Проверяем, что объект успешно создался
    assert result is not None

    # Очищаем за собой БД после теста
    db.delete_subject(subject)


# Обновить сущность: update
def test_update():
    subject = "NEW_SUBJECT"
    db.insert_subject(subject)
    
    new_subject = "NEW_SUBJECT_2"
    updated = db.update_subject(new_subject)
    
    # Проверяем, что название действительно изменилось
    assert updated["subject"] == new_subject
    
    # Удаляем измененную сущность, чтобы очистить БД
    db.delete_subject(new_subject)


# Удалить сущность: delete
def test_delete():
    subject = "NEW_SUBJECT"
    db.insert_subject(subject)
    
    deleted = db.delete_subject(subject)
    
    # Проверяем корректность ответа об удалении
    assert deleted["subject"] == subject
    assert deleted["detail"] == "Компания успешно удалена"

if __name__ == "__main__":
    test_insert()