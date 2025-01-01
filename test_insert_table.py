
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


    search = requests.get('http://127.0.0.1:8000/company/searchCompany', headers=headers, params={"inn":"5259107913"})
    print(search)
    print(search.text)
    addCompany = requests.post('http://127.0.0.1:8000/company/addCompany', headers=headers, json=json.loads(search.text)["data"])
    print(addCompany)
    print(addCompany.text)


working_api_CompanyStructure()

# tt='{"data":{"ОГРН":"1135259004286","ИНН":"5259107913","КПП":"525901001","ОКПО":"25645293","ДатаРег":"2013-08-29","ДатаОГРН":"2013-08-29","НаимСокр":"ООО СК МТИ","НаимАнгл":null,"НаимПолн":"ОБЩЕСТВО С ОГРАНИЧЕННОЙ ОТВЕТСТВЕННОСТЬЮ СК МОНТАЖТЕХИНВЕСТ","Статус":{"Код":"001","Наим":"Действует"}}}'
# res= json.loads(tt)