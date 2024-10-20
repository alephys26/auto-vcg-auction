class InputHandler:
    input_directory = "../input/"

    def __init__(self):
        self.input = []

    def processFile(self, file) -> list[list[str, str, float]]:
        lines = open(InputHandler.input_directory + file).readlines()
        input = []
        for line in lines:
            bid_info = line.split(':')
            bid_info[2] = float(bid_info[2])
            input.append(bid_info)
        self.input = input

    def clear(self):
        self.input = []

    def getTopBannerBids(self) -> list[tuple[str, float]]:
        if not self.input:
            raise ValueError(
                "No Input. Provide Input file or run processFile.")
        top_bids = []
        for i in self.input:
            if i[1] == 't' or i[1] == 'T':
                top_bids.append((i[0], i[2]))
        return sorted(top_bids, key=lambda item: item[1], reverse=True)

    def getSideBannerBids(self) -> list[tuple[str, float]]:
        if not self.input:
            raise ValueError(
                "No Input. Provide Input file or run processFile.")
        side_bids = []
        for i in self.input:
            if i[1] == 's' or i[1] == 'S':
                side_bids.append((i[0], i[2]))
        return sorted(side_bids, key=lambda item: item[1], reverse=True)

    def getBothBannerBids(self) -> list[tuple[str, float]]:
        if not self.input:
            raise ValueError(
                "No Input. Provide Input file or run processFile.")
        both_bids = []
        for i in self.input:
            if i[1] == 'b' or i[1] == 'B':
                both_bids.append((i[0], i[2]))
        return sorted(both_bids, key=lambda item: item[1], reverse=True)

    def getBids(self) -> dict[str, list[tuple[str, float]]]:
        bids = {}
        bids['t'] = self.getTopBannerBids()
        bids['s'] = self.getSideBannerBids()
        bids['b'] = self.getBothBannerBids()
        return bids
