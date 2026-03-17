def calcular_media(notas):
    soma = sum(notas)
    quantidade = len(notas)
    return soma / quantidade

notas = (8,9,10,7)
media = calcular_media(notas)
print(f"Media: {media: .2f}")