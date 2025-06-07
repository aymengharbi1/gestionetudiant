from dataclasses import dataclass, asdict
import json
from typing import List, Optional


@dataclass
class Student:
    id: int
    name: str
    age: int
    grade: float


class StudentManager:
    def __init__(self, storage_path: str = "students.json"):
        self.storage_path = storage_path
        self.students: List[Student] = []
        self._load()
        self._next_id = max((s.id for s in self.students), default=0) + 1

    def _load(self) -> None:
        try:
            with open(self.storage_path, "r", encoding="utf-8") as f:
                data = json.load(f)
            self.students = [Student(**item) for item in data]
        except FileNotFoundError:
            self.students = []

    def _save(self) -> None:
        with open(self.storage_path, "w", encoding="utf-8") as f:
            json.dump([asdict(s) for s in self.students], f, indent=2)

    def add_student(self, name: str, age: int, grade: float) -> Student:
        student = Student(id=self._next_id, name=name, age=age, grade=grade)
        self._next_id += 1
        self.students.append(student)
        self._save()
        return student

    def list_students(self) -> List[Student]:
        return list(self.students)

    def get_student(self, student_id: int) -> Optional[Student]:
        for student in self.students:
            if student.id == student_id:
                return student
        return None

    def remove_student(self, student_id: int) -> bool:
        student = self.get_student(student_id)
        if student:
            self.students.remove(student)
            self._save()
            return True
        return False

    def update_student(
        self,
        student_id: int,
        name: Optional[str] = None,
        age: Optional[int] = None,
        grade: Optional[float] = None,
    ) -> bool:
        student = self.get_student(student_id)
        if not student:
            return False
        if name is not None:
            student.name = name
        if age is not None:
            student.age = age
        if grade is not None:
            student.grade = grade
        self._save()
        return True
