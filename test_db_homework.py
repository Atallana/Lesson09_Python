import pytest
from SubjectTable import SubjectTable
from SubjectTable import db


db_connection_string = "postgresql://postgres:@localhost:5432/QA"

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
    updated = db.update_subject(new_subject)  # Передаем новое значение или старое+новое, в зависимости от вашей реализации
    
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