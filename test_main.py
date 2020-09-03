import pytest
from main import arquivoString

NOME_ARQ = 'sarscov2.fasta'

class Test_arquivoString:
    def test_sem_excecao(self):
        arquivoString(NOME_ARQ)
    def test_tipo_retorno(self):
        string = arquivoString(NOME_ARQ)
        assert type(string) == str
    def test_sem_espacos(self):
        string = arquivoString(NOME_ARQ)
        for i in range(len(string)):
            assert string[i].isspace() == False, f"erro na posição {i}"
    def test_sem_cabecalho(self):
        string = arquivoString(NOME_ARQ)
        for i in range(len(string)):
            assert string[i].isupper() == True, f"erro na posição {i}"


