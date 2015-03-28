change = []
def coinChange(amt, listcoin) :
    global change
    while amt > 0 :
        tmp = [i for i in listcoin if i <= amt]
        coin = max(tmp)
        change.append(coin)
        coinChange(amt - coin, listcoin)
    return change

print coinChange(100,[1,5,25])
