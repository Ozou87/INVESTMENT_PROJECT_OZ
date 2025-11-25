
#creating table with revenue growth limits and score limits
GROWTH_THRESHOLDS = [
    (0.0,20),
    (5.0,40),
    (15.0,60),
    (30.0,80),
                    ]
GROWTH_DEFAULT = 95

#creating table with operating margin pct limits and score limits
PROFIT_THRESHOLDS = [
    (0.0,20),
    (5.0,40),
    (15.0,60),
    (25,80),
                    ]
PROFIT_DEFAULT = 95

DER_THRESHOLDS = [
    (0.2, 95), 
    (0.5, 80),  
    (1.0, 60), 
    (2.0, 40),
                 ]
DER_DEFAULT = 20


#generic function that will find growth score and send it to "score_growth" func
def score_by_thresholds(value, thresholds, default_score):
    for limit, score in thresholds:
        if value < limit:
            return score
    return default_score

#specific function that sends info to the generic function in order to help it find score
def growth_score(growth_pct: float) -> int:
    return score_by_thresholds(growth_pct, GROWTH_THRESHOLDS, GROWTH_DEFAULT)

#specific function that sends info to the generic function in order to help it find score
def profit_score(profit_pct: float) -> int:
    return score_by_thresholds(profit_pct,PROFIT_THRESHOLDS,PROFIT_DEFAULT)

#specific function that sends info to the generic function in order to help it find score
def der_score(debt_to_eqity: float) -> int:
    return score_by_thresholds(debt_to_eqity,DER_THRESHOLDS,DER_DEFAULT)

#let user input annual rev growth
user_growth_input = input("PLS enter annual revenue growth in %: ")
user_profit_input = input("PLS enter operating margin in %: ")
user_der_input = input("PLS enter dept to equity ratio: ")

#converting the input into a float
growth_value = float(user_growth_input)
profit_value = float(user_profit_input)
der_ratio = float(user_der_input)


#calling the score growth function and placing the value in "result"
result_1 = growth_score(growth_value)
result_2 = profit_score(profit_value)
result3 = der_score(der_ratio)

#printing output for user
print(f"Growth Score is: {result_1}")
print(f"Profit score is: {result_2}")
print(f"Debt score is: {result3}")
