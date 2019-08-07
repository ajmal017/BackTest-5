# !/bin/bash
sudo apt-get install python3.6 python3-pip
pip install -r requirements.txt
cores=$(nproc)
echo "Cores = ${cores}"
workers=$((2*${cores}+1))
echo "Recommended Workers = ${workers}"
gunicorn --workers $workers --bind 0.0.0.0:5000 wsgi:app