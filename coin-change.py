
"""
Jonathan Abbott
3-26-2020

In preperation for CS python quesitons during interviews, Ive started to look at differnt quesitons that may be asked.
They are kinda fun little challenges as I sit here becasue of quarentine!

Question: https://leetcode.com/problems/coin-change/

You are given coins of different denominations and a total amount of money amount. Write a function to compute the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

Example 1:

Input: coins = [1, 2, 5], amount = 11
Output: 3 
Explanation: 11 = 5 + 5 + 1
Example 2:

Input: coins = [2], amount = 3
Output: -1
Note:
You may assume that you have an infinite number of each kind of coin.


Thinking:I thought of this as a coin slot machine or a cashier giving change, you always use the largest denomination coins first then go down. 
If you use another large coin and go over, remove the coin and try the next largest coin(hense the .sort(descending= True side of things)). Always keepign track of the amount of coins used.

"""



def coinchange(Coins, Amount):
    Total = 0
    CoinAmount = 0
    Coins.sort(reverse=True)
    CoinsUsed = []
    for Coin in Coins:
        while Total <= Amount: #Keep adding coins while its under the Amount needed
            Total += Coin
            CoinAmount += 1
            CoinsUsed.append(Coin)

            if Total > Amount: #If it goes over, remove that coin and break out of loop. 
                Total -= Coin
                CoinAmount -= 1
                CoinsUsed.pop()
                break

            elif Total == Amount: #If total equals the Amount needed finish 
                return (CoinAmount,CoinsUsed)
    if Total != Amount:
        return (-1)






if __name__ == "__main__":
    x = coinchange([2], 3)
    print(x)
    print(sum(x[1]))