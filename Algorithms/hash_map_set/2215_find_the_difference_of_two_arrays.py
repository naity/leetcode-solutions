class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        """
        Use sets
        
        Time: O(N+M) Both converting to set and check takes linear time
        Space: O(max(N, m)): hashset of nums1 or nums2
        """

        results = []

        def helper(list1, list2):
            """ Find unique nums in list1 that are not in list2"""
            # convert list2 to set
            target = set(list2)
            res = set()
            for num in list1:
                if num not in target:
                    res.add(num)

            return list(res)
            

        results.append(helper(nums1, nums2))
        results.append(helper(nums2, nums1))

        return results