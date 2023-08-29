# GOOGLE AUTHENTICATOR

Script útil para criação de QR codes do google authenticator, chaves secretas e validação de hotp tokens.

## Criação do ambiente virtual.

```bash
pipenv install -r requirements.txt
```
```bash
pipenv shell
```
## Execute o comando abaixo para gerar uma chave secreta do google authenticator.
```bash
python .\generate_secret_token.py

OAUTH SECRET: MHKAOHUADQJCNCOG
```
## Execute o comando abaixo para gerar um QR code do google authenticator.
```bash
python .\generate_qr_code.py service=teste oauth_secret=MHKAOHUADQJCNCOG email=teste@gmail.com

Successfully generated QR code.
## QR code é salvo na pasta generated_qr_code
```
## Execute o comando abaixo para obter um hotp token do google authenticator.
```bash
python .\get_hotp_token.py oauth_secret=MHKAOHUADQJCNCOG

hotp token: 57279
```
