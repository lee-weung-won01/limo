def print_3_time():
    print("hello")
    print("hello")
    print("hello")
    a = 100
    return "ok", 1, "complete", a

# def print_n_time(n):
#     for i in range(n):
#         print("hi")

def main():
    re = print_3_time()
    #print_n_time(3)
    print(re)

if __name__ == "__main__":
    main()