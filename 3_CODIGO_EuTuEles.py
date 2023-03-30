lição = input("Vamos tomar sorvete? Mas, para isso preciso saber se você fez a lição de casa?").lower()

if lição == "sim":
    banho = input("Você deu banho no sniff?").lower()
    if banho == "sim":
        print("Legal! Vamos à sorveteria!")
    else:
        print("Que pena! Não vamos à sorveteria.")
else:
    print("Que pena! Não vamos à sorveteria.")


