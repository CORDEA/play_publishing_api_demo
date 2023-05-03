import sys

import google.auth
from googleapiclient import discovery

SCOPES = ['https://www.googleapis.com/auth/androidpublisher']


def main(name):
    credentials, _ = google.auth.default(scopes=SCOPES)
    client = discovery.build(
        'androidpublisher',
        'v3',
        credentials=credentials
    )

    response = client.edits().insert(packageName=name).execute()
    edit_id = response['id']

    response = client.edits().bundles().list(editId=edit_id, packageName=name).execute()
    bundles = response['bundles']
    print(bundles)


if __name__ == '__main__':
    if len(sys.argv) < 2:
        exit(1)
    main(sys.argv[1])
