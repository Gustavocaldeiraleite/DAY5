def SockPairs(all_socks):
    socks = [c for c in all_socks] 
    pairs = 0
    while True:
        for i in socks:
            socks.remove(i)
            if i in socks:
                socks.remove(i)
                pairs +=1
            if socks == []:
                return pairs
            



