import requests
from requests import get

phone_no = input("enter ph: ")
msg = input("enter message: ")

resp = requests.post("https://textbelt.com/text",{
  "phone" : phone_no,
  "message" : msg
})
print(resp.text)
