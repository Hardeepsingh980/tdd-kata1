class StringCalculator:
    def add(self, numbers):
        if numbers == "":
            return 0
        
        # Replace new lines with commas
        numbers = numbers.replace("\n", ",")
        
        if "," in numbers:
            parts = numbers.split(",")
            return sum(int(part) for part in parts)
        
        return int(numbers) 