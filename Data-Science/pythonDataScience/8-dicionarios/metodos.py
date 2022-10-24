#metodos da classe dict
#{}.clear - apaga todos os valores do dicionário
pessoa = {"nome": "Jonathan", "idade": 25, "telefone": "973303152"}
#pessoa.clear()
print(pessoa)

#{}.copy - faz uma cópia do dicionário

#{}.fromkeys - cria chaves para você
#nesse caso pode ser útil em duas situações, quando queremos criar um dicionário e não passar nenhuma informação para as chaves
#ou quando queremos passar um valor padrão
peole = {}
peole.fromkeys(["email", "endereço"], "vazio")
print(peole)

#{}.get - uma outra forma de acessar valores dentro do dicionário
#{}.items - retorna uma lista de tuplas, muito útil com o comando for
#{}.keys - retorna somente as chaves
#{}.pop - remove um valor(chave) do dicionário
#{}.popitem - remove itens na sequencia, sem precisar indicar a chave especifica

#{}.setdefault - se a chave já existe e já tem um valor, o setdefault respeita esse valor inicial
#caso não tenha valor inicial ou ainda não exista a chave o setdefault altera/adiciona um valor

#{}.update - permite a atualização do nosso dicionário com outro dicionário
#{}.values - values retorna todos os valores, mas sem voltar a chave

#in - serve para consultar se um valor se encontra em um dicionário
#del - remove um valor após ser atribuido ao del
