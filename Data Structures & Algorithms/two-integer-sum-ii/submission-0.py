class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        front = 0
        back = len(numbers) - 1
        result = []

        while (front < back):
            sum = numbers[front] + numbers[back]

            #Condition 1: found target
            if (sum == target):
                result.append(front +1)
                result.append(back +1)
                return result
            # Condition 2: sum is greater than target    
            elif (sum > target): 
                back -= 1
            # Condition 3: sum is less than target    
            else:
                front += 1       
        