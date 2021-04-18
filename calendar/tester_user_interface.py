# import urllib.request
url = "http://comp2152.gblearn.com/2021/winter/a2_tester_user_interface.php"
# tester_file = urllib.request.urlopen(url)
# # print(tester_file.readlines())
# exec(tester_file.read())

# # print(dir(tester_file))
# # with open("uitester.py", 'w') as f:
# #     f.write(tester_file.read().decode('utf8'))

import requests

v = requests.get(url=url)
print(v.text)
