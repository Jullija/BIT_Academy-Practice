class robotStatus:
    ALIVE = 0
    DEAD  = 1
    CRASH = 2
    WATER = 3

BATTERY_VAL = 10
class robot:
    # mapa, x, y, bateria
    def __init__(self, T, x, y, b):
        self.__T = T
        self.__x = x
        self.__y = y
        self.__b = b
        self.__s = None #pole na status

    def left(self, val = 1):
        robot_status = self.get_status()
        robot_battery = self.get_battery()

        if val > 0 and robot_status == robotStatus.ALIVE and robot_battery > 0:
            map = self.get_map()
            x = self.get_x()
            y = self.get_y()
            
            iter = 0
            while iter != val:

                while robot_battery > 0 and y - 1 >=0 :
                    y -= 1

                    if map[x][y] == "T":
                        robot_battery -= 1
                    elif map[x][y] == "W":
                        robot_battery -= 1
                        self.set_battery(robot_battery)
                        self.set_y(y)
                        self.set_status(robotStatus.WATER)
                        break
                    elif map[x][y] == "G":
                        robot_battery -= 1
                        self.set_battery(robot_battery)
                        self.set_y(y)
                        self.set_status(robotStatus.CRASH)
                        break
                    else:
                        robot_battery -= 1
                        robot_battery += BATTERY_VAL
                        map[x][y] = "T"
                        self.__T[x][y] = "T"
                    
                    iter += 1
            

                if iter != val: #nie udało się dotrzeć do końca
                    if y - 1 >= 0: #mogłabym zrobić ruch, ale to oznacza, że nie miałam baterii
                        self.set_battery(0)
                        self.set_status(robotStatus.DEAD)
                    else: #wyszłam poza mapę
                        self.set_status(robotStatus.DEAD)

                        


    def right(self, val = 1):
        robot_status = self.get_status()
        robot_battery = self.get_battery()

        if val > 0 and robot_status == robotStatus.ALIVE and robot_battery > 0:
            map = self.get_map()
            x = self.get_x()
            y = self.get_y()
            
            iter = 0
            while iter != val:

                while robot_battery > 0 and y + 1 < len(map[x]):
                    y += 1

                    if map[x][y] == "T":
                        robot_battery -= 1
                    elif map[x][y] == "W":
                        robot_battery -= 1
                        self.set_battery(robot_battery)
                        self.set_y(y)
                        self.set_status(robotStatus.WATER)
                        break
                    elif map[x][y] == "G":
                        robot_battery -= 1
                        self.set_battery(robot_battery)
                        self.set_y(y)
                        self.set_status(robotStatus.CRASH)
                        break
                    else:
                        robot_battery -= 1
                        robot_battery += BATTERY_VAL
                        map[x][y] = "T"
                        self.__T[x][y] = "T"
                    
                    iter += 1
            

                if iter != val: #nie udało się dotrzeć do końca
                    if y + 1 < len(map[x]): #mogłabym zrobić ruch, ale to oznacza, że nie miałam baterii
                        self.set_battery(0)
                        self.set_status(robotStatus.DEAD)
                    else: #wyszłam poza mapę
                        self.set_status(robotStatus.DEAD)


    def up(self, val = 1):
        robot_status = self.get_status()
        robot_battery = self.get_battery()

        if val > 0 and robot_status == robotStatus.ALIVE and robot_battery > 0:
            map = self.get_map()
            x = self.get_x()
            y = self.get_y()
            
            iter = 0
            while iter != val:

                while robot_battery > 0 and x - 1 >=0 :
                    x -= 1

                    if map[x][y] == "T":
                        robot_battery -= 1
                    elif map[x][y] == "W":
                        robot_battery -= 1
                        self.set_battery(robot_battery)
                        self.set_y(y)
                        self.set_status(robotStatus.WATER)
                        break
                    elif map[x][y] == "G":
                        robot_battery -= 1
                        self.set_battery(robot_battery)
                        self.set_y(y)
                        self.set_status(robotStatus.CRASH)
                        break
                    else:
                        robot_battery -= 1
                        robot_battery += BATTERY_VAL
                        map[x][y] = "T"
                        self.__T[x][y] = "T"
                    
                    iter += 1
            

                if iter != val: #nie udało się dotrzeć do końca
                    if x - 1 >= 0: #mogłabym zrobić ruch, ale to oznacza, że nie miałam baterii
                        self.set_battery(0)
                        self.set_status(robotStatus.DEAD)
                    else: #wyszłam poza mapę
                        self.set_status(robotStatus.DEAD)



    def down(self, val = 1):
        robot_status = self.get_status()
        robot_battery = self.get_battery()

        if val > 0 and robot_status == robotStatus.ALIVE and robot_battery > 0:
            map = self.get_map()
            x = self.get_x()
            y = self.get_y()
            
            iter = 0
            while iter != val:

                while robot_battery > 0 and x + 1 <len(map[y]) :
                    x += 1

                    if map[x][y] == "T":
                        robot_battery -= 1
                    elif map[x][y] == "W":
                        robot_battery -= 1
                        self.set_battery(robot_battery)
                        self.set_y(y)
                        self.set_status(robotStatus.WATER)
                        break
                    elif map[x][y] == "G":
                        robot_battery -= 1
                        self.set_battery(robot_battery)
                        self.set_y(y)
                        self.set_status(robotStatus.CRASH)
                        break
                    else:
                        robot_battery -= 1
                        robot_battery += BATTERY_VAL
                        map[x][y] = "T"
                        self.__T[x][y] = "T"
                    
                    iter += 1
            

                if iter != val: #nie udało się dotrzeć do końca
                    if x + 1 < len(map[y]): #mogłabym zrobić ruch, ale to oznacza, że nie miałam baterii
                        self.set_battery(0)
                        self.set_status(robotStatus.DEAD)
                    else: #wyszłam poza mapę
                        self.set_status(robotStatus.DEAD)







    def set_status(self, stat):
        self.__s = stat
    
    def set_battery(self, val):
        self.__b = val

    def set_x(self, val):
        self.__x = val

    def set_y(self, val):
        self.__y = val









    def get_status(self):
        if self.__s == None:
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
        return self.__s



    def get_battery(self):
        return self.__b

    def get_map(self):
        robot_status = self.get_status()
        x = self.get_x()
        y = self.get_y()
        T = self.__T

        if robot_status == robotStatus.ALIVE:
            T[x][y] = "R"
        else:
            T[x][y] = "X"
        return T



    def get_x(self):
        return self.__x
        
    def get_y(self):
        return self.__y
