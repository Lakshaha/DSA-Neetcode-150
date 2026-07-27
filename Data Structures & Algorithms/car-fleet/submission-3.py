class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        n = len(position)
        stack = []
        cars = sorted(zip(position,speed))
        cars.reverse()

        for pos,spd in cars:
            time = (target - pos)/spd

            if not stack or stack[-1] < time:
                stack.append(time)
        
        return len(stack)
