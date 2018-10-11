x = [{'domain': '.ziroom.com', 'expiry': 1535368520.787031, 'httpOnly': True, 'name': 'CURRENT_CITY_CODE', 'path': '/', 'secure': False, 'value': '110000'}, {'domain': 'www.ziroom.com', 'expiry': 1535094920, 'httpOnly': False, 'name': 'mapType', 'path': '/', 'secure': False, 'value': '%20'}, {'domain': '.ziroom.com', 'expiry': 1535010316, 'httpOnly': False, 'name': 'gr_session_id_8da2730aaedd7628_0cc41143-ef56-4812-b49b-e805a30f8e51', 'path': '/', 'secure': False, 'value': 'true'}, {'domain': '.ziroom.com', 'expiry': 1850368520, 'httpOnly': False, 'name': 'gr_user_id', 'path': '/', 'secure': False, 'value': '69c285bd-1f74-4f5a-a859-c348e6ff176c'}, {'domain': '.ziroom.com', 'httpOnly': True, 'name': 'uid', 'path': '/', 'secure': False, 'value': 'b3fa9d34-9cd7-4eb7-aa9c-6ffd3714b017'}, {'domain': '.ziroom.com', 'expiry': 1535010315, 'httpOnly': False, 'name': 'gr_session_id_8da2730aaedd7628', 'path': '/', 'secure': False, 'value': '0cc41143-ef56-4812-b49b-e805a30f8e51'}, {'domain': '.ziroom.com', 'httpOnly': True, 'name': 'passport_token', 'path': '/', 'secure': False, 'value': 'dc5c2381-6691-4a17-9ce9-d14ba9ece0c5'}]
z = {'domain': '.ziroom.com', 'expiry': 1535368520.787031, 'httpOnly': True, 'name': 'CURRENT_CITY_CODE', 'path': '/', 'secure': False, 'value': '110000'}
# for a,b in z.items():
#     print(a+":"+str(b))
e = [m + n for m in 'ABC' for n in 'XYZ']
print(e)
y = [str(d) for i in x  for c,d in i.items() if c=="name" or c=="value"]
print(y)


