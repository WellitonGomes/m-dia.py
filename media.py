def obter_nome():
    while True:
        try:
            nome = input("Por favor, informe seu nome: ")
            return nome
        except ValueError:
            print("Por favor, digite apenas seu nome.")

def obter_notas():
    while True:
        try:
            num_notas = int(input("Quantas notas você deseja inserir? "))
            notas = []
            for i in range(num_notas):
                nota = float(input(f"Digite a nota {i+1}: "))
                notas.append(nota)
            return notas
        except ValueError:
            print("Por favor, digite um número inteiro para a quantidade de notas.")
        except Exception as e:
            print(f"Ocorreu um erro: {e}")

def calcularMedia(notas, nome):
    if not notas:
        print("Nenhuma nota foi inserida.")
        return

    soma = sum(notas)
    media = soma / len(notas)
    print(nome, "sua média é:", media)

# Fluxo principal do programa
nome = obter_nome()
notas = obter_notas()
calcularMedia(notas, nome)
