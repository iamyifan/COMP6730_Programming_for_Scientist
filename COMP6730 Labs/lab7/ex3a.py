global_X = 27


def my_function(param1=123, param2="hi mom"):
    local_X = 654.321
    global_X = 5  # creat a local varibale with the same name
   
    print("\n=== local namespace ===")
    for name, val in list(locals().items()):
        print("name:", name, "value:", val)
    print("======================")
    
    print("\n=== global namespace ===")
    for name, val in list(globals().items()):
        print("name:", name, "value:", val)
    print("======================")


my_function()
print(locals().items())  # same as globals().items()
print(globals().items())
