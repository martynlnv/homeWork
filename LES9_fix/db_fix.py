from sqlalchemy import create_engine, text

class StudentTable:
    @staticmethod
    def insert_student(conn, name):
        conn.execute(text(
            "INSERT INTO students(name) VALUES (:name)"),
                     {"name" :name})
        conn.commit()

    @staticmethod
    def get_count(conn):
        result = conn.execute(text(
            "SELECT COUNT(*) FROM students"
        )).scalar()
        return result

    @staticmethod
    def find_student_by_name(conn, name):
        result = conn.execute(text("SELECT id FROM students WHERE name = :name"),
                              {"name":name}).fetchone()
        if result:
            return  result[0]
        return None

    @staticmethod
    def get_student_by_id(conn, student_id):
        result = conn.execute(text("SELECT id, name FROME students WHERE id = :id"), {"id": student_id}).fetchone()
        if result:
            return {"id": result[0], "name":result[1]}
        return None

    @staticmethod
    def update_student_name(conn, student_id, new_name):
        conn.execute(text("UPDATE students SET name =:new_name WHERE id = :id"),
                     {"new_name" :new_name, "id" : student_id})
        conn.commit()

    @staticmethod
    def delete_student(conn, name):
        conn.execute(text("DELETE FROM students WHERE name = :name"), {"name": name})
        conn.commit()

    @staticmethod
    def delete_student_by_id(conn, student_id):
        conn.execute(text("DELETE FROM students WHERE id = :id"), {"id": student_id})
        conn.commit()










