# Definir a lista de tuplos para armazenar informações de voos
flights = [
    ('TP100', 'Lisboa', 'Paris', '10:00'),
    ('TP200', 'Porto', 'Madrid', '12:00'),
    ('TP300', 'Faro', 'Londres', '14:00')
]

# Definir o método para adicionar um novo voo à lista
def add_flight(number, origin, destination, departure_time):
    flights.append((number, origin, destination, departure_time))


# Definir o método para pesquisar informações sobre um voo
def search_flight(number):
    for flight in flights:
        if number == flight[0]:
            print(flight[0])
            print(flight[1])
            print(flight[2])
            print(flight[3])
    print('No flights found')



def main():
    # Pedir ao utilizador para adicionar novos voos ou pesquisar informações sobre voos existentes
    while True:
        print("Escolha uma opção:")
        print("1 - Adicionar novo voo")
        print("2 - Pesquisar informações sobre um voo")
        print("3 - Sair")

        # Ler a opção escolhida pelo utilizador
        choice = input()

        # Adicionar um novo voo
        if choice == "1":
            # Pedir ao utilizador para introduzir as informações do novo voo
            number = input("Introduza o número do voo: ")
            origin = input("Introduza a origem do voo: ")
            destination = input("Introduza o destino do voo: ")
            departure_time = input("Introduza a hora de partida do voo: ")
            add_flight(number, origin, destination, departure_time)
        # Pesquisar informações sobre um voo existente
        elif choice == "2":
            # Pedir ao utilizador para introduzir o número do voo a ser pesquisado
            number = input("Introduza o número do voo: ")
            search_flight(number)

        # Sair do programa
        elif choice == "3":
            break

        # Opção inválida
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()