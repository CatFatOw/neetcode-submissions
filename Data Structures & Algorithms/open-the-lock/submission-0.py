from collections import deque 
class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        if "0000" in deadends:
            return -1

        def bfs(pattern, deadends, target):

            queue = deque([(pattern, 0)])
            visited = set(["".join(pattern)])

            while queue:
                combination, steps = queue.popleft()
                if combination == target:
                    return steps 
                # For each combination idx, we can either increment or decrement the values by 1

                for i in range(len(combination)):
                    for j in range(2):
                        pins = list(combination)
                        pin = int(pins[i])
                        # We incremet
                        if j == 0:
                            if pin == 9:
                                pin = (pin + 1) % 10
                            else:
                                pin += 1
                        else:
                            if pin == 0:
                                pin = (pin - 1) % 10
                            else:
                                pin -= 1
                        
                        pins[i] = str(pin)
                        new_combination = "".join(pins)

                        # We have our unique combiantion
                        if new_combination not in visited and new_combination not in deadends:
                            visited.add("".join(new_combination))
                            queue.append((new_combination, steps+1))
            return -1
        return bfs("0000", deadends, target)

                            


        