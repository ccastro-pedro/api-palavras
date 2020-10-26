# REST API para Vetor de Palavras

Repositório com os arquivos para o desafio da Cinnecta

Foi utilizada uma classe chamada Words para encapsular a lógica do problema. O atributo Words.content contêm todas as informações de saída da classe. Ele é um dicionário disposto da seguinte forma:

Words.content = {'nome do arquivo 1': {'texto':[], 'Vetor N únicos': [], 'Vetor N TwoGram': []},
                'nome do arquivo 2': {'texto':[], 'Vetor N únicos': [], 'Vetor N TwoGram': []}, ...,
                'nome do arquivo N': {'texto':[], 'Vetor N únicos': [], 'Vetor N TwoGram': []},
                'Vocabulario Único': [],
                'Vocabulario TwoGram': []}
                
 Para executar o programa, deve-se, primeiramente, instalar todas as bibliotecas necessárias. Isto é feito executando o comando 'pip install -r requirements.txt'. Então, pode-se inicializar o servidor do REST API. Isto é feito rodando o script 'server.py'. Então, basta executar o código 'main.py' e seguir as instruções que aparecem no terminal. 
 
