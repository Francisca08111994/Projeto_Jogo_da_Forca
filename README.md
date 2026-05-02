# Projeto_Jogo_da_Forca
O jogo da forca consiste em adivinhar uma palavra escondida através da indicação das suas letras, uma de cada vez. 

# Objetivo 
O objetivo do jogo da forca é adivinhar uma palavra secreta, indicando letras, antes que o número máximo de tentativas seja atingido (antes do boneco na forca seja comletado).

# Regras Principais
- O jogo escolhe aleatoriamente uma palavra secreta.
- A palavra é apresentada ao jogador com traços (ex: _ _ _ _) representando cada letra.
- O jogador tenta adivinhar a palavra indicando uma letra de cada vez.
- Se a letra existir na palavra:
  - Ela é revelada em todas as posições corretas.
- Se a letra não existir:
  - O jogador perde uma tentativa.
- Letras já tentadas não devem contar novamente.

# Condoções de Vitória/ Derrota
- Vitória
  - O jogador ganha quando consegue descobrir todas as letras da palavra antes de esgotar as tentativas.
- Derrota
  - O jogador perde quando atinge o número máximo de tentativas erradas.
 
# Limitações do jogo
- Número de tentativas:
  - 6 tentativas erradas (cabeça, tronco, dois braços e duas pernas)
- Tipo de input:
  - Apenas uma letra por jogada
  - Não são aceites números nem símbolos
  - Ignorar maiúsculas/minúsculas
- Palavras:
  - Lista de palavras predefinida e com um tema
- Repetições:
  - Letras já usadas não devem penalizar novamente

