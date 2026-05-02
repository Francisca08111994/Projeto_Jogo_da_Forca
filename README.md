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

# Condições de Vitória/ Derrota
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


## Requisitos do Sistema

### Requisitos Funcionais (o que o sistema faz)

1. O sistema deve selecionar aleatoriamente uma palavra secreta a partir de uma lista predefinida.
2. O sistema deve apresentar a palavra sob a forma de traços (`_`), ocultando as letras.
3. O sistema deve permitir ao jogador inserir uma letra por tentativa.
4. O sistema deve verificar se a letra inserida pertence à palavra secreta.
5. O sistema deve atualizar o estado do jogo após cada jogada.
6. O sistema deve identificar automaticamente o fim do jogo (vitória ou derrota).

### Requisitos Não Funcionais (como o sistema deve ser) 

1. O jogo deve ser simples e intuitivo.
2. O sistema deve responder rapidamente às ações do jogador.
3. O sistema deve validar a entrada. O sistema deve ignorar caracteres especiais ou números, aceitando apenas letras do alfabeto sem interromper a execução.





