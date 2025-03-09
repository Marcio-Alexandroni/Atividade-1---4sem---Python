# O paciente é inserido no final da lista.
def adicionar_paciente(fila):
    nome = input("Nome do paciente: ")
    prioridade = input("Prioridade (E - Emergência, U - Urgência, N - Normal): ").upper()
    if prioridade not in {'E', 'U', 'N'}:
        print("Prioridade inválida. Use E, U ou N.")
        return
    fila.append((nome, prioridade))
    print("Paciente adicionado com sucesso!")

# O usuário informa o nome do paciente e ele é removido da lista.
def remover_paciente(fila):
    nome = input("Nome do paciente a ser removido: ")
    for paciente in fila:
        if paciente[0] == nome:
            fila.remove(paciente)
            print("Paciente removido com sucesso!")
            return
    print("Paciente não encontrado.")

# Função para ordenar a fila de pacientes com base nas prioridades
def ordenar_fila(fila):
    prioridades = {'E': 1, 'U': 2, 'N': 3}
    return sorted(fila, key=lambda x: prioridades[x[1]])

# O programa deve exibir os três primeiros pacientes da lista, priorizando primeiro Emergência (E), depois Urgência (U) e, por último, Normal (N). Use slices para extrair os três primeiros pacientes ordenados corretamente.
def chamar_proximos_pacientes(fila):
    if not fila:
        print("Nenhum paciente na fila.")
        return
    fila_ordenada = ordenar_fila(fila)
    print("Próximos 3 pacientes para atendimento: ")
    for paciente in fila_ordenada[:3]:
        print(f"Nome: {paciente[0]}, Prioridade: {paciente[1]}")

# O usuário informa um número N, e o programa deve exibir os N primeiros pacientes na ordem de prioridade correta.
def exibir_proximos_n_pacientes(fila):
    if not fila:
        print("Nenhum paciente na fila.")
        return
    try:
        n = int(input("Quantos pacientes deseja exibir? "))
        if n <= 0:
            print("Número inválido.")
            return
    except ValueError:
        print("Erro. Digite um número inteiro.")
        return
    fila_ordenada = ordenar_fila(fila)
    print(f"Próximos {n} pacientes para atendimento:")
    for paciente in fila_ordenada[:n]:
        print(f"Nome: {paciente[0]}, Prioridade: {paciente[1]}")

# Função para o Menu
def menu():
    print("\nMenu de Opções:")
    print("1. Adicionar um paciente")
    print("2. Remover um paciente")
    print("3. Chamar os 3 próximos pacientes")
    print("4. Exibir os próximos N pacientes")
    print("5. Sair")

# Função Main
def main():
    fila = []
    while True:
        menu()
        opcao = input("Escolha uma opção: ")
        if opcao == "1":
            adicionar_paciente(fila)
        elif opcao == "2":
            remover_paciente(fila)
        elif opcao == "3":
            chamar_proximos_pacientes(fila)
        elif opcao == "4":
            exibir_proximos_n_pacientes(fila)
        elif opcao == "5":
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")

# Chamada da Função Main
if __name__ == "__main__":
    main()
