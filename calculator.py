class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return b - a

    def multiply(self, a, b):
        result = 0
        count = b

        if count < 0:
            a = -a
            count = -count
        while count > 0:
                result =result + a
                count = count - 1
        return result

    def divide(self, a, b):
        if b==0:
            raise ZeroDivisionError("Cannot devide by zero")
        negative = (a < 0)!= (b < 0)

        if a < 0:
            a = -a
        if b <0:
            b = -b
        result = 0

        while a >= b:
            a = a - b
            result = result = result + 1
        if negative:
            result = -result
            
        return result
    
    def modulo(self, a, b):
       
         if b == 0:
            raise ZeroDivisionError("Cannot modulo by zero")
        
         pos_a = 0 - a if a < 0 else a
         pos_b = 0 - b if b < 0 else b
        
 
         while pos_a >= pos_b:
                pos_a = pos_a - pos_b
            
         if a < 0 and pos_a != 0:
            return 0 - pos_a
            
         return pos_a


# Example usage:
if __name__ == "__main__":
    calc = Calculator()
    print("This is a simple calculator class!")
    print("Example: addition: ", calc.add(1, 2))
    print("Example: subtraction: ", calc.subtract(4, 2))
    print("Example: multiplication: ", calc.multiply(2, 3))
    print("Example: division: ", calc.divide(10, 2))
    print("Example: modulo: ", calc.modulo(10, 3))