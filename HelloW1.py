import sys

# Argument required when run
def example():
    # or code breaks right here
    try:
        mystring = sys.argv[1]
    except:
        mystring = "World"
    print("Hello", mystring)

if __name__ == "__main__":
    example()