import pandas as pd

questions = [
    ["Qual é uma das principais vantagens do Python como linguagem de programação?", "Legibilidade de código", "Performance extrema","Portabilidade universal", "Interface gráfica avançada", 1],
    ["Qual é o nome da estrutura de controle de repetição em Python que permite executar um bloco de código várias vezes enquanto uma condição for verdadeira?", "Força Bruta", "Loop Incondicional", "Estrutura de Controle de Repetição", "Loop For", 4],
    ["Qual dos seguintes não é um tipo de dado em Python?", "Lista", "Tupla", "Conjunto", "Diretório", 4],
    ["Qual é a função da instrução 'elif' em uma estrutura condicional em Python?", "Encerrar o programa", "Definir uma condição padrão", "Executar um bloco de código quando a condição anterior for falsa", "Ignorar o bloco de código", 3],
    ["Qual é o módulo em Python usado para trabalhar com expressões regulares?", "math","random","re","os", 3]
]

# Dataframe do pandas
df = pd.DataFrame(questions, columns=["Perguntas", "Opção 1", "Opção 2", "Opção 3", "Opção 4", "Resposta"])

#Salvar arquivo excel
df.to_excel("questions.xlsx", index=False)

print("Perguntas inseridas com sucesso")