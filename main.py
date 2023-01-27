class Plateau():
    def __init__(self, top_x, top_y):
        self.top_x = top_x
        self.top_y = top_y
        self.bottom_x = 0
        self.bottom_y = 0

class MarsRover():
    def __init__(self, plateau, x, y, heading):
        self.x_top = plateau.top_x
        self.y_top = plateau.top_y
        self.x = x
        self.y = y
        self.heading = heading

        # possible letters: L, R, M
        # L, R are turns (no moving a spot)
        # M means move forward and maintain the same heading
        self.command = {
            "Left": "L",
            "Right": "R",
            "Move": "M"
        }

        self.left_rotate = {
            "N": "W",
            "E": "N",
            "W": "S",
            "S": "E"
        }

        self.right_rotate = {
            "N": "E",
            "E": "S",
            "W": "N",
            "S": "W"
        }

    def __left_turn(self):
        ### turns left in a 90 degree angle
        self.heading = self.left_rotate[self.heading]

    def __move(self):
        ### moves rover by 1 grid
        match self.heading:
            case "N":
                if (self.y + 1) <= self.y_top: self.y += 1
            case "E":
                if (self.x + 1) <= self.x_top: self.x += 1
            case "W":
                if (self.x - 1) >= 0: self.x -= 1 
            case "S":
                if (self.y - 1) >= 0: self.y -= 1
    
    def __right_turn(self):
        ### turns right in a 90 degree angle
        self.heading = self.right_rotate[self.heading]
    
    def execute(self, command):
        if command == self.command["Left"]:
            self.__left_turn()
        elif command == self.command["Right"]:
            self.__right_turn()
        elif command == self.command["Move"]:
            self.__move()
        else:
            raise ValueError("Incorrect Command")
    
    def __str__(self):
        return "{} {} {}".format(self.x, self.y, self.heading)

def main():
    plateau = Plateau(5, 5)
    mars_rover = MarsRover(plateau, 3, 3, "E")

    while True:
        command = input("Enter a command: ")

        if command == "": break

        mars_rover.execute(command)
        print(mars_rover)

main()