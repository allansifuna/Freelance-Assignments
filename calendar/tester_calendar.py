import urllib.request
url = "http://comp2152.gblearn.com/2021/winter/a2_tester_calendar.php"
tester_file = urllib.request.urlopen(url)
# exec(tester_file.read())
print(dir(tester_file))
with open("cale.py", 'w') as f:
    f.write(tester_file.read().decode('utf8'))
# for i in dir(tester_file):
#     try:
#         print(f"{tester_file.i()}")
#     except:
#         print(f"{tester_file.i}")
