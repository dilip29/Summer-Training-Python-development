class car:
    def __init__(self,a=40):
        self.set_speed=a

    def get_speed(self):
        return self._speed

    def set_speed(self,a):
        if a>=0  and a <=160:
            self._speed=a
        else:
            print("speed not in range")
        return
    
    speed=property(get_speed,set_speed)
    
