from random import choice

student1 = str(input('Primeiro aluno: '))
student2 = str(input('Segundo aluno: '))
student3 = str(input('Terceiro aluno: '))
student4 = str(input('Quarto aluno: '))
list_students = [student1, student2, student3, student4]
print(f'O aluno escohlido foi {choice(list_students)}')
