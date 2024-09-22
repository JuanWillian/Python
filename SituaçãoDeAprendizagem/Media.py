vet = [int(input("Número:")) for i in range(20)]
media =0
for i in range(20):
    media +=vet[i]
media = media/len(vet)
print("Maior número:", max(vet), "Menor número:", min(vet),"Média:",media)

