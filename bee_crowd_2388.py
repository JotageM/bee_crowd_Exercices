def cases():
    cases = int(input())
    return cases

def total_distance():
    time,speed = map(int,input().split())
    total_distance = time * speed
    return total_distance



def main():
    n = cases()
    distance = 0
    for i in range(n):
        distance += total_distance()
    print(distance)

if __name__ == "__main__":
    main()

