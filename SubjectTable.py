from sqlalchemy import create_engine
from sqlalchemy import text


class SubjectTable:
    __scripts = {
        "INSERT_INTO": text("INSERT INTO subject (subject_title) VALUES (:subject_title)"),
        "UPDATE": text("UPDATE subject SET subject_title = :new_subject WHERE subject_title = :old_subject"),
        "DELETE_BY_TITLE": text("DELETE FROM subject WHERE subject_title = :subject_title")
    }

    def __init__(self, connection_string):
        self._db = create_engine(connection_string)

    def insert_subject(self, subject):
        with self._db.connect() as db:
            db.execute(self.__scripts["INSERT_INTO"], {"subject_title": subject})
            db.commit()

    def update_subject(self, old_subject, new_subject):
        with self._db.connect() as db:
            db.execute(self.__scripts["UPDATE"], {"old_subject": old_subject, "new_subject": new_subject})
            db.commit()

    def delete_subject(self, subject):
        with self._db.connect() as db:
            db.execute(self.__scripts["DELETE_BY_TITLE"], {"subject_title": subject})
            db.commit()
