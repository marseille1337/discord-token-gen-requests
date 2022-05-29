# Made by github.com/its-vichy
# fucked discord another time <3

import httpx, threading, json, itertools, random, string
from colorama import Fore, init; init()

from config import __KEY__, __HEADLESS__, __WAIT__

"""
#'cookie': '__dcfduid=; __sdcfduid=; __cf_bm=; locale=',
"""

__proxies__ = itertools.cycle(open('./proxies.txt', 'r+').read().splitlines())

class GeneratorThread(threading.Thread):
    def __init__(self, captcha_payload: dict, captcha_headers: dict, captcha_url: str):
        threading.Thread.__init__(self)
        self.base_headers ={
            'accept': '*/*',
            'accept-encoding': 'gzip, deflate, br',
            'accept-language': captcha_headers['accept-language'],
            'referer': 'https://discord.com/',
            'sec-ch-ua': captcha_headers['sec-ch-ua'],
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': "Windows",
            'sec-fetch-site': captcha_headers['sec-fetch-site'],
            'sec-fetch-mode': captcha_headers['sec-fetch-mode'],
            'sec-fetch-dest': captcha_headers['sec-fetch-dest'],
            'user-agent': captcha_headers['user-agent'],
            'x-track': 'eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiQ2hyb21lIiwiZGV2aWNlIjoiIiwic3lzdGVtX2xvY2FsZSI6InpoLUNOIiwiYnJvd3Nlcl91c2VyX2FnZW50IjoiTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzEwMi4wLjUwMDUuNjIgU2FmYXJpLzUzNy4zNiIsImJyb3dzZXJfdmVyc2lvbiI6IjEwMi4wLjUwMDUuNjIiLCJvc192ZXJzaW9uIjoiMTAiLCJyZWZlcnJlciI6IiIsInJlZmVycmluZ19kb21haW4iOiIiLCJyZWZlcnJlcl9jdXJyZW50IjoiIiwicmVmZXJyaW5nX2RvbWFpbl9jdXJyZW50IjoiIiwicmVsZWFzZV9jaGFubmVsIjoic3RhYmxlIiwiY2xpZW50X2J1aWxkX251bWJlciI6OTk5OSwiY2xpZW50X2V2ZW50X3NvdXJjZSI6bnVsbH0=',

            'origin': 'https://discord.com',
        }

        self.captcha_url = captcha_url
        self.captcha_payload = captcha_payload
        self.captcha_headers = captcha_headers

    def run(self):
        #print('[THREADS] Starting new session.')
        
        #self.captcha_payload['serverdomain'] = "discord.com" # cant submit the shit
        #print(self.captcha_payload)

        try:
            proxy = None #f'http://{next(__proxies__)}' # put if you use proxies or home ip

            with httpx.Client(headers=self.base_headers, timeout=30) as client:
                # here is how to bypass the shit captcha by creating payload on browser, spoof motiondata mouse and made working paylad PROXYLESS ULTRA FAST
                captcha_key =  httpx.post(str(self.captcha_url), headers=self.captcha_headers, json=self.captcha_payload, timeout=30, proxies=proxy).json()['generated_pass_UUID']
                print(f'[{captcha_key[:25]}] Bypassed HCaptcha ({len(captcha_key)}).')

                # Get Fingerprint (useless i can made unlock without fingerprint)
                fingerprint = client.get('https://discord.com/api/v9/experiments').json()['fingerprint']

                # Build the register payload
                register_payload = {
                    "captcha_key": captcha_key,
                    "consent": True,
                    "fingerprint": fingerprint,
                    "username": ''.join(random.choice(string.ascii_letters + string.ascii_lowercase + string.ascii_uppercase) for _ in range(15))
                }

                # Update headers
                client.headers['cookie'] = f'__dcfduid={client.cookies.get("__dcfduid")}; __sdcfduid={client.cookies.get("__sdcfduid")}; locale=zh-CN' # ; locale=fr
                client.headers['content-length'] = str(len(json.dumps(register_payload)))
                client.headers['content-type'] = 'application/json'
                client.headers['x-fingerprint'] = fingerprint # gen worked without

                response = httpx.post('https://discord.com/api/v9/auth/register', json=register_payload, proxies=proxy, headers=client.headers, cookies=client.cookies).json()

                if 'token' in str(response):
                    token = response['token']

                    # update headers
                    client.headers['cookie'] = f'__dcfduid={client.cookies.get("__dcfduid")}; __sdcfduid={client.cookies.get("__sdcfduid")}; locale=zh-CN'
                    client.headers['authorization'] = token
                    client.headers['accept-language'] = self.captcha_headers['accept-language']
                    client.headers['x-debug-options'] = 'bugReporterEnabled'
                    client.headers['x-discord-locale'] = 'zh-CN'
                    client.headers['x-super-properties'] = 'eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiQ2hyb21lIiwiZGV2aWNlIjoiIiwic3lzdGVtX2xvY2FsZSI6InpoLUNOIiwiYnJvd3Nlcl91c2VyX2FnZW50IjoiTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzEwMi4wLjUwMDUuNjIgU2FmYXJpLzUzNy4zNiIsImJyb3dzZXJfdmVyc2lvbiI6IjEwMi4wLjUwMDUuNjIiLCJvc192ZXJzaW9uIjoiMTAiLCJyZWZlcnJlciI6IiIsInJlZmVycmluZ19kb21haW4iOiIiLCJyZWZlcnJlcl9jdXJyZW50IjoiIiwicmVmZXJyaW5nX2RvbWFpbl9jdXJyZW50IjoiIiwicmVsZWFzZV9jaGFubmVsIjoic3RhYmxlIiwiY2xpZW50X2J1aWxkX251bWJlciI6MTMwMDg5LCJjbGllbnRfZXZlbnRfc291cmNlIjpudWxsfQ=='

                    client.headers.pop('content-length')
                    client.headers.pop('x-track')

                    if client.get('https://discord.com/api/v9/users/@me/library').status_code == 200:
                        print(Fore.GREEN + f'[Unlocked] {token}' + Fore.RESET)

                        with open('./gen.txt', 'a+') as f:
                            f.write(token+'\n')
                    else:
                        print(Fore.RED + f'[Locked] {token}' + Fore.RESET)
                    
                    __WAIT__ = 120
                else:
                    print(response)
        except Exception as e:
            print(f'[ERROR] {e}')
            pass