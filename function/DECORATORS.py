def make_pretty(func):
    def inner():
        print("i get ordinary")
        func()
    return inner()

@make_pretty
def ordinary():
    print("i am ordinary")
ordinary()