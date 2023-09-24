# Random Print
- Scan a QR code, it will pickup a file randomly then print.
- Creative Expo Taiwan 2023 @ C-LAB Creators
## Usage
### Clone this project on both printer and server
```
git clone https://github.com/danchouzhou/randomprint.git
```
### Server
- [Setup JSON database server](https://github.com/danchouzhou/http_json_db)
### Printer
- Connecte your printer to a Raspberry Pi.
- Install CUPS and printer driver (such like hplip).
- Config your printer with CUPS
- Replace the printer and server URL
```
python3 ./randomprint/printer/randomprint.py
```
Run the script automaticlly by systemd
```
sudo cp randomprint.service /etc/systemd/system/
sudo systemctl daemon-reload
systemctl enable randomprint.service
```