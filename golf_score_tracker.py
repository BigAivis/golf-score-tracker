first_half = [("1st", 4), ("2nd", 4), ("3rd", 3), ("4th", 5), ("5th", 4), ("6th", 5), ("7th", 3), ("8th", 4), ("9th", 5)]
second_half = [("10th", 3), ("11th", 4), ("12th", 3), ("13th", 4), ("14th", 5), ("15th", 4), ("16th", 4), ("17th", 3), ("18th", 5)]
full_course = first_half + second_half
user_strokes = []
user_putts = []
current_score = 0

print("\nHello! Welcome to the Capitals Golf Course!")
print("\nGolf course type options:")
print("\t1. 1st Half")
print("\t2. 2nd Half")
print("\t3. Full Course")

course_type = int(input("Select which side are you going to play: "))

def format_score(score):
    if score > 0:
        return "+" + str(score)
    else:
        return score

def score_counter(course_pars):
    for hole_information in course_pars:
        strokes = int(input(f"How many strokes that it took in {hole_information[0]} hole? "))
        putts = int(input("And how many putts on green? "))

        user_strokes.append(strokes)
        user_putts.append(putts)

        hole_score = strokes - hole_information[1]
        print(f"Hole score: {format_score(hole_score)}")

        global current_score
        current_score = current_score + hole_score
        print(f"Current score: {format_score(current_score)}")
    
    total_putts = sum(user_putts)
    total_strokes = sum(user_strokes)
    total_strokes_before_green = total_strokes - total_putts

    print("\nFull game details:")
    print(f"Final score: {format_score(current_score)}")
    print(f"Total strokes: {total_strokes}")
    print(f"Total putts on green: {total_putts}")
    print(f"Total strokes before green: {total_strokes_before_green}")

if course_type == 1:
    print("\nYour playing first half, good luck!")
    score_counter(first_half)
elif course_type == 2:
    print("\nYour playing second half, good luck!")
    score_counter(second_half)
elif course_type == 3:
    print("\nYour playing full course, good luck!")
    score_counter(full_course)
else:
    print("\nInvalid course type")