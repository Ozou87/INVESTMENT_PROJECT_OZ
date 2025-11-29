import math

PE_INVALID = float('nan')
PE_RATIO_THRESHOLDS = [
    (0.6,95),
    (0.85,80),
    (1.15,50),
    (1.5,30),
    (2.0,15),
                    ]
PE_RATIO_DEFAULT = 0

F_PE_INVALID = float('nan')
F_PE_RATIO = [
    (0.60,95),
    (0.80,90),
    (0.90,75),
    (1.10,55),
    (1.30,40),
    (1.60,25),
    (2.00,15),
            ]
F_PE_DEFAULT = 5

PS_INVALID = float('nan')
PS_RATIO_THRESHOLDS = [
    (0.70, 95), 
    (0.90, 85),    
    (1.10, 60),   
    (1.40, 40),   
    (2.00, 25),   
    (3.00, 15),  
                    ]
PS_RATIO_DEFAULT = 5   

EVEBITDA_INVALID = float('nan')
EVEBITDA_RATIO_THRESHOLDS = [
    (0.70, 95),   
    (0.90, 85),   
    (1.10, 60),   
    (1.40, 40),   
    (2.00, 25),  
    (3.00, 15),   
                            ]
EVEBITDA_RATIO_DEFAULT = 5   

PFCF_INVALID = float('nan')
PFCF_RATIO_THRESHOLDS = [
    (0.70, 95),   
    (0.90, 85),  
    (1.10, 60),   
    (1.40, 40),   
    (2.00, 25),   
    (3.00, 15), 
                        ]
PFCF_RATIO_DEFAULT = 5   

#generic function that will find score and send it to specific function
def score_by_thresholds(stock_value: float, sector_value: float, thresholds, default_score) -> float:
    
    #protecting from dividing by - 0
    #checking weather stock_val/sector_cal is 'nan' ex.
    if sector_value == 0 or math.isnan(stock_value) or math.isnan(sector_value):
        return default_score
    
    relative_multiple = stock_value / sector_value

    for limit, score in thresholds:
        if relative_multiple < limit:
            return score
    return default_score

stock_pe = float(input("pls enter stock P/E: "))
sector_pe = float(input("pls enter sector P/E: "))

stock_fpe = float(input("Enter stock Forward P/E: "))
sector_fpe = float(input("Enter sector Forward P/E: "))

result_1 = score_by_thresholds(stock_pe,sector_pe, PE_RATIO_THRESHOLDS, PE_RATIO_DEFAULT)
print(f"this is the score for this data: {result_1}")

