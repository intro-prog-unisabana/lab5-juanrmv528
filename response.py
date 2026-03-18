def input_response(secret, guess):
    if guess < secret:
        return ("Too low! Try a higher number.", False)
    elif guess > secret:
        return ("Too high! Try a lower number.", False)
    else:
        return ("Correct! You guessed the number!", True)