def towerBreakers(n:int, m:int) -> int:
    """Function to calculate the player who reduces towers first leaving the other with no chance to play

    Args:
        n (int): number of towers
        m (int): length of each tower

    Returns:
        int: winner, either 1 or 2
    """
    # Write your code here
    
    # create the towers and their initial height

    if n == 1 and m != 1:
        return 1
    elif n == 1 and m == 1:
        return 2
    elif n != 1 and m == 1:
        return 2
    
    towers = {}
    winner = None
    for idx in range(n):
        towers[idx] = m

    end = False
    # start an infinite loop for the players until no possible move
    while not end:
        # start chances for the two players
        for i in range(1, 3):
            print(f"\n\nPlayer {i}")
            played = False
            for tower in towers:
                if sum(towers.values()) == len(towers):
                    end = True
                    break
                else:
                    if not played:
                        height = towers[tower]
                        if height != 1:
                            for num in range(round(height/2), 0, -1):
                                if height % num == 0:
                                    if len(towers) == 1 or tower == len(towers) -1:
                                        towers[tower] = height - (height - 1)
                                        played = True
                                        print("Immediately Reduced tower: ", towers)
                                        winner = i
                                        break

                                    towers[tower] = height - num
                                    print("Reduced tower: ", towers)
                                    winner = i
                                    played = True
                                    break
                                elif num == 1:
                                    towers[tower] = height - (height - num)
                                    played = True
                                    print("Not Reduced tower: ", towers)
                                    break
                            
    return winner



def main():
    print(f"\n\n\nWinner: {towerBreakers(1, 4)}\n")


if __name__ == "__main__":
    main()