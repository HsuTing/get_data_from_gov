import subprocess

commond = "python get_data.py -t urls.json"
subprocess.call([commond ,'shell arguments'], shell=True)
