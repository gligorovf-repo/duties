#!/usr/bin/env python

import requests
from selenium import webdriver
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile
from selenium.webdriver import FirefoxOptions
from sys import argv

print "start script"

firefox_options = FirefoxOptions()
firefox_options.add_argument("--headless")

user = argv[1]
passw = argv[2]
start = argv[3]
finish = argv[4]
product = argv[6]

print "User: ", user
print "Passwd: ", passw

firefoxProfile = FirefoxProfile()
firefoxProfile.set_preference("plugin.state.flash", 2)
# driver = webdriver.Firefox(firefoxProfile, executable_path='/godata/pipelines/duty/geckodriver.exe')
driver = webdriver.Firefox(firefoxProfile, firefox_options = firefox_options, executable_path='C:/cygwin64/home/Filip.Gligorov/projects/duties/geckodriver.exe')
url = "http://sdc-devvatfxap1/HealthRoster/"+product
driver.get(url)

username = driver.find_element_by_id("txtUsername")
password = driver.find_element_by_id("txtPassword")

username.send_keys(user)
password.send_keys(passw)
driver.find_element_by_id("btnLogin").click()

request_cookie_browser = driver.get_cookie('.HRFedAuth_3601_'+product)
cookies={'.HRFedAuth_3601_FLEXAUTOPS':str(request_cookie_browser['value'])}

print cookies

# s = requests.Session()

# for i in range(int(start),int(finish)+1):
# 	body = '<BulkSendDutyToBank IsPartOfBlock="false"> <SendDutiesToBank> <SendDutyToBank ID="',i,'" FulfilledOnlyByNHSpWebPortal="false"> <OrgUnit ID="',argv[5],'"/> <BookingReason ID="1"/> <Competences/> </SendDutyToBank> </SendDutiesToBank> </BulkSendDutyToBank>'
# 	print body
# 	# response = s.post('http://sdc-devvatfxap1/HealthRoster/FLEXAUTOPS/Process', cookies=cookies, data=body)
# 	# print response.content

# s.close()
driver.quit()