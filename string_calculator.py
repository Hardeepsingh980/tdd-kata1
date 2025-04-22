import re

class StringCalculator:
    def add(self, numbers):
        if numbers == "":
            return 0
        
        delimiter = ","
        
        # Check for custom delimiter
        if numbers.startswith("//"):
            # Handle multiple delimiters with [delim1][delim2] format
            if numbers.startswith("//[") and "]" in numbers:
                # Extract all delimiters
                delimiters = re.findall(r'\[(.*?)\]', numbers)
                
                # Extract numbers part
                match = re.match(r'//(?:\[.*?\])+\n(.*)', numbers)
                if match:
                    numbers = match.group(1)
                    
                    # Replace each delimiter with comma
                    for d in delimiters:
                        numbers = numbers.replace(d, ",")
            else:
                delimiter_line, numbers = numbers.split("\n", 1)
                delimiter = delimiter_line[2:]
                numbers = numbers.replace(delimiter, ",")
        
        # Replace new lines with comma
        numbers = numbers.replace("\n", ",")
        
        if "," in numbers:
            parts = numbers.split(",")
            
            # Check for negative numbers
            negatives = [int(part) for part in parts if int(part) < 0]
            if negatives:
                neg_str = ", ".join(str(n) for n in negatives)
                raise ValueError(f"negatives not allowed: {neg_str}")
            
            # Ignore numbers bigger than 1000
            return sum(int(part) for part in parts if int(part) <= 1000)
        
        # Check for single negative number
        num = int(numbers)
        if num < 0:
            raise ValueError(f"negatives not allowed: {numbers}")
        
        # Ignore numbers bigger than 1000
        return num if num <= 1000 else 0 