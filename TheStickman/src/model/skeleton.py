from limb import Limb
from bone import Bone
from joint import Joint
from head import Head

class Stickman:
    def __init__(self):

        # מפרק מרכזי של צוואר
        #ומפה תתחיל להצטייר הדמות
        #
        self.core = Joint("core/neck", x=200, y=200)
        #בנייה של הקו המייצג את הבטן
        self.stomach = Bone("stomach",parent_joint = self.core ,length = 60 ,angel =  270 )
        # הראש יכול להיות עצם אחת
        self.head = Head( self.core)

        # איברים
        self.limbs = {
            # הידיים מתחילות מ-self.core
            "right_arm": Limb("right_arm", self.core, 40, 35, angle_upper=300, angle_lower=300),
            "left_arm": Limb("left_arm", self.core, 40, 35, angle_upper=240, angle_lower=240),
            # הרגליים מתחילות מהמפרק הסופי של הבטן
            "right_leg": Limb("right_leg", self.stomach.get_end_joint(), 50, 45, angle_upper=250, angle_lower=250),
            "left_leg": Limb("left_leg", self.stomach.get_end_joint(), 50, 45, angle_upper=290, angle_lower=290),
        }