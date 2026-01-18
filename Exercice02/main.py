students = {
    "Alice": {"Mathematiques": 90, "Francais": 80, "Histoire": 95},
    "Bob": {"Mathematiques": 75, "Francais": 85, "Histoire": 70},
    "Charlie": {"Mathematiques": 88, "Francais": 92, "Histoire": 78},
}

name_student_ask = input("Entrez le nom de l’étudiant : ")
found = False

if name_student_ask in students:
    student_items = students[name_student_ask]
    for matiere, note in student_items.items():
        print(f"{matiere}: {note}")
    total_student_grades = sum(student_items.values())
    moyenne = total_student_grades / len(student_items)
    print(f"Le moyenne de l'etudiant {name_student_ask} est de {moyenne} ")

# for name_student in students:
#     if name_student == name_student_ask:
#         found = True
#         total = 0
#         print(f"{name_student}:")
#         for matiere, note in students[name_student].items():
#             print(f"{matiere}: {note}")
#         for note in students[name_student].values():
#             total += note
#         denom = len(students[name_student].values())
#         moyenne = total / denom
#         print(f"Moyenne de l'étudiant {name_student} : {moyenne}")

#         break
# if not found:
#     print(f"Etudiant {name_student_ask} ,n'existe pas")
