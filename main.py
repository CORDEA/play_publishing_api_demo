import sys

import authorizer


def list_bundles(client, name):
    response = client.edits().insert(packageName=name).execute()
    edit_id = response['id']

    response = client.edits().bundles().list(editId=edit_id, packageName=name).execute()
    return response['bundles']


def list_apks(client, name):
    response = client.edits().insert(packageName=name).execute()
    edit_id = response['id']

    response = client.edits().apks().list(editId=edit_id, packageName=name).execute()
    return response['apks']


def main(name):
    client = authorizer.authorize()
    bundles = list_bundles(client, name)
    for bundle in bundles:
        print(bundle['versionCode'])
        print(bundle['sha1'])

    apks = list_apks(client, name)
    for apk in apks:
        print(apk['versionCode'])
        print(apk['binary']['sha1'])


if __name__ == '__main__':
    if len(sys.argv) < 2:
        exit(1)
    main(sys.argv[1])
