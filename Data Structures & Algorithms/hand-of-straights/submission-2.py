class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        hand.sort()
        hashmap = Counter(hand)
        for i in range(len(hand)):
            val = hand[i]
            if hashmap[val] == 0:
                continue
            for j in range(val, val+groupSize):
                if hashmap[j] <= 0:
                    return False
                hashmap[j] -= 1

        return True 