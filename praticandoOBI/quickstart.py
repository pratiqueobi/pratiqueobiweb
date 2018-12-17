from __future__ import print_function
from googleapiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools
from apiclient.http import MediaFileUpload

#If modifying these scopes, delete the file token.json.
SCOPES = 'https://www.googleapis.com/auth/drive'

def main():


    store = file.Storage('token.json')
    creds = store.get()
    if not creds or creds.invalid:
        flow = client.flow_from_clientsecrets('credentials.json', SCOPES)
        creds = tools.run_flow(flow, store)
    service = build('drive', 'v3', http=creds.authorize(Http()))


    file_metadata = {
        'name': 'Prova.docx',
    }
    media = MediaFileUpload('Prova.docx',
                            mimetype='text/',
                            resumable=True)
    prova = service.files().create(body=file_metadata,
                                        media_body=media).execute()
    #prova.get('id')
    print("ID:")
    print(prova.get('id'))

# def upload_drive(filename, filepath, mimetype):
#
#     store = file.Storage('token.json')
#     creds = store.get()
#     if not creds or creds.invalid:
#         flow = client.flow_from_clientsecrets('credentials.json', SCOPES)
#         creds = tools.run_flow(flow, store)
#     service = build('drive', 'v3', http=creds.authorize(Http()))
#
#
#     file_metadata = {
#         'name': filename,
#     }
#     media = MediaFileUpload(filepath,
#                             mimetype=mimetype,
#                             resumable=True)
#     prova = service.files().create(body=file_metadata,
#                                         media_body=media).execute()
#
# upload_drive('Prova.docx', 'Prova.docx', 'text/')

if __name__ == '__main__':
   main()
