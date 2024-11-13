import logging
import os
import subprocess
from datetime import datetime

#
logging.basicConfig(
    filename='process_script.log',
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s',
)

APP_HOME = os.getenv('APP_HOME')
DATA_HOME = os.getenv('DATA_HOME')
commonConfigurationFilePath = os.getenv('commonConfigurationFilePath')

with open(commonConfigurationFilePath) as f:
    exec(f.read())

sleep_time = 60
repdate = datetime.now().strftime("%F_%T")
today_date = datetime.now().strftime('%Y%m%d')
table_name = f"app.edr_{today_date}"

control_file_dir = f"{DATA_HOME}/scripts/P4Process/CtlFiles"
log_file_dir = f"{DATA_HOME}/logs/scripts/P4Process"

# parents=true create parent directory if not exists


os.makedirs(control_file_dir, parents=True, exist_ok=True)
os.makedirs(log_file_dir, parents=True, exist_ok=True)


def create_ctl_file(file_path, file_name):
    tag = (f"OPTIONS (SKIP=1) load data infile '{file_path}' append into table {table_name} "
           f"fields terminated by ',' (actual_imei, imsi, msisdn, protocol, edr_date_time timestamp 'YYYY-MM-DD HH24:MI:SS', "
           f"source, file_name, imei_arrival_time timestamp 'YYYY-MM-DD')")
    ctl_file_path = f"{control_file_dir}/{file_name}.ctl"
    with open(ctl_file_path, 'w') as ctl_file:
        ctl_file.write(tag)


def start_sql_loader(file_path, file_name):
    print(f"Sql Loader Start for {file_path}")
    log_file = f"{log_file_dir}/{file_name}_{repdate}.log"
    command = [
        "sqlldr",
        f"userid={dbUsername}/{dbDecryptPassword}@//{dbIp}:{dbPort}/{dbServiceOrcl}",
        f"control={control_file_dir}/{file_name}.ctl",
        f"log={log_file}",
        "SKIP_INDEX_MAINTENANCE=true",
        "direct=true",
        "readsize=1048576",
        "bindsize=5048576",
        "Parallel=true",
        "multithreading=true"
    ]
    result = subprocess.run(command, capture_output=True, text=True)

    if result.returncode != 0:
        print("The script failed. Please refer to the logs for more information")
        print(f"Error code {result.returncode}")
        exit(0)


def remove_file(file_path, file_name):
    pass


def start_process(directory):
    for file in os.listdir(directory):
        if 'csv' in file:
            file_path = os.path.join(directory, file)
            file_name = os.path.basename(file_path)
            print(f"Starting for file - {file_name}")
            create_ctl_file(file_path, file_name)
            start_sql_loader(file_path, file_name)
            remove_file(file_path, file_name)
        else:
            print("Filename does not contain 'csv'")
            exit(1)
