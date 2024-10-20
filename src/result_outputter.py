class ResultOutputter:
    results_directory = "../results/"

    def __init__(self):
        pass

    def write(self, auction_type, case, bids, winner):
        outfile = open(ResultOutputter.results_directory+f"a{case}.txt", "w")
        outfile.write('=================================================\n')
        auc_type = "VCG"
        if auction_type == "s":
            auc_type = "Second Bid" 
        outfile.write(f"Case {case}:\nAuction Type: {auc_type}\nBids:\n\t'Position': [('Bidder_Id', 'Bid')]\n")
        outfile.writelines(self.__write_dict(bids))
        outfile.write('\n=================================================\n')
        outfile.write(
            'Auction Winners:\n\t["Bidder Id", "Bid", "Payment Made"]\n')
        outfile.writelines(self.__write_dict(winner))
        revenue = sum([i[2] for i in winner.values()])
        outfile.write(f'\nAuction Revenue: {revenue}')
        outfile.write('\n=================================================\n')
        outfile.close()
        print(
            f"Please open the file {ResultOutputter.results_directory}a{case}.txt to view the results.")

    def __write_dict(self, di)->str:
        s = ""
        for f in di:
            s+=f+" : \n"
            for bid in di[f]:
                s += f"\t{bid},\n"
        return s
