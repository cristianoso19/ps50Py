students = [
    {"name": "Hermione", "house":"Gryffindor", "patronus":"Otter"},
    {"name": "Harry", "house":"Gryffindor", "patronus":"Stag"},
    {"name": "Ron", "house":"Gryffindor", "patronus":"Jack Rusell Terrier"},
    {"name": "Draco", "house":"Slytherin", "patronus":None}, #None ausence of a value
]

for student in students:
    print(student["name"], student["house"], student["patronus"], sep=", ")