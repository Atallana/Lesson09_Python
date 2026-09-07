import pytest
from SubjectTable import SubjectTable


db_connection_string = "postgresql://postgres:1809@localhost:5432/QA"
db = SubjectTable(db_connection_string)

# Добавить сущность
def test_create_subject():
    subject = "NEW_SUBJECT"
    db.create_subject(subject)

    assert subject == "NEW_SUBJECT"

    # Очищаем за собой БД после теста
    db.delete_subject(subject)

# Изменить сущность
def test_update():
    subject = "NEW SUBJECT"
    db.create_subject(subject)
    
    new_subject = "NEW_SUBJECT_2"
    updated = db.update_subject(subject, new_subject)
    
    assert updated["subject"] == new_subject
    
    # Очищаем за собой БД после теста
    db.delete_subject(new_subject)

# Удалить сущность
def test_delete():
    subject = "NEW SUBJECT"
    db.create_subject(subject)
    
    deleted = db.delete_subject(subject)
    
    assert deleted["subject"] == subject
    