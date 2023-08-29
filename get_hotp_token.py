from google_oauth import GoogleOauth
import sys
from marshmallow import Schema, fields, validate


class GetHOTPTokenSchema(Schema):
    oauth_secret = fields.String(required=True, validate=[validate.Length(min=16, max=16)])

if __name__ == "__main__":
    try:
        argv= sys.argv[1:] 
        kwargs={kw[0]:kw[1] for kw in [ar.split('=') for ar in argv if ar.find('=')>0]}

        schema = GetHOTPTokenSchema()
        kwargs_errors = schema.validate(kwargs)
        if kwargs_errors:
            print(kwargs_errors)

        else:
            google_oauth = GoogleOauth()
            hotp_token = google_oauth.get_hotp_token(
                secret=kwargs['oauth_secret']
            )

            print(f"hotp token: {hotp_token}")
    
    except Exception as ex:
        print(ex)
