זההו מבנה כללי של חלקי הקלאסים בMODEL, מבנה בסיסי של כל התכנית ומכאן צריך להוסיף מחלקת אנימציה צביעה חישוב וכו.
המבנה:
skeleton- קלאסס בסיסי
בנוי מ-צירים(JOINTS) ומעצמות(BONES)
יש לו ציר מרכזי שהוא "core" וממנו נבנים כל שאר האיברים.
בהתחלה נבנה הציר המרכזי: /n self.core = Joint("core/neck", x=200, y=200)
ועליו נבנה הראש:self.head = Head( self.core)
מלמטה ממשיכה אותו הבטן(שגם מייוצגת ע"י עצם):self.stomach = Bone("stomach",base_joint = self.core ,length = 60 ,angel =  270 )
ואז יש מילון של איברים שהם מורכבים מעצמות וצירים, הידיים והרגליים הם אוסף של צירים: /n
self.limbs = {
            "right_arm": Limb("right_arm", self.core, 40, 35),
            "left_arm": Limb("left_arm", self.core, 40, 35),
            "right_leg": Limb("right_leg", self.stomach.get_end_joint(), 50, 45),
            "left_leg": Limb("left_leg", self.stomach.get_end_joint(), 50, 45),
        }
        


<img width="960" height="540" alt="סרטוט של מבנה קלאסים בפרוייקט" src="https://github.com/user-attachments/assets/9298a4c0-29a8-4a3f-8a60-6bc9c8d6c127" />
