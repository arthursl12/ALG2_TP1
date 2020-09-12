from trie import CompactTrie
from memory_profiler import profile

NOME_ARQ = 'sarscov2.fasta'

@profile
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

@profile
def main():
    string = arquivoString(NOME_ARQ)
    trie = criaArvoreSufixos(string)
    qtd, strMaior = trie.maiorSubstring()
    f = open('maior.txt','w')
    f.write(str(qtd) + '\n' + strMaior)
    f.close()

if __name__=='__main__':
    main()