from bone import Bone
from joint import Joint

class Limb:
    def __init__(self, name,parent_joint: Joint, length_upper, length_lower, angle_upper=0, angle_lower=0):
        self.name = name
        
        # מפרקים
        self.joint_start = parent_joint
        self.joint_mid = Joint(name + "_mid")
        self.joint_end = Joint(name + "_end")
        
       # עצמות
        # עצם ה-Upper מתחילה מ-parent_joint שקיבלנו
        self.upper = Bone(name + "_upper", self.joint_start, length_upper, angle_upper)
        self.lower = Bone(name + "_lower", self.joint_mid, length_lower, angle_lower)
        
        # קישורים לוגיים - הגדרת המפרקים הסופיים של כל עצם
        self.upper.child_joint = self.joint_mid
        self.lower.child_joint = self.joint_end
        
        # חישוב ראשוני של מיקום ה-Mid וה-End
        self.update_joints_position()
    
    # חובה לקרוא לפונקציה הזו אחרי שינוי זווית כל עצם כדי לעדכן את מיקומי המפרקים
    def update_joints_position(self):
        
        # חישוב מיקום joint_mid על בסיס upper bone
        self.upper.calculate_end_joint_position()
        
        # חישוב מיקום joint_end על בסיס lower bone
        self.lower.calculate_end_joint_position()
    
    # ה-self חסר בפונקציה הזו
    def get_start_joint(self):
        return self.joint_start
    
    def get_mid_joint(self):
        return self.joint_mid
    
    def get_end_joint(self):
        return self.joint_end