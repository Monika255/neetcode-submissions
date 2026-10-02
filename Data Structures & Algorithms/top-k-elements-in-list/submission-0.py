class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count={}
        for num in nums:
            if  num in count:
             count[num]=count[num]+1
            else:
             count[num]=1
        count_s=sorted(count.items(),key=lambda pair:pair[1],reverse=True)
        result=[]
        for pair in count_s[:k]:
            result.append(pair[0])
        return result
