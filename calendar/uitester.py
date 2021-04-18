from Calendar import *
import sys, os
import builtins
import math

current_command = [
"add 2017-10-21 9 10 budget meeting",
"add 2017-10-22 6 7 go to the gym",
"boo",
"add 2017-10-23 5 6 go to the gym",
"add 2017-11-01 15 16 Make sure to submit csc108 assignment 2",
"list",
"add 2017-12-02 16 17 Make sure to submit csc108 assignment 3",
"add 2017-11-06 8 10 Term test 2",
"add 2017-10-29 7 8 Get salad stuff,lettuce, red peppers, green peppers",
"add 2017-11-06 19 22 Sid's birthday",
"show",
"delete 2017-10-29 7",
"delete 2015-12-03 9",
"delete 2017-12-02 16",
"show",
"quit",
]
total = 25
score = 0
command_count = -1
def disable_input(*args):
    global command_count
    command_count += 1
    return current_command[command_count]

builtins.input = disable_input

output_filename = 'outputfile.txt'
calendar_filename = "calendar.txt"
sys.stdout = open(output_filename, 'w')
# Something here that provides a write method.
# calls to print, ie import module1
try:
    with open("calendar.txt", 'w') as stream:
        pass

    user_interface()

    sys.stdout = sys.__stdout__

    with open(output_filename) as stream:
        content = stream.read()
        if content.count("calendar loaded") == 1:
            score += 1
            print("Calendar Loaded message present. 1/1 marks given")
        else:
            print("Calendar Loaded message NOT present. 0/1 marks given", file=sys.stderr)

        if content.count("calendar saved") == 1:
            score += 1
            print("Calendar saved message present. 1/1 marks given")
        else:
            print("Calendar saved message NOT present. 0/1 marks given", file=sys.stderr)

        if content.count("deleted") == 4:
            score += 4
            print("Delete commands correctly implemented 4/4 marks given")
        else:
            score += content.count("deleted")
            print("Delete commands incorrectly implemented. {0:d}/4 marks given. "
                  "Expecting 4 'deleted' outputs, but {0:d} given".format(content.count("deleted")), file=sys.stderr)

        if content.count("added") == 8:
            score += 8
            print("Add commands correctly implemented 8/8 marks given")
        else:
            score += content.count("added")
            print("Add commands incorrectly implemented. {0:d}/8 marks given. "
                  "Expecting 8 'added' outputs but {0:d} given".format(content.count("added")), file=sys.stderr)

        if content.count("2015-12-03 is not a date in the calendar") == 1:
            score += 1
            print("Error message correctly outputted. 1/1 marks given")
        else:
            print("Error message NOT correctly outputted. 0/1 marks given", file=sys.stderr)

        if content.count("Help for Calendar. The calendar commands are") == 2:
            score += 2
            print("Help command correctly outputted.  2/2 marks given")
        else:
            score += content.count("Help for Calendar. The calendar commands are")
            print("Help command incorrectly implemented. {0:d}/2 marks given. "
                  "Expecting 2 'help' outputs, but {0:d} given".format(content.count("Help for Calendar. The calendar commands are")), file=sys.stderr)


        if content.count("title : Sid's birthday") == 4:
            score += 4
            print("Calendar entries correctly added and displayed 4/4 marks given")
        else:
            score += content.count("title : Sid's birthday")
            print("Calendar entries correctly added and displayed. {0:d}/4 marks given. "
                  "Expecting 4 outputs, but {0:d} given".format(content.count("title : Sid's birthday")), file=sys.stderr)


    calendar_content_text = "2017-11-06:08-10 Term test 2\t19-22 Sid's birthday\n2017-11-01:15-16 Make sure to submit csc108 assignment 2\n2017-10-23:05-06 go to the gym\n2017-10-22:06-07 go to the gym\n2017-10-21:09-10 budget meeting\n"
    with open(calendar_filename) as stream:
        content = stream.read()
        if content == calendar_content_text:
            score += 4
            print("Calendar file content is correct 4/4 marks given")
        else:
            print("Calendar file content not correct 0/4 marks\nExpected content was \n{}\nReceived content was \n{}\n".format(calendar_content_text, content), file=sys.stderr)

except Exception as e:
    print("There was an error with your file\nError is", e, file=sys.stderr)

score = score if score > 0 else 0

score *= 1.0
total *= 1.0

compressed_weight = 0.4
score = math.floor(score * compressed_weight)
total = math.floor(total * compressed_weight)

print()
print("Results of user_interface() = {}/{} = {}%".format(score, total, round((score / total) * 100)))

# os.remove(output_filename)
