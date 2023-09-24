# Random Print
- Scan a QR code, it will pickup a file randomly then print.
- Creative Expo Taiwan 2023 @ C-LAB Creators
## Usage
### Clone this project on both printer and server
```
git clone https://github.com/danchouzhou/randomprint.git
```
### Server
```
python3 ./randomprint/printer/server.py
```
### Printer
- Connecte your printer to a Raspberry Pi.
- Install CUPS and printer driver (such like hplip).
- Config your printer with CUPS
- Replace the printer and server URL
```
python3 ./randomprint/printer/main.py
```