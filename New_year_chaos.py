def minimumBribes(q):
    # Write your code here
    irregularities = 0
    run_status = True
    while (q != sorted(q) and run_status):
        idx = 0
        while idx < len(q) -1:
            if q[idx] > q[idx + 1]:
                if q[idx] - idx > 3:
                    print(q, run_status)
                    irregularities = "Too chaotic"
                    run_status = False
                    break
                else:
                    q[idx], q[idx+1] = q[idx+1], q[idx]
                    irregularities += 1
            idx += 1
    
    print(irregularities)
       


def main():
    queue = [2,5,1,3,4]
    minimumBribes(queue)



if __name__ == "__main__":
    main()