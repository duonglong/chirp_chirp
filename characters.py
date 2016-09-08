class swordBehavior():
    def useWeapon(self):
        print "Pull the Excalibur from the rock"

class bowBehavior():
    def useWeapon(self):
        print "Ready.....steady......Bang !!!"


class elveRace():
    def WeildWeapon(self):
        if hasattr(self, 'weapon'):
            self.weapon.useWeapon()
        else:
            print "i'm not armed"

    def setWeapon(self, WeaponType):
        self.weapon = WeaponType

Leonard = elveRace()
Leonard.WeildWeapon()
Leonard.setWeapon(bowBehavior())
Leonard.WeildWeapon()
