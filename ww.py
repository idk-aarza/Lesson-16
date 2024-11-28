def total_cal( bill_amount, tip_per ):
    total=bill_amount*(1 + 0.01* tip_per)
    total=round(total, 2)
    print("Please pay ", total)
total_cal(150,20)
    