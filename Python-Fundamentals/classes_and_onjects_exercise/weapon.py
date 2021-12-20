class Weapon:
    def __init__(self, bullets):
        self.bullets = int(bullets)

    def __repr__(self):
        return f"Remaining bullets: {self.bullets}"

    def shoot(self):
        if self.bullets > 0:
            self.bullets -= 1
            return f"shooting..."
        return f"no bullets left"


weapon = Weapon(7)
weapon.shoot()
weapon.shoot()
weapon.shoot()
weapon.shoot()
weapon.shoot()
weapon.shoot()
print(weapon)