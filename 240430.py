# l = list("asbhbciabcihbihcbnamkmmib")
# letra = "c"
# for i,char in enumerate(l):
#     if char == letra:
#         print(f"Letra {letra} está na posição {indice}")
#         break
#     else:
#         print("Não encontrado")

# ________ ATENÇÃO:    ipython ________ comando para o terminal
def index (l, letra):
    for i, char in enumerate(l):
        if char ==letra:
            print(f"Letra{letra} está na posição {i}")
            return i
    return None
l = list("knmdndnsnnn")
letra=input("digite uma letra:")
index(l,letra)

def encontra_max(lista):
    if len(lista)==0:
        return None
    maior_numero = lista[0]
    # maior_numero = None
    for i in lista:
        if i > maior_numero:
        # if maior_numero is None or i >maior_numero:
            maior_numero=i
    return maior_numero

def encontra_min(lista):
    menor_numero= lista[0]
    for i in lista:
        if i<menor_numero:
            menor_numero =i
    return menor_numero

def ordem_crescente(lista):
    lista_ordenada =[]
    while len(lista):
        i = index(encontra_min(lista))
        lista_ordenada.append(lista.pop(i))
    return lista_ordenada

def ordena__decrescente(lista):
    return ordem_crescente(lista)[::-1]

def ordena(lista,decrescnte =False):
    if decrescnte:
        return ordena__decrescente(lista)
    return ordena__decrescente(lista)