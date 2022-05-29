# -*- coding: utf-8 -*-
# Time       : 2022/1/16 0:25
# Author     : QIN2DIM
# Github     : https://github.com/QIN2DIM
# Description:

# "made" (Edited) by github.com/its-vichy

import time, json, os
from typing import Optional

from selenium.common.exceptions import WebDriverException

from services.hcaptcha_challenger import ArmorCaptcha, ArmorUtils
from services.hcaptcha_challenger.exceptions import ChallengePassed
from services.settings import logger, HCAPTCHA_DEMO_SITES, DIR_MODEL, DIR_CHALLENGE
from services.utils import get_challenge_ctx

from generator import GeneratorThread
from config import __KEY__, __HEADLESS__, __WAIT__

def interceptor(request):
    if request.method == 'POST':
        if str(request.url).startswith('https://hcaptcha.com/checkcaptcha/') and str(request.url).endswith(f'?s={__KEY__}'):
            request.abort()

            js = json.loads(request.body.decode('utf-8'))

            motionData = json.loads(js['motionData'])
            
            # spoof mouse data to unlock tokens :)
            js['motionData'] = '{"st":1653703335944,"dct":1653703335944,"mm":[[8,280,1653703336211],[22,280,1653703336227],[37,280,1653703336244],[53,281,1653703336260],[66,282,1653703336277],[75,283,1653703336294],[82,284,1653703336310],[84,285,1653703336327],[85,285,1653703336627],[86,285,1653703336644],[89,285,1653703336660],[93,285,1653703336677],[98,285,1653703336694],[105,285,1653703336710],[112,284,1653703336727],[119,283,1653703336744],[125,281,1653703336760],[130,279,1653703336777],[133,277,1653703336794],[136,276,1653703336810],[138,275,1653703336827],[139,274,1653703336844],[142,273,1653703337110],[146,273,1653703337127],[151,271,1653703337144],[158,269,1653703337161],[164,267,1653703337177],[169,265,1653703337194],[173,263,1653703337210],[177,261,1653703337227],[178,259,1653703337244],[180,258,1653703337261],[181,257,1653703337677],[184,256,1653703337694],[188,254,1653703337711],[194,250,1653703337727],[204,247,1653703337744],[214,241,1653703337761],[224,236,1653703337777],[234,230,1653703337794],[241,225,1653703337810],[246,221,1653703337827],[249,217,1653703337844],[250,216,1653703337860],[251,216,1653703338061],[252,216,1653703338077],[253,216,1653703338094],[252,216,1653703338194],[246,217,1653703338211],[234,219,1653703338227],[216,219,1653703338244],[187,219,1653703338261],[154,217,1653703338278],[125,213,1653703338294],[106,210,1653703338311],[94,208,1653703338327],[89,206,1653703338344],[88,206,1653703338361],[200,320,1653703338718],[88,209,1653703338827],[90,213,1653703338844],[93,218,1653703338861],[96,222,1653703338877],[99,226,1653703338894],[103,229,1653703338910],[107,232,1653703338927],[113,234,1653703338945],[118,235,1653703338961],[127,236,1653703338977],[136,236,1653703338994],[147,236,1653703339011],[158,234,1653703339027],[172,232,1653703339044],[183,231,1653703339061],[191,231,1653703339077],[196,232,1653703339094],[200,235,1653703339111],[203,241,1653703339127],[203,253,1653703339144],[203,268,1653703339160],[203,281,1653703339177],[202,291,1653703339194],[200,299,1653703339210],[198,305,1653703339228]],"mm-mp":34.71264367816091,"md":[[200,320,1653703338718],[70,450,1653703338963],[350,562,1653703339231]],"md-mp":256.5,"mu":[[200,320,1653703338719],[70,450,1653703338963],[350,562,1653703339231]],"mu-mp":256,"topLevel":{"inv":false,"st":1653703330120,"sc":{"availWidth":1920,"availHeight":1040,"width":1920,"height":1080,"colorDepth":24,"pixelDepth":24,"availLeft":0,"availTop":0,"onchange":null,"isExtended":false},"nv":{"vendorSub":"","productSub":"20030107","vendor":"Google Inc.","maxTouchPoints":0,"userActivation":{},"doNotTrack":null,"geolocation":{},"connection":{},"pdfViewerEnabled":true,"webkitTemporaryStorage":{},"webkitPersistentStorage":{},"hardwareConcurrency":16,"cookieEnabled":true,"appCodeName":"Mozilla","appName":"Netscape","appVersion":"5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.62 Safari/537.36","platform":"Win32","product":"Gecko","userAgent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.62 Safari/537.36","language":"zh-CN","languages":["zh-CN","zh"],"onLine":true,"webdriver":false,"scheduling":{},"bluetooth":{},"clipboard":{},"credentials":{},"keyboard":{},"managed":{},"mediaDevices":{},"storage":{},"serviceWorker":{},"wakeLock":{},"deviceMemory":8,"ink":{},"hid":{},"locks":{},"mediaCapabilities":{},"mediaSession":{},"permissions":{},"presentation":{},"serial":{},"virtualKeyboard":{},"usb":{},"xr":{},"userAgentData":{"brands":[{"brand":" Not A;Brand","version":"99"},{"brand":"Chromium","version":"102"},{"brand":"Google Chrome","version":"102"}],"mobile":false},"plugins":["internal-pdf-viewer","internal-pdf-viewer","internal-pdf-viewer","internal-pdf-viewer","internal-pdf-viewer"]},"dr":"","exec":false,"wn":[[929,887,1,1653703330122]],"wn-mp":0,"xy":[[0,0,1,1653703330122]],"xy-mp":0,"mm":[[465,369,1653703330128],[422,388,1653703330144],[386,398,1653703330160],[352,404,1653703330177],[324,405,1653703330194],[309,402,1653703330210],[300,398,1653703330227],[295,395,1653703330244],[292,392,1653703330260],[289,388,1653703330277],[285,385,1653703330294],[282,381,1653703330310],[280,377,1653703330327],[280,373,1653703330344],[281,373,1653703330361],[287,371,1653703330377],[297,367,1653703330394],[303,366,1653703330410],[307,365,1653703330427],[311,365,1653703330444],[317,364,1653703330460],[323,363,1653703330477],[327,363,1653703330494],[328,363,1653703330557],[336,364,1653703330579],[354,368,1653703330610],[360,370,1653703330627],[364,375,1653703330644],[375,387,1653703330661],[395,397,1653703330677],[396,398,1653703330924],[402,399,1653703330944],[408,400,1653703330960],[409,400,1653703330977],[409,399,1653703331009],[409,397,1653703331028],[406,395,1653703331046],[397,391,1653703331077],[394,389,1653703331094],[393,389,1653703331110],[394,389,1653703331258],[410,397,1653703331277],[447,413,1653703331294],[926,422,1653703332781],[708,381,1653703332810],[631,360,1653703332827],[593,348,1653703332844],[579,343,1653703332860],[578,343,1653703332877],[578,342,1653703333394],[580,342,1653703333410],[582,341,1653703333460],[585,341,1653703333477],[584,342,1653703333560],[573,346,1653703333577],[553,349,1653703333594],[519,350,1653703333610],[476,350,1653703333627],[423,341,1653703333644],[364,327,1653703333660],[63,295,1653703335994],[65,294,1653703336011],[66,294,1653703336027],[67,293,1653703336044],[68,293,1653703336061],[69,292,1653703336077],[70,292,1653703336094],[72,292,1653703336110],[73,292,1653703336127],[75,292,1653703336144],[77,291,1653703336160],[82,291,1653703336177],[88,291,1653703336194]],"mm-mp":76.78481012658227,"md":[[578,343,1653703332892]],"md-mp":0,"mu":[[578,343,1653703332973]],"mu-mp":0},"v":1}'.replace('165370333', str(motionData['st'])[:9])

            h = {
                'sec-ch-ua': request.headers['sec-ch-ua'],
                'sec-ch-ua-mobile': request.headers['sec-ch-ua-mobile'],
                'user-agent': request.headers['user-agent'],
                'sec-ch-ua-platform': request.headers['sec-ch-ua-platform'],
                'content-type': request.headers['content-type'],
                'accept': request.headers['accept'],
                'origin': request.headers['origin'],
                'sec-fetch-site': request.headers['sec-fetch-site'],
                'sec-fetch-mode': request.headers['sec-fetch-mode'],
                'sec-fetch-dest': request.headers['sec-fetch-dest'],
                'referer': request.headers['referer'],
                'accept-encoding': request.headers['accept-encoding'],
                'accept-language': request.headers['accept-language'],
                'cookie': request.headers['cookie']
            }
            
            GeneratorThread(js, h, request.url).start()


#@logger.catch()
def runner(
    sample_site: str,
    lang: Optional[str] = "zh",
    silence: Optional[bool] = False,
    onnx_prefix: Optional[str] = None,
):
    """Human-Machine Challenge Demonstration | Top Interface"""
    #logger.info("Starting demo project...")

    # Instantiating Challenger Components
    challenger = ArmorCaptcha(dir_workspace=DIR_CHALLENGE, lang=lang, debug=False)
    challenger_utils = ArmorUtils()

    # Instantiating the Challenger Drive
    ctx = get_challenge_ctx(silence=__HEADLESS__, lang=lang)
    ctx.minimize_window()

    ctx.request_interceptor = interceptor

    os.system('cls')

    try:
        while True:
            try:
                # Read the hCaptcha challenge test site
                ctx.get(sample_site)

                # Detects if a clickable `hcaptcha checkbox` appears on the current page.
                # The `sample site` must pop up the `checkbox`, where the flexible wait time defaults to 5s.
                # If the `checkbox` does not load in 5s, your network is in a bad state.
                if not challenger_utils.face_the_checkbox(ctx):
                    break
                start = time.time()

                # Enter iframe-checkbox --> Process hcaptcha checkbox --> Exit iframe-checkbox
                challenger.anti_checkbox(ctx)

                #print('o')
                #time.sleep(125) try to sleep with proxyless mode

                # Enter iframe-content --> process hcaptcha challenge --> exit iframe-content
                resp = challenger.anti_hcaptcha(ctx, dir_model=DIR_MODEL, onnx_prefix=onnx_prefix)

                

                if resp == challenger.CHALLENGE_SUCCESS:
                    challenger.log(f"End of demo - total: {round(time.time() - start, 2)}s")
                    logger.success(f"PASS[{i + 1}|5]".center(28, "="))
                elif resp == challenger.CHALLENGE_RETRY:
                    ctx.refresh()

            # Do not capture the `ChallengeReset` signal in the outermost layer.
            # In the demo project, we wanted the human challenge to pop up, not pass after processing the checkbox.
            # So when this happens, we reload the page to activate hcaptcha repeatedly.
            # But in your project, if you've passed the challenge by just handling the checkbox,
            # there's no need to refresh the page!
            except ChallengePassed:
                ctx.refresh()
            except WebDriverException as err:
                logger.exception(err)
    finally:
        print("[EXIT] Press any key to exit...")

        pass


@logger.catch()
def test():
    """Check if the Challenger driver version is compatible"""
    ctx = get_challenge_ctx(silence=True)
    try:
        ctx.get(HCAPTCHA_DEMO_SITES[0])
    finally:
        ctx.quit()

    logger.success("The adaptation is successful")
