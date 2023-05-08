#Aula 03: Funções embutidas, entrada e saída, operadores e expressões aritméticas

#Expressão: combinação de operandos com um ou mais operadores e que resulta em um valor. Operandos
#podem ser constantes ou variáveis

#Precedência é importante, como em matemática (Ex: 2 + 3 * 5 = 17; (2 + 3) * 5 = 25)

#Associatividade: No python às vezes a precedência não basta, usamos a associatividade, que define
#como operadores de mesma precedência devem ser agrupados, caso haja ausência de parênteses.
#Exemplo: 2 ** 1 ** 2 = 2
##Tabela:
##    Operador        Descrição               Associatividade
##    __________________________________________________
##      **            Exponenciação                   à direita
##    __________________________________________________
##     +, -           Identidade e
##    (unários)       negação (inversão
##                             de sinal)
##    
##    *, /, //, %     Multiplicação,      
##                    divisão real,                   }à esquerda
##                    divisão inteira
##                    e resto da divisão
##    
##    +, -            Adição e subtração
##    (binários)
##    __________________________________________________
##    =, +=, -=, *=,
##    /=, //=, %=, **=    Atribuição (simples         Não associativos
##                                    e composta)
##    __________________________________________________

#Este código retorna 47.0
a,b,c,d,e,f,s = [5,4,9,7,1,2,10]; s += a + b ** (c - d) / e * f; print(s)
#Este código retorna 47.0

#Função: Sequência de instruções que executa uma tarefa específica e tem um nome:
#Integradas: estão disponíveis na própria linguagem de programação e podem ser usadas a qualquer momento;
#Importadas: criadas por outros programadores e disponibilizadas para serem utilizadas no ambiente de desenvolvimento;
#Definidas: criadas por nós mesmos e estão no código fonte.

#Saída de dados: Exibição de dados na tela, com a função "print". Exemplo:
print('Olá mundo!')    #1 argumento (dados dentro dos parênteses de uma função)
print('2 + 2 = ', 2+2) #2 argumentos: quando uma função tem mais de um argumento, a separação é feita por vírgula
#Entrada de dados: Entrada por parte do usuário, com a função "input". Exemplo:
nome = input('Digite seu nome: '); print(nome)
#A função input sempre irá retornar o que foi digitado como string.
#Pode-se especificar o tipo da entrada do usuário assim:
TesteEntrada1 = int(input('Digite um número inteiro: ')); TesteEntrada2 = float(input('Digite um número real: '))

#Erros mais comuns na programação:
#Erros de sintaxe: Erros na escrita das instruções da linguagem, violação de regras e estruturas;
#Erros de tempo de execução: Aparecem só quando o programa é executado, quando o usuário digita um
#valor incompatível com o tipo de dado solicitado, por exemplo;
#Erros de lógica/semântica: Erros no algoritmo. Nesse caso o programa pode executar normalmente, mas
#não resolve o problema proposto.

##  Treino: Crie uma solução, onde o programa solicita o valor de um produto e a quantidade desse
##  produto e por fim exibe o preço total com desconto de 10%. Considere que o total será um número
##  inteiro positivo.

valorProduto = float(input('Digite o valor do produto: '))
quantidadeProduto = int(input('Digite a quantidade: '))
valorTotal = quantidadeProduto * valorProduto - ((quantidadeProduto * valorProduto) * 0.1)
print(f'Foram compradas {quantidadeProduto} unidades. O valor total com desconto de 10% é: {valorTotal:.2f}.')
