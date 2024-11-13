import json
import os

# import mysql.connector

db_params = {
    'host': 'your_host',
    'user': 'your_username',
    'password': 'your_password',
    'database': 'your_database'
}


def readfile(filename):
    with open(filename, "r") as f:
        jsondata = json.load(f)
    return jsondata


def updatedb(data):
    query = """update gdce_data set sim = %s, brand = %s, device_type = %s, model = %s, goods_description = %s where imei = %s"""
    #    conn = mysql.connector.connect(**db_params)
    #    stmt = conn.cursor()
    for item in data:
        imei = item.get("imei")
        sim = item.get("sim")
        brand = item.get("brand")
        device_type = item.get("device_type")
        model = item.get("model")
        goods_description = item.get("goods_description")
        print("Imei : " + imei + " , brand :" + brand)

#        stmt.execute(query, (sim, brand, device_type, model, goods_description, imei))
#    conn.commit()


if __name__ == "_main__":

    directory_path = ""
    for i in os.listdir(directory_path):
        file = i + '_req.txt'
        dir = directory_path + "/" + i + "/" + file
        print("Full File Name:: ", dir)
        jsond = readfile(dir)
        updatedb(jsond)
