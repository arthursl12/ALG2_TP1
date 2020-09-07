import numpy as np
from trie import CompactTrie

NOME_ARQ = 'sarscov2.fasta'

def criaArvoreSufixos(string):
    trie = CompactTrie(string)
    for i in range(len(string)):
        trie.insert(i,len(string)-1)
    return trie

def arquivoString(nomeArq):
    with open(nomeArq,'r') as arquivo:
        next(arquivo)     # Ignorar cabeçalho
        string = arquivo.readline()
        for linha in arquivo:
            if string[-1].isspace():
                string = string[:-1]
            string += linha
    return string

def main():
    string = arquivoString(NOME_ARQ)
    trie = criaArvoreSufixos(string)
    print(string[0:800])


if __name__=='__main__':
    main()