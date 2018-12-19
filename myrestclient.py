import requests
import json

apiURL = "http://brilabs.azurewebsites.net/api/Pegawai"

def get_all_pegawai():
    req = requests.get(apiURL)
    json_results = json.loads(req.content)
    return json_results

def get_pegawai_by_nip(nip):
    req = requests.get(apiURL+"/{}".format(nip))
    json_result = json.loads(req.content)
    return json_result

def post_data_pegawai(data):
    newData = data
    result = requests.post(apiURL,data=newData)
    return result

def put_data_pegawai(data):
    alldata = get_all_pegawai()
    for d in alldata:
        if d["Nip"]==data["Nip"]:
            result = requests.put(apiURL,data=data)
            return result
        else:
            return None

def delete_data_pegawai(nip):
    alldata = get_all_pegawai()
    for d in alldata:
        if d["Nip"]==nip:
            url = apiURL+"/{}".format(nip)
            result = requests.delete(url)
            return result
            
def main():
    Nip = input("Masukan Nip data yang akan didelete :")
    result = delete_data_pegawai(Nip)
    print("Status {}, Keterangan {}".format(result.status_code,result.content.decode("utf-8")))
    """
    Nama = input("Masukan Nama :")
    Email = input("Masukan Email :")
    Telp = input("Masukan Telepon :")
    Umur = input("Masukan Umur :")
    editPegawai = {"Nip":Nip,"Nama":Nama,"Email":Email,"Telp":Telp,"Umur":Umur}
    result = put_data_pegawai(editPegawai)
    if not result == None:
        print("Status {}, Pesan: {}".format(result.status_code,
        result.content.decode("utf-8")))
    else:
        print("Data {} tidak ditemukan".format(Nip))
    """
   
if __name__ == "__main__":
    main()