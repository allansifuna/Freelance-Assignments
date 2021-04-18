import unittest
import os
import inspect

try:
    import Calendar

except Exception:
    pass

FAILURE_MESSAGE = '''
When we called {}, we expected this return value:
{}
but your code returned this:
{}'''

help = """
Help for Calendar. The calendar commands are

add DATE DETAILS               add the event DETAILS at the specified DATE
show                           show all events in the claendar
delete DATE NUMBER             delete the specified event (by NUMBER) from
                               the calendar
quit                           quit this program
help                           display this help message

Examples: user data follows command:

command: add 2017-10-12 dinner with jane
added

command: show
    2017-10-12:
        0: Eye doctor
        1: lunch with sid
        2: dinner with jane
    2017-10-29:
        0: Change oil in blue car
        1: Fix tree near front walkway
        2: Get salad stuff, leuttice, red peppers, green peppers
    2017-11-06:
        0: Sid's birthday

command: delete 2017-10-29 2
deleted

A DATE has the form YYYY-MM-DD, for example
2017-12-21
2016-01-02

Event DETAILS consist of alphabetic characters,
no tabs or newlines allowed.
"""


class TestCalendar(unittest.TestCase):

    def test_01_help(self):
        call = "Calendar.help()"
        expected = ""
        returned = Calendar.command_help()
        returned = "".join(returned.split())
        msg = FAILURE_MESSAGE.format(call, expected, returned)
        self.assertNotEqual(expected, returned, msg)

    def test_02_command_add(self):
        date = '2019-11-25'
        start_time = 13
        end_time = 14

        title = 'MAT157 Help'
        calendar = {}
        call = "Calendar.command_add\
                ('{}, {}, {}')".format(date, start_time, end_time, title, str(calendar))
        expected = {date: [{"start": start_time, "end": end_time, "title": title}]}
        result = Calendar.command_add(date, start_time, end_time, title, calendar)
        returned = calendar
        msg = FAILURE_MESSAGE.format(call, expected, returned)
        self.assertEqual(expected, returned, msg)

    def test_03_command_add(self):
        date = '2019-10-31'
        title = 'MAT157 Tutorial'
        start_time = 8
        end_time = 10

        calendar = {}
        call = "Calendar.command_add\
                    ('{}, {}, {}')".format(date, start_time, end_time, title, str(calendar))
        expected = True
        returned = Calendar.command_add(date, start_time, end_time, title, calendar)
        msg = FAILURE_MESSAGE.format(call, expected, returned)
        self.assertEqual(expected, returned, msg)

    def test_04_command_add(self):
        date = '2019-07-18'
        title = 'MAT157 Tutorial'
        start_time = 14
        end_time = 15

        calendar = {'2019-07-18': [{"start": 16, "end": 18, "title": "Gym"}]}

        call = "Calendar.command_add\
                    ('{}, {}, {}')".format(date, start_time, end_time, title, str(calendar))

        expected = {
            '2019-07-18': [{"start": 14, "end": 15, "title": "MAT157 Tutorial"}, {"start": 16, "end": 18, "title": "Gym"}]}
        result = Calendar.command_add(date, start_time, end_time, title, calendar)
        returned = calendar
        msg = FAILURE_MESSAGE.format(call, expected, returned)
        self.assertEqual(expected, returned, msg)

    def test_05_command_add(self):
        date = '2017-03-01'
        title = 'Python class'
        start_time = 19
        end_time = 18
        calendar = {}

        call = "Calendar.command_add\
                    ('{}, {}, {}')".format(date, start_time, end_time, title, str(calendar))
        expected = False
        result = Calendar.command_add(date, start_time, end_time, title, calendar)
        returned = calendar
        msg = FAILURE_MESSAGE.format(call, expected, returned)
        self.assertEqual(expected, result, msg)

    def test_06_command_add(self):
        date = '2019-01-22'
        title = 'Python Tutorial'
        start_time = 9
        end_time = 12

        calendar = {
            '2019-07-18': [{"start": 14, "end": 15, "title": "MAT157 Tutorial"}, {"start": 16, "end": 18, "title": "Gym"}]}

        call = "Calendar.command_add\
                    ('{}, {}, {}')".format(date, start_time, end_time, title, str(calendar))

        expected = {
            '2019-07-18': [{"start": 14, "end": 15, "title": "MAT157 Tutorial"}, {"start": 16, "end": 18, "title": "Gym"}],
            date: [{"start": start_time, "end": end_time, "title": title}]}

        result = Calendar.command_add(date, start_time, end_time, title, calendar)
        returned = calendar
        msg = FAILURE_MESSAGE.format(call, expected, returned)
        self.assertEqual(expected, returned, msg)

    def test_07_command_add(self):
        date = '2020-09-02'

        title = 'Python Tutorial'
        start_time = 9
        end_time = 12
        calendar = {
            '2019-07-18': [{"start": 14, "end": 15, "title": "MAT157 Tutorial"}, {"start": 16, "end": 18, "title": "Gym"}]}

        call = "Calendar.command_add\
                    ('{}, {}, {}')".format(date, start_time, end_time, title, str(calendar))

        expected = {date: [{"start": start_time, "end": end_time, "title": title}],
                    '2019-07-18': [{"start": 14, "end": 15, "title": "MAT157 Tutorial"},
                                   {"start": 16, "end": 18, "title": "Gym"}]}

        result = Calendar.command_add(date, start_time, end_time, title, calendar)
        returned = calendar
        msg = FAILURE_MESSAGE.format(call, expected, returned)
        self.assertEqual(expected, returned, msg)

    def test_08_command_add(self):
        date = '2017-03-41'
        title = 'Python class'
        start_time = 19
        end_time = 18

        calendar = {}

        call = "Calendar.command_add\
                    ('{}, {}, {}')".format(date, start_time, end_time, title, str(calendar))
        expected = False
        result = Calendar.command_add(date, start_time, end_time, title, calendar)
        returned = calendar
        msg = FAILURE_MESSAGE.format(call, expected, returned)
        self.assertEqual(expected, result, msg)

    def test_09_command_add(self):
        date = '2017-03-11'
        title = 'Python class'
        start_time = 29
        end_time = 38
        calendar = {}


        call = "Calendar.command_add\
                    ('{}, {}, {}')".format(date, start_time, end_time, title, str(calendar))
        expected = False
        result = Calendar.command_add(date, start_time, end_time, title, calendar)
        returned = calendar
        msg = FAILURE_MESSAGE.format(call, expected, result)
        self.assertEqual(expected, result, msg)

    def test_10_command_add(self):
        date = '2017-03-11'
        title = 'Python class'
        start_time = -5
        end_time = -1

        calendar = {}

        call = "Calendar.command_add\
                    ('{}, {}, {}')".format(date, start_time, end_time, title, str(calendar))
        expected = False
        result = Calendar.command_add(date, start_time, end_time, title, calendar)
        returned = calendar
        msg = FAILURE_MESSAGE.format(call, expected, result)
        self.assertEqual(expected, result, msg)

    def test_11_command_show(self):
        calendar = {
            '2019-07-18': [{"start": 14, "end": 15, "title": "MAT157 Tutorial"}, {"start": 16, "end": 18, "title": "Gym"}]}


        expected = "\n2019-07-18 : \n    start : 14:00,\n    end : 15:00,\n    title : MAT157 Tutorial\n\n    start : 16:00,\n    end : 18:00,\n    title : Gym"

        call = "Calendar.command_show\
                    ('{}')".format(str(calendar))
        returned = Calendar.command_show(calendar)
        msg = FAILURE_MESSAGE.format(call, expected, returned)
        self.assertEqual(expected, returned, msg)

    def test_12_command_show(self):
        calendar = {}
        expected = ""
        call = "Calendar.command_show\
                ('{}')".format(str(calendar))
        returned = Calendar.command_show(calendar)
        msg = FAILURE_MESSAGE.format(call, expected, returned)
        self.assertEqual(expected, returned, msg)

    def test_13_command_show(self):
        calendar = {
            '2019-07-18': [{"start": 14, "end": 15, "title": "MAT157 Tutorial"}, {"start": 16, "end": 18, "title": "Gym"}],
            '2019-02-10': [{"start": 17, "end": 20, "title": "python assignment"}]}


        expected = "\n2019-07-18 : \n    start : 14:00,\n    end : 15:00,\n    title : MAT157 Tutorial\n\n    start : 16:00,\n    end : 18:00,\n    title : Gym\n2019-02-10 : \n    start : 17:00,\n    end : 20:00,\n    title : python assignment"
        call = "Calendar.command_show\
                    ('{}')".format(str(calendar))
        returned = Calendar.command_show(calendar)
        msg = FAILURE_MESSAGE.format(call, expected, returned)
        self.assertEqual(expected, returned, msg)

    def test_14_command_show(self):
        calendar = {'2020-05-19': [{"start": 6, "end": 8, "title": "wake up for school"}],
                    '2019-07-18': [{"start": 14, "end": 15, "title": "MAT157 Tutorial"},
                                   {"start": 16, "end": 18, "title": "Gym"}]}


        expected = "\n2020-05-19 : \n    start : 06:00,\n    end : 08:00,\n    title : wake up for school\n2019-07-18 : \n    start : 14:00,\n    end : 15:00,\n    title : MAT157 Tutorial\n\n    start : 16:00,\n    end : 18:00,\n    title : Gym"
        call = "Calendar.command_show\
                    ('{}')".format(str(calendar))
        returned = Calendar.command_show(calendar)
        msg = FAILURE_MESSAGE.format(call, expected, returned)
        self.assertEqual(expected, returned, msg)

    def test_15_command_delete(self):
        calendar = {'2020-05-19': [{"start": 6, "end": 8, "title": "wake up for school"}],
                    '2019-07-18': [{"start": 14, "end": 15, "title": "MAT157 Tutorial"},
                                   {"start": 16, "end": 18, "title": "Gym"}]}

        expected = {'2020-05-19': [{"start": 6, "end": 8, "title": "wake up for school"}],
                    '2019-07-18': [{"start": 14, "end": 15, "title": "MAT157 Tutorial"},
                                   {"start": 16, "end": 18, "title": "Gym"}]}

        date = '2020-05-19'
        entry = 7
        call = "Calendar.command_delete\
                    ('{}, {}, {}')".format(date, entry, str(calendar))
        result = Calendar.command_delete(date, entry, calendar)
        returned = calendar
        msg = FAILURE_MESSAGE.format(call, expected, returned)
        self.assertEqual(expected, returned, msg)

    def test_16_command_delete(self):
        calendar = {'2020-05-19': [{"start": 6, "end": 8, "title": "wake up for school"}],
                    '2019-07-18': [{"start": 14, "end": 15, "title": "MAT157 Tutorial"},
                                   {"start": 16, "end": 18, "title": "Gym"}]}


        date = '2020-05-19'
        entry = 8
        expected = "There is no event with start time of {} on date {} in the calendar".format(entry, date)
        call = "Calendar.command_delete\
                    ('{}, {}, {}')".format(date, entry, str(calendar))
        result = Calendar.command_delete(date, entry, calendar)
        returned = calendar
        msg = FAILURE_MESSAGE.format(call, expected, result)
        self.assertEqual(expected, result, msg)

    def test_17_command_delete(self):
        calendar = {'2020-05-19': [{"start": 6, "end": 8, "title": "wake up for school"}],
                    '2019-07-18': [{"start": 14, "end": 15, "title": "MAT157 Tutorial"},
                                   {"start": 16, "end": 18, "title": "Gym"}]}

        expected = {'2020-05-19': [{"start": 6, "end": 8, "title": "wake up for school"}],
                    '2019-07-18': [{"start": 16, "end": 18, "title": "Gym"}]}

        date = '2019-07-18'
        entry = 14
        call = "Calendar.command_delete\
                    ('{}, {}, {}')".format(date, entry, str(calendar))
        result = Calendar.command_delete(date, entry, calendar)
        returned = calendar
        msg = FAILURE_MESSAGE.format(call, expected, returned)
        self.assertEqual(expected, returned, msg)

    def test_18_command_delete(self):
        calendar = {'2020-05-19': [{"start": 6, "end": 8, "title": "wake up for school"}],
                    '2019-07-18': [{"start": 14, "end": 15, "title": "MAT157 Tutorial"},
                                   {"start": 16, "end": 18, "title": "Gym"}]}

        expected = True

        date = '2019-07-18'
        entry = 16
        call = "Calendar.command_delete\
                    ('{}, {}, {}')".format(date, entry, str(calendar))
        result = Calendar.command_delete(date, entry, calendar)
        returned = calendar
        msg = FAILURE_MESSAGE.format(call, expected, result)
        self.assertEqual(expected, result, msg)

    def test_19_command_delete(self):
        calendar = {'2020-05-19': [{"start": 6, "end": 8, "title": "wake up for school"}],
                    '2019-07-18': [{"start": 14, "end": 15, "title": "MAT157 Tutorial"},
                                   {"start": 16, "end": 18, "title": "Gym"}]}


        date = '2021-01-14'
        entry = 7
        expected = "{} is not a date in the calendar".format(date)
        call = "Calendar.command_delete\
                    ('{}, {}, {}')".format(date, entry, str(calendar))
        result = Calendar.command_delete(date, entry, calendar)
        returned = calendar
        msg = FAILURE_MESSAGE.format(call, expected, result)
        self.assertEqual(expected, result, msg)

    def test_20_command_delete(self):
        calendar = {'2020-05-19': [{"start": 6, "end": 8, "title": "wake up for school"}],
                    '2019-07-18': [{"start": 14, "end": 15, "title": "MAT157 Tutorial"},
                                   {"start": 16, "end": 18, "title": "Gym"}]}


        date = '2022-02-29'
        entry = 7
        expected = "{} is not a date in the calendar".format(date)
        call = "Calendar.command_delete\
                    ('{}, {}, {}')".format(date, entry, str(calendar))
        result = Calendar.command_delete(date, entry, calendar)
        returned = calendar
        msg = FAILURE_MESSAGE.format(call, expected, result)
        self.assertEqual(expected, result, msg)

    def test_21_save_calendar(self):
        calendar = {}
        expected = True
        call = "Calendar.save_calendar\
                ('{}')".format(str(calendar))
        returned = Calendar.save_calendar(calendar)
        msg = FAILURE_MESSAGE.format(call, expected, returned)
        self.assertEqual(expected, returned, msg)

    def test_22_save_calendar(self):
        calendar = {}
        expected = ""
        call = "Calendar.save_calendar\
                ('{}')".format(str(calendar))
        result = Calendar.save_calendar(calendar)
        returned = ""
        if os.path.exists("calendar.txt"):
            f = open("calendar.txt")
            for line in f:
                returned += line
            f.close()
        msg = FAILURE_MESSAGE.format(call, expected, returned)
        self.assertEqual(expected, returned, msg)

    def test_23_save_calendar(self):
        calendar = {
            '2019-07-18': [{"start": 14, "end": 15, "title": "MAT157 Tutorial"}, {"start": 16, "end": 18, "title": "Gym"}],
            '2019-02-10': [{"start": 17, "end": 20, "title": "python assignment"}]}

        expected = True
        call = "Calendar.save_calendar\
                ('{}')".format(str(calendar))
        returned = Calendar.save_calendar(calendar)
        msg = FAILURE_MESSAGE.format(call, expected, returned)
        self.assertEqual(expected, returned, msg)

    def test_24_save_calendar(self):
        calendar = {
            '2019-07-18': [{"start": 14, "end": 15, "title": "MAT157 Tutorial"}, {"start": 16, "end": 18, "title": "Gym"}],
            '2019-02-10': [{"start": 17, "end": 20, "title": "python assignment"}]}

        expected_list = ['2019-07-18:14-15 MAT157 Tutorial\t16-18 Gym\n', '2019-02-10:17-20 python assignment\n']
        call = "Calendar.save_calendar\
                ('{}')".format(str(calendar))
        result = Calendar.save_calendar(calendar)
        returned_list = []
        if os.path.exists("calendar.txt"):
            f = open("calendar.txt")
            returned_list = [x for x in f]
        f.close()
        expected = True
        returned = True
        print(returned_list)
        for s in returned_list:
            returned = returned and (s in expected_list)
        msg = FAILURE_MESSAGE.format(call, expected_list, returned_list)
        self.assertEqual(expected, returned, msg)

    def test_25_save_calendar(self):
        calendar = {'2020-09-02': [{"start": 7, "end": 9, "title": "Go to school"}],
                    '2019-07-18': [{"start": 14, "end": 15, "title": "MAT157 Tutorial"},
                                   {"start": 16, "end": 18, "title": "Gym"}],
                    '2019-02-10': [{"start": 17, "end": 20, "title": "python assignment"}]}


        expected_list = ['2020-09-02:07-09 Go to school\n', '2019-07-18:14-15 MAT157 Tutorial\t16-18 Gym\n',
                         '2019-02-10:17-20 python assignment\n']
        call = "Calendar.save_calendar\
                    ('{}')".format(str(calendar))
        result = Calendar.save_calendar(calendar)
        returned_list = []
        if os.path.exists("calendar.txt"):
            f = open("calendar.txt")
            returned_list = [x for x in f]
        f.close()
        expected = True
        returned = True
        for s in returned_list:
            returned = returned and (s in expected_list)
        msg = FAILURE_MESSAGE.format(call, expected_list, returned_list)
        self.assertEqual(expected, returned, msg)

    def test_26_save_calendar(self):
        calendar = {
            '2019-07-18': [{"start": 14, "end": 15, "title": "MAT157 Tutorial"}, {"start": 16, "end": 18, "title": "Gym"}],
            '2019-02-10': [{"start": 17, "end": 20, "title": "python assignment"},
                           {"start": 19, "end": 21, "title": "take study break"},
                           {"start": 20, "end": 22, "title": "finish reading"}]}


        expected_list = ['2019-07-18:14-15 MAT157 Tutorial\t16-18 Gym\n',
                         '2019-02-10:17-20 python assignment\t19-21 take study break\t20-22 finish reading\n']

        call = "Calendar.save_calendar\
                    ('{}')".format(str(calendar))
        result = Calendar.save_calendar(calendar)
        returned_list = []
        if os.path.exists("calendar.txt"):
            f = open("calendar.txt")
            returned_list = [x for x in f]
        f.close()
        expected = True
        returned = True
        for s in returned_list:
            returned = returned and (s in expected_list)
        msg = FAILURE_MESSAGE.format(call, expected_list, returned_list)
        self.assertEqual(expected, returned, msg)

    def test_27_load_calendar(self):
        expected = {'2019-07-18': [{"start": 14, "end": 15, "title": "MAT157 Tutorial"},
                                   {"start": 16, "end": 18, "title": "Gym"}],
                    '2019-02-10': [{"start": 17, "end": 20, "title": "python assignment"}]}


        cal_data = ['2019-07-18:14-15 MAT157 Tutorial\t16-18 Gym\n',
                    '2019-02-10:17-20 python assignment\n']
        f = open("calendar.txt", "w")
        for s in cal_data:
            f.write(s)
        f.close()
        call = "Calendar.load_calendar()"
        returned = Calendar.load_calendar()
        msg = FAILURE_MESSAGE.format(call, expected, returned)
        self.assertEqual(expected, returned, msg)

    def test_28_load_calendar(self):
        expected = {
            '2019-07-18': [{"start": 14, "end": 15, "title": "MAT157 Tutorial"}, {"start": 16, "end": 18, "title": "Gym"}],
            '2019-02-10': [{"start": 17, "end": 20, "title": "python assignment"},
                           {"start": 19, "end": 21, "title": "take study break"},
                           {"start": 20, "end": 22, "title": "finish reading"}]}

        calendar = {
            '2019-07-18': [{"start": 14, "end": 15, "title": "MAT157 Tutorial"}, {"start": 16, "end": 18, "title": "Gym"}],
            '2019-02-10': [{"start": 17, "end": 20, "title": "python assignment"},
                           {"start": 19, "end": 21, "title": "take study break"},
                           {"start": 20, "end": 22, "title": "finish reading"}]}


        result = Calendar.save_calendar(calendar)
        call = "Calendar.load_calendar()"
        returned = Calendar.load_calendar()
        msg = FAILURE_MESSAGE.format(call, expected, returned)
        self.assertEqual(expected, returned, msg)

    def test_29_is_command(self):
        expected = True
        command = "add"
        result = Calendar.is_command(command)
        call = "Calendar.is_command\
                ('{}')".format(str(command))
        returned = Calendar.is_command(command)
        msg = FAILURE_MESSAGE.format(call, expected, returned)
        self.assertEqual(returned, expected, msg)

    def test_30_is_command(self):
        expected = False
        command = "deLete"
        result = Calendar.is_command(command)
        call = "Calendar.is_command\
                ('{}')".format(str(command))
        returned = Calendar.is_command(command)
        msg = FAILURE_MESSAGE.format(call, expected, returned)
        self.assertEqual(expected, returned, msg)

    def test_31_is_command(self):
        expected = False
        command = "QUIT"
        result = Calendar.is_command(command)
        call = "Calendar.is_command\
                ('{}')".format(str(command))
        returned = Calendar.is_command(command)
        msg = FAILURE_MESSAGE.format(call, expected, returned)
        self.assertEqual(expected, returned, msg)

    def test_32_is_command(self):
        expected = False
        command = "  show "
        result = Calendar.is_command(command)
        call = "Calendar.is_command\
                ('{}')".format(str(command))
        returned = Calendar.is_command(command)
        msg = FAILURE_MESSAGE.format(call, expected, returned)
        self.assertEqual(expected, returned, msg)

    def test_33_is_command(self):
        expected = False
        command = "hepl"
        result = Calendar.is_command(command)
        call = "Calendar.is_command\
                ('{}')".format(str(command))
        returned = Calendar.is_command(command)
        msg = FAILURE_MESSAGE.format(call, expected, returned)
        self.assertEqual(expected, returned, msg)

    def test_34_is_calendar_date(self):
        src = ''.join(inspect.getsourcelines(Calendar.is_calendar_date)[0])
        returned = "isnumeric()" in src
        call = "checked if is_calendar_date calls isnumeric()"
        expected = False
        msg = FAILURE_MESSAGE.format(call, expected, returned)
        self.assertEqual(expected, returned, msg)

    def test_35_is_calendar_date(self):
        expected = True
        src = ''.join(inspect.getsourcelines(Calendar.is_calendar_date)[0])
        used_is_numeric = "isnumeric()" in src
        date = "2017-03-12"
        result = Calendar.is_calendar_date(date)
        result = result and not used_is_numeric
        call = "Calendar.is_calendar_date\
                ('{}')".format(str(date))
        returned = Calendar.is_calendar_date(date)
        msg = FAILURE_MESSAGE.format(call, expected, returned)
        self.assertEqual(expected, returned, msg)

    def test_36_is_calendar_date(self):
        expected = True
        src = ''.join(inspect.getsourcelines(Calendar.is_calendar_date)[0])
        used_is_numeric = "isnumeric()" in src
        date = "2017-02-31"
        result = Calendar.is_calendar_date(date)
        call = "Calendar.is_calendar_date\
                ('{}')".format(str(date))
        returned = Calendar.is_calendar_date(date)
        returned = returned and not used_is_numeric
        msg = FAILURE_MESSAGE.format(call, expected, returned)
        self.assertEqual(expected, returned, msg)

    def test_37_is_calendar_date(self):
        expected = False
        src = ''.join(inspect.getsourcelines(Calendar.is_calendar_date)[0])
        used_is_numeric = "isnumeric()" in src
        date = "2017-03-33"
        result = Calendar.is_calendar_date(date)
        result = result or used_is_numeric
        call = "Calendar.is_calendar_date\
                ('{}')".format(str(date))
        returned = Calendar.is_calendar_date(date)
        msg = FAILURE_MESSAGE.format(call, expected, returned)
        self.assertEqual(expected, returned, msg)

    def test_38_is_calendar_date(self):
        expected = False
        src = ''.join(inspect.getsourcelines(Calendar.is_calendar_date)[0])
        used_is_numeric = "isnumeric()" in src
        date = "217-03-30"
        result = Calendar.is_calendar_date(date)
        result = result or used_is_numeric
        call = "Calendar.is_calendar_date\
                ('{}')".format(str(date))
        returned = Calendar.is_calendar_date(date)
        msg = FAILURE_MESSAGE.format(call, expected, returned)
        self.assertEqual(expected, returned, msg)

    def test_39_is_calendar_date(self):
        expected = False
        src = ''.join(inspect.getsourcelines(Calendar.is_calendar_date)[0])
        used_is_numeric = "isnumeric()" in src
        date = "2017-0-30"
        result = Calendar.is_calendar_date(date)
        result = result or used_is_numeric
        call = "Calendar.is_calendar_date\
                ('{}')".format(str(date))
        returned = Calendar.is_calendar_date(date)
        msg = FAILURE_MESSAGE.format(call, expected, returned)
        self.assertEqual(expected, returned, msg)

    def test_40_is_calendar_date(self):
        expected = False
        src = ''.join(inspect.getsourcelines(Calendar.is_calendar_date)[0])
        used_is_numeric = "isnumeric()" in src
        date = "2017-19-30"
        result = Calendar.is_calendar_date(date)
        result = result or used_is_numeric
        call = "Calendar.is_calendar_date\
                ('{}')".format(str(date))
        returned = Calendar.is_calendar_date(date)
        msg = FAILURE_MESSAGE.format(call, expected, returned)
        self.assertEqual(expected, returned, msg)

    def test_41_is_natural_number(self):
        expected = False
        src = ''.join(inspect.getsourcelines(Calendar.is_natural_number)[0])
        used_is_numeric = "isnumeric()" in src
        n = "123 "
        result = Calendar.is_natural_number(n)
        result = result or used_is_numeric
        call = "Calendar.is_natural_number\
                ('{}')".format(str(n))
        returned = Calendar.is_natural_number(n)
        msg = FAILURE_MESSAGE.format(call, expected, returned)
        self.assertEqual(expected, returned, msg)

    def test_42_is_natural_number(self):
        expected = False
        src = ''.join(inspect.getsourcelines(Calendar.is_natural_number)[0])
        used_is_numeric = "isnumeric()" in src
        n = "-1"
        result = Calendar.is_natural_number(n)
        result = result or used_is_numeric
        call = "Calendar.is_natural_number\
                ('{}')".format(str(n))
        returned = Calendar.is_natural_number(n)
        msg = FAILURE_MESSAGE.format(call, expected, returned)
        self.assertEqual(expected, returned, msg)

    def test_43_is_natural_number(self):
        expected = False
        src = ''.join(inspect.getsourcelines(Calendar.is_natural_number)[0])
        used_is_numeric = "isnumeric()" in src
        n = "1a9"
        result = Calendar.is_natural_number(n)
        result = result or used_is_numeric
        call = "Calendar.is_natural_number\
                ('{}')".format(str(n))
        returned = Calendar.is_natural_number(n)
        msg = FAILURE_MESSAGE.format(call, expected, returned)
        self.assertEqual(expected, returned, msg)

    def test_44_is_natural_number(self):
        expected = False
        src = ''.join(inspect.getsourcelines(Calendar.is_natural_number)[0])
        used_is_numeric = "isdigit()" in src
        n = "1.1"
        result = Calendar.is_natural_number(n)
        result = result or used_is_numeric
        call = "Calendar.is_natural_number\
                ('{}')".format(str(n))
        returned = Calendar.is_natural_number(n)
        msg = FAILURE_MESSAGE.format(call, expected, returned)
        self.assertEqual(expected, returned, msg)

    def test_45_parse_command(self):
        expected = ['help']
        line = "ADD 2017-04-12 Python test"
        result = Calendar.parse_command(line)
        call = "Calendar.parse_command\
                ('{}')".format(str(line))
        returned = Calendar.parse_command(line)
        msg = FAILURE_MESSAGE.format(call, expected, returned)
        self.assertEqual(expected, returned, msg)

    def test_46_parse_command(self):
        expected = ['error', 'add DATE START_TIME END_TIME DETAILS']
        line = "add 2017-04-12 5"
        result = Calendar.parse_command(line)
        call = "Calendar.parse_command\
                ('{}')".format(str(line))
        returned = Calendar.parse_command(line)
        msg = FAILURE_MESSAGE.format(call, expected, returned)
        self.assertEqual(expected, returned, msg)

    def test_47_parse_command(self):
        expected = ['error', 'not a valid calendar date']
        line = "add 217-04-12 8 10 Python test"
        result = Calendar.parse_command(line)
        call = "Calendar.parse_command\
                ('{}')".format(str(line))
        returned = Calendar.parse_command(line)
        msg = FAILURE_MESSAGE.format(call, expected, returned)
        self.assertEqual(expected, returned, msg)

    def test_48_parse_command(self):
        expected = ['quit']
        line = "quit"
        result = Calendar.parse_command(line)
        call = "Calendar.parse_command\
                ('{}')".format(str(line))
        returned = Calendar.parse_command(line)
        msg = FAILURE_MESSAGE.format(call, expected, returned)
        self.assertEqual(expected, returned, msg)

    def test_49_parse_command(self):
        expected = ['delete', '2019-07-18', 14]
        line = "delete 2019-07-18 14"
        result = Calendar.parse_command(line)
        call = "Calendar.parse_command\
                ('{}')".format(str(line))
        returned = Calendar.parse_command(line)
        msg = FAILURE_MESSAGE.format(call, expected, returned)
        self.assertEqual(expected, result, msg)

    def test_50_parse_command(self):
        expected = ['add', '2017-04-12', 11, 15, 'Python test']
        line = "add 2017-04-12 11 15 Python test"
        result = Calendar.parse_command(line)
        call = "Calendar.parse_command\
                ('{}')".format(str(line))
        returned = Calendar.parse_command(line)
        msg = FAILURE_MESSAGE.format(call, expected, returned)
        self.assertEqual(expected, returned, msg)


if __name__ == '__main__':

    try:
        import UI_Tester
    except Exception:
        print("User Interface not found")
        
    try:
        unittest.main()
    except SystemExit as inst:
        if inst.args[0] is True:  # raised by sys.exit(True) when tests failed
            raise
