# Lista Mágica do Usuário - Gerenciador Interativo 🧙‍♂️✨

def mostrar_menu():
    print("\n✨ MENU DE OPERAÇÕES ✨")
    print("1. Adicionar item")
    print("2. Inserir item em posição")
    print("3. Adicionar vários itens")
    print("4. Remover item")
    print("5. Remover por posição")
    print("6. Limpar lista")
    print("7. Ver posição de um item")
    print("8. Contar item")
    print("9. Ordenar lista")
    print("10. Inverter lista")
    print("11. Mostrar lista")
    print("0. Sair")


# Lista principal do usuário
lista_magica = []

print("🪄 Bem-vindo à sua Lista Mágica de Tarefas! 🪄")

while True:
    mostrar_menu()
    escolha = input("Escolha uma opção: ")

    if escolha == '1':
        item = input("Digite o item a adicionar: ")
        lista_magica.append(item)
        print(f"'{item}' foi adicionado à lista.")

    elif escolha == '2':
        item = input("Digite o item a inserir: ")
        try:
            posicao = int(input("Digite a posição onde inserir: "))
            lista_magica.insert(posicao, item)
            print(f"'{item}' foi inserido na posição {posicao}.")
        except ValueError:
            print("❌ Posição inválida. Tente novamente.")

    elif escolha == '3':
        novos_itens = input("Digite os itens separados por vírgula: ").split(',')
        novos_itens = [item.strip() for item in novos_itens]
        lista_magica.extend(novos_itens)
        print(f"Itens {novos_itens} foram adicionados à lista.")

    elif escolha == '4':
        item = input("Digite o item a remover: ")
        if item in lista_magica:
            lista_magica.remove(item)
            print(f"'{item}' foi removido da lista.")
        else:
            print("❌ Item não encontrado na lista.")

    elif escolha == '5':
        try:
            indice = int(input("Digite a posição do item a remover: "))
            removido = lista_magica.pop(indice)
            print(f"'{removido}' foi removido da posição {indice}.")
        except (IndexError, ValueError):
            print("❌ Posição inválida.")

    elif escolha == '6':
        lista_magica.clear()
        print("✨ Lista esvaziada com sucesso!")

    elif escolha == '7':
        item = input("Digite o item para buscar a posição: ")
        if item in lista_magica:
            pos = lista_magica.index(item)
            print(f"O item '{item}' está na posição {pos}.")
        else:
            print("❌ Item não encontrado.")

    elif escolha == '8':
        item = input("Digite o item para contar: ")
        contagem = lista_magica.count(item)
        print(f"O item '{item}' aparece {contagem} vez(es) na lista.")

    elif escolha == '9':
        lista_magica.sort()
        print("📚 Lista ordenada em ordem alfabética.")

    elif escolha == '10':
        lista_magica.reverse()
        print("🔁 Lista invertida com sucesso.")

    elif escolha == '11':
        print("📋 Sua Lista Mágica:")
        if lista_magica:
            for i, item in enumerate(lista_magica):
                print(f"{i}. {item}")
        else:
            print("A lista está vazia.")

    elif escolha == '0':
        print("👋 Até logo! Sua lista mágica foi encerrada.")
        break

    else:
        print("❌ Opção inválida. Tente novamente.")
