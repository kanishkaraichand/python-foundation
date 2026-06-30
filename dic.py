#creating a basic dictionary

n = int(input('how many students?'))
winner = {}
for a in range(n):
    key= input('name of student:')
    value = int(input('number of competition won:'))
    winner[key]= value
print('the dictionary now is:')
print(winner)
if winner:  # Check if the dictionary is not empty
    max_student = ""
    max_wins = -1

    for name,wins in winner.items():
        if wins > max_wins:
            max_wins = wins
            max_student = name

    print(
        f"\n🏆 Top Performer: {max_student} with {max_wins} competition wins!")
