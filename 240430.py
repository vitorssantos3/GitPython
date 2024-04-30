# l = list("asbhbciabcihbihcbnamkmmib")
# letra = "c"
# for i,char in enumerate(l):
#     if char == letra:
#         print(f"Letra {letra} está na posição {indice}")
#         break
#     else:
#         print("Não encontrado")

def index (l, letra):
    for i, char in enumerate(l):
        if char ==letra:
            print(f"Letra{letra} está na posição {i}")
            return i
    return None
l = list("knmdndnsnnn")
letra=input("digite uma letra:")
index(l,letra)