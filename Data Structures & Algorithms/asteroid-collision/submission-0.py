class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for curr in asteroids:
            while stack and stack[-1] > 0 and curr < 0:
                diff = stack[-1] + curr

                if diff < 0:
                    stack.pop()
                    continue
                elif diff > 0:
                    break
                else:
                    stack.pop()
                    break
            else:
                stack.append(curr)
        return stack