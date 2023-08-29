from google_oauth import GoogleOauth


if __name__ == "__main__":
    try:
        google_oauth = GoogleOauth()
        oauth_secret = google_oauth.generate_oauth_secret()

        print(f"OAUTH SECRET: {oauth_secret}")

    except Exception as ex:
        print(ex)
