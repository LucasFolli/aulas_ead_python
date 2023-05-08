#Aula 02: Ambiente de desenvolvimento, tipos de dados e variáveis

#Shell: Modo shell ou modo interativo, interpretador interativo do IDLE

print('Olá, mundo!')

#Constantes (também chamadas de literais) são símbolos que representam
#valores escritos diretamente no código e não podem ser alterados em tempo de execução
#int: números inteiros; float: representação de números reais; bool: valores lógicos;
#string: caracteres.

#Operadores são símbolos pré-definidos que realizam uma operação sobre um ou mais operandos
#produzindo valor como resultado.

#Variáveis são espaços alocados na memória para armazenar um valor, um dado.
#Exemplo:
dia_semana = "Sábado" #Variável "dia_semana" com valor do tipo string "Sábado"
#O sinal "=" é um operador de atribuição.
#O nome (identificador) da variável é formado por uma sequência de um ou mais caracteres. Regras:
#Pode conter letras, números e underline; não pode começar com número; não pode ser palavra reservada;
#não pode conter caracteres especiais (como: &, ", %, $, #, @, !).
#Palavras reservadas:
help('keywords')

#Exemplo de código: operação de subtração
n1 = int(input('Insira um número inteiro: '))
n2 = int(input('Insira outro: '))
sub = n1-n2
print(f"A subtração n1-n2 ({n1}-{n2}) é igual a: {sub}")

