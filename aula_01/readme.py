#Aula 01: Introdução à disciplina e conceitos iniciais

#"Algoritmo é uma sequência finita de passos logicamente ordenados para obtenção de uma solução para um problema"
#Representação: Capta os detalhes mais importantes do problema, abstraindo detalhes desnecessários

#Fazendeiro e o rio -> Homem, Lobo, Bode, Repolho (H, L, B, R); 0 (lado a), 1 (lado b)
# {H0, L0, B0, R0}
# H, B [0 -> 1]; H [1 -> 0]; H, R [0 -> 1]; H, B [1 -> 0]; H, L [0 -> 1]; H [1 -> 0]; H, B [0 -> 1]
# {H1, L1, B1, R1}

#Linguagem de programação: Conjunto de símbolos e regras de sintaxe, que permitem a construção
#de instruções que descrevem, de forma não ambígua, ações que podem ser entendidas e executadas
#por computadores.

#Computador simplificado
A, B, C, X, Y, Z = [0,0,0,0,0,0]
A = int(input())
C = int(input())
Z = A + C
print(f'Tela computador: {Z}')
diario = Z / 2
print(f'Diário: {diario}')
