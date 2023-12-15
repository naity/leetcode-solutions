class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        """
        Use a stack and push positive numbers to the stack
        In case of a negative number, keep popping until there is
        1) a bigger or equal positive number
        2) a negative number
        3) stack is empty

        If the negative number is not exploded, push it to the stack

        Time: O(N) at most push and pop once
        Space: O(N)
        """

        res = []

        for num in asteroids:
            if num > 0:
                res.append(num)
            else:
                negative_explode = False
                while res and res[-1] > 0 and not negative_explode:
                    if res[-1] > abs(num):
                        negative_explode = True
                    elif res[-1] == abs(num):
                        # both explode
                        negative_explode = True
                        res.pop()
                    else:
                        res.pop()

                # if negative doesn't explode, push it to stack
                if not negative_explode:
                    res.append(num)

        return res
