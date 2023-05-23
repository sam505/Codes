def truckTour(petrolpumps):
   # Write your code here
    start = 0
    idx = 0
    petrol = 0
    while idx < len(petrolpumps)-1:
        petrol = petrolpumps[idx][0]
        distance = petrolpumps[idx][1]
        if petrol > distance:
            start = idx
            while idx < len(petrolpumps)-1:
                if petrol > 0:
                    petrol -= distance
                    petrol += petrolpumps[idx+1][0]
                    distance = petrolpumps[idx+1][1]
                    idx += 1
                else:
                    idx = start
                    break
        idx += 1
                
    return start


def main():
    arr = [
        [1, 5],
        [10, 3],
        [3, 4]
    ]
    print(truckTour(arr))
    

if __name__ == "__main__":
    main()