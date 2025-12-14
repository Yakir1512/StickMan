from bone import Bone
from joint import Joint
from limb import Limb 

# השלמה מינימלית
class Head:
    def __init__(self, parent_joint: Joint, size=30, angle=270):
        self.parent_joint = parent_joint
        self.head_bone = Bone("head_bone", parent_joint, size, angle)
        self.head_joint = self.head_bone.get_end_joint()