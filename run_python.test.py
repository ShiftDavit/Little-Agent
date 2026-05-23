from functions.run_python import run_python

SEPARATOR = "========================"

def test() -> None:
    result = run_python("calculator", "main.py")
    print(result)
    print(SEPARATOR)

    result = run_python("calculator", "main.py", ["3 + 5"])
    print(result)
    print(SEPARATOR)

    result = run_python("calculator", "tests.py")
    print(result)
    print(SEPARATOR)

    result = run_python("calculator", "../main.py")
    print(result)
    print(SEPARATOR)

    result = run_python("calculator", "nonexistent.py")
    print(result)
    print(SEPARATOR)

    result = run_python("calculator", "lorem.txt")
    print(result)


    



if __name__ == "__main__":
    test()
