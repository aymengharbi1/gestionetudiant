from student_manager import StudentManager


def test_add_list_remove(tmp_path):
    storage = tmp_path / "students.json"
    mgr = StudentManager(str(storage))

    s1 = mgr.add_student("Alice", 12, 15.5)
    assert s1.id == 1
    students = mgr.list_students()
    assert len(students) == 1
    assert students[0].name == "Alice"

    assert mgr.remove_student(s1.id) is True
    assert mgr.list_students() == []

def test_update_student(tmp_path):
    storage = tmp_path / "students.json"
    mgr = StudentManager(str(storage))
    s1 = mgr.add_student("Bob", 13, 14.0)

    assert mgr.update_student(s1.id, grade=16.0) is True
    student = mgr.get_student(s1.id)
    assert student.grade == 16.0

    assert mgr.update_student(999, name="ghost") is False
