from random import shuffle

student1 = str(input('Primeiro aluno: '))
student2 = str(input('Segundo aluno: '))
student3 = str(input('Terceiro aluno: '))
student4 = str(input('Quarto aluno: '))
list_students = [student1, student2, student3, student4]
shuffle(list_students)
print(f'A ordem de apresentação será {list_students}')
