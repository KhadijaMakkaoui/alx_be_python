def safe_divide(numerator, denominator):
    
   
    try:
        num=float(numerator) 
        den=float(denominator)
        result= num / den
        return str("The result of the division is "+ str(result))
    except ZeroDivisionError:
        return str("Error: Cannot divide by zero.")
    except ValueError:
        return str("Error: Please enter numeric values only.")