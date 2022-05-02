echo "[SETUP] Installing..."
    echo "[SETUP] Update"
    sudo pacman -Syy
    echo " "
    echo "[SETUP] Installing Python"
    sudo pacman -S python
    echo " "
    echo "[SETUP] Installing Python-pip"
    sudo pacman -S python-pip
    pip install pandas pandas-datareader plotly
    pip install requests_html
    pip install tqdm
    pip install sockets
    sudo pacman -S php
    sudo pacman -S hostapd
    pip install instabot
    pip install matplotlib
    sudo pacman -S dhcpd
    pip install google
    sudo pacman -S bettercap
    pip3 install requests bs4
    pip install urllib3
    pip install platform
    pip install pyfiglet
    sudo pacman -S gcc
    sudo pacman -S python python2
    pip install requests
    pip install validate_email
    pip install beautifulsoup4
    pip install twilio
    echo " "
    echo "[SETUP] Installing Scapy Packet"
    pip install scapy
    echo " "
    echo "[SETUP] Installing Os Packet"
    pip install os
    echo " "
    echo "[SETUP] Installing Lolcat"
    sudo pacman -S lolcat
    echo " "
    echo "[SETUP] Installing Figlet"
    sudo pacman -S figlet
    pip install colorama
    pip install phonenumbers
    sudo pip install phonenumbers
    echo " "
    echo "[SETUP] Installing Aircrack-ng"
    sudo pacman -S aircrack-ng
    
    echo " "
    echo "[SETUP] Installing Cowpatty"
    
    sudo pacman -S cowpatty
    echo " "
    echo "[SETUP] Installing Pandas Packet"
    pip install pandas
    echo " "
    echo "[SETUP] Installing TLD Packet"
    pip install tld
    echo " "
    echo "[SETUP] Installing NMAP"
    sudo pacman -S nmap
    echo " "


echo "[RUN] Running..."
echo "[RUN] Run Command : sudo python3 main.py"
sudo python3 main.py
