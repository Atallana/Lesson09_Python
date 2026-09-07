from sqlalchemy import create_engine
from sqlalchemy import text


class SubjectTable:
    __scripts = {
        "INSERT_NEW": text("INSERT INTO subject(\"subject\") values (:new_subject)"),
        "UPDATE": text("UPDATE subject SET subject_title = :new_subject WHERE subject_title = :subject"),
        "DELETE_BY_TITLE": text("DELETE FROM subject WHERE subject_title = :subject_title")
    }

    def __init__(self, connection_string):
        self.__db = create_engine(connection_string)

    def create_subject(self, subject):
        self.__db.execute(self.__scripts["INSERT_NEW"], new_subject=subject)
    
    def update_subject(self, subject, new_subject):
        self.__db.execute(self.__scripts["UPDATE"], {
                "subject": subject, "new_subject": new_subject})

    def delete_subject(self, subject):
        self._db.execute(self.__scripts["DELETE_BY_TITLE"], {"subject_title": subject})
