import requests
import os

if __name__ == '__main__':
    BASE = 'http://127.0.0.1:5000/'
    while True:
        #default_path = input('Digite o valor do diretório default: ')
        print('\n\n')
        print('Escolha uma opção: \n1) Enviar arquivo(s) \n2) Vocabulário formado pelas palavras isoladas'
              '\n3) Vocabulário formado pelos grupos de 2 palavras \n4) Os N vetores de palavras, '
              'considerando o vocabulário de palavras únicas'
              '\n5) Os N vetores de palavras, '
              'considerando o vocabulário do grupo de palavras \n6) Sair ')
        print("------------------------------------------")
        userInput = input('Digite a opção escolhida: ')
        try:
            resp = int(userInput or 6)
            if resp == 1:
                default_path = os.getcwd()

                print("------------------------------------------")
                path = str(input(
                    'Diretório onde se encontram o(s) arquivo(s) (ou aperte ENTER para o valor default): ') or default_path)
                print("------------------------------------------")
                print(f"Diretório escolhido: {path}")
                print("------------------------------------------")
                files = []
                print("Digite o nome dos arquivos (digite q + enter para sair)")
                print("------------------------------------------")
                while True:
                    r = str(input('Digite o nome do(s) arquivo(s):') or 'q')
                    print("------------------------------------------")
                    if r == 'q':
                        break
                    else:
                        files.append(r)
                print("Todos arquivos escolhidos: \n")
                for i in range(len(files)):
                    print(f"Arquivo {i + 1}: {files[i]}")

                print("\nEnviando os arquivos para o banco de dados...\n")
                for name in files:
                    file = os.path.join(path, name.split('.')[0])
                    if len(name.split('.')) > 1:
                        if name.split('.')[1] != 'txt':
                            print(f'O arquivo {name} não está no formato adequado!\n'
                                  f'Por favor, envie um arquivo .txt')
                        else:
                            r = requests.put(f'{BASE}/UploadFile/{file}')
                    else:
                        print(f'{file}.txt')
                        r = requests.put(f'{BASE}/UploadFile/{file}.txt')
            elif resp == 2:
                r = requests.get(BASE + 'UniqueVocab')
                r = r.json()
                print(f"O vocabulário completo formado pelas palavras isoladas: \n{r}")
            elif resp == 3:
                r = requests.get(BASE + 'TwoGramVocab')
                r = r.json()
                print(f"O vocabulário completo formado pelo conjunto de duas palavras (TWO-GRAM): \n{r}")
            elif resp == 4:
                r = requests.get(BASE + 'NumberUnique')
                r = r.json()
                print(f"Os N vetores de palavras de todos os documentos, "
                      f"considerando o vocabulário formado pelas palavras isoladas: \n{r}")
            elif resp == 5:
                r = requests.get(BASE + 'NumberTwoGram')
                r = r.json()
                print(f"Os N vetores de palavras de todos os documentos, "
                      f"considerando o vocabulário formado por grupos de 2 palavras em sequência (2-gram): \n{r}")
            elif resp == 6:
                break
        except ValueError:
            print(f"'{userInput}' não é um comando válido!")
