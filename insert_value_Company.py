
import requests
import json

import string
import random
# number_of_strings = 5
# length_of_string = 15
# for x in range(number_of_strings):
#     print("" .join(random.choice(string.ascii_letters + string.digits) for _ in range(length_of_string) ) )

def random_string (length: int,options: string):
    return options+" "+"".join(random.choice(string.ascii_letters + string.digits) for _ in range(length))

def random_Construction (length: int):
    ff=[]
    for i in range(length):
        ff.append({"idCompanyStructure":"","Наименнование":random_string(10,"Наименнование"),"Местоположение":random_string(10,"Местоположение"),"ВидОбъекта":random_string(10,"ВидОбъекта"),"Описание":random_string(10,"Описание")})
    return ff

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
    inns_construct={"5259107913":random_Construction(1)
    ,"6143087120":random_Construction(1)
    ,"5609044282":random_Construction(2)
    ,"7017061036":random_Construction(3)
    ,"3525457593":random_Construction(4)
    ,"6312058600":random_Construction(5)
    ,"5003049878":random_Construction(7)
    ,"7404039101":random_Construction(9)
    ,"6662091900":random_Construction(11)
    ,"7701013265":random_Construction(13)
    ,"7717140237":random_Construction(15)
    }
    inns=list(inns_construct.keys())
    company = requests.get('http://127.0.0.1:8000/company/getCompany', headers=headers)
    for inn in json.loads(company.text):
        if inn["ИНН"] in inns:
            for i,v in enumerate(inns_construct[inn["ИНН"]]):
                inns_construct[inn["ИНН"]][i]["idCompanyStructure"]=inn["id"]
                addConstruction = requests.post('http://127.0.0.1:8000/construction/addConstruction', headers=headers,json=inns_construct[inn["ИНН"]][i])
                print(addConstruction)
                print(addConstruction.text)
            inns.pop(inns.index(inn["ИНН"]))

    for inn in inns:

            search = requests.get('http://127.0.0.1:8000/company/searchCompany', headers=headers, params={"inn":inn})
            print(inn)
            print(search.status_code)
            if search.status_code == 200:
                addCompany = requests.post('http://127.0.0.1:8000/company/addCompany', headers=headers, json=json.loads(search.text)["ЮЛ"])
                print(addCompany)
                print(addCompany.text)
                for i,v in enumerate(inns_construct[json.loads(addCompany.text)["ИНН"]]):
                    inns_construct[json.loads(addCompany.text)["ИНН"]][i]["idCompanyStructure"]=json.loads(addCompany.text)["id"]
                    addConstruction = requests.post('http://127.0.0.1:8000/construction/addConstruction', headers=headers,json=inns_construct[json.loads(addCompany.text)["ИНН"]][i])
                    print(addConstruction)
                    print(addConstruction.text)


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