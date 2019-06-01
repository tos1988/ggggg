#بِسْمِ اللهِ الرَّحْمنِ الرَّحِيمِ
# Maker : Khie # N̴̳̰̓ͬ͡ǫ̷̅̏̚ͅỗ͍̟̏͡b̴͙͙ͮ͢͜C̛͈̿ͥͣ͠ơ̡͑̈́ͩ͜d̼ͯ͋͌ͬ͡e̢̢̝̞̯̅ŗ̞̺̈̾̽ 
from linepy  import *
from liff.ttypes import LiffChatContext, LiffContext, LiffSquareChatContext, LiffNoneContext, LiffViewRequest
from akad.ttypes import Message
from akad.ttypes import ContentType as Type
from akad.ttypes import TalkException
from datetime import datetime, timedelta
from time import sleep
from bs4 import BeautifulSoup as bSoup
from bs4 import BeautifulSoup
from humanfriendly import format_timespan, format_size, format_number, format_length
from gtts import gTTS
from threading import Thread
from io import StringIO
from multiprocessing import Pool
from urllib.parse import urlencode
from tmp.MySplit import *
from random import randint
from Naked.toolshed.shell import execute_js
import subprocess, youtube_dl, humanize, traceback
import subprocess as cmd
import platform
import requests, json
import time, random, sys, json, null, pafy, codecs, html5lib ,shutil ,threading, glob, re, base64, string, os, requests, six, ast, pytz, wikipedia, urllib, urllib.parse, atexit, asyncio, traceback
_session = requests.session()
try:
    import urllib.request as urllib2
except ImportError:
    import urllib2
#=====================================================================
#=====================================================================
try:
    with open('token1.txt','r') as tokens:
        token = tokens.read()
    print(str(token))
except Exception as e:
    noobcoder = LINE()
noobcoder = LINE(token,appName="IOSIPAD\t11.2.5\tiPhone X\t11.2.5")
Channel(noobcoder, "1643727178").getChannelResult().channelAccessToken
waitOpen = codecs.open("khie/wait.json","r","utf-8")
settingsOpen = codecs.open("khie/temp.json","r","utf-8")
noobcoderProfile = noobcoder.getProfile()
noobcoderSettings = noobcoder.getSettings()
noobcoderPoll = OEPoll(noobcoder)
noobcoderStart = time.time()
noobcoderMID = noobcoder.getProfile().mid
loop = asyncio.get_event_loop()
admin =["u2cf74acf6ed04d122def4db8ffdd2e39"]
botStart = time.time()
kuciyose = {}
wait = json.load(waitOpen)
settings = json.load(settingsOpen)
mulai = time.time()

# BERANTAKAN

chatbot = {
    "admin": [],
    "botMute": [],
    "botOff": [],
}

read = { 
    "readMember": {},
    "readPoint": {}
}

sppam = {
  "list": [],
  "status": False
}
#=====================================================================
settings["myProfile"]["displayName"] = noobcoderProfile.displayName
settings["myProfile"]["statusMessage"] = noobcoderProfile.statusMessage
settings["myProfile"]["pictureStatus"] = noobcoderProfile.pictureStatus
cont = noobcoder.getContact(noobcoderMID)
settings["myProfile"]["videoProfile"] = cont.videoProfile
coverId = noobcoder.getProfileDetail()["result"]["objectId"]
settings["myProfile"]["coverId"] = coverId
#=====================================================================
with open("khie/temp.json", "r", encoding="utf_8_sig") as f:
    anu = json.loads(f.read())
    anu.update(settings)
    settings = anu
with open("khie/wait.json", "r", encoding="utf_8_sig") as f:
    itu = json.loads(f.read())
    itu.update(wait)
    wait = itu

#=====================================================================
def sendFooter(to, isi):
    data = {
        "type": "text",
        "text": isi,
        "sentBy": {
            "label": "JAVA SCRIPT",
            "iconUrl": "https://i.ibb.co/yqF3RcJ/Screenshot-2019-03-31-21-47-08-964-com-UCMobile-intl-picsay.png",
            "linkUrl": "line://nv/profilePopup/mid=u2cf74acf6ed04d122def4db8ffdd2e39"
        }
    }
    sendTemplate(to, data)
def sendTemplate(to, data):
    xyz = LiffChatContext(to)
    xyzz = LiffContext(chat=xyz)
    view = LiffViewRequest('1643727178-0XPGAaRX', xyzz)
    token = noobcoder.liff.issueLiffView(view)
    url = 'https://api.line.me/message/v3/share'
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer %s' % token.accessToken
    }
    data = {"messages":[data]}
    requests.post(url, headers=headers, data=json.dumps(data))
#=====================================================================
def restartBot():
    print ("[ INFO ] BOT RESETTED")
    backupData()
    python = sys.executable
    os.execl(python, python, *sys.argv)
#=====================================================================
def sendMessageCustom(to, text, icon , name):
    annda = {'MSG_SENDER_ICON': icon,
        'MSG_SENDER_NAME':  name,
    }
    noobcoder.sendMessage(to, text, contentMetadata=annda)
def sendMessageCustomContact(to, icon, name, mid):
    annda = { 'mid': mid,
    'MSG_SENDER_ICON': icon,
    'MSG_SENDER_NAME':  name,
    }
    noobcoder.sendMessage(to, '', annda, 13)    
#=====================================================================
def logError(text):
    noobcoder.log("ERROR 404 !\n" + str(text))
    tz = pytz.timezone("Asia/Jakarta")
    timeNow = datetime.now(tz=tz)
    timeHours = datetime.strftime(timeNow,"(%H:%M)")
    day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
    hari = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
    bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
    inihari = datetime.now(tz=tz)
    hr = inihari.strftime('%A')
    bln = inihari.strftime('%m')
    for i in range(len(day)):
        if hr == day[i]: hasil = hari[i]
    for k in range(0, len(bulan)):
        if bln == str(k): bln = bulan[k-1]
    time = hasil + ", " + inihari.strftime('%d') + " - " + bln + " - " + inihari.strftime('%Y') + " | " + inihari.strftime('%H:%M:%S')
    with open("khie/errorLog.txt","a") as error:
        error.write("\n[%s] %s" % (str(time), text))
#=====================================================================
def command(text):
    pesan = text.lower()
    if settings["setKey"] == True:
        if pesan.startswith(settings["keyCommand"]):
            cmd = pesan.replace(settings["keyCommand"],"")
        else:
            cmd = "Undefined command"
    else:
        cmd = text.lower()
    return cmd
#=====================================================================
def removeCmd(cmd, text):
	key = settings["keyCommand"]
	if settings["setKey"] == False: key = ''
	rmv = len(key + cmd) + 1
	return text[rmv:]
#=====================================================================
def backupData():
    try:
        backup = settings
        f = codecs.open('khie/temp.json','w','utf-8')
        json.dump(backup, f, sort_keys=True, indent=4, ensure_ascii=False)
        backup = wait
        f = codecs.open('khie/wait.json','w','utf-8')
        json.dump(backup, f, sort_keys=True, indent=4, ensure_ascii=False)
        return True
    except Exception as error:
        logError(error)
        return False
#=====================================================================
async def noobcoderBot(op):
    try:
        if settings["restartPoint"] != None:
            noobcoder.sendMessage(settings["restartPoint"], 'Activated♪')
            settings["restartPoint"] = None
        if op.type == 0:
            return
#=====================================================================
#=====================================================================
        if op.type == 25:
            print("[ 25 ] SEND MESSAGE")
            msg = op.message
            text = str(msg.text)
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
            to = msg.to
            isValid = True
            cmd = command(text)
            setkey = settings['keyCommand'].title()
            if settings['setKey'] == False: setkey = ''
            if isValid != False:
                if msg.contentType == 0:
                    if msg.toType == 0 or msg.toType == 2:
                        if cmd == "logout" and sender == noobcoderMID:
                            noobcoder.generateReplyMessage(msg.id)
                            noobcoder.sendReplyMessage(msg.id, to, "Your selfbot has been logout ♪")
                            sys.exit("Logout")
                        elif cmd == "help":
                            sendFooter(to, "Help Message :\n\n1. @kickall\n2. @kick <name>\n3. @bypass\n4. @target on/off\n5. @gc spam <name>\n6. @groups\n7. @reject all")
                        elif cmd == "@kickall":
                          xyz = noobcoder.getGroup(to)
                          mem = [c.mid for c in xyz.members]
                          targets = []
                          for x in mem:
                            if x not in ["u2cf74acf6ed04d122def4db8ffdd2e39","u09c11f239846b06539d08608099f7733",noobcoder.profile.mid]:targets.append(x)
                          if targets:
                            imnoob = 'simple.js gid={} token={} app={}'.format(to, noobcoder.authToken, "IOSIPAD\t11.2.5\tiPhone X\t11.2.5")
                            for target in targets:
                              imnoob += ' uid={}'.format(target)
                            success = execute_js(imnoob)
                            if success:noobcoder.sendMessage(to, "Success kick %i members." % len(targets))
                            else:noobcoder.sendMessage(to, "Failed kick %i members." % len(targets))
                          else:noobcoder.sendMessage(to, "Target not found.")
                        elif cmd == "@bypass":
                          xyz = noobcoder.getGroup(to)
                          if xyz.invitee == None:pends = []
                          else:pends = [c.mid for c in xyz.invitee]
                          targp = []
                          for x in pends:
                            if x not in ["u2cf74acf6ed04d122def4db8ffdd2e39","u09c11f239846b06539d08608099f7733",noobcoder.profile.mid]:targp.append(x)
                          mems = [c.mid for c in xyz.members]
                          targk = []
                          for x in mems:
                            if x not in ["u2cf74acf6ed04d122def4db8ffdd2e39","u09c11f239846b06539d08608099f7733",noobcoder.profile.mid]:targk.append(x)
                          imnoob = 'dual.js gid={} token={}'.format(to, noobcoder.authToken)
                          for x in targp:imnoob += ' uid={}'.format(x)
                          for x in targk:imnoob += ' uik={}'.format(x)
                          execute_js(imnoob)
                        elif cmd.startswith("@kick "):
                           sep = text.split(" ")
                           midn = text.replace(sep[0] + " ","")
                           hmm = text.lower()
                           G = noobcoder.getGroup(msg.to)
                           members = [G.mid for G in G.members]
                           targets = []
                           imnoob = 'simple.js gid={} token={} app={}'.format(to, noobcoder.authToken, "IOSIPAD\t11.2.5\tiPhone X\t11.2.5")
                           for x in members:
                               contact = noobcoder.getContact(x)
                               msg = op.message
                               testt = contact.displayName.lower()
                                   #print(testt)
                               if midn in testt:targets.append(contact.mid)
                           if targets == []:return noobcoder.sendMessage(to,"not found name "+midn)
                           for target in targets:
                             imnoob += ' uid={}'.format(target)
                           success = execute_js(imnoob)
                        elif cmd.startswith("@gc spam "):
                          nm = text.replace("@gc spam ","")
                          if sppam["list"] != []:
                            imnoob = "spam.js name={} token={}".format(nm,noobcoder.authToken)
                            for target in sppam["list"]:
                              noobcoder.findAndAddContactsByMid(target)
                              imnoob += " uid={}".format(target)
                            success = execute_js(imnoob)
                            if success:noobcoder.sendMessage(to,"Done")
                            else:noobcoder.sendMessage(to,"Error")
                          else:noobcoder.sendMessage(to,"target is empty.")
                        elif cmd == "@target on":
                          sppam["status"] = True
                          noobcoder.sendMessage(to,"send a contact.")
                        elif cmd == "@target off":
                          sppam["status"] = False
                          noobcoder.sendMessage(to,"done.")
                        elif cmd == "@reject all":
                          gids = noobcoder.getGroupIdsInvited()
                          xyzs = []
                          for x in gids:xyzs.append(x)
                          for x in gids:
                            noobcoder.acceptGroupInvitation(x)
                          for x in xyzs:
                            noobcoder.leaveGroup(x)
                          noobcoder.sendMessage(to, "Success reject %i invitation." % len(xyzs))
                        elif cmd == "@groups":
                            key = settings["keyCommand"].title()
                            if settings['setKey'] == False:key = ''
                            gid = noobcoder.getGroupIdsJoined()
                            sd = noobcoder.getGroups(gid)
                            ret = "「 Group List 」\n"
                            no = 0
                            total = len(gid)
                            cd = "\n\nTotal {} Groups".format(total)
                            for G in sd:
                                member = len(G.members)
                                no += 1
                                ret += "\n{}. {} | {}".format(no, G.name[0:20], member)
                            ret += cd
                            k = len(ret)//10000
                            for aa in range(k+1):
                                sendFooter(to,'{}'.format(ret[aa*10000 : (aa+1)*10000]))

                if msg.contentType == 13 and sppam["status"] == True:
                  if msg.contentMetadata["mid"] not in sppam["list"]:
                    sppam["list"].append(msg.contentMetadata["mid"])
                    noobcoder.sendMessage(to,"user added to list.")
                  else:
                    noobcoder.sendMessage(to,"user already in list.")
#=====================================================================
        if op.type == 55:
            if op.param1 in read["readPoint"]:
                _name = noobcoder.getContact(op.param2).displayName
                tz = pytz.timezone("Asia/Jakarta")
                timeNow = datetime.now(tz=tz)
                timeHours = datetime.strftime(timeNow," (%H:%M)")
                read["readMember"][op.param1][op.param2] = str(_name) + str(timeHours)

        backupData()
    except Exception as error:
        logError(error)
        traceback.print_tb(error.__traceback__)
   

def run():
    while True:
        try:
            ops = noobcoderPoll.singleTrace(count=50)
            if ops != None:
                for op in ops:
                   loop.run_until_complete(noobcoderBot(op))
                   noobcoderPoll.setRevision(op.revision)
        except Exception as e:
            logError(e)
            
if __name__ == "__main__":
    run()