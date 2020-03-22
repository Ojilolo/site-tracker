'''
Author: Akila Bandara
ContactMe: www.twitter.com/@akilaontweet
FollwMe: www.instagram.com/@akilaoninsta
'''

import os

os.system('cls')


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

print(f"""


				   _____ _ _         _______             _             
				  / ____(♥) |       |__   __|           | |            
				 | (___  _| |_ ___     | |_ __ __ _  ___| | _____ _ __ 
				  \___ \| | __/ _ \    | | '__/ _` |/ __| |/ / _ \ '__|
				  ____) | | ||  __/    | | | | (☻| | (__|   <  __/ |   
				 |_____/|_|\__\___|    |_|_|  \__,_|\___|_|\_\___|_| 
	
				 {bcolors.UNDERLINE}Akila Bandara 2020 (c) www.twitter.com/@akilaontweet{bcolors.ENDC}
				 {bcolors.OKGREEN}---------------------------------------------------
				 	 {bcolors.OKGREEN}Let's track all websites and get IP!
				 		#SiteTrackerByAkila 
				 ---------------------------------------------------
                                                       
                                                       
	""")
print(f"{bcolors.WARNING}[i]Author: Akila Bandara{bcolors.ENDC}")
print(bcolors.WARNING + "[i]Follow: www.twitter.com/@akilaontweet\n" + bcolors.ENDC)

url = input(f"{bcolors.OKBLUE}[*]Enter URL of the website you want to track&getIP: ")
print("It's taking some time")
os.system('tracert ' + url)