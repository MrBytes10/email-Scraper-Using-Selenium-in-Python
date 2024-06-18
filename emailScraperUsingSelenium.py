import re # re is regex
from selenium import webdriver

# Now we initiate our Chrome Driver
"""chrome_driver= "E:\Anaconda_Python3_Codes\Data_Science_Projects\EmailScrapers\emailScraperUsingSelenium\chromedriver"""
driver= webdriver.Chrome()  #chrome_driver
driver.get("https://www.randomlists.com/email-addresses?qty=50") # qty is the quantity/number of emails you want

page_source= driver.page_source

EMAIL_REGEX= r"""(?:[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*|"(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21\x23-\x5b\x5d-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])*")@(?:(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?|\[(?:(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9]))\.){3}(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9])|[a-z0-9-]*[a-z0-9]:(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21-\x5a\x53-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])+)\])""" # to get this regex search on google this; "validate email regex"

list_of_emails= []
for re_match in re.finditer(EMAIL_REGEX, page_source):
    list_of_emails.append(re_match.group())
    # this is a for loop to look for all the matches
    # then is appends the te empty array created above

# Now we print the emails to the console
for i, email in enumerate(list_of_emails): # a quick way to get i and avoid incrementing i manually
    print(f"{i+1}: {email}")
    
    






