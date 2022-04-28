# EXERCICIO 1
# Entrada
# A entrada contém uma única linha contendo um nome de estudante s. 
# Saída
# Seu programa deve exibir “Hello, s”. No lugar da letra s, o programa deve exibir o nome lido. As aspas não devem ser exibidas. Não deve haver espaço em branco no final da linha. A saída não deve conter linhas em branco.

# Exemplo
# Entrada
# Afonso

# Saída
# Hello, Afonso

# Resposta:
# nome = input()
# print ("Hello, " + nome, end = "")

# //esse end = "" é para não pular linha

nome=input()
print("Hello, "+nome, end = "")
