class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        if num <= 1:
            return False
            
        divisor_sum = 1  # 1 is always a proper divisor for num > 1
        
        # Iterate up to the square root of num
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                divisor_sum += i
                # Add the counterpart divisor if it's different
                other = num // i
                if other != i:
                    divisor_sum += other
                    
        return divisor_sum == num