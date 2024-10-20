class ResultOutputter:
    results_directory = "..\\results\\"

    def __init__(self):
        self.dir = ResultOutputter.results_directory

    def write(self, case, bids, winner):
        outfile = open(self.dir+f"a{case}.txt", "w")
        outfile.write('=================================================')
        outfile.write(f"Case {case}:\n\tBids:")
        outfile.writelines(bids)
        outfile.write('=================================================')
        outfile.write('\tAuction Winners:')
        outfile.writelines(winner)
        outfile.write('=================================================')
