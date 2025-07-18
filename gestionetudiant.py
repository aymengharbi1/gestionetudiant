import sqlite3
import argparse

DB_NAME = "gestion.db"


def create_tables() -> None:
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute(
        """CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            first_name TEXT NOT NULL,
            last_name TEXT NOT NULL,
            parent_contact TEXT
        )"""
    )
    c.execute(
        """CREATE TABLE IF NOT EXISTS absences (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            student_id INTEGER,
            date TEXT,
            FOREIGN KEY(student_id) REFERENCES students(id)
        )"""
    )
    c.execute(
        """CREATE TABLE IF NOT EXISTS notes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            student_id INTEGER,
            subject TEXT,
            score REAL,
            FOREIGN KEY(student_id) REFERENCES students(id)
        )"""
    )
    conn.commit()
    conn.close()


def add_student(first_name: str, last_name: str, parent_contact: str) -> None:
    create_tables()
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute(
        "INSERT INTO students (first_name, last_name, parent_contact) VALUES (?,?,?)",
        (first_name, last_name, parent_contact),
    )
    conn.commit()
    conn.close()
    print("Student added.")


def record_absence(student_id: int, date: str) -> None:
    create_tables()
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute(
        "INSERT INTO absences (student_id, date) VALUES (?,?)",
        (student_id, date),
    )
    conn.commit()
    conn.close()
    print("Absence recorded.")


def record_note(student_id: int, subject: str, score: float) -> None:
    create_tables()
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute(
        "INSERT INTO notes (student_id, subject, score) VALUES (?,?,?)",
        (student_id, subject, score),
    )
    conn.commit()
    conn.close()
    print("Note recorded.")


def show_student(student_id: int) -> None:
    create_tables()
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute(
        "SELECT id, first_name, last_name, parent_contact FROM students WHERE id=?",
        (student_id,),
    )
    student = c.fetchone()
    if not student:
        print("Student not found.")
        return
    print(
        f"Student {student[0]}: {student[1]} {student[2]}, parent contact: {student[3]}"
    )
    c.execute("SELECT date FROM absences WHERE student_id=?", (student_id,))
    absences = c.fetchall()
    if absences:
        print("Absences:")
        for (date,) in absences:
            print(f"  {date}")
    c.execute("SELECT subject, score FROM notes WHERE student_id=?", (student_id,))
    notes = c.fetchall()
    if notes:
        print("Notes:")
        for subject, score in notes:
            print(f"  {subject}: {score}")
    conn.close()


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Gestion des étudiants")
    sub = parser.add_subparsers(dest="command")

    add = sub.add_parser("add-student", help="Add a new student")
    add.add_argument("first_name")
    add.add_argument("last_name")
    add.add_argument("parent_contact")

    absence = sub.add_parser("record-absence", help="Record an absence")
    absence.add_argument("student_id", type=int)
    absence.add_argument("date")

    note = sub.add_parser("record-note", help="Record a note")
    note.add_argument("student_id", type=int)
    note.add_argument("subject")
    note.add_argument("score", type=float)

    show = sub.add_parser("show-student", help="Display student information")
    show.add_argument("student_id", type=int)

    return parser.parse_args()


def main() -> None:
    args = parse_args()
    if args.command == "add-student":
        add_student(args.first_name, args.last_name, args.parent_contact)
    elif args.command == "record-absence":
        record_absence(args.student_id, args.date)
    elif args.command == "record-note":
        record_note(args.student_id, args.subject, args.score)
    elif args.command == "show-student":
        show_student(args.student_id)
    else:
        print("No command provided.")


if __name__ == "__main__":
    main()
