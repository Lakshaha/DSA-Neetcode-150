class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        n = len(position)
        fleet = 0
        cars = sorted(zip(position,speed))
        cars.reverse()
        lastTime = float("inf")
        for pos,spd in cars:
            time = (target - pos)/spd

            if lastTime == float("inf") or lastTime < time:
                fleet += 1
                lastTime = time

        
        return fleet
