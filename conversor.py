
def converte(simbolo):
    acumuladora=0
    dicionario={'I': 1, 'II':2, 'V':5, 'IX':9, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
    for x in simbolo:
        acumuladora +=dicionario.get(x)
    return acumuladora
   
