import requests

def check_website_status(url) :
    r = requests.get(url)
    if (r.status_code == 200) :
        print("Website is up and running!")
    else :
        print("Website returned a status code of 404")

url = input("Enter the URL of the website to check: ")
check_website_status(url)



