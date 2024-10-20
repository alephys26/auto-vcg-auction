class Processor:
    def __init__(self):
        pass

    def vcg(self, bids):
        both_bid = bids['b'][0][1]
        top_bid = bids['t'][0][1]
        side_bid = bids['s'][0][1]
        if side_bid + top_bid > both_bid:
            payments = self.__getVCGPayments(both_bid, top_bid, side_bid, 1)
            winners = {'t': [bids['t'][0][0], bids['t'][0][1], payments['t']], 's': [
                bids['s'][0][0], bids['s'][0][1], payments['s']]}
            return winners
        payments = self.__getVCGPayments(both_bid, top_bid, side_bid, 0)
        winner = {'b': [bids['b'][0][0], bids['b'][0][1], payments['b']]}
        return winner

    def __getVCGPayments(self, b, t, s, case):
        payments = {}
        if case == 0:
            payments['b'] = t+s
            return payments
        if b >= s:
            payments['t'] = b
        else:
            payments['t'] = 0
        if b >= t:
            payments['s'] = b
        else:
            payments['s'] = 0
        return payments

    def secondBid(self, bids):
        both_bid = bids['b'][0][1]
        top_bid = bids['t'][0][1]
        side_bid = bids['s'][0][1]
        bid = [('b', both_bid), ('t', top_bid), ('s', side_bid)]
        bid = sorted(bid, key=lambda item: item[1], reverse=True)
        winner = {}
        x = bid[0][0]
        winner[x] = [bids[x][0][0], bids[x][0][1], bid[1][1]]
        return winner
