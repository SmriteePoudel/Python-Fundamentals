def handle_exceptions():
    try:
       
        result = 10 / 0  
    except ArithmeticError as e:
        print(f"ArithmeticError occurred: {e}")

    try:
       
        import nonexistent_module  
    except ImportError as e:
        print(f"ImportError occurred: {e}")

    try:
      
        lst = [1, 2, 3]
        print(lst[5])  
    except IndexError as e:
        print(f"IndexError occurred: {e}")

    try:
       
        dct = {"a": 1, "b": 2}
        print(dct["c"])  
    except KeyError as e:
        print(f"KeyError occurred: {e}")


handle_exceptions()
