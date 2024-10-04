from input_handler import InputHandler
from result_outputter import ResultOutputter
from processor import Processor


class VCGAuction:
    def __init__(self):
        self.input_handler = InputHandler()
        self.result_outputter = ResultOutputter()
        self.processor = Processor()
