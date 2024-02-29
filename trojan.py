import random

class Computer:
    def __init__(self, name):
        self.name = name
        self.infected = False

    def infect(self):
        self.infected = True

    def is_infected(self):
        return self.infected

class Network:
    def __init__(self):
        self.computers = []

    def add_computer(self, computer):
        self.computers.append(computer)

    def spread_worm(self):
        for computer in self.computers:
            if computer.is_infected():
                for other_computer in self.computers:
                    if not other_computer.is_infected() and random.random() < 0.5:
                        other_computer.infect()
                        print(f"Компьютер {other_computer.name} был заражен червем.")
        print("Червь завершил свое распространение.")

if __name__ == "__main__":
    network = Network()

    # Создание компьютеров в сети
    computer1 = Computer("Компьютер 1")
    computer2 = Computer("Компьютер 2")
    computer3 = Computer("Компьютер 3")

    # Заражение одного из компьютеров
    computer1.infect()

    # Добавление компьютеров в сеть
    network.add_computer(computer1)
    network.add_computer(computer2)
    network.add_computer(computer3)

    # Попытка распространения червя по сети
    network.spread_worm()
