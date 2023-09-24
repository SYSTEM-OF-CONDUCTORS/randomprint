# Random Print
- Scan a QR code, it will pickup a file randomly then print
- Creative Expo Taiwan 2023 @ C-LAB Creators
## Usage
### Clone this project
Clone this project to a Raspberry Pi which connect with your printer.
```
git clone https://github.com/danchouzhou/randomprint.git
```
### Server
- [Setup JSON database server](https://github.com/danchouzhou/http_json_db)
### QR code
Create a QR code with your server link.
```
http://127.0.0.1:9693/?print=true
```
### Printer
- Connecte your printer to a Raspberry Pi
- Install CUPS and printer driver (such like hplip)
- Config your printer with CUPS
- Replace the printer and server URL inside the script
```
python3 ./randomprint/printer/randomprint.py
```
To run the script automaticlly by systemd
```
sudo cp randomprint.service /etc/systemd/system/
sudo systemctl daemon-reload
sudo systemctl enable randomprint.service
```