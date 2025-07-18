class Solution:
    def asteroidsDestroyed(self, mass: int, asteroids: List[int]) -> bool:
        asteroids = sorted(asteroids)
        curMass = mass

        for i in range(len(asteroids)):
            if asteroids[i] > curMass:
                return False
            else:
                curMass += asteroids[i]
        return True
        