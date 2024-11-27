def roman_to_int(roman_nbr:str) -> int:
    result:int = 0

    for i, char in enumerate(roman_nbr):
        match char:
            case 'M':
                result += 800 if i >= 1 and roman_nbr[i-1] == 'C' else 1000
            case 'D':
                result += 300 if i >= 1 and roman_nbr[i-1] == 'C' else 500
            case 'C':
                result += 80 if i >= 1 and roman_nbr[i-1] == 'X' else 100
            case 'L':
                result += 30 if i >= 1 and roman_nbr[i-1] == 'X' else 50
            case 'X':
                result += 8 if i >= 1 and roman_nbr[i-1] == 'I' else 10
            case 'V':
                result += 3 if i >= 1 and roman_nbr[i-1] == 'I' else 5
            case 'I':
                result += 1
    
    return result


print(roman_to_int('CMIX'))