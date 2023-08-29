from google_oauth import GoogleOauth
import sys
from marshmallow import Schema, fields, validate


class GenerateQRCodeSchema(Schema):
    service = fields.String(required=True, validate=[validate.Length(min=1)])
    oauth_secret = fields.String(required=True, validate=[validate.Length(min=16, max=16)])
    email = fields.String(required=True, validate=[validate.Email()])

if __name__ == "__main__":
    try:
        argv= sys.argv[1:] 
        kwargs={kw[0]:kw[1] for kw in [ar.split('=') for ar in argv if ar.find('=')>0]}

        schema = GenerateQRCodeSchema()
        kwargs_errors = schema.validate(kwargs)
        if kwargs_errors:
            print(kwargs_errors)

        else:
            google_oauth = GoogleOauth()
            google_oauth.generate_qr_code(
                service=kwargs['service'],
                email=kwargs['email'],
                secret=kwargs['oauth_secret']
            )

            print("Successfully generated QR code.")

    except Exception as ex:
        print(ex)
