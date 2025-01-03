
import requests
import json


headers = {'Content-Type': 'application/x-www-form-urlencoded', 'Accept': 'application/json'}
#
#
res = requests.post('http://127.0.0.1:8000/auth/sign-in/', headers=headers,
                    data="grant_type=&username=admin&password=admin&scope=&client_id=&client_secret=")
access_token = json.loads(res.text)


def working_api_CompanyStructure():


    global access_token

    headers = {'Content-Type': 'application/json', 'Accept': 'application/json',
               "Authorization": "Bearer " + access_token["access_token"],
               "Cookie": "Authorization=bearer " + access_token["access_token"]
               }
    inns=["5259107913","6143087120","5609044282","7017061036","3525457593","6312058600","5003049878","7404039101","6662091900","7701013265","7717140237"]

    company = requests.get('http://127.0.0.1:8000/company/getCompany', headers=headers)
    for inn in json.loads(company.text):
        if inn["ИНН"] in inns:
            inns.pop(inns.index(inn["ИНН"]))

    for inn in inns:

            search = requests.get('http://127.0.0.1:8000/company/searchCompany', headers=headers, params={"inn":inn})
            print(inn)
            print(search.status_code)
            if search.status_code == 200:
                addCompany = requests.post('http://127.0.0.1:8000/company/addCompany', headers=headers, json=json.loads(search.text)["ЮЛ"])
                print(addCompany)
                print(addCompany.text)


working_api_CompanyStructure()


# headers = {'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8', 'Accept': 'application/json, text/javascript, */*; q=0.01'}
#
# search = requests.post('https://egrul.nalog.ru/', headers=headers, data={"vyp3CaptchaToken":"","page":"","query":"5259107913","region":"","PreventChromeAutocomplete":""})
# # search = requests.post('https://egrul.nalog.ru/', headers=headers, params="vyp3CaptchaToken=&page=&query=5259107913&region=&PreventChromeAutocomplete=")
# print(search)
# print(search.text)
#
# response = requests.get(f'https://egrul.nalog.ru/search-result/{json.loads(search.text)["t"]}?r=1735744564139&_=1735744564139', headers=headers, data={"vyp3CaptchaToken":"","page":"","query":"5259107913","region":"","PreventChromeAutocomplete":""})
# print(response)
# print(response.text)