L = [5,7,2,9,4,1,3]
print("Tamanho da lista:",len(L))
print("Menor número da lista:",min(L))
print("Maior número da lista:",max(L))
L.sort()
print("Soma da lista",sum(L))
print("Lista em ordem crescente: ", L)
L.sort(reverse= True)
print("Lista em ordem decrescente:", L)