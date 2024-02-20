class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        """
        Try each index

        Time: O(N^2)
        Space: O(1)

        for i in range(len(gas)):
            tank = 0
            j = i
            finished = True

            for _ in range(len(gas)):
                tank += gas[j]

                if tank < cost[j]:
                    finished = False
                    break
                else:
                    # have enough gas to travel to the next station
                    tank -= cost[j]
                    j = (j + 1) % len(gas)

            if finished:
                return i

        return -1

        This approach exceeds the time limit

        keys:
        1. the sum of gas should >= the sum of cost, otherwise, no solution
        2. calculate the net change in gas for each station i
        3. if i < 0, it can't be the start
        4. use a variable to track the sum of changes, whenever the sum < 0, reset and
           try the next station as the start because we know there must be one

        Time: O(N)
        Space: O(1)
        """
        if sum(gas) < sum(cost):
            return -1

        sum_changes = 0
        res = 0
        for i in range(len(gas)):
            change = gas[i] - cost[i]
            sum_changes += change

            if sum_changes < 0:
                # reset
                sum_changes = 0
                # try next station
                res = i + 1

        return res
