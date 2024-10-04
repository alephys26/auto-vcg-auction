from input_handler import InputHandler
from result_outputter import ResultOutputter
from processor import Processor


class VCGAuction:
    def __init__(self):
        self.input_handler = InputHandler()
        self.result_outputter = ResultOutputter()
        self.processor = Processor()

    def getInput(self, case) -> dict[str, dict[int, int]]:
        input_file = f"a{case}.txt"
        self.input_handler.clear()
        self.input_handler.processFile(input_file)
        bids = self.input_handler.getBids()
        return bids

    def processBids(self, bids):
        pass

    def run(self, case):
        bids = self.getInput(case)
        self.processBids(bids)
