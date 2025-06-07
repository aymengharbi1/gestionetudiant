import argparse
from student_manager import StudentManager


def main() -> None:
    parser = argparse.ArgumentParser(description="Gestion des élèves")
    subparsers = parser.add_subparsers(dest="cmd")

    add_parser = subparsers.add_parser("add", help="Ajouter un élève")
    add_parser.add_argument("name")
    add_parser.add_argument("age", type=int)
    add_parser.add_argument("grade", type=float)

    subparsers.add_parser("list", help="Lister les élèves")

    remove_parser = subparsers.add_parser("remove", help="Supprimer un élève")
    remove_parser.add_argument("id", type=int)

    update_parser = subparsers.add_parser("update", help="Mettre à jour un élève")
    update_parser.add_argument("id", type=int)
    update_parser.add_argument("--name")
    update_parser.add_argument("--age", type=int)
    update_parser.add_argument("--grade", type=float)

    args = parser.parse_args()
    manager = StudentManager()

    if args.cmd == "add":
        student = manager.add_student(args.name, args.age, args.grade)
        print(f"Élève ajouté: {student}")
    elif args.cmd == "list":
        for s in manager.list_students():
            print(f"{s.id}: {s.name}, {s.age} ans, note {s.grade}")
    elif args.cmd == "remove":
        if manager.remove_student(args.id):
            print("Élève supprimé")
        else:
            print("Élève introuvable")
    elif args.cmd == "update":
        if manager.update_student(args.id, args.name, args.age, args.grade):
            print("Élève mis à jour")
        else:
            print("Élève introuvable")
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
