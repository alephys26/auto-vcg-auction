# auto-vcg-auction
## IIT Jodhpur | CSL7560: Autnomous Systems
## Course Assignment 2: A VCG Auction mechanism simulation 

The assignment runs to simulate VCG Auctions and Second Bid Auctions.  
The input format is a text file stored in the _input_ folder. The format of bids is  
`bidder_id:banner_position:bid_value`  
It can be seen in the available example files in the _input_ folder.  
To run the simulations, run the script __main.py__ in the src folder, using the following command set:  
```
cd src\
python3 main.py
```
This will run all the cases from a1.txt to a7.txt present in the folder _input_ in both VCG and Second Bid Mechanism and the results will be stored in the results folder in the format a1v.txt or a1s.txt for input a1.txt in VCG and second bid mechanism respectively.  
If you want to run a specific file or case in input folder. Make the file named as a{some integer value}.txt for exampe a16.txt. Populate it with the bids in the aforementioned format. Then run it using `python3 main.py 16v` for VCG and `python3 main.py 16s` for second bid or `python3 main.py 16v 16s` for running both the cases.   

> _Yash Shrivastava, B21CS079_  
  _Yash Mangal, B21AI047_  