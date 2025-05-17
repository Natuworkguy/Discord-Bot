python3 ~/dbot/banner.py
sudo apt install -y screen python3 python3-pip
pip install -r ~/dbot/requirements.txt
echo "Completed dependency install"
screen -DdmS discord python3 ~/dbot/main.py
echo "Proccess started successfully"
