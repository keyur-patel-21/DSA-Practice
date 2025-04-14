class Solution(object):
    def numberToWords(self, num):
        thousands = ["", "Thousand", "Million", "Billion"]
        tens = ["", "", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
        under20 = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven" , "Eight", "Nine", "Ten", "Eleven", "Twelve", "Thirteen",      "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]

        result = ""

        def helper(num):
            if num < 20:
                return (under20[num])
            elif num < 100:
                return tens[num//10] + " "+under20[num%10]
            else:
                return under20[num/100] + " Hundred " + helper(num%100)

        if num == 0:
            return "Zero"

        i = 0
        while num > 0:
            triplet = num % 1000
            if triplet > 0:
                result = helper(triplet).strip() + " " + thousands[i] + " " + result
            i += 1
            num = num/1000

        return result.strip()

        