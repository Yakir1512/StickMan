class Joint:
    def __init__(self, name, x=0, y=0, angle=0):
        self.name = name
        self.x = x
        self.y = y
        self.angle = angle

    # הגדרת זווית חדשה
    def set_angle(self, new_angle):
        self.angle = new_angle