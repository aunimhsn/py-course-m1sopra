def roman_to_int(roman_nbr:str) -> int:
    result:int = 0

    for i, char in enumerate(roman_nbr):
        match char:
            case 'M':
                if i >= 1 and roman_nbr[i-1] == 'C':
                    result += 800
                else:
                    result += 1000
            case 'D':
                if i >= 1 and roman_nbr[i-1] == 'C':
                    result += 300
                else:
                    result += 500
            case 'C':
                if i >= 1 and roman_nbr[i-1] == 'X':
                    result += 80
                else:
                    result += 100
            case 'L':
                if i >= 1 and roman_nbr[i-1] == 'X':
                    result += 30
                else:
                    result += 50
            case 'X':
                if i >= 1 and roman_nbr[i-1] == 'I':
                    result += 8
                else:
                    result += 10
            case 'V':
                if i >= 1 and roman_nbr[i-1] == 'I':
                    result += 3
                else:
                    result += 5
            case 'I':
                result += 1
    
    return result


print(roman_to_int('CMIX'))

