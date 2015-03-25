# coding=utf-8
# Install the Python Requests library:
# `pip install requests`

import requests
import json
import os
import sys

def send_request(threadid,page):
    # My API (11) (GET http://h.acfun.tv/api/t/117617)

    try:
        r = requests.get(
            url="http://h.koukuko.com/api/t/"+str(threadid),
            params = {
                "page":str(page),
            },
        )
        # print('Response HTTP Status Code : {status_code}'.format(status_code=r.status_code))
        # print('Response HTTP Response Body : {content}'.format(content=r.content))
        return r.content
    except requests.exceptions.RequestException as e:
        print('HTTP Request failed')

def get_img(threadsid):
    path = path+str(threadsid)
    os.system('mkdir '+path+'/')

    value = send_request(threadsid,1)
    o = json.loads(value)
    imgurl = imghost+str(o['threads']['image'])
    # print o['replys'][1]['image']
    totalreplay = int(o['threads']['replyCount'])
    totalpage = int(o['page']['size'])
    os.system('wget -P '+path+' '+imgurl)
    # print totalpage
    for page in range(1,totalpage+1):
        print page
        tempvalue = send_request(threadsid,page)
        o = json.loads(tempvalue)
        replyrange = totalreplay-(page-1)*20
        if replyrange>20:
            replyrange = 20
            # print "~"+str(replyrange)
        else:
            replyrange = totalreplay-(page-1)*20
            # print "~"+str(replyrange)
        # print o['replys'][1]['image']
        for replys in range(1,replyrange):
            replysimg = str(o['replys'][replys]['image'])
            if replysimg != "":
                imgurl = imghost+replysimg
                # print imgurl
                os.system('wget -P '+path+' '+imgurl)
        


imghost = "http://static.koukuko.com/h/"
path = "/Volumes/Transcend/Temp/Adao/"

#print len(sys.argv)
if len(sys.argv)==1:
    print "请运行时加入串ID作为参数"
else:
    threadsid = sys.argv[1]
    get_img(threadsid)
