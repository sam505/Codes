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

    if n and m == 1:
        return 2
    elif n % 2 == 0:
        return 2
    else:
        return 1



def main():
    print(f"\n\n\nWinner: {towerBreakers(1, 4)}\n")


if __name__ == "__main__":
    main()