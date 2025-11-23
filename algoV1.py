
#creating table with revenue growth limits and score limits
GROWTH_THRESHOLDS = [
    (0.0,20),
    (5.0,40),
    (15.0,60),
    (30.0,80),
                    ]
GROWTH_DEFAULT = 95

#generic function that will find growth score and send it to "score_growth" func
def score_by_thresholds(value, thresholds, default_score):
    for limit, score in thresholds:
        if value < limit:
            return score
    return default_score

#specific function that sends info to the generic function in order to help it find score
def score_growth(growth_pct: float) -> int:
    return score_by_thresholds(growth_pct, GROWTH_THRESHOLDS, GROWTH_DEFAULT)

#let user input annual rev growth
user_input = input("PLS enter annual revenue growth in %: ")
#converting the input into a float
growth_value = float(user_input)

#calling the score growth function and placing the value in "result"
result = score_growth(growth_value)
#printing output for user
print(f"Growth Score is: {result}")

