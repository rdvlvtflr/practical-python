# sears.py
note_thickness = 0.11 * 0.001 # height of note in metres
sears_height = 442 # height of building in metres
num_notes = 1
day = 1

while num_notes * note_thickness < sears_height:
    print ("Day", day, "Number of notes", num_notes, num_notes * note_thickness)
    day = day + 1
    num_notes = num_notes *2

print("Number of days", day)
print("Number of notes", num_notes)
print("Final height", round(num_notes * note_thickness), "meters")