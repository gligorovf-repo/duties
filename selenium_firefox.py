import requests
from selenium import webdriver
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile
from sys import argv

print "start script"

username = argv[1]
password = argv[2]
start = argv[3]
finish = argv[4]

print "User: ", username
print "Passwd: ", password

# firefoxProfile = FirefoxProfile()
# firefoxProfile.set_preference("plugin.state.flash", 2)
# driver = webdriver.Firefox(firefoxProfile, executable_path='C:/cygwin64/home/Filip.Gligorov/requests/geckodriver.exe')
# url = "http://sdc-devvatfxap1/HealthRoster/FLEXAUTOPS/"
# driver.get(url)

# username = driver.find_element_by_id("txtUsername")
# password = driver.find_element_by_id("txtPassword")

# username.send_keys(username)
# password.send_keys(password)
# driver.find_element_by_id("btnLogin").click()

# request_cookie_browser = driver.get_cookie('.HRFedAuth_3601_FLEXAUTOPS')
# cookies={'.HRFedAuth_3601_FLEXAUTOPS':str(request_cookie_browser['value'])}

# s = requests.Session()

for i in range(int(start),int(finish)+1):
	body = '<BulkSendDutyToBank IsPartOfBlock="false"> <SendDutiesToBank> <SendDutyToBank ID="',i,'" FulfilledOnlyByNHSpWebPortal="false"> <OrgUnit ID="',argv[5],'"/> <BookingReason ID="1"/> <Competences/> </SendDutyToBank> </SendDutiesToBank> </BulkSendDutyToBank>'
	print body
# 	response = s.post('http://sdc-devvatfxap1/HealthRoster/FLEXAUTOPS/Process', cookies=cookies, data=body)

# s.close()
# driver.quit()