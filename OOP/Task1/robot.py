class robotStatus:
    ALIVE = 0
    DEAD  = 1
    CRASH = 2
    WATER = 3

BATTERY_VAL = 10
class robot:
    # mapa, x, y, bateria
    def __init__(self, T, x, y, b):
<<<<<<< HEAD
        self.__T = T
        self.__x = x
        self.__y = y
        self.__b = b
=======
        pass
>>>>>>> cdf8f8f56e712959e4661374914589e6e166f510

    def left(self, val = 1):
        pass
    def right(self, val = 1):
        pass
    def up(self, val = 1):
        pass
    def down(self, val = 1):
        pass

    def get_status(self):
<<<<<<< HEAD
        if self.get_battery() == 0:
            return robotStatus.DEAD

        T = self.__T
        x = self.get_x()
        y = self.get_y()

        if T[x][y] == "T":
            return robotStatus.ALIVE
        elif T[x][y] == "W":
            return robotStatus.WATER
        else:
            return robotStatus.CRASH






    def get_battery(self):
        return self.__b

    def get_map(self):
        pass

    def get_x(self):
        return self.__x
        
    def get_y(self):
        return self.__y
=======
        pass
    def get_battery(self):
        pass
    def get_map(self):
        pass
    def get_x(self):
        pass
    def get_y(self):
        pass
>>>>>>> cdf8f8f56e712959e4661374914589e6e166f510
