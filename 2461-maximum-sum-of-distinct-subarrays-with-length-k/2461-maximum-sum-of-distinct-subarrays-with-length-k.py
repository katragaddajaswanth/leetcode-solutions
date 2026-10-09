class Solution:
    def maximumSubarraySum(self, nums: list[int], k: int) -> int:
        
        cur_sum = 0
        max_sum = 0
        dictt = defaultdict(int)

        l = 0
        for r in range(len(nums)) :

            cur_sum += nums[r]
            dictt[nums[r]] +=1 

            if r -l  + 1 > k :
                cur_sum -= nums[l]
                dictt[nums[l]]-=1
                if dictt[nums[l]] == 0 :
                    dictt.pop(nums[l])
                l+=1

            if len(dictt) == k and r - l + 1 == k :
                max_sum = max(cur_sum,max_sum)

        return max_sum

