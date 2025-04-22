class StringCalculator:
    def add(self, numbers):
        if numbers == "":
            return 0
        
        if "," in numbers:
            parts = numbers.split(",")
            return int(parts[0]) + int(parts[1])
        
        return int(numbers) 