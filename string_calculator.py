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
            return sum(int(part) for part in parts)
        
        return int(numbers) 