from main import win_game

output = 0

red_count, green_count = win_game(output)

if red_count > green_count:
    winner = "Red wins!"
elif green_count > red_count:
    winner = "Green wins!"
elif red_count == green_count:
    winner = "It's a tie!"

print("""Number of red entered: {}
Number of green entered: {}
{}""".format(red_count, green_count, winner))
