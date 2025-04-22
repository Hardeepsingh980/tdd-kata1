class StringCalculator:
    def add(self, numbers):
        if numbers == "":
            return 0
        
        delimiter = ","
        
        # Check for custom delimiter
        if numbers.startswith("//"):
            delimiter_line, numbers = numbers.split("\n", 1)
            delimiter = delimiter_line[2:]
        
        # Replace new lines with delimiter
        numbers = numbers.replace("\n", ",")
        
        # Replace delimiter with comma for consistent processing
        if delimiter != ",":
            numbers = numbers.replace(delimiter, ",")
        
        if "," in numbers:
            parts = numbers.split(",")
            
            # Check for negative numbers
            negatives = [int(part) for part in parts if int(part) < 0]
            if negatives:
                neg_str = ", ".join(str(n) for n in negatives)
                raise ValueError(f"negatives not allowed: {neg_str}")
            
            return sum(int(part) for part in parts)
        
        # Check for single negative number
        num = int(numbers)
        if num < 0:
            raise ValueError(f"negatives not allowed: {numbers}")
        
        return num 