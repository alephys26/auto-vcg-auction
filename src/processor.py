import copy


class Processor:
    def __init__(self):
        pass

    def vcg(self, bids):
        winners = self.__getVCGWinners(bids)
        payments = self.__getVCGPayments(bids, winners)
        for banner in winners:
            winners[banner].append(payments[banner])
        return winners

    def __getVCGWinners(self, bids):
        both_bid = 0
        side_bid = 0
        top_bid = 0
        if bids['b']:
            both_bid = bids['b'][0][1]
        if bids['t']:
            top_bid = bids['t'][0][1]
        if bids['s']:
            side_bid = bids['s'][0][1]
        if side_bid + top_bid > both_bid:
            winners = {'t': [bids['t'][0][0], bids['t'][0][1]], 's': [
                bids['s'][0][0], bids['s'][0][1]]}
        else:
            winners = {'b': [bids['b'][0][0], bids['b'][0][1]]}
        return winners

    def __getVCGPayments(self, bids, winners):
        payments = {}
        for bidder in winners:
            remaining_bids = copy.deepcopy(bids)
            remaining_bids[bidder].remove(bids[bidder][0])
            new_winners = self.__getVCGWinners(remaining_bids)
            actual_revenue_without_bidder = sum(
                [i[1][1] for i in winners.items() if i[0] != bidder])
            if actual_revenue_without_bidder == None:
                actual_revenue_without_bidder = 0
            external_revenue = sum([i[1][1] for i in new_winners.items()])
            payments[bidder] = external_revenue - actual_revenue_without_bidder
        return payments

    def secondBid(self, bids):
        all_bids = [(key, item[0], item[1])
                    for key, values in bids.items() for item in values]
        bid = sorted(all_bids, key=lambda x: x[2], reverse=True)
        winner = {}
        winner[bid[0][0]] = [bid[0][1], bid[0][2], bid[1][2]]
        return winner
