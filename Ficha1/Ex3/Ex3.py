class Robot:
    name: str
    state: str

    def __init__(self, nome):
        name = nome
        state = "inactive"

    def activate(self):
        state = "active"

    def deactivate(self):
        state = "inactive"

    def is_active(self):
        return self.state == "active"


# Instanciar um objeto da classe Robot
r2d2 = Robot("R2D2")

# Ativar o robô e verificar se está ativo
r2d2.activate()
print("Robô está ativo:", r2d2.is_active())

# Desativar o robô e verificar o estado novamente
r2d2.deactivate()
print("Robô está ativo:", r2d2.is_active())


class SuperRobot(Robot):
    speed: int

    def increase_speed(self, quantity):
        self.speed += quantity
