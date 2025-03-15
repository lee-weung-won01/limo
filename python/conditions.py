def main():
    #conditions
    number = int(input("input number: "))
    if number % 2 ==0:
        print("even number")
    else:
        print("False")
    #repeat for
    for i in range(10):
        print(f"{i}")
    print(list(range(10)))

    
if __name__ == "__main__":
    main()
