from input_handler import InputHandler
from result_outputter import ResultOutputter
from processor import Processor


class Auction:
    def __init__(self):
        self.input_handler = InputHandler()
        self.result_outputter = ResultOutputter()
        self.processor = Processor()

    def getInput(self, case) -> dict[str, list[tuple[int, int]]]:
        input_file = f"a{case}.txt"
        self.input_handler.clear()
        self.input_handler.processFile(input_file)
        bids = self.input_handler.getBids()
        return bids

    def processBids(self, bids, auction_type) -> dict[str, list[int, int, int]]:
        if auction_type == 'v':
            return self.processor.vcg(bids)
        return self.processor.secondBid(bids)

    def run(self, case, auction_type):
        bids = self.getInput(case)
        results = self.processBids(bids, auction_type)
        self.result_outputter.write(auction_type, case, bids, results)
