def solution(nums):
    answer = 0
    size=len(nums)/2
    nums=list(set(nums))
    if size<=len(nums):
        return size
    else :
        return len(nums)
    return answer