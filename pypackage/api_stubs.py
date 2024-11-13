import os

from flask import Flask

app = Flask(__name__)


@app.route('/gettoken')
def get_token():
    return


l = ['error', 'output', 'processed']
dir = '/u02/eirsdata/etl_cdr/processed_cdr/'
ops = [name for name in os.listdir(dir) if os.path.isdir(os.path.join(dir, name))]

for op in ops:
    sr = [name for name in os.listdir(dir + op) if os.path.isdir(os.path.join(dir + op, name))]
    print(f"Sources {sr}")
    for li in l:
        print(dir + '/' + op + '/' + sr)

l = ['error', 'output', 'processed']
dir = '/u02/eirsdata/etl_cdr/processed_cdr/'
ops = [name for name in os.listdir(dir) if os.path.isdir(os.path.join(dir, name))]

for op in ops:
    sr = [name for name in os.listdir(dir + op) if os.path.isdir(os.path.join(dir + op, name))]
    print(f"Sources {sr}")
    for s in sr:
        print("Sr: ", s)

l = ['error', 'output', 'processed']
dir = '/u02/eirsdata/etl_cdr/processed_cdr/'
ops = [name for name in os.listdir(dir) if os.path.isdir(os.path.join(dir, name))]

for op in ops:
    sr = [name for name in os.listdir(dir + op) if os.path.isdir(os.path.join(dir + op, name))]
    print(f"Sources {sr}")
    for s in sr:
        print("Sr: ", s)
        for li in l:
            print(dir + " " + op + " " + s)

    [name for name in os.listdir('/u02/eirsdata/etl_cdr/processed_cdr/') if
     os.path.isdir(os.path.join('/u02/eirsdata/etl_cdr/processed_cdr/', name))]

    l = []
