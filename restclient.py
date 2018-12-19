import requests
import json

def get_alldata():
    req = requests.get('http://brilabs.azurewebsites.net/api/Pegawai')
    #print("HTTP Status Code: " + str(req.status_code))
    #print(req.headers)
    json_response = json.loads(req.content)
    return json_response
    #print(type(json_response))
    #print(json_response)
    #for key in json_response:
        #print(key["Nip"])

def get_bynip(nip):
    req = requests.get('http://brilabs.azurewebsites.net/api/Pegawai/{0}'.format(nip))
    json_response = json.loads(req.content)
    return json_response

def post_data_pegawai():
    newData = {"Nip":"123123","Nama":"Erick Kurniawan",
    "Email":"erick@actual-training.com","Telp":"08156881169","Umur":"20"}
    r = requests.post('http://brilabs.azurewebsites.net/api/Pegawai',data=newData)
    print(r.status_code,r.reason)

def put_data_pegawai():
    editData = {"Nip":"123123","Nama":"Erick Aja",
    "Email":"erick@actual-training.com","Telp":"08156881169","Umur":"25"}
    r = requests.put('http://brilabs.azurewebsites.net/api/Pegawai',data=editData)
    print(r.status_code,r.reason)

def delete_data_pegawai(nip):
    r = requests.delete("http://brilabs.azurewebsites.net/api/Pegawai/{0}".format(nip))
    print(r.status_code,r.reason)

def main():
    #print(get_alldata())
    #post_data_pegawai()
    #put_data_pegawai()
    #delete_data_pegawai("8c58dcd9-89d3-4c0d-bcc0-94aaf9c90060")
    #print(get_bynip("123123")["Nip"])

if __name__ == "__main__":
    main()