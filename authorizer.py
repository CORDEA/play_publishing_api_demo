import google.auth
from googleapiclient import discovery

SCOPES = ['https://www.googleapis.com/auth/androidpublisher']


def authorize():
    credentials, _ = google.auth.default(scopes=SCOPES)
    return discovery.build(
        'androidpublisher',
        'v3',
        credentials=credentials
    )
