# Conciliador Bancário Sodexo

## **30/01/2025**

# **VISÃO GERAL**

O Conciliador Bancário Sodexo tem como objetivo desenvolver uma solução para a conciliação bancária da operadora Sodexo/Pluxee. Atualmente, não conseguimos realizar a conciliação automática devido à imprevisibilidade dos depósitos da operadora. Criamos um molde para o desenvolvimento de uma solução que possa auxiliar. A proposta é utilizar análise combinatória para conciliar extratos bancários e os valores pagos (créditos).

# **OBJETIVOS**

1. Automatizar o processo da conciliação bancária da Sodexo (não funcional até o momento)

# **ESPECIFICAÇÕES**

Tecnologias Utilizadas:

* Linguagem de Programação: Python  
* Bibliotecas:  
  * `pandas`: Para manipulação e análise de dados.  
  * `numpy`: Para operações matemáticas e manipulação de arrays.  
  * `time`: Para monitoramento do tempo de execução.  
* Código disponível neste [link](https://github.com/matheussilvano/analise-combinatoria-conciliacao-terceiro-nivel/tree/main)

O código explora conceitos centrais da análise combinatória, especificamente no uso de programação dinâmica para resolver o problema de soma de subconjuntos (também conhecido como problema do "knapsack" ou "mochila"). Abaixo estão os principais conceitos abordados:

Combinatória de Subconjuntos: O código trata da busca por combinações de elementos que, quando somados, resultam em um valor alvo (o valor de cada depósito). A combinação é feita a partir de um conjunto de valores (os créditos pagos), e a tarefa é encontrar quais valores somados geram exatamente o valor de um depósito.

Programação Dinâmica (Knapsack Problem): A implementação utiliza programação dinâmica, uma técnica combinatória para otimização que resolve problemas quebrando-os em subproblemas menores. O código aplica essa técnica para armazenar e reutilizar os resultados intermediários de somas de subconjuntos de créditos, facilitando a determinação de se uma combinação de créditos pode formar o valor de um depósito. A tabela dp armazena somas possíveis e as combinações que geram essas somas.

[image1]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAnAAAAAHCAYAAACIq3DzAAAAQUlEQVR4Xu3WMQ0AIADAMFziCFGYgx8FLOnRZwo25l4HAICO8QYAAP5m4AAAYgwcAECMgQMAiDFwAAAxBg4AIOYClIUh9UOLBN8AAAAASUVORK5CYII=>
