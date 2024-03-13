class Robot:
    name: str
    state: str

    def __init__(self, nome):
        self.name = nome
        self.state = "inactive"

    def activate(self):
        self.state = "active"

    def deactivate(self):
        self.state = "inactive"

    def is_active(self):
        return self.state


class SuperRobot(Robot):
    speed: int

    def __init__(self, nome, speed):
        super().__init__(nome)
        self.speed = speed

    def increase_speed(self, quantity):
        self.speed += quantity


def main():
    # Instanciar um objeto da classe Robot
    r2d2 = Robot("R2D2")

    # Ativar o robô e verificar se está ativo
    r2d2.activate()
    print("Robô está ativo:", r2d2.is_active())

    # Desativar o robô e verificar o estado novamente
    r2d2.deactivate()
    print("Robô está ativo:", r2d2.is_active())
    superrobot = SuperRobot("S3P0", 100)


if __name__ == "__main__":
    main()
