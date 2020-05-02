# !/bin/bash
sudo apt-get install python3.6 python3-pip python3-dev 
pip3 install -r requirements.txt
echo "Do you wish to install TA-Lib to use additional charting patterns(DOJI,MARUBOZU,etc) or indicators from the TA-Lib library ?"
select yn in "Yes" "No"; do
    case $yn in
        Yes ) pip3 install TA-Lib==0.4.17; break;;
        No ) break;;
    esac
done
mkdir Scripts
mkdir Outputs
mkdir Data
cores=$(nproc)
echo "Cores = ${cores}"
workers=$((2*${cores}+1))
echo "Recommended Workers = ${workers}"
gunicorn --workers $workers --bind 0.0.0.0:5000 wsgi:app