from ast import IsNot


curso = "Curso de Python"
nome_curso = curso
saldo, limite = 200, 200

# is - comparar se uma variável ocupa o mesmo espaço de memória de outra variável
print(curso is nome_curso)

print(curso is not nome_curso)

print(saldo is limite)