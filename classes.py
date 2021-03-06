"""
Classe utilizada para realização do problema

Words.content = {'nome do arquivo 1': {'texto':[], 'Vetor N únicos': [], 'Vetor N TwoGram': []},
                'nome do arquivo 2': {'texto':[], 'Vetor N únicos': [], 'Vetor N TwoGram': []}, ...,
                'nome do arquivo N': {'texto':[], 'Vetor N únicos': [], 'Vetor N TwoGram': []},
                'Vocabulario Único': [],
                'Vocabulario TwoGram': []}
"""
import re
import os

STOP_WORDS = ['o', 'a', 'que', 'me', 'na', 'em', 'no', 'para', 'de', 'da', 'do', 'das', 'dos', 'nas', 'nos']


def add_element(d, key, value):
    if key not in d:
        d[key] = []
    d[key].append(value)


class Words:
    """
    Classe Words com todos os atributos e métodos para o desafio do vetor de palavras. Toda a lógica para resolução
    do problema está encapsulado dentro desta classe
    """
    def __init__(self):
        """
        Construtor de um objeto da classe Words
        """
        self.__files = []
        self.__content = {}

    def add_files(self, *args):
        """
        Método para se adicionar arquivos ao objeto

        Caso seja inserido algum arquivo novo, o método __run() será executado.


        :param args: arquivos (path + filename)
        :return:
        """
        new_files = False
        for file in args:
            if file not in self.__files:
                self.__files.append(file)
                new_files = True
        if new_files:
            self.__run()

    def __get_text(self):
        """
        Método para ler o texto dos arquivos

        Separa todas as pontuações e aplica .lower() em todas as strings

        :return:
        """
        for file in self.__files:
            with open(file, 'r', encoding="utf8") as f:
                name = os.path.basename(f.name)
                text = f.read()
            text = re.findall(r"[\w']+", text)  # (?<![0-9])
            text = [i.lower() for i in text]
            text_sem_stop_words = [word for word in text if word not in STOP_WORDS]
            self.__content[name] = {'texto': text_sem_stop_words}

    def __unique_words(self):
        """
        Obter a lista de palavras únicas presentes nos textos


        :return:
        """
        # A ordem é importante? Caso não fosse, seria interessante usar unique = set() e entao unique.update(text)
        #self.__get_text()
        all_words = [item for sublist in [self.__content[key]['texto'] for key in self.__content
                                          if key != 'unique' and key != 'two_gram'] for item in sublist]
        self.__content['unique'] = []
        for i in all_words:
            if i not in self.__content['unique']:
                self.__content['unique'].append(i)

    def __two_gram(self):
        """
        Obter o vocabulário composto de grupos de duas palavras em sequência (2-gram).

        :return:
        """
        texto = [self.__content[key]['texto'] for key in self.__content
                                          if key != 'unique' and key != 'two_gram']
        two_gram = []
        for txt in texto:
            two_gram.append([txt[i:i + 2] for i in range(len(txt) - 2 + 1)])
        flat_two_gram = [item for sublist in two_gram for item in sublist]
        self.__content['two_gram'] = []
        for i in flat_two_gram:
            exp = ' '.join(i)
            if exp not in self.__content['two_gram']:
                self.__content['two_gram'].append(exp)

    def __count_unique(self):
        """
        Contar o número de vezes que uma palavra aparece em um texto, com base no vocabulário de
        palavras únicas
        :return:
        """
        for name in self.__content:
            if name != 'unique' and name != 'two_gram':
                add_element(self.__content[name], 'num_unique',
                            [self.__content[name]['texto'].count(word) for word in self.__content['unique']])

    def __count_two_gram(self):
        """
        Contar o número de vezes que uma palavra aparece em um texto, com base no vocabulário de
        grupo de duas palavras
        :return:
        """
        for name in self.__content:
            if name != 'unique' and name != 'two_gram':
                texto = [self.__content[name]['texto']]
                two_gram = []
                for txt in texto:
                    two_gram.append([txt[i:i + 2] for i in range(len(txt) - 2 + 1)])
                flat_two_gram = [item for sublist in two_gram for item in sublist]
                text_gram = []
                for i in flat_two_gram:
                    text_gram.append(' '.join(i))
                add_element(self.__content[name], 'num_two_gram',
                            [text_gram.count(word) for word in self.__content['two_gram']])

    def __run(self):
        """
        Executar os métodos privados da classe Words
        :return:
        """
        if self.files:
            self.__get_text()
            self.__unique_words()
            self.__two_gram()
            self.__count_unique()
            self.__count_two_gram()

    @property
    def content(self):
        """
        :return: atributo content da classe Words
        """
        return self.__content

    @property
    def files(self):
        """
        :return: atributo files da classe Words
        """
        return self.__files

    @property
    def unique_vocab(self):
        """
        :return: vocabulário das palavras únicas de todos os textos
        """
        return self.__content['unique']

    @property
    def two_gram_vocab(self):
        """
        :return: vocabulário dos grupos de 2 palavras de todos os textos
        """
        return self.__content['two_gram']

    @property
    def num_unique(self):
        """
        :return: retorna um vetor, para cada texto, com o número de repetições de cada palavra comparando ao
        vocabulário de palavras únicas
        """
        output = {}
        for name in self.__content:
            if name != 'unique' and name != 'two_gram':
                num_unique = self.__content[name]['num_unique']
                output[name] = num_unique
        return output

    @property
    def num_two_gram(self):
        """
        :return: retorna um vetor, para cada texto, com o número de repetições de cada grupo de 2 palavras comparando ao
        vocabulário two gram
        """
        output = {}
        for name in self.__content:
            if name != 'unique' and name != 'two_gram':
                num_two_gram = self.__content[name]['num_two_gram']
                output[name] = num_two_gram
        return output
