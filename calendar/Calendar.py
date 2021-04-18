import os
'''

IMPORTANT NOTE: Do NOT change any of the function names or their signatures
(the parameters they take).
Your functions must behave exactly as described. Please check correctness by
running DocTests  included in function headers. You may not use any print or
input statements in your code.

Manage a calendar database.

A calendar is a dictionary keyed by date ("YYYY-MM-DD") with value being a list
of strings, the events on the specified date.

'''


# -----------------------------------------------------------------------------
# Please implement the following calendar commands
# -----------------------------------------------------------------------------

def command_help():
    """
    () -> str
    This function is already implemented. Please do not change it.
    Returns a help message for the system. That is...
    """

    help_me = """
    Help for Calendar. The calendar commands are

    add DATE START END DETAILS               add the event DETAILS at the specified DATE with specific START and END time
    show                                     show all events in the calendar
    delete DATE NUMBER             delete the specified event (by NUMBER) from
                                   the calendar
    quit                           quit this program
    help                           display this help message

    Examples: user data follows command:

    command: add 2018-10-12 18 19 dinner with jane
    success

    command: show
        2018-10-12 :
            start : 08:00,
            end : 09:00,
            title : Eye doctor

            start : 12:30,
            end : 13:00,
            title : lunch with sid

            start : 18:00,
            end : 19:00,
            title : dinner with jane
        2018-10-29 :
            start : 10:00,
            end : 11:00,
            title : Change oil in blue car

            start : 12:00,
            end : 14:00,
            title : Fix tree near front walkway

            start : 18:00,
            end : 19:00,
            title : Get salad stuff, leuttice, red peppers, green peppers
        2018-11-06 :
            start : 18:00,
            end : 22:00,
            title : Sid's birthday

    command: delete 2018-10-29 10
    deleted

    A DATE has the form YYYY-MM-DD, for example
    2018-12-21
    2016-01-02

    START and END has a format HH where HH is an hour in 24h format, for example
    09
    21

    Event DETAILS consist of alphabetic characters,
    no tabs or newlines allowed.
    """
    return help_me


def command_add(date, start_time, end_time, title, calendar):
    """
    (str, int, int, str, dict) -> boolean
    Add title to the list at calendar[date]
    Create date if it was not there
    Adds the date if start_time is less or equal to the end_time

    date: A string date formatted as "YYYY-MM-DD"
    start_time: An integer from 0-23 representing the start time
    end_time: An integer from 0-23 representing the start time
    title: A string describing the event
    calendar: The calendar database
    return: boolean of whether the even was successfully added

    >>> calendar = {}
    >>> command_add("2018-02-28", 11, 12, "Python class", calendar)
    True
    >>> calendar == {"2018-02-28": [{"start": 11, "end": 12, "title": "Python class"}]}
    True
    >>> command_add("2018-03-11", 14, 16, "CSCA08 test 2", calendar)
    True
    >>> calendar == {"2018-03-11": [{"start": 14, "end": 16, "title": "CSCA08 test 2"}], \
    "2018-02-28": [{"start": 11, "end": 12, "title": "Python class"}]}
    True
    >>> command_add("2018-03-11", 10, 9, "go out with friends after test", calendar)
    False
    >>> calendar == {"2018-03-11": [{"start": 14, "end": 16, "title": "CSCA08 test 2"}], \
    "2018-02-28": [{"start": 11, "end": 12, "title": "Python class"}]}
    True
    >>> command_add("2018-03-13", 13, 13, "Have fun", calendar)
    True
    >>> calendar == {"2018-03-13": [{"start": 13, "end": 13, "title": "Have fun"}], \
    "2018-03-11": [{"start": 14, "end": 16, "title": "CSCA08 test 2"}], \
    "2018-02-28": [{"start": 11, "end": 12, "title": "Python class"}]}
    True
    """
    if is_calendar_date(date) and all([(i in range(0, 24)) for i in (start_time, end_time)]) and start_time <= end_time and is_natural_number(str(start_time)) and is_natural_number(str(end_time)):
        event = {
            "start": start_time,
            "end": end_time,
            "title": title,
        }
        if calendar.get(date) is None:
            calendar[date] = [event]
        else:
            calendar[date].insert(0, event)
            # calendar[date].append(event)
        return True
    return False


def command_show(calendar):
    r"""
    (dict) -> str
    Returns the list of events for calendar sorted in decreasing date order
    and increasing time order within the date
    as a string, see examples below for a sample formatting
    calendar: the database of events

    Example:
    >>> calendar = {}
    >>> command_add("2018-01-15", 11, 13, "Eye doctor", calendar)
    True
    >>> command_add("2018-01-15", 8, 9, "lunch with sid", calendar)
    True
    >>> command_add("2018-02-10", 12, 23, "Change oil in blue car", calendar)
    True
    >>> command_add("2018-02-10", 20, 22, "dinner with Jane", calendar)
    True
    >>> command_add("2017-12-22", 5, 8, "Fix tree near front walkway", calendar)
    True
    >>> command_add("2017-12-22", 13, 15, "Get salad stuff", calendar)
    True
    >>> command_add("2018-05-06", 19, 23, "Sid's birthday", calendar)
    True
    >>> command_show(calendar)
    "\n2018-05-06 : \n    start : 19:00,\n    end : 23:00,\n    title : Sid's birthday\n2018-02-10 : \n    start : 12:00,\n    end : 23:00,\n    title : Change oil in blue car\n\n    start : 20:00,\n    end : 22:00,\n    title : dinner with Jane\n2018-01-15 : \n    start : 08:00,\n    end : 09:00,\n    title : lunch with sid\n\n    start : 11:00,\n    end : 13:00,\n    title : Eye doctor\n2017-12-22 : \n    start : 05:00,\n    end : 08:00,\n    title : Fix tree near front walkway\n\n    start : 13:00,\n    end : 15:00,\n    title : Get salad stuff"
    """
    cal = {k: v for k, v in sorted(calendar.items(), key=lambda item: (
        item[0][0:4], item[0][5:7], item[0][8:]))}
    cal = {k: v for k, v in sorted(
        calendar.items(), key=lambda item: item[1][0]["start"])}

    cal_str = "\n"
    for key in cal.keys():
        cal_str += f"{key} : \n"

        for event in cal[key]:
            for sub_key in event.keys():
                if sub_key in ("start", "end"):
                    cal_str += f"    {sub_key} : {str(event[sub_key]).zfill(2)}:00,\n"
                else:
                    cal_str += f"    {sub_key} : {event[sub_key]}\n"
                    if len(cal[key]) > 1:
                        cal_str += "\n"
        cal_str = cal_str.rstrip()
        cal_str += "\n"
    return cal_str.rstrip()


def command_delete(date, start_time, calendar):
    """
    (str, int, dict) -> str
    Delete the entry at calendar[date][start_time]
    If calendar[date] is empty, remove this date from the calendar.
    If the entry does not exist, do nothing
    date: A string date formatted as "YYYY-MM-DD"
    start_time: An integer indicating the start of the event in calendar[date] to delete
    calendar: The calendar database
    return: a string indicating any errors, True for no errors

    Example:


    >>> calendar = {}
    >>> command_add("2018-02-28", 11, 12, "Python class", calendar)
    True
    >>> calendar == {"2018-02-28": [{"start": 11, "end": 12, "title": "Python class"}]}
    True
    >>> command_add("2018-03-11", 14, 16, "CSCA08 test 2", calendar)
    True
    >>> calendar == {"2018-03-11": [{"start": 14, "end": 16, "title": "CSCA08 test 2"}], \
    "2018-02-28": [{"start": 11, "end": 12, "title": "Python class"}]}
    True
    >>> calendar == {"2018-03-11": [{"start": 14, "end": 16, "title": "CSCA08 test 2"}], \
    "2018-02-28": [{"start": 11, "end": 12, "title": "Python class"}]}
    True
    >>> command_add("2018-03-13", 13, 13, "Have fun", calendar)
    True
    >>> calendar == {"2018-03-13": [{"start": 13, "end": 13, "title": "Have fun"}], "2018-03-11": \
    [{"start": 14, "end": 16, "title": "CSCA08 test 2"}], "2018-02-28": [{"start": 11, "end": 12, \
    "title": "Python class"}]}
    True
    >>> command_delete("2015-01-01", 1, calendar)
    '2015-01-01 is not a date in the calendar'
    >>> command_delete("2018-03-11", 3, calendar)
    'There is no event with start time of 3 on date 2018-03-11 in the calendar'
    >>> command_delete("2018-02-28", 11, calendar)
    True
    >>> calendar == {"2018-03-13": [{"start": 13, "end": 13, "title": "Have fun"}], "2018-03-11": [{"start": 14, "end": 16, "title": "CSCA08 test 2"}]}
    True
    >>> command_delete("2018-03-11", 14, calendar)
    True
    >>> calendar == {"2018-03-13": [{"start": 13, "end": 13, "title": "Have fun"}]}
    True
    >>> command_delete("2018-03-13", 13, calendar)
    True
    >>> calendar == {}
    True

    """
    if date in calendar.keys():
        ind = None
        for i, ev in enumerate(calendar[date]):
            if ev["start"] == start_time:
                ind = i
                break
        if not ind == None:
            calendar[date].pop(ind)
        else:
            return f"There is no event with start time of {start_time} on date {date} in the calendar"

        if calendar[date] == []:
            del calendar[date]

        return True
    else:
        return f"{date} is not a date in the calendar"


# -----------------------------------------------------------------------------
# Functions dealing with calendar persistence
# -----------------------------------------------------------------------------


"""
The calendar is read and written to disk.

...

date_i is "YYYY-MM-DD"'
description can not have tab or new line characters in them.

"""


def save_calendar(calendar):
    """
    (dict) -> bool
    Save calendar to 'calendar.txt', overwriting it if it already exists. The calendar events do not have
    to be saved in any particular order

    The format of calendar.txt is the following:

    date_1:start_time_1-end_time_1 description_1\tstart_time_2-end_time_2 description_2\t...\tstart_time_n-end_time_n description_n\n
    date_2:start_time_1-end_time_1 description_1\tstart_time_2-end_time_2 description_2\t...\tstart_time_n-end_time_n description_n\n
    date_n:start_time_1-end_time_1 description_1\tstart_time_2-end_time_2 description_2\t...\tstart_time_n-end_time_n description_n\n

    Example: The following calendar...



        2018-03-13 :
                start : 13:00,
                end : 13:00,
                title : Have fun
        2018-03-11 :
                start : 10:00,
                end : 12:00,
                title : Another event on this date

                start : 14:00,
                end : 16:00,
                title : CSCA08 test 2
        2018-02-28 :
                start : 8:00,
                end : 9:00,
                title : Linux class

                start : 11:00,
                end : 12:00,
                title : Python class

     appears in calendar.txt as ...

    2018-03-13:13-13 Have fun
    2018-03-11:10-12 Another event on this date    14-16 CSCA08 test 2
    2018-02-28:08-09 Linux class    11-12 Python class

    calendar: dictionary containing a calendar
    return: True if the calendar was saved.
    """
    with open("calendar.txt", "w") as fl:
        ls_str = ""
        keys = list(calendar.keys())[::-1]
        for key in keys:
            ls_str += f"{key}:"
            for ev in calendar[key]:
                ls_str += f"{str(ev['start']).zfill(2)}-{str(ev['end']).zfill(2)} {ev['title']}\t"
            ls_str = ls_str[:-1]
            ls_str += "\n"
        fl.write(ls_str)
    return True


def load_calendar():
    '''
    () -> dict
    Load calendar from 'calendar.txt'. If calendar.txt does not exist,
    create and return an empty calendar. For the format of calendar.txt
    see save_calendar() above.

    return: calendar.

    '''
    calendar = {}
    basedir = os.path.abspath(os.path.dirname(__file__))
    full_path = os.path.join(basedir, 'calendar.txt')
    if os.path.exists(full_path):
        with open("calendar.txt", "r") as fl:
            lines = fl.readlines()
            for line in lines:
                key, data = line.split(":")
                data_arr = data.split("\t")
                calendar[key] = []
                for datum in data_arr:
                    times, *title = datum.split()
                    st, en = times.split("-")
                    full_title = " ".join(title)
                    event = {
                        "start": int(st),
                        "end": int(en),
                        "title": full_title
                    }
                    calendar[key].append(event)
        return calendar
    else:
        return calendar


# -----------------------------------------------------------------------------
# Functions dealing with parsing commands
# -----------------------------------------------------------------------------


def is_command(command):
    '''
    (str) -> bool
    Return whether command is a valid command
    Valid commands are any of the options below
    "add", "delete", "quit", "help", "show"
    You are not allowed to use regular expressions in your implementation.
    command: string
    return: True if command is one of ["add", "delete", "quit", "help", "show"]
    false otherwise
    Example:
    >>> is_command("add")
    True
    >>> is_command(" add ")
    False
    >>> is_command("List")
    False

    '''

    return command in ["add", "delete", "quit", "help", "show"]


def is_calendar_date(date):
    '''
    (str) -> bool
    Return whether date looks like a calendar date
    date: a string
    return: True, if date has the form "YYYY-MM-DD" and False otherwise
    You are not allowed to use regular expressions in your implementation.
    Also you are not allowed to use isdigit() or the datetime module functions.

    Example:

    >>> is_calendar_date("15-10-10") # invalid year
    False
    >>> is_calendar_date("2015-10-15")
    True
    >>> is_calendar_date("2015-5-10") # invalid month
    False
    >>> is_calendar_date("2015-15-10") # invalid month
    False
    >>> is_calendar_date("2015-05-10")
    True
    >>> is_calendar_date("2015-10-55") # invalid day
    False
    >>> is_calendar_date("2015-55") # invalid format
    False
    >>> is_calendar_date("jane-is-gg") # YYYY, MM, DD should all be digits
    False

    Note: This does not validate days of the month, or leap year dates.

    # True even though April has only 30 days.
    >>> is_calendar_date("2015-04-31")
    True

    '''
    # Algorithm: Check length, then pull pieces apart and check them. Use only
    # basic string
    # manipulation, comparisons, and type conversion. Please do not use any
    # powerful date functions
    # you may find in python libraries.
    # 2015-10-12
    # 0123456789

    # YOUR CODE GOES HERE
    year, mon, dat = date.split("-")
    if not len(year) == 4 or not is_natural_number(year):
        return False
    elif not len(mon) == 2 or not is_natural_number(mon) or not int(mon) in range(1, 13):
        return False
    elif not len(dat) == 2 or not is_natural_number(dat) or not int(dat) in range(1, 32):
        return False
    return True


def is_natural_number(str):
    '''
    (str) -> bool
    Return whether str is a string representation of a natural number,
    that is, 0,1,2,3,...,23,24,...1023, 1024, ...
    In CS, 0 is a natural number
    param str: string
    Do not use string functions
    return: True if num is a string consisting of only digits. False otherwise.
    Example:

    >>> is_natural_number("0")
    True
    >>> is_natural_number("05")
    True
    >>> is_natural_number("2015")
    True
    >>> is_natural_number("9 3")
    False
    >>> is_natural_number("sid")
    False
    >>> is_natural_number("2,192,134")
    False

    '''
    # Algorithm:
    # Check that the string has length > 0
    # Check that all characters are in ["0123456789"]

    return len(str) > 0 and all([i in "0123456789" for i in str])


def parse_command(line):
    '''
    (str) -> list
    Parse command and arguments from the line. Return a list
    [command, arg1, arg2, ...]
    Return ["error", ERROR_DETAILS] if the command is not valid.
    Return ["help"] otherwise.
    The valid commands are

    1) add DATE START_TIME END_TIME DETAILS
    2) show
    3) delete DATE START_TIME
    4) quit
    5) help

    line: a string command
    return: A list consiting of [command, arg1, arg2, ...].
    Return ["error", ERROR_DETAILS], if line can not be parsed.
    ERROR_DETAILS displays how to use the

    Example:
    >>> parse_command("add 2015-10-21 10 11 budget meeting")
    ['add', '2015-10-21', 10, 11, 'budget meeting']
    >>> parse_command("")
    ['help']
    >>> parse_command("not a command")
    ['help']
    >>> parse_command("help")
    ['help']
    >>> parse_command("add")
    ['error', 'add DATE START_TIME END_TIME DETAILS']
    >>> parse_command("add 2015-10-22")
    ['error', 'add DATE START_TIME END_TIME DETAILS']
    >>> parse_command("add 2015-10-22 7 7 Tims with Sally.")
    ['add', '2015-10-22', 7, 7, 'Tims with Sally.']
    >>> parse_command("add 2015-10-35 7 7 Tims with Sally.")
    ['error', 'not a valid calendar date']
    >>> parse_command("show")
    ['show']
    >>> parse_command("show calendar")
    ['error', 'show']
    >>> parse_command("delete")
    ['error', 'delete DATE START_TIME']
    >>> parse_command("delete 15-10-22")
    ['error', 'delete DATE START_TIME']
    >>> parse_command("delete 15-10-22 11")
    ['error', 'not a valid calendar date']
    >>> parse_command("delete 2015-10-22 3,14")
    ['error', 'not a valid event start time']
    >>> parse_command("delete 2015-10-22 14")
    ['delete', '2015-10-22', 14]
    >>> parse_command("delete 2015-10-22 14 hello")
    ['error', 'delete DATE START_TIME']
    >>> parse_command("quit")
    ['quit']

    '''
    # HINT: You can first split, then join back the parts of
    # the final argument.
    coms = line.split()
    if coms[0] == "add":
        if not len(coms) >= 5:
            return ['error', 'add DATE START_TIME END_TIME DETAILS']
        elif not is_calendar_date(coms[1]):
            return ['error', 'not a valid calendar date']
        new_coms = coms[:2]
        new_coms.append(int(coms[2]))
        new_coms.append(int(coms[3]))
        new_coms.append(" ".join(coms[4:]))
        return new_coms
    if coms[0] == "show":
        if not len(coms) == 1:
            return ['error', 'show']
        return ['show']
    if coms[0] == "quit":
        return ['quit']

    if coms[0] == 'delete':
        if not len(coms) == 3:
            return ['error', 'delete DATE START_TIME']
        elif not is_calendar_date(coms[1]):
            return ['error', 'not a valid calendar date']
        elif not is_natural_number(coms[2]):
            return ['error', 'not a valid event start time']
        new_coms = coms[:2]
        new_coms.append(int(coms[-1]))
        return new_coms

    return ['help']


def user_interface():
    """
    Load calendar.txt and then interact with the user. The user interface
operates as follows, the text after command: is the command entered by the
user.
calendar loaded
command: add 2017-10-21 9 10 budget meeting
added
command: add 2017-10-22 6 7 go to the gym
added
command: add 2017-10-23 5 6 go to the gym
added
command: add 2017-11-01 15 16 Make sure to submit csc108 assignment 2
added
command: add 2017-12-02 16 17 Make sure to submit csc108 assignment 3
added
command: add 2017-11-06 8 10 Term test 2
added
command: add 2017-10-29 7 8 Get salad stuff,lettuce, red peppers, green peppers
added
command: add 2017-11-06 19 22 Sid's birthday
added
command: show


    2017-12-02 :
        start : 16:00,
        end : 17:00,
        title: Make sure to submit csc108 assignment 3
    2017-11-06 :
        start : 8:00,
        end : 10:00,
        title: Term test 2

        start : 19:00,
        end : 22:00,
        title: Sid's birthday
    2017-11-01 :
        start : 15:00,
        end : 16:00,
        title: Make sure to submit csc108 assignment 2
    2017-10-29 :
        start : 7:00,
        end : 8:00,
        title: Get salad stuff, lettuce, red peppers, green peppers
    2017-10-23 :
        start : 5:00,
        end : 6:00,
        title: go to the gym
    2017-10-22 :
        start : 6:00,
        end : 7:00,
        title : go to the gym
    2017-10-21 :
        start : 9:00,
        end : 10:00,
        title : budget meeting


command: delete 2017-10-29 7
deleted
command: delete 2015-12-03 9
2015-12-03 is not a date in the calendar
command: delete 2017-12-02 16
deleted
command: show

    2017-11-06 :
        start : 8:00,
        end : 10:00,
        title: Term test 2

        start : 19:00,
        end : 22:00,
        title: Sid's birthday
    2017-11-01 :
        start : 15:00,
        end : 16:00,
        title: Make sure to submit csc108 assignment 2
    2017-10-23 :
        start : 5:00,
        end : 6:00,
        title: go to the gym
    2017-10-22 :
        start : 6:00,
        end : 7:00,
        title : go to the gym
    2017-10-21 :
        start : 9:00,
        end : 10:00,
        title : budget meeting
command: quit
calendar saved

:return: None
    """
    calendar = load_calendar()
    print("calendar loaded")
    while True:
        line = input()
        comms = parse_command(line)
        print(comms)
        if comms[0] == 'help':
            print(command_help())
        if comms[0] == 'add':
            resp = command_add(comms[1], comms[2],
                               comms[3], comms[4], calendar)
            if resp:
                print("added")
        if comms[0] == 'delete':
            resp = command_delete(comms[1], comms[2], calendar)
            if resp == True:
                print("deleted")
            else:
                print(resp)
        if comms[0] == 'show':
            print(command_show(calendar))
        if comms[0] == 'quit':
            break
    save_calendar(calendar)
    print("calendar saved")


if __name__ == "__main__":
    import doctest
    doctest.testmod()
    user_interface()

# user_interface()
