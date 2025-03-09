# O usuário informa o código do pacote, a cidade de destino e o peso. O código do pacote não pode se repetir
def adicionar_pacote(pacotes):
    codigo = input("Informe o Código do Pacote: ")
    if codigo in pacotes:
        print("Código Inválido, já existente")
        return
    cidade_destino = input("Informe a Cidade de Destino do Pacote: ")
    peso = float(input("Informe o peso do pacote (kg): "))
    pacotes[codigo] = (cidade_destino, peso)
    print("Pacote adicionado com sucesso")
    
# O usuário informa o código do pacote e ele deve ser removido da lista de entregas.
def remover_pacote(pacotes):
    codigo = input("Informe o Código do Pacote a ser Removido: ")
    if codigo in pacotes:
        del pacotes[codigo]
        print("Pacote de ID " + codigo + " Removido")
    else:
        print("Pacote não encontrado pelo Código.")
    
    
# Exibir uma lista dos três pacotes com maior peso.
def exibir_tres_pesados(pacotes):
    if len(pacotes) == 0:
        print("Lista de Pacotes vazia.")
        return
    else:
        pacotes_ordenados = sorted(pacotes.items(), key=lambda x: x[1][1], reverse=True)[:3]
    print("Três pacotes mais pesados: ")
    for codigo, (cidade, peso) in pacotes_ordenados:
        print(f"Código: {codigo}, Cidade: {cidade}, Peso: {peso} kg")

        
# O usuário informa a cidade, e o programa retorna a média do peso dos pacotes enviados para essa cidade. 
def peso_medio(pacotes):
    cidade = input("Digite o nome da cidade: ")
    pesos = [peso for c, peso in pacotes.values() if c == cidade]
    if len(pesos) == 0:
        print("Nenhum pacote encontrado para essa cidade.")
    else:
        print(f"Peso médio dos pacotes para {cidade}: {sum(pesos) / len(pesos):.2f} kg")
    

#  Exibir as cidades que mais recebem pacotes ordenadas pela quantidade.
def cidades_mais_pacotes(pacotes):
    from collections import Counter
    if len(pacotes) == 0:
        print("Nenhum pacote cadastrado.")
        return
    contagem = Counter(cidade for cidade, _ in pacotes.values())
    cidades_ordenadas = contagem.most_common(3)
    print("Três cidades que mais recebem pacotes:")
    for cidade, quantidade in cidades_ordenadas:
        print(f"Cidade: {cidade}, Quantidade: {quantidade}")
    
# Função do Menu
def menu():
    print("\nMenu de Opções:")
    print("1. Adicionar um novo pacote")
    print("2. Remover um pacote")
    print("3. Exibir os três pacotes mais pesados")
    print("4. Calcular o peso médio dos pacotes para uma cidade")
    print("5. Listar as três cidades com maior número de pacotes")
    print("6. Sair")
    
# Função main
def main():
    pacotes = {}
    while True:
        menu()
        opcao = input("Escolha uma opção: ")
        if opcao == "1":
            adicionar_pacote(pacotes)
        elif opcao == "2":
            remover_pacote(pacotes)
        elif opcao == "3":
            exibir_tres_pesados(pacotes)
        elif opcao == "4":
            peso_medio(pacotes)
        elif opcao == "5":
            cidades_mais_pacotes(pacotes)
        elif opcao == "6":
            print("Sair")
            break
        else:
            print("Opção inválida")
    
    
# chamada da função Main
if __name__ == "__main__":
    main()