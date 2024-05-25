def test(x):
    if not type(x) is int:
        raise TypeError("Only Integers are allowed") 
    if x < 0:
        raise Exception("Sorry, no numbers below zero")
    
test("ruan")