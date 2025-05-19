if [[ $EUID -ne 0 ]]; then
    echo "This script must be ran as root."
    exit 1
fi
apt install -y screen python3 python3-pip || exit 1
pip install -r ./requirements.txt || exit 1
python3 ./banner.py || exit 1
echo "Completed dependency install"
screen -DdmS discord python3 .dbot/main.py || exit 1
echo "Proccess started successfully"
