def convert_base(num_to_convert: str, input_base: int, output_base: int) -> str | None:
    """Converts a number from one base to another. Returns None in case of errors."""
    
    # Dictionary to store mappings between characters and their numerical values
    conversions = dict()
    for i in range(0, 36):
        if i < 10:
            conversions.setdefault(''.join(chr(ord('0') + i)), i)
        else:
            conversions.setdefault(''.join(chr(ord('A') + i - 10)), i)

    # Inverted dictionary for convenience in reverse conversions
    reversed_conversions = {v: k for k, v in conversions.items()}

    def base_to_decimal(num: str, base: int) -> int | None:
        """Converts a number from the given base to decimal. Returns None in case of errors."""
        
        decimal_num = 0
        n = 0
        
        # Iterating through the characters of the input number in reverse order
        for char in num[::-1]:
            # Checking if the character is valid for the given base
            if conversions.get(char.upper(), -1) < base:
                # Converting the character to its numerical value and updating the decimal number
                decimal_num += conversions[char.upper()] * base ** n
            else:
                return None
            n += 1
            
        return decimal_num

    def decimal_to_base(dec_num: int | None, base: int) -> str | None:
        """Converts a decimal number to the given base. Returns None in case of errors."""
        
        if dec_num is None:
            return None
        elif dec_num == 0:
            return '0'
        
        remainder = dec_num
        output_num = ''
        
        # Iterating through the remainder of the division of the decimal number by the output base
        while remainder:
            # Appending the corresponding character from the reversed conversions dictionary
            output_num += reversed_conversions[remainder % base]
            # Updating the remainder by integer division of the previous remainder by the output base
            remainder //= base
        
        # Reversing the string to get the correct representation of the converted number
        output_num = output_num[::-1]
        
        return output_num

    # Checking if the input and output bases are within the specified range
    if input_base not in range(2, 37) or output_base not in range(2, 37):
        return None
    
    # Checking if valid parameters are passed to the function
    if not num_to_convert or not input_base or not output_base:
        return None 

    # Converting the input number to decimal
    decimal_number = base_to_decimal(num_to_convert, input_base)
    
    # Converting the decimal number to the output base
    converted_number = decimal_to_base(decimal_number, output_base)
    
    return converted_number