echo "[SETUP] Installing..."

echo "[SETUP] Update"
sudo apt-get upgrade 
echo " "
echo "[SETUP] Installing Python"
sudo apt install python
echo " "
echo "[SETUP] Installing Python-pip"
sudo apt install python-pip
echo " "
echo "[SETUP] Installing Scapy Packet"
pip install scapy 
echo " "
echo "[SETUP] Installing Os Packet"
pip install os
echo " "
echo "[SETUP] Installing Lolcat"
sudo apt install lolcat
echo " "
echo "[SETUP] Installing Figlet"
sudo apt install figlet
echo " "
echo "[SETUP] Installing Aircrack-ng"
sudo apt install aircrack-ng
echo " "
echo "[SETUP] Installing Cowpatty"
sudo apt install cowpatty
echo " "
echo "[SETUP] Installing Pandas Packet"
pip install pandas
echo " "
echo "[SETUP] Installing TLD Packet"
pip install tld
echo " "
echo "[SETUP] Installing NMAP"
sudo apt install nmap
echo " "


echo "[RUN] Running..."
echo "[RUN] Run Command : sudo python3 main.py"
sudo python3 main.py