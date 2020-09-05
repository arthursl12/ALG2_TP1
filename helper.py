def checkPrefixSubstring(string, sub):
    """
    Retorna o tamanho do maior prefixo de string que é prefixo de sub
    """
    n = min([len(string),len(sub)])
    if n == 0: 
        # Alguma string vazia
        return 0
    for i in range(n):
        if string[i] != sub[i]:
            return i
    return n