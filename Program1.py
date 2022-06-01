
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def Question1(self, nums:list, target:int):
        new_list = {}
        for idex, vaule in enumerate(nums):
            if target - vaule in new_list:
                return [idex, new_list[target - vaule]]       
            new_list[vaule] = idex

    def Question2(self, s:str) -> int:
        result = 0
        map = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}   
        for i in range(len(s)-1):
            if map[s[i]] < map[s[i+1]]:  
                result -= map[s[i]]
            else:
                result += map[s[i]]
        result += map[s[-1]]  
        return  result

    def Question3(self, l1:ListNode, l2:ListNode)->ListNode:
        result = []
        preResult = result
        if not l1: return l2
        if not l2: return l1
        while l1 and l2:
            if l1.val <= l2.val:  
                preResult.next = l1  
                l1 = l1.next  
            else:  
                preResult.next = l2  
                l2 = l2.next  
            preResult = preResult.next  
            preResult.next = l1 or l2  
  
        return result.next  
    def Question3_1(self, num:int)->str:
        map = {1:'I', 4: 'IV', 5:'V', 9:'IX', 10:'X',
                40:'XL', 50:'L', 90:'XC', 100:'C',
                400:'CD', 500:'D', 900:'CM', 1000:'M'}
        result = ""
        index=-1
        keys = [i for i in map.keys()]
        # print(keys[0])
        while num != 0:
            if num // keys[index] == 0:
                if num % keys[index] == 0:
                    result = map[keys[index]]
                    return result
                else:
                    num %= keys[index]
                    index -= 1
            else:
                for _ in range(num//keys[index]):
                    result += map[keys[index]]
                num %= keys[index]
                index -= 1

        return result

    def Question6(self, num:int) ->bool:
        if num < 1 :return False
        num = bin(num) 
        count = 0  
        for i in num[2:]:
            if i == "1":
                count += 1
        return count == 1  


test = Solution()
print(test.Question1([3,2,4], 6))
print(test.Question1([3,3], 6))

print(test.Question2("LVIII"))
print(test.Question2("MCMXCIV"))


print(test.Question3_1(58))
print(test.Question3_1(1994))

print(test.Question6(16))
print(test.Question6(5))
print(test.Question6(1))
