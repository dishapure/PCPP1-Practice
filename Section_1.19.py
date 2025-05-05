class CustomCalc:
    def __init__(self,factor):
        self.factor = factor;
        print(f"Calculator initialized with factor: {self.factor}")

    def __call__(self,value):
        result = value*self.factor;
        print(f"Multiplying {value} by {self.factor} results in {result}")
        return result

calculator  = CustomCalc(3);

res1 = calculator(5);
res2 = calculator(10);