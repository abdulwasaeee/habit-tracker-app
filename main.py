from datetime import datetime

import requests
URL="https://pixe.la/v1/users"
p={
    "token":"abdulwasaeee",
    "username":"wasae",
    "agreeTermsOfService":"yes",
    "notMinor":"yes"
}
response=requests.post(url=URL,json=p)
print(response.text)

URL2="https://pixe.la/v1/users/wasae/graphs"
graphp={
    "id":"h23",
    "name":"habit_tracker",
    "unit":"commit",
     "type":"int",
    "color":"ajisai"
}
head={
    "X-USER-TOKEN":"abdulwasaeee"
}
response2=requests.post(url=URL2,json=graphp,headers=head)
print(response2.text)

URL3="https://pixe.la/v1/users/wasae/graphs/h23"
head={
    "X-USER-TOKEN":"abdulwasaeee"
}
pixelp={
"date":datetime.now().strftime("%Y%m%d"),
"quantity":input("how many commits?")
}

response3=requests.post(url=URL3,json=pixelp,headers=head)
print(response3.text)

URL4="https://pixe.la/v1/users/wasae/graphs/h23"

head={
    "X-USER-TOKEN":"abdulwasaeee"
}
updatep={
    "color":"momiji"
}
response4=requests.put(url=URL4,json=updatep,headers=head)
print(response4.text)

URL5="https://pixe.la/v1/users/wasae/graphs/h23"
head={
    "X-USER-TOKEN":"abdulwasaeee"
}
response5=requests.delete(url=URL5,headers=head)
print(response5.text)
