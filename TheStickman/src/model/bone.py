from joint import Joint
import math
class Bone:
    """
    מייצגת עצם בסטיקמן. כל עצם מחוברת למפרק אחד ויוצאת ממנו בזווית מסוימת ובאורך קבוע.

    Attributes:
        name (str): שם העצם (לוגי בלבד, לצורכי זיהוי).
        parent_joint (Joint): המפרק שממנו העצם מתחילה.
        length (float): האורך של העצם בפיקסלים.
        angle (float): הזווית הנוכחית של העצם במעלות.
        child_joint:המפרק שבו העצם מסתיימת.
    """

    def __init__(self, name, parent_joint, length, angle):
        self.name = name
        self.parent_joint = parent_joint
        self.length = length
        self.angle = angle
        self.child_joint = None   # נוסיף בהמשך

    #יחזיר לך את נקודת הציר ההתחלתית של
    # החלק העליון או התחתון של היד או הרגל 
    #החלק שקרוב יותר למרכז הגוף
    def get_bone_start(self):
        return(self.parent_joint)
    
    #יחזיר את הנקודה הסופית של החלק המסויים באיבר
    def get_bone_end(self):
        return(self.child_joint)
    
    #כמו הפונקצייה הקודמת אבל רק עם חישוב לפי אורך עצם וזווית בראדיאנים
    def get_end_joint(self):
        x0, y0 = self.get_start()
        # חישוב פשוט: נקודת הקצה לפי אורך וזווית
        rad = math.radians(self.angle) #המרת זווית לראדיאנים
        x_end = x0 + math.cos(rad) * self.length
        y_end = y0 + math.sin(rad) * self.length
        return Joint(f"{self.name}_end", x_end, y_end, self.angle)