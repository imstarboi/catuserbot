from pyrogram import Client,filters
from pyrogram.types import ChatPermissions,ChatEventFilter
from pyrogram.raw.types import InputPeerUser
from pyrogram.raw.functions.messages import DeleteHistory
from pyrogram.raw.functions.account import DeleteAccount
import time,redis
import jdatetime
from random import choice , randint
import asyncio
from datetime import datetime
import json
import wikipedia
from prettytable import PrettyTable
from requests import get
#Mohammad
helptxt='''
~**𝗖𝗼𝗹𝗲𝗦𝗲𝗹𝗳**~
✵✵✵✵✵✵✵✵✵✵✵✵✵✵✵✵✵✵✵✵
╔════❰**🄷🄴🄻🄿**❱═❍⊱❁
║╭━━━━━━━━━━━━━━━➣ 
║┣⪼ `anshlp` -> **𝚊𝚞𝚝𝚘 𝚊𝚗𝚜𝚠𝚎𝚛 𝚑𝚎𝚕𝚙**
║┣⪼ `fhlp` -> **𝚎𝚗𝚎𝚖𝚢 𝚑𝚎𝚕𝚙**
║┣⪼ `gphlp` -> **𝚐𝚛𝚘𝚞𝚙 𝚑𝚎𝚕𝚙**
║┣⪼ `funhlp` -> **𝚏𝚞𝚗 𝚑𝚎𝚕𝚙**
║┣⪼ `shlp` -> **𝚎𝚗𝚝𝚎𝚛𝚝𝚊𝚒𝚗𝚖𝚎𝚗𝚝 𝚑𝚎𝚕𝚙**
║┣⪼ **𝑫𝒆𝒗=**Amiralirj** & 𝑬𝒅𝒊𝒕=**🩺`ᵐᵒʰᵃᵐᵐᵃᵈ`🩺
║╰━━━━━━━━━━━━━━━➣
╚══════════════════❍⊱❁
'''
foshhelp='''
~**𝗖𝗼𝗹𝗲𝗦𝗲𝗹𝗳**~
✵✵✵✵✵✵✵✵✵✵✵✵✵✵✵✵✵✵✵✵
╔════❰🅔︎🅝︎🅔︎🅜︎🅨︎ 🅗︎🅔︎🅛︎🅟︎❱═❍⊱❁
║╭━━━━━━━━━━━━━━━➣ 
║┣⪼ `enemy` -> [𝒓𝒆𝒑𝒍𝒚]**𝚜𝚎𝚝 𝚎𝚗𝚎𝚖𝚢**
║┣⪼ `friend` -> [𝒓𝒆𝒑𝒍𝒚]**𝚍𝚎𝚕 𝚎𝚗𝚎𝚖𝚢**
║┣⪼ `all f` -> **𝚍𝚎𝚕 𝚊𝚕𝚕 𝚎𝚗𝚎𝚖𝚢**
║┣⪼ `fosh` -> **𝚜𝚎𝚝 𝚏𝚘𝚜𝚑 𝚖𝚘𝚍 𝙾𝚗 𝚘𝚛 𝙾𝚏𝚏**
║┣⪼ **𝑫𝒆𝒗=**Amiralirj** & 𝑬𝒅𝒊𝒕=**🩺`ᵐᵒʰᵃᵐᵐᵃᵈ`🩺
║╰━━━━━━━━━━━━━━━➣
╚══════════════════❍⊱❁
'''
gphelp='''
~**𝗖𝗼𝗹𝗲𝗦𝗲𝗹𝗳**~
✵✵✵✵✵✵✵✵✵✵✵✵✵✵✵✵✵✵✵✵
╔══❰**🅖︎🅡︎🅞︎🅤︎🅟︎ 🅗︎🅔︎🅛︎🅟︎**❱═❍⊱❁
║╭━━━━━━━━━━━━━━━➣ 
║┣⪼ `id` -> [𝒓𝒆𝒑𝒍𝒚]**𝚐𝚎𝚝 𝚒𝚍**
║┣⪼ `pinn` -> [𝒓𝒆𝒑𝒍𝒚]**𝚙𝚒𝚗 𝚊 𝚖𝚎𝚜𝚜𝚊𝚐𝚎**
║┣⪼ `unpinn` -> [𝒓𝒆𝒑𝒍𝒚]**𝚞𝚗𝚙𝚒𝚗 𝚊 𝚖𝚎𝚜𝚜𝚊𝚐𝚎**
║┣⪼ `bann` -> [𝒓𝒆𝒑𝒍𝒚]**𝚋𝚊𝚗 𝚊 𝚖𝚎𝚖𝚋𝚎𝚛**
║┣⪼ `bann` -> [𝒓𝒆𝒑𝒍𝒚]**𝚞𝚗𝚋𝚊𝚗 𝚊 𝚖𝚎𝚖𝚎𝚋𝚎𝚛**
║┣⪼ `lockk` -> **𝚕𝚘𝚌𝚔 𝚐𝚛𝚘𝚞𝚙**
║┣⪼ `unlockk` -> **𝚞𝚗𝚕𝚘𝚌𝚔 𝚐𝚛𝚘𝚞𝚙**
║┣⪼ `leave` -> **𝚕𝚎𝚊𝚟𝚎 𝚏𝚛𝚘𝚖 𝚐𝚛𝚘𝚞𝚙**
║┣⪼ `/left` -> [𝒐𝒏 | 𝒐𝒇𝒇]**𝚗𝚘 𝚗𝚎𝚠 𝚐𝚛𝚘𝚞𝚙**
║┣⪼ `delmy` -> **𝚍𝚎𝚕 𝚊𝚕𝚕 𝚜𝚎𝚕𝚏 𝚖𝚜𝚐**
║┣⪼ `tagg` -> **𝚝𝚊𝚐𝚐 𝚖𝚎𝚖𝚋𝚎𝚛𝚜**
║┣⪼ `stopp` -> **𝚜𝚝𝚘𝚙 𝚝𝚊𝚐𝚐**
║┣⪼ `deltagg` -> **𝚍𝚎𝚕 𝚜𝚎𝚕𝚏 𝚝𝚊𝚐𝚜**
║┣⪼ `/speed` -> [0.1~10]**𝚜𝚙𝚎𝚎𝚍 𝚘𝚏 𝚝𝚊𝚐𝚐**
║┣⪼ `sett` -> [𝒓𝒆𝒑𝒍𝒚]**𝚜𝚎𝚝 𝚝𝚊𝚐𝚐 𝚝𝚎𝚡𝚝**
║┣⪼ **𝑫𝒆𝒗=**Amiralirj** & 𝑬𝒅𝒊𝒕=**🩺`ᵐᵒʰᵃᵐᵐᵃᵈ`🩺
║╰━━━━━━━━━━━━━━━➣
╚══════════════════❍⊱❁
'''
anshelp='''
~**𝗖𝗼𝗹𝗲𝗦𝗲𝗹𝗳**~
✵✵✵✵✵✵✵✵✵✵✵✵✵✵✵✵✵✵✵✵
╔❰︎🅐︎🅤︎🅣︎🅞︎ 🅐︎🅝︎🅢︎🅦︎🅔︎🅡︎ 🅗︎🅔︎🅛︎🅟︎❱═❍⊱❁
║╭━━━━━━━━━━━━━━━➣ 
║┣⪼ `/setans` -> [𝙷𝚒 | 𝙷𝚎𝚕𝚕𝚘]**𝚜𝚎𝚝 𝚊𝚗𝚜𝚠𝚎𝚛**
║┣⪼ `/delans` -> [𝙷𝚒]**𝚍𝚎𝚕 𝚊𝚗𝚜𝚠𝚎𝚛**
║┣⪼ `anslist` -> **𝚕𝚒𝚜𝚝 𝚘𝚏 𝚊𝚗𝚜𝚠𝚎𝚛𝚜**
║┣⪼ `/cleanallans` -> **𝚍𝚎𝚕 𝚊𝚕𝚕 𝚊𝚗𝚜𝚠𝚎𝚛𝚜**
║┣⪼ **𝑫𝒆𝒗=**Amiralirj** & 𝑬𝒅𝒊𝒕=**🩺`ᵐᵒʰᵃᵐᵐᵃᵈ`🩺
║╰━━━━━━━━━━━━━━━➣
╚══════════════════❍⊱❁
'''
funhelp='''
~**𝗖𝗼𝗹𝗲𝗦𝗲𝗹𝗳**~
✵✵✵✵✵✵✵✵✵✵✵✵✵✵✵✵✵✵✵✵
╔════❰**🅕︎🅤︎🅝︎ 🅗︎🅔︎🅛︎🅟︎**❱═❍⊱❁
║╭━━━━━━━━━━━━━━━➣ 
║┣⪼ `corona` -> **𝚐𝚎𝚝 𝚌𝚟_19
𝚜𝚝𝚊𝚝𝚎**
║┣⪼ `fal` -> **khorafat bmola**
║┣⪼ `/corona` -> [𝒄𝒐𝒖𝒏𝒕𝒓𝒚]**𝚌𝚟_19 𝚜𝚝𝚊𝚝𝚎 𝚙𝚛 𝚌**
║┣⪼ `reload` -> **𝚏𝚞𝚗𝚛𝚎𝚕𝚘𝚊𝚍𝚒𝚗𝚐**
║┣⪼ `/cat` -> **𝚛𝚊𝚗𝚍𝚘𝚖 𝚙𝚒𝚌 𝚘𝚏 𝚌𝚊𝚝**
║┣⪼ `/dog` -> **𝚛𝚊𝚗𝚍𝚘𝚖 𝚙𝚒𝚌 𝚘𝚏 𝚍𝚘𝚐**
║┣⪼ `love` and `🤍` and `🖐`
║┣⪼ `dobsdobs`
║┣⪼ `نخوندم`
║┣⪼ **𝑫𝒆𝒗=**Amiralirj** & 𝑬𝒅𝒊𝒕=**🩺`ᵐᵒʰᵃᵐᵐᵃᵈ`🩺
║╰━━━━━━━━━━━━━━━➣
╚══════════════════❍⊱❁
'''
shelp='''
~**𝗖𝗼𝗹𝗲𝗦𝗲𝗹𝗳**~
✵✵✵✵✵✵✵✵✵✵✵✵✵✵✵✵✵✵✵✵
╔════❰**🅢︎🅔︎🅛︎🅕︎ 🅗︎🅔︎🅛︎🅟︎**❱═❍⊱❁
║╭━━━━━━━━━━━━━━━➣ 
║┣⪼ `spam` -> []1~100][𝒓𝒆𝒑𝒍𝒚]**𝚏𝚕𝚘𝚘𝚍**
║┣⪼ `today` -> **𝚍𝚊𝚝𝚎 𝚊𝚗𝚍 𝚝𝚒𝚖𝚎**
║┣⪼ `usrinf` -> [𝒓𝒆𝒑𝒍𝒚]**𝚐𝚎𝚝 𝚞𝚜𝚎𝚛 𝚒𝚗𝚏𝚘**
║┣⪼ `block` -> [𝒓𝒆𝒑𝒍𝒚]**𝚋𝚕𝚘𝚌𝚔 𝚙𝚎𝚛𝚜𝚘𝚗**
║┣⪼ `unblock` -> [𝒓𝒆𝒑𝒍𝒚]**𝚞𝚗𝚋𝚕𝚘𝚌𝚔 𝚙𝚎𝚛𝚜𝚘𝚗**
║┣⪼ `/wiki` -> [𝒕𝒆𝒙𝒕]**𝚜𝚛𝚌𝚑 𝚒𝚗 𝚠𝚒𝚔𝚒
║┣⪼ `/wikifa` -> [𝒕𝒆𝒙𝒕]**𝚙𝚎𝚛𝚜𝚒𝚊𝚗 𝚠𝚒𝚔𝚒**
║┣⪼ `/login` -> [𝒐𝒏 | 𝒐𝒇𝒇]**𝚕𝚘𝚌𝚔 𝚕𝚘𝚐𝚒𝚗**
║┣⪼ `offline` -> [𝒐𝒏 | 𝒐𝒇𝒇][𝒕𝒆𝒙𝒕 𝒐𝒑𝒕𝒊𝒐𝒏𝒂𝒍]
║┣⪼ **𝑫𝒆𝒗=**Amiralirj** & 𝑬𝒅𝒊𝒕=**🩺`ᵐᵒʰᵃᵐᵐᵃᵈ`🩺
║╰━━━━━━━━━━━━━━━➣
╚══════════════════❍⊱❁
'''
# -----fosh-----
one = [
  "کیرم",
  "دسته مبل",
  "آیفون صوتی با سیم",
  "آیفون تصویری ",
  "کیر خمینی(ره)",
  "دسته جارو",
  "چاقو میوه خوری",
  "یخچال ساید بای ساید",
  "هایپ ایرانی",
  "شمشیر جومونگ",
  "بالشت قرمز درازا",
]

tow = [
  "نشستگاه",
  "صورت",
  "ناف",
  "کون",
  "رون",
  "کص",
  "چشم",
  "قیافه",
]

three = [
  "مادر جندت",
  "خاله فاحشت",
  "عمه کیرخوارت",
  "اقوام درجه یکت",
  "خودت",
  "خواهرت",
]

four = [
  "تو",
  "وسط",
  "لا",
  "بین",
]
emoji = [
  "😂",
  "😂😂",
  " ",
]

def fosh_saz():
  o1 = random.choice(one)
  o2 = random.choice(tow)
  o3 = random.choice(three)
  o4 = random.choice(four)
  o5 = random.choice(emoji)
  fosh_txt = f"{o1} {o4} {o2} {o3} {o5}"
  return fosh_txt
#-------
biomod = 0
lname = 0
#-------
api_id =3004334
api_hash = 'd397c51379c24e45aed0d984ebca414b'
bot = Client('Cole-Self', api_id, api_hash,workers=7)
mtx=""
speed=1
autotag=0
mutes = [
    "text",
    "photo",
    "sticker",
    "gif",
    "voice",
]
foshlist = []
fmaker = ("off")
fosh = []

with bot:
    admin=bot.get_me().id
    me=bot.get_me().first_name


# Do not edit this part -------------------------------------------------
Has_Sended=list()
Answer_Dic=dict()
is_tagging =dict()



safe_turn=0
safe_blk=0
action_type=0
Offline_text=''
welcome=False
welcome_txt='welcome:)'


Anti_Login=False
left_gaps=False
New_PV=False
offline=False



mute_group = ChatPermissions(can_send_messages=False)
unmute_group = ChatPermissions(
    can_send_messages=True,
    can_send_other_messages=True,
    can_send_media_messages=True,
    can_send_polls=True,
  )
# -----------------help-----------------
@bot.on_message(filters.me & filters.regex('(?i)^help$'))
def help(c,m):
  m.edit_text(helptxt)
@bot.on_message(filters.me & filters.regex('(?i)^anshlp$'))
def help(c,m):
  m.edit_text(anshelp)
@bot.on_message(filters.me & filters.regex('(?i)^safhlp$'))
def help(c,m):
  m.edit_text(safhelp)
@bot.on_message(filters.me & filters.regex('(?i)^gphlp$'))
def help(c,m):
  m.edit_text(gphelp)
@bot.on_message(filters.me & filters.regex('(?i)^funhlp$'))
def help(c,m):
  m.edit_text(funhelp)
@bot.on_message(filters.me & filters.regex('(?i)^lovhlp$'))
def help(c,m):
  m.edit_text(lovhelp)
@bot.on_message(filters.me & filters.regex('(?i)^shlp$'))
def help(c,m):
  m.edit_text(shelp)
@bot.on_message(filters.me & filters.regex('(?i)^fhlp$'))
def help(c,m):
  m.edit_text(foshhelp)
# --------------end help--------------
# ---------------ping-----------------
@bot.on_message( filters.me & filters.regex('(?i)^ping$'))
def ping(c,m):
    m.edit_text(
'**Online**')
# ---------------Tagger---------------
def add_istagging(chat_id):
    global is_tagging
    if chat_id not in is_tagging:
        is_tagging.update({chat_id: False})
# --------------------------------------
@bot.on_message(filters.me & filters.regex('(?i)^tagg$'))
def tagge2r(c,m):
    global is_tagging
    rag=''
    s=0
    chat_id = m.chat.id
    add_istagging(chat_id)
    m.edit_text('Ok')
    if not is_tagging[chat_id]:
        is_tagging[chat_id] = True
        chat_members = bot.iter_chat_members(chat_id=chat_id)
        for usr in chat_members:
            if usr['user']['username']:
                if is_tagging[chat_id]:
                    bot.send_chat_action(chat_id, 'typing')
                    if not usr.user.is_bot:
                        rag+= f"**{(mtx)} {usr.user.mention()} ** \n "
                        s+=1
                        if s==1:
                            bot.send_message(chat_id,rag)
                            rag=''
                            s=0
                            time.sleep(speed)
                else:
                    return
        is_tagging[chat_id] = False
# ------------------------------------
@bot.on_message(filters.me & filters.regex('(?i)^stopp$'))
def Stop_Tag(c,m):
    global is_tagging
    chat_id = m.chat.id
    if is_tagging[chat_id]:
        is_tagging[chat_id] = False
        m.edit_text('ok')
# --------------------------------------
@bot.on_message(filters.command(['speed']) & filters.group)
def stwerop(c,m):
    global speed
    speed=float(m.command[1])
    m.edit_text(f"setted {speed}")
# -------------------------------------
@bot.on_message(filters.me & filters.regex('(?i)^sett$'))
def sto1p(c,m):
    global mtx
    if m.reply_to_message:
        mtx = m.reply_to_message.text
        m.edit_text("setted")
    else:
        m.edit_text('**pls reply to a msg**')
# --------------------------------------
@bot.on_message(filters.me & filters.regex('(?i)^deltagg$'))
def Delete_Tags(c,m):
    x=0
    chatid = m.chat.id
    m.edit_text(f"ok")
    try:
        tag_msgs = [msg for msg in bot.iter_history(chatid,limit=1000) if msg.entities]
        for tagmsg in tag_msgs:
            for ent in tagmsg.entities:
              if ent.type in ("mention", "text_mention"):
               if tagmsg.from_user.id==(admin):
                 tagmsg.delete()
                 x+=1
               else:
                 x+=1
                 time.sleep(0)
                 time.sleep(0)
        m.reply_text(f"{x} tag deleted ")
    except Exception as e:
        m.reply_text(f"Error: {e}")
# -------------------------------------
@bot.on_message(filters.me & filters.regex('(?i)^delmy$'))
def Delete_msgs(c,m):
    x=0
    chatid = m.chat.id
    m.edit_text(f"ok")
    try:
        msgs = [msg for msg in bot.iter_history(chatid,limit=1000)]
        for my_msgs in msgs:
            if my_msgs.from_user.id==(admin):
               my_msgs.delete()
               x+=1
            else:
               x+=1
               time.sleep(0)
        c.send_message(f"{x} deleted ")
    except Exception as e:
        c.send_message(f"Error: {e}")
# --------------End Tagger-------------
# -----------time name--------------
@bot.on_message(filters.me & filters.regex('bio on'))
def bio_time(c,m):
  biomod = 1
  m.edit_text('bio mod running')
  while True:
    if biomod == 1:
      t = jdatetime.datetime.now().strftime("%H:%M")
      name = bot.get_me().first_name
      nametime = (f"time is: '{t}'")
      bot.update_profile(bio=nametime)
      time.sleep(60)
# --------------------------------------
@bot.on_message(filters.me & filters.regex('bio off'))
def bio_time(c,m):
  biomod = 0
  m.edit_text('name time is off now')
# -------------------------------------
@bot.on_message(filters.me & filters.regex('lname on'))
def bio_time(c,m):
  lname = 1
  m.edit_text('lname running')
  while True:
    if lname == 1:
      t = jdatetime.datetime.now().strftime("%H:%M")
      nametime = (t)
      bot.update_profile(last_name=nametime)
    time.sleep(60)
# --------------------------------------
@bot.on_message(filters.me & filters.regex('lname off'))
def bio_time(c,m):
  lname = 0
  bot.update_profile(last_name=" ")
  m.edit_text('name time is off now')
# ------------Block&Unblock-------------
@bot.on_message( filters.me & (filters.regex('(?i)^block$')))
def Block(c,m):
    id=m.reply_to_message.from_user.id
    bot.block_user(id)
    m.edit_text('user blocked')
# --------------------------------------
@bot.on_message( filters.me & (filters.regex('(?i)^unblock$')))
def Unblock(c,m):
    id=m.reply_to_message.from_user.id
    bot.unblock_user(id)
    m.edit_text('user unblocked')
# --------------Pin&Unpin-------------------
@bot.on_message(filters.group & filters.reply & filters.regex("^[Pp]inn$") , group=1)
def pin(c,m):
    myid = m.from_user.id
    if myid != admin:return
    msgid = m.reply_to_message.message_id
    text = f"**Pinned**"
    bot.edit_message_text(m.chat.id,m.message_id,text)
    bot.pin_chat_message(m.chat.id,msgid )
# --------------------------------------
@bot.on_message(filters.group & filters.reply & filters.regex("^[Uu]npinn$") , group=1)
def pin(c,m):
    myid = m.from_user.id
    if myid != admin:return
    msgid = m.reply_to_message.message_id
    text = f"**UnPinned**"
    bot.edit_message_text(m.chat.id,m.message_id,text)
    bot.unpin_chat_message(m.chat.id,msgid )
# -------------Ban&Unban----------------
@bot.on_message(filters.me & filters.regex('(?i)^bann$'))
def ban(c,m):
    if m.reply_to_message:
      bot.kick_chat_member(m.chat.id, m.reply_to_message.from_user.id)
      m.edit_text(f'{m.reply_to_message.mention} **banned** ')
    else:
        id=(str(m.text[4:]))
        try:
            user=bot.get_users(int(id))
            bot.kick_chat_member(m.chat.id,int(id))
            m.edit_text(f'{user.mention} **banned** ')
        except:
            try:
                user=bot.get_users(id)
                bot.kick_chat_member(m.chat.id,id)
                m.edit_text(f'{user.mention} **banned** ')
            except:
                m.edit_text('please use username or pear id after command ')
# --------------------------------------
@bot.on_message(filters.me & filters.regex('(?i)^unbann$'))
def unban(c,m):
    if m.reply_to_message:
      bot.unban_chat_member(m.chat.id, m.reply_to_message.from_user.id)
      m.edit_text(f'{m.reply_to_message.mention} **Unbanned** ')
    else:
        id=(str(m.text[6:]))
        try:
            user=bot.get_users(int(id))
            bot.unban_chat_member(m.chat.id,int(id))
            m.edit_text(f'{user.mention} Unbanned ')
        except:
            try:
                user=bot.get_users(id)
                bot.unban_chat_member(m.chat.id,id)
                m.edit_text(f'{user.mention} Unbanned ')
            except:
                m.edit_text('please use username or pear id after command ')
# --------------------------------------
@bot.on_message(filters.me & filters.regex('(?i)^lockk$'))
def lock(c,m):
    bot.set_chat_permissions(m.chat.id, mute_group)
    m.edit_text('group locked')
# --------------------------------------
@bot.on_message(filters.me & filters.regex('(?i)^unlockk$'))
def unlock_command(c,m):
    bot.set_chat_permissions(m.chat.id, unmute_group)
    m.edit_text('group unlocked')
# -------------Wiki------------------
@bot.on_message( filters.me & filters.command(['wiki']))
def wikipedia_search(c,m):
    try:
        text=m.text[6:]
        wikipedia.set_lang('en')
        result = wikipedia.page(text)
        m.edit_text(result.summary[0:1000])
    except :
        m.edit_text('does not match any pages. Try another id! ')
# --------------------------------------
@bot.on_message( filters.me & filters.command(['wikifa']))
def wikipedia_search_fa(c,m):
    try:
        text=m.text[8:]
        wikipedia.set_lang('fa')
        result = wikipedia.page(text)
        m.edit_text(result.summary[0:1000])
    except:
        m.edit_text('صفحه ای با این مضمون پیدا نشد  ')
# --------------Enemy---------------
@bot.on_message(filters.regex("^[Ee]nemy$") & filters.reply)
def addblacklist(c,m):
    global foshlist
    myid = m.from_user.id
    userid = m.reply_to_message.from_user.id
    if myid != admin:return
    foshlist.append(str(userid))
    bot.delete_messages(m.chat.id,[m.message_id])
# --------------------------------------
@bot.on_message(filters.regex("^[Ff]riend$") & filters.reply)
def delblacklist(c,m):
    global foshlist
    myid = m.from_user.id
    userid = m.reply_to_message.from_user.id
    if myid != admin:return
    foshlist.remove(str(userid))
    bot.delete_messages(m.chat.id,[m.message_id])       
# --------------------------------------
@bot.on_message(filters.regex("^[Aa]ll f$"))
def cole_clearf(c,m):
    global foshlist
    myid = m.from_user.id
    if myid != admin:return
    foshlist.clear
    send = bot.edit_message_text(m.chat.id,m.message_id,"All Friends")
    bot.delete_messages(m.chat.id,[send.message_id])
# --------------------------------------
@bot.on_message(filters.regex("^[Ff]osh$") & filters.me)
def cole_foshmaker(c,m):
  global fmaker
  if fmaker == "on":
      fmaker = "off"
      text = "FoshSaz Is `OFF` Now"
  else:
      fmaker = "on"
      text = "FoshSaz Is `ON` Now"

      bot.edit_message_text(m.chat.id,m.message_id,text)
# --------------------------------------
@bot.on_message(filters.me & filters.regex('^spam (\d*)$') & filters.reply )
def spam(c,m):
    msgid = m.reply_to_message.message_id
    chatid = m.chat.id
    spam = int(m.text.split(" ")[1])
    for i in range(spam):
        bot.forward_messages(
            chat_id=chatid,
            from_chat_id=chatid,
            message_ids=[msgid]
        )
# --------------------------------------
@bot.on_message(filters.me & filters.regex('(?i)^usrinf'))
def UserId(c,m):
    try:
        if m.reply_to_message:
            id=m.reply_to_message.from_user.id
            User_Info=bot.get_users(id)
            photo=bot.get_profile_photos(id,limit=2)[0]
            if User_Info.is_deleted:
                m.edit_text('user is deleted')
            else:
                details=(f'''User Info:●{User_Info.mention}●
username:●@{User_Info.username}●
status:●{User_Info.status}●
pear id:●{User_Info.id}●
dc id :●{User_Info.dc_id }●''')
                bot.reply_photo(photo=photo.file_id,caption=details)
    except:
        id=m.reply_to_message.from_user.id
        User_Info=bot.get_users(id)
        if User_Info.is_deleted:
            m.edit_text('user is deleted')
        else:
            details=(f'''     User Info
    {User_Info.mention}
username:@{User_Info.username}
status:{User_Info.status}
pear id: {User_Info.id}
dc id :{User_Info.dc_id }''')
            m.edit_text(details)
    else:
        try:
            id=int(str(m.text)[7:])
            User_Info=bot.get_users(id)
            photo=bot.get_profile_photos(id,limit=2)[0]
            if User_Info.is_deleted:
                m.edit_text('user is deleted')
            else:
                details=(f'''     User Info
    {User_Info.mention}
username:@{User_Info.username}
status:{User_Info.status}
pear id: {User_Info.id}
dc id :{User_Info.dc_id }''')
            bot.reply_photo(photo=photo,caption=details)
        except:
            id=(str(m.text))[9:]
            User_Info=bot.get_users(id)
            if User_Info.is_deleted:
                m.edit_text('user is deleted')
            else:
                details=(f'''     User Info
    {User_Info.mention}
username:@{User_Info.username}
status:{User_Info.status}
pear id: {User_Info.id}
dc id :{User_Info.dc_id }''')
            m.edit_text(details)
# ---------------Welcome----------------
@bot.on_message( filters.me & filters.command(['wel']))
def welcome_func(c,m):
    global welcome
    on_off=str(m.command[1])
    if on_off.lower()=='on':
        welcome=True
        m.edit_text(f'welcome is {on_off} now')
    elif on_off.lower()=='off':
        welcome=False
        m.edit_text(f'welcome is {on_off} now')
# --------------------------------------
@bot.on_message( filters.me & filters.command(['welset']))
def welcome_txt_func(c,m):
    global welcome_text
    try:
        welcome_text=str(m.reply_to_message.text)
        m.edit_text(f'welcome text setted : {welcome_text}')
    except:
        m.edit_text(f'reply this command to welcome text')
# -------------Auto Answer------------
def answer(c,m):
    '''answer to the submited texted '''
    global Answer_Dic
    for i in Answer_Dic:
        if str(m.text) in str(i).strip() or str(m.text)==str(i).strip():
            x=m.reply_text(Answer_Dic[i])
            Has_Sended.append(x.message_id)
# --------------------------------------
@bot.on_message( filters.me & filters.command(['setans']))
def Set_Answer(c,m):
    answer=str(m.text).split('|')[-1]
    text=str(m.text)[7:].split('|')[0]
    Answer_Dic[text]=answer
    m.edit_text(f'this answer {text} setted for {answer} text ')
# --------------------------------------
@bot.on_message( filters.me & filters.command(['delans']))
def Delete_Answer(c,m):
    try:
        text=m.text[11:]
        m.edit_text(f'this answer {text} deleted with {Answer_Dic[text]} text ')
        Answer_Dic.pop(text)
    except:
        m.edit_text(f'this text {text} is not in answer list ')
# --------------------------------------
@bot.on_message( filters.me & filters.regex('(?i)^anslist$'))
def AnswerList(c,m):
    Answer_List='answers : \n \n'
    num=1
    for i in Answer_Dic:
        Answer_List+=f'{num}- {i} --- {Answer_Dic[i]} \n '
    m.edit_text(Answer_List)
# --------------------------------------
@bot.on_message( filters.me & filters.regex('(?i)^cleanallans$'))
def CleanAnswerList(c,m):
    Answer_Dic.clear()
    m.edit_text('cleaned')
# --------------------------------------
@bot.on_message(filters.me & (filters.regex('^فال')|filters.regex('^fal')))
def fal_Func(c,m):
    bot.send_photo(m.chat.id, f"https://seemorgh.com/images/fal/hafez/{randint(1, 163)}.gif", reply_to_message_id=m.message_id)
# --------------------------------------
@bot.on_message(filters.me & filters.regex('^XO (\d*)$'))
def XO_Anim(c,m,events):
    msgid = m.reply_to_message.message_id
    chatid = m.chat.id
    loptime = int(m.text.split(" ")[1])
    repetition_txt = m.text.split(" ")[2]
    msg = events.respond(repetition_txt)
    for i in range(loptime):
        for j in range(len(repetition_txt)):
            if repetition_txt[j] != ' ':
                m.edit_text(msg, repetition_txt[0:j+1])
# ------------------------------_id--------
@bot.on_message( filters.me & filters.command(['typing']))
def copy_Text_func(c,m):
    global action_type
    text=str(m.command[1])
    if text.lower()=='copy' :
        action_type=1
        m.edit_text('copy mode on')

    if text.lower()=='bold' :
        action_type=2
        m.edit_text('bold mode on')

    if text.lower()=='off' :
        action_type=0
        m.edit_text('typing edit is of now')
# ---------------Corona----------------
@bot.on_message(filters.me & filters.regex('(?i)^corona$'))
def corona_All(_,m):
  try:
    r = get("https://corona.lmao.ninja/v2/all?yesterday=true").json()
    last_update = datetime.fromtimestamp(r["updated"]/1000).strftime("%Y-%m-%d %I:%M:%S")
    ac = PrettyTable()
    ac.header = False
    ac.title = "Global Statistics"
    ac.add_row(["Cases", f"{r['cases']:,}"])
    ac.add_row(["Cases Today", f"{r['todayCases']:,}"])
    ac.add_row(["Deaths", f"{r['deaths']:,}"])
    ac.add_row(["Deaths Today", f"{r['todayDeaths']:,}"])
    ac.add_row(["Recovered", f"{r['recovered']:,}"])
    ac.add_row(["Active", f"{r['active']:,}"])
    ac.add_row(["Critical", f"{r['critical']:,}"])
    ac.align = "l"
    m.edit_text(f"'''{str(ac)}'''\nLast Updated on: {last_update}")
  except Exception as e:
    m.edit_text("'api corona not found'")
    print(e)
    time.sleep(3)
    m.delete()
# --------------------------------------
@bot.on_message(filters.me & filters.command('corona'))
def corona_c(_,m):
  cmd = m.command
  if not (len(cmd)>=2):
    m.edit_text('not enough provided')
    time.sleep(3)
    m.delete()
  country = cmd[1]
  m.edit_text('Getting corona state for: '+ country)
  r = get(f"https://corona.lmao.ninja/v2/countries/{country}").json()
  if "cases" not in r:
    m.edit_text('not available in this country')
    time.sleep(3)
    m.delete()
  else:
    last_update = datetime.fromtimestamp(r["updated"]/1000).strftime("%Y-%m-%d %I:%M:%S")
    cc = PrettyTable()
    cc.header = False
    country = r["countryInfo"]["iso3"] if len(r["country"]) > 12 else r["country"]
    cc.title = f"corona state in {country}"
    cc.add_row(["Population", f"{r['population']:,}"])
    cc.add_row(["Cases", f"{r['cases']:,}"])
    cc.add_row(["Cases Today", f"{r['todayCases']:,}"])
    cc.add_row(["Deaths", f"{r['deaths']:,}"])
    cc.add_row(["Deaths Today", f"{r['todayDeaths']:,}"])
    cc.add_row(["Recovered", f"{r['recovered']:,}"])
    cc.add_row(["Active", f"{r['active']:,}"])
    cc.add_row(["critical", f"{r['critical']:,}"])
    cc.add_row(["Tests", f"{r['tests']:,}"])
    cc.align = "l"
    m.edit_text(f"'''{str(cc)}'''\nLast Updated on: {last_update}")
# --------------------------------------
@bot.on_message(filters.me & filters.command(['cat']))
def meow(c,m):
  r = get("https://api.thecatapi.com/v1/images/search")
  rj = r.json()
  m.reply_photo(rj[0]["url"])
  m.delete()
# --------------------------------------
@bot.on_message(filters.me & filters.command(['dog']))
def woof(c,m):
  r = get("https://random.dog/woof.json")
  rj = r.json()
  m.reply_photo(rj["url"])
  m.delete()
# --------------------------------------
@bot.on_message( filters.me & filters.regex('(?i)^bid$'))
def bid(c,m):
  giveVar = m.text
  bid = giveVar[4:5]
  if not bid:
    bid = "😂"
    m.edit_text( f"{bid}{bid}{bid}{bid}{bid}{bid}{bid}\n{bid}{bid}{bid}{bid}{bid}{bid}{bid}{bid}\n{bid}{bid} {bid}{bid}\n{bid}{bid} {bid}{bid}\n{bid}{bid}{bid}{bid}{bid}{bid}{bid}{bid}\n{bid}{bid}{bid}{bid}{bid}{bid}{bid}{bid}\n{bid}{bid}{bid}{bid}{bid}{bid}{bid}{bid}\n{bid}{bid} {bid}{bid}\n{bid}{bid} {bid}{bid}\n{bid}{bid}{bid}{bid}{bid}{bid}{bid}{bid}\n{bid}{bid}{bid}{bid}{bid}{bid}{bid}\n\n{bid}{bid}{bid}{bid}{bid}{bid}\n{bid}{bid}{bid}{bid}{bid}{bid}\n {bid}{bid}\n {bid}{bid}\n {bid}{bid}\n {bid}{bid}\n {bid}{bid}\n {bid}{bid}\n{bid}{bid}{bid}{bid}{bid}{bid}\n{bid}{bid}{bid}{bid}{bid}{bid}\n\n{bid}{bid} {bid}{bid}\n{bid}{bid}{bid} {bid}{bid}\n{bid}{bid}{bid}{bid} {bid}{bid}\n{bid}{bid} {bid}{bid} {bid}{bid}\n{bid}{bid} {bid}{bid} {bid}{bid}\n{bid}{bid} {bid}{bid} {bid}{bid}\n{bid}{bid} {bid}{bid} {bid}{bid}\n{bid}{bid} {bid}{bid}{bid}{bid}\n{bid}{bid} {bid}{bid}{bid}\n{bid}{bid} {bid}{bid}\n\n {bid}{bid}{bid}{bid}{bid}\n {bid}{bid}{bid}{bid}{bid}{bid}{bid}\n {bid}{bid} {bid}{bid}\n {bid}{bid} {bid}{bid}\n{bid}{bid} {bid}{bid}\n{bid}{bid} {bid}{bid}\n {bid}{bid} {bid}{bid}\n {bid}{bid} {bid}{bid}\n {bid}{bid}{bid}{bid}{bid}{bid}{bid}\n {bid}{bid}{bid}{bid}{bid}\n\n{bid}{bid}{bid}{bid}{bid}{bid}{bid}\n{bid}{bid}{bid}{bid}{bid}{bid}{bid}{bid}\n{bid}{bid} {bid}{bid}\n{bid}{bid} {bid}{bid}\n{bid}{bid} {bid}{bid}\n{bid}{bid} {bid}{bid}\n{bid}{bid} {bid}{bid}\n{bid}{bid} {bid}{bid}\n{bid}{bid}{bid}{bid}{bid}{bid}{bid}{bid}\n{bid}{bid}{bid}{bid}{bid}{bid}{bid}" )
# --------------------------------------

# --------------------------------------
@bot.on_message( filters.me & filters.regex('(?i)^fakk$'))
def fu_fun(c, m): 
  time.sleep(0.5) 
  m.edit_text(''' 
‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌🏿🏿🏿🏿🏿 
       🏿🏿🏿🏿🏿🏿 
      🏿🏿 
     🏿🏿 
🏿🏿🏿🏿🏿 
🏿🏿🏿🏿🏿 
     🏿🏿 
     🏿🏿 
     🏿🏿 
     🏿🏿 
''') 
  time.sleep(0.5) 
  m.edit_text(''' 
🖕🖕                  🖕🖕 
🖕🖕                  🖕🖕 
🖕🖕                  🖕🖕 
🖕🖕                  🖕🖕 
 🖕🖕                🖕🖕 
   🖕🖕🖕🖕🖕🖕 🖕🖕 
        🖕🖕🖕🖕      🖕🖕 
''') 
  time.sleep(0.5) 
  m.edit_text(''' 
‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ 🏿🏿🏿🏿🏿 
    🏿🏿🏿🏿🏿🏿🏿 
 🏿🏿 
🏿🏿 
 🏿🏿 
    🏿🏿🏿🏿🏿🏿🏿 
         🏿🏿🏿🏿🏿 
''') 
  time.sleep(0.5) 
  m.edit_text(''' 
🖕🖕 
🖕🖕 
🖕🖕            🖕🖕 
🖕🖕       🖕🖕 
🖕🖕     🖕🖕 
🖕🖕🖕🖕 
🖕🖕  🖕🖕 
🖕🖕      🖕🖕 
🖕🖕          🖕🖕 
🖕🖕             🖕🖕 
''') 
  time.sleep(0.5) 
  m.edit_text(''' 
🏿🏿              🏿🏿 
  🏿🏿          🏿🏿 
     🏿🏿      🏿🏿 
        🏿🏿  🏿🏿 
           🏿🏿🏿 
              🏿🏿 
             🏿🏿 
            🏿🏿 
           🏿🏿 
          🏿🏿 
''') 
  time.sleep(0.5) 
  m.edit_text(''' 
‌ ‌‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌🖕🖕🖕🖕 
    🖕🖕🖕🖕🖕🖕 
 🖕🖕               🖕🖕 
🖕🖕                 🖕🖕 
 🖕🖕               🖕🖕 
    🖕🖕🖕🖕🖕🖕 
         🖕🖕🖕🖕 
''') 
  time.sleep(0.5) 
  m.edit_text(''' 
🏿🏿                  🏿🏿 
🏿🏿                  🏿🏿 
🏿🏿                  🏿🏿 
🏿🏿                  🏿🏿 
 🏿🏿                🏿🏿 
   🏿🏿🏿🏿🏿🏿 🏿🏿 
        🏿🏿🏿🏿      🏿🏿 
''') 
  time.sleep(1) 
  m.edit_text(''' 
   ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌🏿🏿🏿🏿🏿 
       🏿🏿🏿🏿🏿🏿 
      🏿🏿 
     🏿🏿 
🏿🏿🏿🏿🏿 
🏿🏿🏿🏿🏿 
     🏿🏿 
     🏿🏿 
     🏿🏿 
     🏿🏿 
 
 
 
 
🖕🖕                  🖕🖕 
🖕🖕                  🖕🖕 
🖕🖕                  🖕🖕 
🖕🖕                  🖕🖕 
 🖕🖕                🖕🖕 
   🖕🖕🖕🖕🖕🖕 🖕🖕 
        🖕🖕🖕🖕      🖕🖕 
 
 
 
 
         🏿🏿🏿🏿🏿 
    🏿🏿🏿🏿🏿🏿🏿 
 🏿🏿 
🏿🏿 
 🏿🏿 
    🏿🏿🏿🏿🏿🏿🏿 
         🏿🏿🏿🏿🏿 
 
🖕🖕 
🖕🖕 
🖕🖕            🖕🖕 
🖕🖕       🖕🖕 
🖕🖕     🖕🖕 
🖕🖕🖕🖕 
🖕🖕  🖕🖕 
🖕🖕      🖕🖕 
🖕🖕          🖕🖕 
🖕🖕             🖕🖕 
 
 
 
 
 
🏿🏿              🏿🏿 
  🏿🏿          🏿🏿 
     🏿🏿      🏿🏿 
        🏿🏿  🏿🏿 
           🏿🏿🏿 
              🏿🏿 
             🏿🏿 
            🏿🏿 
           🏿🏿 
          🏿🏿 
 
 
 
 
         🖕🖕🖕🖕 
    🖕🖕🖕🖕🖕🖕 
 🖕🖕               🖕🖕 
🖕🖕                 🖕🖕 
 🖕🖕               🖕🖕 
    🖕🖕🖕🖕🖕🖕 
         🖕🖕🖕🖕 
 
 
 
 
🏿🏿                  🏿🏿 
🏿🏿                  🏿🏿 
🏿🏿                  🏿🏿 
🏿🏿                  🏿🏿 
 🏿🏿                🏿🏿 
   🏿🏿🏿🏿🏿🏿 🏿🏿 
        🏿🏿🏿🏿      🏿🏿 
''')
# --------------------------------------
@bot.on_message( filters.me & filters.regex('(?i)^beee$'))
def fu_fun(c, m): 
  time.sleep(0.5) 
  m.edit_text(''' 
☹
''') 
  time.sleep(0.5) 
  m.edit_text(''' 
🤪
''') 
  time.sleep(0.5) 
  m.edit_text(''' 
😘 
''') 
  time.sleep(0.5) 
  m.edit_text(''' 
🤩
''') 
  time.sleep(0.5) 
  m.edit_text('''
 😎
''') 
  time.sleep(0.5) 
  m.edit_text(''' 
😉         
''') 
  time.sleep(0.5) 
  m.edit_text('''
 🙃
''') 
  time.sleep(1) 
  m.edit_text('''
🤤
''')
# --------------------------------------
@bot.on_message( filters.me & filters.regex('(?i)^mnij$'))
def fu_fun(c, m): 
  time.sleep(0.5) 
  m.edit_text(''' 
💩
''') 
  time.sleep(0.5) 
  m.edit_text(''' 
🤪
''') 
  time.sleep(0.5) 
  m.edit_text(''' 
🙃 
''') 
  time.sleep(0.5) 
  m.edit_text(''' 
🤩
''') 
  time.sleep(0.5) 
  m.edit_text('''
 🥳
''') 
  time.sleep(0.5) 
  m.edit_text(''' 
😉         
''') 
  time.sleep(0.5) 
  m.edit_text('''
 🤤
''') 
  time.sleep(1) 
  m.edit_text('''
🤪
''')
# --------------------------------------
@bot.on_message( filters.me & filters.regex('(?i)^joon$'))
def fu_fun(c, m): 
  time.sleep(0.5) 
  m.edit_text(''' 
🚶🏽‍♂️
''') 
  time.sleep(0.5) 
  m.edit_text(''' 
🚶🏽‍♂️🚶🏽‍♂️
''') 
  time.sleep(0.5) 
  m.edit_text(''' 
🚶🏽‍♂️🚶🏽‍♂️🚶🏽‍♂️ 
''') 
  time.sleep(0.5) 
  m.edit_text(''' 
🚶🏽‍♂️🚶🏽‍♂️🚶🏽‍♂️🚶🏽‍♂️
''') 
  time.sleep(0.5) 
  m.edit_text('''
 🚶🏽‍♂️🚶🏽‍♂️🚶🏽‍♂️🚶🏽‍♂️🚶🏽‍♂️
''') 
  time.sleep(0.5) 
  m.edit_text(''' 
🚶🏽‍♂️🚶🏽‍♂️🚶🏽‍♂️🚶🏽‍♂️🚶🏽‍♂️🚶🏽‍♂️         
''') 
  time.sleep(0.5) 
  m.edit_text('''
 🚶🏽‍♂️🚶🏽‍♂️🚶🏽‍♂️🚶🏽‍♂️🚶🏽‍♂️🚶🏽‍♂️🚶🏽‍♂️
''') 
  time.sleep(1) 
  m.edit_text('''
هعیییپ🚶🏽‍♂️🚶🏽‍♂️🚶🏽‍♂️
''')
# --------------------------------------
@bot.on_message( filters.me & filters.regex('(?i)^offs$'))
def fu_fun(c, m): 
  time.sleep(0.5) 
  m.edit_text(''' 
ژون🤤
''') 
  time.sleep(0.5) 
  m.edit_text(''' 
اوفس 🤤
''') 
  time.sleep(0.5) 
  m.edit_text(''' 
بیععع🤤 
''') 
  time.sleep(0.5) 
  m.edit_text(''' 
نیا اون طور ها🤤
''') 
  time.sleep(0.5) 
  m.edit_text('''
 😐
   
       😐

                😐

           😐

       😐
   
       😐

                😐

           😐

       😐
   
       😐

                😐

           😐

       😐
   
       😐

                😐

           😐

       😐
   
       😐

                😐

           😐

       😐
   
       😐

                😐

           😐

       😐
   
       😐

                😐

           😐

       😐
   
       😐

                😐

           😐

       😐
   
       😐

                😐

           😐

       😐
   
       😐

                😐

           😐

       😐
   
       😐

                😐

           😐

       😐
   
       😐

                😐

           😐

       😐
''') 
  time.sleep(0.5) 
  m.edit_text(''' 
🍑         
''') 
  time.sleep(0.5) 
  m.edit_text('''
 نود🤤
''') 
  time.sleep(1) 
  m.edit_text('''
⠛⠛⣿⣿⣿⣿⣿⡷⢶⣦⣶⣶⣤⣤⣤⣀   
   ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⡀ 
   ⠉⠉⠉⠙⠻⣿⣿⠿⠿⠛⠛⠛⠻⣿⣿⣇ 
  ⢤⣀⣀⣀  ⢸⣷   ⣁⣀⣤⣴⣿⣿⣿⣆
    ⠹⠏   ⣿⣧ ⠹⣿⣿⣿⣿⣿⡿⣿
         ⠛⠿⠇⢀⣼⣿⣿⠛⢯⡿⡟
          ⠦⠴⢿⢿⣿⡿⠷ ⣿ 
       ⠙⣷⣶⣶⣤⣤⣤⣤⣤⣶⣦⠃ 
       ⢐⣿⣾⣿⣿⣿⣿⣿⣿⣿⣿  
       ⠈⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇
''')
# --------------------------------------
@bot.on_message( filters.me & filters.regex('(?i)^iopa$'))
def fu_fun(c, m): 
  time.sleep(0.5) 
  m.edit_text(''' 
👊🏿👇🏿👇🏿👇🏿👇🏿👇🏿👇🏿👇🏿👇🏿👇🏿👊🏿
👉🏿👍🏾👇🏾👇🏾👇🏾👇🏾👇🏾👇🏾👇🏾👍🏾👈🏿
👉🏿👉🏾👍🏽👇🏽👇🏽👇🏽👇🏽👇🏽👍🏽👈🏾👈🏿
👉🏿👉🏾👉🏽👍🏼👇🏼👇🏼👇🏼👍🏼👈🏽👈🏾👈🏿
👉🏿👉🏾👉🏽👉🏼👍🏻👇🏻👍🏻👈🏼👈🏽👈🏾👈🏿
👉🏿👉🏾👉🏽👉🏼👉🏻😐👈🏻👈🏼👈🏽👈🏾👈🏿
👉🏿👉🏾👉🏽👉🏼👍🏻👆🏻👍🏻👈🏼👈🏽👈🏾👈🏿
👉🏿👉🏾👉🏽👍🏼👆🏼👆🏼👆🏼👍🏼👈🏽👈🏾👈🏿
👉🏿👉🏾👍🏽👆🏽👆🏽👆🏽👆🏽👆🏽👍🏽👈🏾👈🏿
👉🏿👍🏾👆🏾👆🏾👆🏾👆🏾👆🏾👆🏾👆🏾👍🏾👈🏿
👊🏿👆🏿👆🏿👆🏿👆🏿👆🏿👆🏿👆🏿👆🏿👆🏿👊🏿
''') 
  time.sleep(0.5) 
  m.edit_text(''' 
👊🏿👇🏿👇🏿👇🏿👇🏿👇🏿👇🏿👇🏿👇🏿👇🏿👊🏿
👉🏿👍🏾👇🏾👇🏾👇🏾👇🏾👇🏾👇🏾👇🏾👍🏾👈🏿
👉🏿👉🏾👍🏽👇🏽👇🏽👇🏽👇🏽👇🏽👍🏽👈🏾👈🏿
👉🏿👉🏾👉🏽👍🏼👇🏼👇🏼👇🏼👍🏼👈🏽👈🏾👈🏿
👉🏿👉🏾👉🏽👉🏼👍🏻👇🏻👍🏻👈🏼👈🏽👈🏾👈🏿
👉🏿👉🏾👉🏽👉🏼👉🏻😂👈🏻👈🏼👈🏽👈🏾👈🏿
👉🏿👉🏾👉🏽👉🏼👍🏻👆🏻👍🏻👈🏼👈🏽👈🏾👈🏿
👉🏿👉🏾👉🏽👍🏼👆🏼👆🏼👆🏼👍🏼👈🏽👈🏾👈🏿
👉🏿👉🏾👍🏽👆🏽👆🏽👆🏽👆🏽👆🏽👍🏽👈🏾👈🏿
👉🏿👍🏾👆🏾👆🏾👆🏾👆🏾👆🏾👆🏾👆🏾👍🏾👈🏿
👊🏿👆🏿👆🏿👆🏿👆🏿👆🏿👆🏿👆🏿👆🏿👆🏿👊🏿
''') 
  time.sleep(0.5) 
  m.edit_text(''' 
👊🏿👇🏿👇🏿👇🏿👇🏿👇🏿👇🏿👇🏿👇🏿👇🏿👊🏿
👉🏿👍🏾👇🏾👇🏾👇🏾👇🏾👇🏾👇🏾👇🏾👍🏾👈🏿
👉🏿👉🏾👍🏽👇🏽👇🏽👇🏽👇🏽👇🏽👍🏽👈🏾👈🏿
👉🏿👉🏾👉🏽👍🏼👇🏼👇🏼👇🏼👍🏼👈🏽👈🏾👈🏿
👉🏿👉🏾👉🏽👉🏼👍🏻👇🏻👍🏻👈🏼👈🏽👈🏾👈🏿
👉🏿👉🏾👉🏽👉🏼👉🏻🤤👈🏻👈🏼👈🏽👈🏾👈🏿
👉🏿👉🏾👉🏽👉🏼👍🏻👆🏻👍🏻👈🏼👈🏽👈🏾👈🏿
👉🏿👉🏾👉🏽👍🏼👆🏼👆🏼👆🏼👍🏼👈🏽👈🏾👈🏿
👉🏿👉🏾👍🏽👆🏽👆🏽👆🏽👆🏽👆🏽👍🏽👈🏾👈🏿
👉🏿👍🏾👆🏾👆🏾👆🏾👆🏾👆🏾👆🏾👆🏾👍🏾👈🏿
👊🏿👆🏿👆🏿👆🏿👆🏿👆🏿👆🏿👆🏿👆🏿👆🏿👊🏿 
''') 
  time.sleep(0.5) 
  m.edit_text(''' 
👊🏿👇🏿👇🏿👇🏿👇🏿👇🏿👇🏿👇🏿👇🏿👇🏿👊🏿
👉🏿👍🏾👇🏾👇🏾👇🏾👇🏾👇🏾👇🏾👇🏾👍🏾👈🏿
👉🏿👉🏾👍🏽👇🏽👇🏽👇🏽👇🏽👇🏽👍🏽👈🏾👈🏿
👉🏿👉🏾👉🏽👍🏼👇🏼👇🏼👇🏼👍🏼👈🏽👈🏾👈🏿
👉🏿👉🏾👉🏽👉🏼👍🏻👇🏻👍🏻👈🏼👈🏽👈🏾👈🏿
👉🏿👉🏾👉🏽👉🏼👉🏻🤪👈🏻👈🏼👈🏽👈🏾👈🏿
👉🏿👉🏾👉🏽👉🏼👍🏻👆🏻👍🏻👈🏼👈🏽👈🏾👈🏿
👉🏿👉🏾👉🏽👍🏼👆🏼👆🏼👆🏼👍🏼👈🏽👈🏾👈🏿
👉🏿👉🏾👍🏽👆🏽👆🏽👆🏽👆🏽👆🏽👍🏽👈🏾👈🏿
👉🏿👍🏾👆🏾👆🏾👆🏾👆🏾👆🏾👆🏾👆🏾👍🏾👈🏿
👊🏿👆🏿👆🏿👆🏿👆🏿👆🏿👆🏿👆🏿👆🏿👆🏿👊🏿
''') 
  time.sleep(0.5) 
  m.edit_text('''
 👊🏿👇🏿👇🏿👇🏿👇🏿👇🏿👇🏿👇🏿👇🏿👇🏿👊🏿
👉🏿👍🏾👇🏾👇🏾👇🏾👇🏾👇🏾👇🏾👇🏾👍🏾👈🏿
👉🏿👉🏾👍🏽👇🏽👇🏽👇🏽👇🏽👇🏽👍🏽👈🏾👈🏿
👉🏿👉🏾👉🏽👍🏼👇🏼👇🏼👇🏼👍🏼👈🏽👈🏾👈🏿
👉🏿👉🏾👉🏽👉🏼👍🏻👇🏻👍🏻👈🏼👈🏽👈🏾👈🏿
👉🏿👉🏾👉🏽👉🏼👉🏻😎👈🏻👈🏼👈🏽👈🏾👈🏿
👉🏿👉🏾👉🏽👉🏼👍🏻👆🏻👍🏻👈🏼👈🏽👈🏾👈🏿
👉🏿👉🏾👉🏽👍🏼👆🏼👆🏼👆🏼👍🏼👈🏽👈🏾👈🏿
👉🏿👉🏾👍🏽👆🏽👆🏽👆🏽👆🏽👆🏽👍🏽👈🏾👈🏿
👉🏿👍🏾👆🏾👆🏾👆🏾👆🏾👆🏾👆🏾👆🏾👍🏾👈🏿
👊🏿👆🏿👆🏿👆🏿👆🏿👆🏿👆🏿👆🏿👆🏿👆🏿👊🏿
''') 
  time.sleep(0.5) 
  m.edit_text(''' 
👊🏿👇🏿👇🏿👇🏿👇🏿👇🏿👇🏿👇🏿👇🏿👇🏿👊🏿
👉🏿👍🏾👇🏾👇🏾👇🏾👇🏾👇🏾👇🏾👇🏾👍🏾👈🏿
👉🏿👉🏾👍🏽👇🏽👇🏽👇🏽👇🏽👇🏽👍🏽👈🏾👈🏿
👉🏿👉🏾👉🏽👍🏼👇🏼👇🏼👇🏼👍🏼👈🏽👈🏾👈🏿
👉🏿👉🏾👉🏽👉🏼👍🏻👇🏻👍🏻👈🏼👈🏽👈🏾👈🏿
👉🏿👉🏾👉🏽👉🏼👉🏻🤯👈🏻👈🏼👈🏽👈🏾👈🏿
👉🏿👉🏾👉🏽👉🏼👍🏻👆🏻👍🏻👈🏼👈🏽👈🏾👈🏿
👉🏿👉🏾👉🏽👍🏼👆🏼👆🏼👆🏼👍🏼👈🏽👈🏾👈🏿
👉🏿👉🏾👍🏽👆🏽👆🏽👆🏽👆🏽👆🏽👍🏽👈🏾👈🏿
👉🏿👍🏾👆🏾👆🏾👆🏾👆🏾👆🏾👆🏾👆🏾👍🏾👈🏿
👊🏿👆🏿👆🏿👆🏿👆🏿👆🏿👆🏿👆🏿👆🏿👆🏿👊🏿         
''') 
  time.sleep(0.5) 
  m.edit_text('''
 👊🏿👇🏿👇🏿👇🏿👇🏿👇🏿👇🏿👇🏿👇🏿👇🏿👊🏿
👉🏿👍🏾👇🏾👇🏾👇🏾👇🏾👇🏾👇🏾👇🏾👍🏾👈🏿
👉🏿👉🏾👍🏽👇🏽👇🏽👇🏽👇🏽👇🏽👍🏽👈🏾👈🏿
👉🏿👉🏾👉🏽👍🏼👇🏼👇🏼👇🏼👍🏼👈🏽👈🏾👈🏿
👉🏿👉🏾👉🏽👉🏼👍🏻👇🏻👍🏻👈🏼👈🏽👈🏾👈🏿
👉🏿👉🏾👉🏽👉🏼👉🏻🥸👈🏻👈🏼👈🏽👈🏾👈🏿
👉🏿👉🏾👉🏽👉🏼👍🏻👆🏻👍🏻👈🏼👈🏽👈🏾👈🏿
👉🏿👉🏾👉🏽👍🏼👆🏼👆🏼👆🏼👍🏼👈🏽👈🏾👈🏿
👉🏿👉🏾👍🏽👆🏽👆🏽👆🏽👆🏽👆🏽👍🏽👈🏾👈🏿
👉🏿👍🏾👆🏾👆🏾👆🏾👆🏾👆🏾👆🏾👆🏾👍🏾👈🏿
👊🏿👆🏿👆🏿👆🏿👆🏿👆🏿👆🏿👆🏿👆🏿👆🏿👊🏿
''') 
  time.sleep(1) 
  m.edit_text('''
😎
''')
# --------------------------------------
@bot.on_message( filters.me & filters.regex('(?i)^mooa$'))
def fu_fun(c, m): 
  time.sleep(0.10) 
  m.edit_text(''' 
⣿⣿⡄⢨⣻⣽⣿⣟⣿⣞⣗⡽⡸⡐⢸⣿⣿⣿⣿⣿⣿⣿ 
⣿⣿⡇⢀⢗⣿⣿⣿⣿⡿⣞⡵⡣⣊⢸⣿⣿⣿⣿⣿⣿⣿ 
⣿⣿⣿⡀⡣⣗⣿⣿⣿⣿⣯⡯⡺⣼⠎⣿⣿⣿⣿⣿⣿⣿ 
⣿⣿⣿⣧⠐⡵⣻⣟⣯⣿⣷⣟⣝⢞⡿⢹⣿⣿⣿⣿⣿⣿ 
⣿⣿⣿⣿⡆⢘⡺⣽⢿⣻⣿⣗⡷⣹⢩⢃⢿⣿⣿⣿⣿⣿ 
⣿⣿⣿⣿⣷⠄⠪⣯⣟⣿⢯⣿⣻⣜⢎⢆⠜⣿⣿⣿⣿⣿ 
⣿⣿⣿⣿⣿⡆⠄⢣⣻⣽⣿⣿⣟⣾⡮⡺⡸⠸⣿⣿⣿⣿ 
⣿⣿⡿⠛⠉⠁⠄⢕⡳⣽⡾⣿⢽⣯⡿⣮⢚⣅⠹⣿⣿⣿ 
⡿⠋⠄⠄⠄⠄⢀⠒⠝⣞⢿⡿⣿⣽⢿⡽⣧⣳⡅⠌⠻⣿
''') 
  time.sleep(0.10) 
  m.edit_text('''  
⣿⣿⣿⣿⡿⠁⠄⣳⢷⣿⣿⣿⣿⡿⣝⠖⠄⣿⣿⣿⣿⣿ 
⣿⣿⣿⣿⠃⠄⢢⡹⣿⢷⣯⢿⢷⡫⣗⠍⢰⣿⣿⣿⣿⣿ 
⣿⣿⣿⡏⢀⢄⠤⣁⠋⠿⣗⣟⡯⡏⢎⠁⢸⣿⣿⣿⣿⣿ 
⣿⣿⣿⠄⢔⢕⣯⣿⣿⡲⡤⡄⡤⠄⡀⢠⣿⣿⣿⣿⣿⣿ 
⣿⣿⠇⠠⡳⣯⣿⣿⣾⢵⣫⢎⢎⠆⢀⣿⣿⣿⣿⣿⣿⣿ 
⣿⣿⠄⢨⣫⣿⣿⡿⣿⣻⢎⡗⡕⡅⢸⣿⣿⣿⣿⣿⣿⣿ 
⣿⣿⠄⢜⢾⣾⣿⣿⣟⣗⢯⡪⡳⡀⢸⣿⣿⣿⣿⣿⣿⣿ 
⣿⣿⠄⢸⢽⣿⣷⣿⣻⡮⡧⡳⡱⡁⢸⣿⣿⣿⣿⣿⣿⣿ 
⣿⣿⡄⢨⣻⣽⣿⣟⣿⣞⣗⡽⡸⡐⢸⣿⣿⣿⣿⣿⣿⣿
''') 
  time.sleep(0.10) 
  m.edit_text(''' 
⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⠛⢉⢉⠉⠉⠻⣿⣿⣿⣿⣿⣿ 
⣿⣿⣿⣿⣿⣿⣿⠟⠠⡰⣕⣗⣷⣧⣀⣅⠘⣿⣿⣿⣿⣿ 
⣿⣿⣿⣿⣿⣿⠃⣠⣳⣟⣿⣿⣷⣿⡿⣜⠄⣿⣿⣿⣿⣿ 
''') 
  
  time.sleep(1) 
  m.edit_text('''
⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⠛⢉⢉⠉⠉⠻⣿⣿⣿⣿⣿⣿ 
⣿⣿⣿⣿⣿⣿⣿⠟⠠⡰⣕⣗⣷⣧⣀⣅⠘⣿⣿⣿⣿⣿ 
⣿⣿⣿⣿⣿⣿⠃⣠⣳⣟⣿⣿⣷⣿⡿⣜⠄⣿⣿⣿⣿⣿ 
⣿⣿⣿⣿⡿⠁⠄⣳⢷⣿⣿⣿⣿⡿⣝⠖⠄⣿⣿⣿⣿⣿ 
⣿⣿⣿⣿⠃⠄⢢⡹⣿⢷⣯⢿⢷⡫⣗⠍⢰⣿⣿⣿⣿⣿ 
⣿⣿⣿⡏⢀⢄⠤⣁⠋⠿⣗⣟⡯⡏⢎⠁⢸⣿⣿⣿⣿⣿ 
⣿⣿⣿⠄⢔⢕⣯⣿⣿⡲⡤⡄⡤⠄⡀⢠⣿⣿⣿⣿⣿⣿ 
⣿⣿⠇⠠⡳⣯⣿⣿⣾⢵⣫⢎⢎⠆⢀⣿⣿⣿⣿⣿⣿⣿ 
⣿⣿⠄⢨⣫⣿⣿⡿⣿⣻⢎⡗⡕⡅⢸⣿⣿⣿⣿⣿⣿⣿ 
⣿⣿⠄⢜⢾⣾⣿⣿⣟⣗⢯⡪⡳⡀⢸⣿⣿⣿⣿⣿⣿⣿ 
⣿⣿⠄⢸⢽⣿⣷⣿⣻⡮⡧⡳⡱⡁⢸⣿⣿⣿⣿⣿⣿⣿ 
⣿⣿⡄⢨⣻⣽⣿⣟⣿⣞⣗⡽⡸⡐⢸⣿⣿⣿⣿⣿⣿⣿ 
⣿⣿⡇⢀⢗⣿⣿⣿⣿⡿⣞⡵⡣⣊⢸⣿⣿⣿⣿⣿⣿⣿ 
⣿⣿⣿⡀⡣⣗⣿⣿⣿⣿⣯⡯⡺⣼⠎⣿⣿⣿⣿⣿⣿⣿ 
⣿⣿⣿⣧⠐⡵⣻⣟⣯⣿⣷⣟⣝⢞⡿⢹⣿⣿⣿⣿⣿⣿ 
⣿⣿⣿⣿⡆⢘⡺⣽⢿⣻⣿⣗⡷⣹⢩⢃⢿⣿⣿⣿⣿⣿ 
⣿⣿⣿⣿⣷⠄⠪⣯⣟⣿⢯⣿⣻⣜⢎⢆⠜⣿⣿⣿⣿⣿ 
⣿⣿⣿⣿⣿⡆⠄⢣⣻⣽⣿⣿⣟⣾⡮⡺⡸⠸⣿⣿⣿⣿ 
⣿⣿⡿⠛⠉⠁⠄⢕⡳⣽⡾⣿⢽⣯⡿⣮⢚⣅⠹⣿⣿⣿ 
⡿⠋⠄⠄⠄⠄⢀⠒⠝⣞⢿⡿⣿⣽⢿⡽⣧⣳⡅⠌⠻⣿
''')
# --------------------------------------
@bot.on_message( filters.me & filters.regex('(?i)^waw$'))
def fu_fun(c, m): 
  time.sleep(1) 
  m.edit_text(''' 
_8888888888____________________
____888888888888888_________________
888888822222228888______________
_88888822222222288888_______________
888888222222222228888822228888______
888882222222222222288222222222888___
8888822222222222222222222222222288__
_8888822222222222222222222222222_88_
88888222222222222222222222222888
_888822222222222222222222222_888
____8888222222222222222222222____888
_8888222222222222222222_____888_
8882222222222222222___8888__
_888822222222222____888888__
____8888882222______88888888____
_888888_____888888888_______
__88888888888888____________
___8888888888_______________
____8888888_________________
_____88888__________________
______888___________________
_______8____________________

ஜ۩۞۩ஜஜ۩۞۩ஜஜ۩۞۩ஜ
█▄█ █ █▀█ █▄█ █▀█ █▀█
█▀█ █ █▀▀ █▀█ █▄█ █▀▀
ஜ۩۞۩ஜஜ۩۞۩ஜஜ۩۞۩ஜ
''')
# --------------------------------------
@bot.on_message( filters.me & filters.regex('(?i)^amirm$'))
def fu_fun(c, m): 
  time.sleep(0.10) 
  m.edit_text(''' 
🟧
''') 
  time.sleep(0.10) 
  m.edit_text(''' 
🟥🟥
''') 
  time.sleep(0.10) 
  m.edit_text(''' 
🟨🟨🟨 
''') 
  time.sleep(0.10) 
  m.edit_text(''' 
🟩🟩🟩🟩
''') 
  time.sleep(0.10) 
  m.edit_text('''
 کوبص میخوام🤤
''') 
  time.sleep(0.10) 
  m.edit_text(''' 
🟩    
''') 
  time.sleep(0.10) 
  m.edit_text('''
 🟨🟨
''') 
  time.sleep(0.10) 
  m.edit_text('''
🟥🟥🟥
''')
def fu_fun(c, m): 
  time.sleep(0.10) 
  m.edit_text(''' 
🟧🟧🟧🟧
''') 
  time.sleep(0.10) 
  m.edit_text(''' 
🟧🟥🟨🟩کوبص میخوام🤤🟩🟨🟥🟧
''') 
  time.sleep(0.10) 
  m.edit_text(''' 
🟧🟥🟨🟩کوبص میخوام 🤩🟩🟨🟥🟧 
''') 
  time.sleep(0.10) 
  m.edit_text(''' 
🟧🟥🟨🟩کوبص میخوام💫🟩🟨🟥🟧
''') 
  time.sleep(0.10) 
  m.edit_text('''
 🟧🟥🟨🟩کوبص میخوام😄🟩🟨🟥🟧
''') 
  time.sleep(1) 
  m.edit_text(''' 
⭐️         
''')
# --------------------------------------
@bot.on_message( filters.me & filters.regex('(?i)^kobs$'))
def fu_fun(c, m): 
  time.sleep(0.5) 
  m.edit_text(''' 
╔╦╦╦╦╦╦╦╦╦╦╗
╠╬╬╬╬╬╬╬╬╬╬╣
╠╬╬█╬╬╬╬█╬╬╣
╠╬╬╬╬╬╬╬╬╬╬╣
╠╬████████╬╣
╠╬█╬╬╬╬╬╬█╬╣
╚╩╩╩╩╩╩╩╩╩╩╝
''') 
  time.sleep(0.5) 
  m.edit_text(''' 
╔╦╦╦╦╦╦╦╦╦╦╗
╠╬╬█╬╬╬╬█╬╬╣
╠╬╬╬╬╬╬╬╣╣╣╣
╠╬█╬╬╬╬╬╬█╬╣
╠╬████████╬╣
╠╬╬╬╬╬╬╬╬╬╣╣
╚╩╩╩╩╩╩╩╩╩╩╝
''') 
  time.sleep(0.5) 
  m.edit_text(''' 
╔╦╦╦╦╦╦╦╦╦╦╗
╠╬╬╬╬╬╬╬╬╬╬╣
╠╬╬█╬╬╬╬█╬╬╣
╠╬╬╬╬╬╬╬╬╬╬╣
╠╬████████╬╣
╠╬█╬╬╬╬╬╬█╬╣
╚╩╩╩╩╩╩╩╩╩╩╝
''') 
  time.sleep(0.5) 
  m.edit_text(''' 
╔╦╦╦╦╦╦╦╦╦╦╗
╠╬╬█╬╬╬╬█╬╬╣
╠╬╬╬╬╬╬╬╣╣╣╣
╠╬█╬╬╬╬╬╬█╬╣
╠╬████████╬╣
╠╬╬╬╬╬╬╬╬╬╣╣
╚╩╩╩╩╩╩╩╩╩╩╝
''') 
  time.sleep(0.5) 
  m.edit_text('''
 ╔╦╦╦╦╦╦╦╦╦╦╗
╠╬╬╬╬╬╬╬╬╬╬╣
╠╬╬█╬╬╬╬█╬╬╣
╠╬╬╬╬╬╬╬╬╬╬╣
╠╬████████╬╣
╠╬█╬╬╬╬╬╬█╬╣
╚╩╩╩╩╩╩╩╩╩╩╝
''') 
  time.sleep(0.5) 
  m.edit_text(''' 
╔╦╦╦╦╦╦╦╦╦╦╗
╠╬╬█╬╬╬╬█╬╬╣
╠╬╬╬╬╬╬╬╣╣╣╣
╠╬█╬╬╬╬╬╬█╬╣
╠╬████████╬╣
╠╬╬╬╬╬╬╬╬╬╣╣
╚╩╩╩╩╩╩╩╩╩╩╝         
''') 
  time.sleep(0.5) 
  m.edit_text('''
 ╔╦╦╦╦╦╦╦╦╦╦╗
╠╬╬╬╬╬╬╬╬╬╬╣
╠╬╬█╬╬╬╬█╬╬╣
╠╬╬╬╬╬╬╬╬╬╬╣
╠╬████████╬╣
╠╬█╬╬╬╬╬╬█╬╣
╚╩╩╩╩╩╩╩╩╩╩╝
''') 
  time.sleep(1) 
  m.edit_text('''
╔╦╦╦╦╦╦╦╦╦╦╗
╠╬╬█╬╬╬╬█╬╬╣
╠╬╬╬╬╬╬╬╣╣╣╣
╠╬█╬╬╬╬╬╬█╬╣
╠╬████████╬╣
╠╬╬╬╬╬╬╬╬╬╣╣
╚╩╩╩╩╩╩╩╩╩╩╝
''')
# --------------------------------------
@bot.on_message( filters.me & filters.regex('(?i)^imoj$'))
def fu_fun(c, m): 
  time.sleep(1) 
  m.edit_text(''' 
♡ⓛⓞⓥⓔ🎀ⓨⓞⓤ♡
🍸🍸😊😊😊😊🍸🍸
🍸😊😊♥♥😊😊🍸
🍸😊😊😊😊😊😊🍸
🍸😊💂😊😊💂😊🍸
🍸😊😊💂💂😊😊🍸
🍸🍸😊😊😊😊🍸🍸
🍸🍸🍸👉👈🍸🍸🍸
''')
# --------------------------------------
@bot.on_message( filters.me & filters.regex('(?i)^heee$'))
def fu_fun(c, m): 
  time.sleep(0.10) 
  m.edit_text(''' 
🟩🟩🟩🟩🟩🟩🟩🟩🟩
''') 
  time.sleep(0.10) 
  m.edit_text(''' 
🟥🟩🟩🟩🟩🟩🟩🟩
''') 
  time.sleep(0.10) 
  m.edit_text(''' 
🟥🟧🟩🟩🟩🟩🟩🟩
''') 
  time.sleep(0.10) 
  m.edit_text(''' 
🟥🟧🟨🟩🟩🟩🟩🟩
''') 
  time.sleep(0.10) 
  m.edit_text('''
🟥🟧🟨🟦🟩🟩🟩🟩
''') 
  time.sleep(0.10) 
  m.edit_text(''' 
🟥🟧🟨🟦🟪🟩🟩🟩    
''') 
  time.sleep(0.10) 
  m.edit_text('''
🟥🟧🟨🟦🟪🟫🟩🟩
''') 
  time.sleep(0.10) 
  m.edit_text('''
🟥🟧🟨🟦🟪🟫⬛🟩
''')
def fu_fun(c, m): 
  time.sleep(0.10) 
  m.edit_text(''' 
🟥🟧🟨🟦🟪🟫⬛⬜
''') 
  time.sleep(0.10) 
  m.edit_text(''' 
(🖤)
''') 
  time.sleep(0.10) 
  m.edit_text(''' 
🖤🖤
''') 
  time.sleep(0.10) 
  m.edit_text(''' 
(🖤🖤🖤)
''') 
  time.sleep(0.10) 
  m.edit_text('''
:(
''') 
  time.sleep(1) 
  m.edit_text('''
:)        
''')
# --------------------------------------
@bot.on_message( filters.me & filters.regex('(?i)^amam$'))
def fu_fun(c, m): 
  time.sleep(0.10) 
  m.edit_text(''' 
⣿⣿⣿⣿⣿⡿⠋⠁⠄⠄⠄⠈⠘⠩⢿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⠃⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠻⣿⣿⣿⣿
⣿⣿⣿⣿⠄⠄⣀⣤⣤⣤⣄⡀⠄⠄⠄⠄⠙⣿⣿⣿
⣿⣿⣿⣿⡀⢰⣿⣿⣿⣿⣿⢿⠄⠄⠄⠄⠄⠹⢿⣿
⣿⣿⣿⣿⣿⡞⠻⠿⠟⠋⠉⠁⣤⡀⠄⠄⠄⠄⠄⠄
⣿⣿⣿⣿⣿⣿⣶⢼⣷⡤⣦⣿⠛⡰⢃⠄⠐⠄⠄⢸
⣿⣿⣿⣿⣿⣿⣿⡯⢍⠿⢾⡿⣸⣿⠰⠄⢀⠄⠄⡬
⣿⣿⣿⣿⣿⣿⣿⣴⣴⣅⣾⣿⣿⡧⠦⡶⠃⠄⠠⢴
⣿⣿⣿⣿⠿⠍⣿⣿⣿⣿⣿⣿⣿⢇⠟⠁⠄⠄⠄⠄
⠟⠛⠉⠄⠄⠄⡽⣿⣿⣿⣿⣿⣯⠏⠄⠄⠄⠄⠄⠄
⠄⠄⠄⢀⣾⣾⣿⣤⣯⣿⣿⡿⠃⠄⠄⠄⠄⠄⠄⠄
''')
# --------------------------------------
@bot.on_message( filters.me & filters.regex('(?i)^hen$'))
def fu_fun(c, m): 
  time.sleep(0.10) 
  m.edit_text(''' 
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⠿⠛⠛⠛⠛⠛⠿⣿⣿⣿⣿⣿⣿⣿
⣿⣏⠀⢙⣿⣧⣄⠀   ⣴⠀⠀⠀⢹⣿⣿⣿⣿⣿⣿
⣿⣿⣷⣿⣿⣿⡟⠿⢿⣿⠀⠀   ⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⡇⠀   ⠀⠀⠀⠀⣸⣿⣿⣿⣿⣿⣿
⣿⣿⠟⢿⣿⣿⠀⠀⠀⠀⠀   ⣶⣿⣿⣿⣿⣿⣿⣿
⣿⣷⣄⣴⣿⡇⠀⠀⣿⡇⠀⠀   ⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣧⡀⠀⣿⣿⠀⠀⠀   ⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣷⣶⣿⠀⠀⠀   ⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⠏⠁⠀⡀⠀⠀⠀   ⠀⠉⠛⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣄⠀⠀⠋⠀⠀⣿⣿⣄⠀⠀⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣶⣶⣶⣿⣿⣿⣆⠀⣿⣿
⣿⣿⣿⣿⣿⣿⠿⠟⠛⠛⠛⠻⢿⣿⣿⣿⣿⣿⣿⣿
⣿⣟⠀⢙⣿⣧⣀⠀   ⣤⠀⠀⠀⢹⣿⣿⣿⣿⣿⣿
⣿⣿⣷⣿⣿⣿⣿⣷⣿⣿⠀⠀  ⠀⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⠿⠟⠛⠉⠀⠀⠀⣠⣾⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣷⣄⠀⣀⣠⣤⡀⠀⠉⢻⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠇⠀⠀⠀⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣯⣀⣀⣀⣀⣼⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⡿⠛⠉⠉⠛⠿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⡟⠀⠀⣰⠀   ⠀⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣄⠀⠙⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿   ⠀⠀⠀⠀⠀⠀⠀   ⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
''')
# --------------------------------------
@bot.on_message( filters.me & filters.regex('(?i)^sar$'))
def fu_fun(c, m): 
  time.sleep(0.10) 
  m.edit_text('''
‎|￣￣￣￣￣￣￣￣￣￣￣￣￣|
‎|   بچه بیا پایین سرمون درد گرف
‎|____＿＿＿＿＿＿＿＿＿＿＿|
‎                    \ (•_•) / 
‎                      \      / 
‎                       ——
‎                       |  |  |
‎                       |_   |_
''')
# --------------------------------------
@bot.on_message( filters.me & filters.regex('(?i)^mashala$'))
def fu_fun(c, m): 
  time.sleep(0.5) 
  m.edit_text('''
وقتی سخت برای گرفتن کامنت اول تمرین می‌کردی، همه ما می‌دانستیم که فقط یک قدم تا موفقیت فاصله داری. توانایی تو برای تسلیم نشدن در برابر مشکلات همیشه به تو کمک می‌کند تا بدرخشی. کامنت اول را تبریک می‌گویم و خوشبختی روزافزون برایت آرزو می کنیم

بسم رب الشهداء و الصدیقین 
زحمات شایان شما در پی کامنت اول و ساخت خاطره ای زیبا و حماسی و غرور آفرین که باعث پیشرفت و ترقی ایران زمین در سطح جامعه بین الملل شد را تبریک و تهنیت عرض می داریم. 
امید است با تلاش های فراوان شما و امثالهم دست به موفقیت های بیشتر در این زمینه زده تا درخشش خود و اسلام را به کل جهانیان نشان دهیم. 
جهت سپاسگزاری از شما که افتخاری قَدَر قَدر را به این مرز و بوم رسانیده اید  یک عدد شورت ویبره دار به همراه جوایز نفیس دیگر به شما تعلق میگیرد.
جهت دریافت پاداش به پیوی بنده مراجعه فرمایید. 
و من الله التوفیقبسم الله الرحمن الرحیم 
بسم الرب الشهدا و الصدیقین 
بحق محمد و ال نبییین 
درود بر شما
دوست محترم 
دستیابی به این موفقیت بزرگ 
و جایگاه مفتخر ، کار بسیار سخت و طاقت فرسایی بود 
اما شما با پشتکار و اراده ای که از خود نشان داده اید ، موفق به دریافت رتبه ی نخست در عرصه ی ورزشی کامنت اول شده اید 
بنده به نمایندگی از کادر فنی 
بازیکنان 
و مدیریت باشگاه تلگرام 
اینجا هستم تا این موفقیت بزرگ را 
به شما 
و خانواده محترمتان 
و دوستان و اشنایانتان 
و همگی افراد فامیلتان 
و خلاصه چپ و راست و وسطتان 
تبریک و تهنیت عرض کنم 
و در راستای پیشرفت این عرصه به شما لوح تقدیر رو اهدا کنم 
🖼🎁 بیا اهدا کردم 
به امید پیشرفت روز افزون شما در این عرصه و دیدارتان در پست بعد و کامنت های اول 
خدانگهدار

تبریک تبریک تبریک
کسب رتبه اول در گذاشتن کامنت را به شما و خانواده گرامی تبریک میگویم.
انشاالله با تلاش مضاعف و یاری خداوند بتوانید این مقام با ارزش را برای خود نگه دارید و باعث افتخار خانواده و تمام دوستان و آشنایان شوید.
ما نیز در رسیدن به این هدف والا شما را یاری کرده و دعا های خیر ما کمک رسان شماست.
با تشکر

Congratulations Congratulations Congratulations
 Congratulations to you and your family for taking the first place in the comments. God willing, with the double effort and help of God, you will be able to keep this valuable position for yourself and make your family and all your friends and acquaintances proud. We also help you to achieve this lofty goal and our good prayers help you. Thanks

مبروك مبروك مبروك 
تهانينا لك ولعائلتك على احتلال المركز الأول في التعليقات. إن شاء الله بجهد ومضاعفة بعون الله ستكون قادرًا على الاحتفاظ بهذا المنصب القيم لنفسك وتجعل عائلتك وجميع أصدقائك ومعارفك فخورين. نحن نساعدك أيضًا على تحقيق هذا الهدف النبيل وتساعدك صلواتنا الطيبة. شکرا

מאַזל - טאָוו צו איר און דיין משפּחה פֿאַר די ערשטער אָרט אין די באַמערקונגען. אויב גאָט וועט וועלן, מיט די טאָפּל מי און הילף פון גאָט, איר וועט קענען צו האַלטן דעם ווערטפול שטעלע פֿאַר זיך און מאַכן דיין משפּחה און אַלע דיין פרענדז און אַקוויינטאַנסיז שטאָלץ. מיר אויך העלפֿן איר דערגרייכן דעם הויך ציל און אונדזער גוטע תפילות העלפֿן איר. דאַנקען אַמין מאָגכאַדאַם

댓글에서 1 위를 차지한 귀하와 귀하의 가족에게 축하드립니다. 하나님께서는 기꺼이 하나님의 두 배의 노력과 도움으로이 귀중한 지위를 유지하고 가족과 모든 친구와 지인을 자랑스럽게 만들 수있을 것입니다. 우리는 또한 당신이이 높은 목표를 달성하도록 돕고 우리의 좋은기도는 당신을 돕습니다. 감사 아민 모 가담

Til hamingju Til hamingju Til hamingju Til hamingju með þig og fjölskyldu þína með fyrsta sætið í athugasemdunum. Guð vilji, með tvöföldum fyrirhöfn og hjálp Guðs, munt þú geta haldið þessari dýrmætu stöðu fyrir þig og gert fjölskyldu þína og alla vini þína og kunningja stolta. Við hjálpum þér einnig að ná þessu háleita markmiði og góðu bænir okkar hjálpa þér. Takk fyrir
''')
# --------------------------------------
@bot.on_message( filters.me & filters.regex('(?i)^men$'))
def fu_fun(c, m): 
  time.sleep(0.5) 
  m.edit_text('''
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣴⣶⣶⣶⣶⣶⣤⡄⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢀⣾⣿⣿⣿⠉⠉⠉⠉⠉⠙⢢⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⠏⠀⠀⠀⠀⠀⠀⠈⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢘⡉⢻⡇⠀⠀⠀⠀⠀⠀⠀⠀⢐⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠳⡦⣸⣷⣄⡀⢀⣀⡀⠀⠀⠀⡂⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⡊⣿⣿⣿⣿⣯⡩⣉⠹⢷⢦⠁⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢰⠀⢻⣿⣿⣿⣿⣿⣿⣶⣶⡞⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢀⡌⠀⠀⢀⠉⠻⣿⣿⣿⣿⣿⡇⠀⠀⠀
⠀⣀⠠⠤⠐⠚⠱⠀⠀⠀⠈⠀⠀⠀⠉⣻⠛⠋⠀⠀⠀⠀
⡇⠀⠀⡊⠠⠐⠁⠀⠀⠀⠀⢰⠀⢀⠆⠿⡀⠀⠀⠀⠀⠀
⡗⠒⠒⠀⠀⠀⠠⠤⢤⡀⠀⢸⠀⠘⠀⠀⢌⠑⢢⠀⠀⠀
⡇⠠⠀⠀⠀⠀⠀⠀⠀⠀⠑⢺⠀⠐⠀⠀⠂⠀⠀⠉⠒⠢⣄ 
⡇⠀⠀⠀⠀⠀⠀⠂⢰⠤⠀⠀⢦⠁⠀⠀⢂⠀⠀⠐⠄⠀⠠⠈⠉⠑⠦⡀
⡇⠀⡀⢀⠐⡀⠀⠀⠈⠀⠀⠀⠀⠀⠀⠐⠀⠀⠀⠀⠀⠀⠀⠁⠄⠀⠀⠘
''')
# --------------------------------------
@bot.on_message( filters.me & filters.regex('(?i)^tel$'))
def fu_fun(c, m): 
  time.sleep(0.5) 
  m.edit_text('''
⠀
⣠⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣆
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠟⠋⠉⢸⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⡿⠿⠛⠋⠉⠀⣠⠔⠀⠀⣸⣿⣿⣿
⣿⣿⣿⡿⠿⠛⠉⠁⠀⠀⢀⣠⣴⠟⠁⠀⠀⠀⣿⣿⣿⣿
⣿⣿⣥⣀⡀⠀⠀⢀⣤⣶⡿⠋⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣆⢻⣿⠋⠀⠀⠀⠀⠀⠀⠀⣼⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⡜⡇⠀⢀⣀⠀⠀⠀⠀⢠⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣷⣀⣴⣿⣿⣷⣤⡀⠀⣸⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⠙⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠏
''')
# --------------------------------------
@bot.on_message( filters.me & filters.regex('(?i)^iopa$'))
def fu_fun(c, m): 
  time.sleep(0.5) 
  m.edit_text(''' 
👊🏿👇🏿👇🏿👇🏿👇🏿👇🏿👇🏿👇🏿👇🏿👇🏿👊🏿
👉🏿👍🏾👇🏾👇🏾👇🏾👇🏾👇🏾👇🏾👇🏾👍🏾👈🏿
👉🏿👉🏾👍🏽👇🏽👇🏽👇🏽👇🏽👇🏽👍🏽👈🏾👈🏿
👉🏿👉🏾👉🏽👍🏼👇🏼👇🏼👇🏼👍🏼👈🏽👈🏾👈🏿
👉🏿👉🏾👉🏽👉🏼👍🏻👇🏻👍🏻👈🏼👈🏽👈🏾👈🏿
👉🏿👉🏾👉🏽👉🏼👉🏻😐👈🏻👈🏼👈🏽👈🏾👈🏿
👉🏿👉🏾👉🏽👉🏼👍🏻👆🏻👍🏻👈🏼👈🏽👈🏾👈🏿
👉🏿👉🏾👉🏽👍🏼👆🏼👆🏼👆🏼👍🏼👈🏽👈🏾👈🏿
👉🏿👉🏾👍🏽👆🏽👆🏽👆🏽👆🏽👆🏽👍🏽👈🏾👈🏿
👉🏿👍🏾👆🏾👆🏾👆🏾👆🏾👆🏾👆🏾👆🏾👍🏾👈🏿
👊🏿👆🏿👆🏿👆🏿👆🏿👆🏿👆🏿👆🏿👆🏿👆🏿👊🏿
''') 
  time.sleep(0.5) 
  m.edit_text(''' 
👊🏿👇🏿👇🏿👇🏿👇🏿👇🏿👇🏿👇🏿👇🏿👇🏿👊🏿
👉🏿👍🏾👇🏾👇🏾👇🏾👇🏾👇🏾👇🏾👇🏾👍🏾👈🏿
👉🏿👉🏾👍🏽👇🏽👇🏽👇🏽👇🏽👇🏽👍🏽👈🏾👈🏿
👉🏿👉🏾👉🏽👍🏼👇🏼👇🏼👇🏼👍🏼👈🏽👈🏾👈🏿
👉🏿👉🏾👉🏽👉🏼👍🏻👇🏻👍🏻👈🏼👈🏽👈🏾👈🏿
👉🏿👉🏾👉🏽👉🏼👉🏻😂👈🏻👈🏼👈🏽👈🏾👈🏿
👉🏿👉🏾👉🏽👉🏼👍🏻👆🏻👍🏻👈🏼👈🏽👈🏾👈🏿
👉🏿👉🏾👉🏽👍🏼👆🏼👆🏼👆🏼👍🏼👈🏽👈🏾👈🏿
👉🏿👉🏾👍🏽👆🏽👆🏽👆🏽👆🏽👆🏽👍🏽👈🏾👈🏿
👉🏿👍🏾👆🏾👆🏾👆🏾👆🏾👆🏾👆🏾👆🏾👍🏾👈🏿
👊🏿👆🏿👆🏿👆🏿👆🏿👆🏿👆🏿👆🏿👆🏿👆🏿👊🏿
''') 
  time.sleep(0.5) 
  m.edit_text(''' 
👊🏿👇🏿👇🏿👇🏿👇🏿👇🏿👇🏿👇🏿👇🏿👇🏿👊🏿
👉🏿👍🏾👇🏾👇🏾👇🏾👇🏾👇🏾👇🏾👇🏾👍🏾👈🏿
👉🏿👉🏾👍🏽👇🏽👇🏽👇🏽👇🏽👇🏽👍🏽👈🏾👈🏿
👉🏿👉🏾👉🏽👍🏼👇🏼👇🏼👇🏼👍🏼👈🏽👈🏾👈🏿
👉🏿👉🏾👉🏽👉🏼👍🏻👇🏻👍🏻👈🏼👈🏽👈🏾👈🏿
👉🏿👉🏾👉🏽👉🏼👉🏻🤤👈🏻👈🏼👈🏽👈🏾👈🏿
👉🏿👉🏾👉🏽👉🏼👍🏻👆🏻👍🏻👈🏼👈🏽👈🏾👈🏿
👉🏿👉🏾👉🏽👍🏼👆🏼👆🏼👆🏼👍🏼👈🏽👈🏾👈🏿
👉🏿👉🏾👍🏽👆🏽👆🏽👆🏽👆🏽👆🏽👍🏽👈🏾👈🏿
👉🏿👍🏾👆🏾👆🏾👆🏾👆🏾👆🏾👆🏾👆🏾👍🏾👈🏿
👊🏿👆🏿👆🏿👆🏿👆🏿👆🏿👆🏿👆🏿👆🏿👆🏿👊🏿 
''') 
  time.sleep(0.5) 
  m.edit_text(''' 
👊🏿👇🏿👇🏿👇🏿👇🏿👇🏿👇🏿👇🏿👇🏿👇🏿👊🏿
👉🏿👍🏾👇🏾👇🏾👇🏾👇🏾👇🏾👇🏾👇🏾👍🏾👈🏿
👉🏿👉🏾👍🏽👇🏽👇🏽👇🏽👇🏽👇🏽👍🏽👈🏾👈🏿
👉🏿👉🏾👉🏽👍🏼👇🏼👇🏼👇🏼👍🏼👈🏽👈🏾👈🏿
👉🏿👉🏾👉🏽👉🏼👍🏻👇🏻👍🏻👈🏼👈🏽👈🏾👈🏿
👉🏿👉🏾👉🏽👉🏼👉🏻🤪👈🏻👈🏼👈🏽👈🏾👈🏿
👉🏿👉🏾👉🏽👉🏼👍🏻👆🏻👍🏻👈🏼👈🏽👈🏾👈🏿
👉🏿👉🏾👉🏽👍🏼👆🏼👆🏼👆🏼👍🏼👈🏽👈🏾👈🏿
👉🏿👉🏾👍🏽👆🏽👆🏽👆🏽👆🏽👆🏽👍🏽👈🏾👈🏿
👉🏿👍🏾👆🏾👆🏾👆🏾👆🏾👆🏾👆🏾👆🏾👍🏾👈🏿
👊🏿👆🏿👆🏿👆🏿👆🏿👆🏿👆🏿👆🏿👆🏿👆🏿👊🏿
''') 
  time.sleep(0.5) 
  m.edit_text('''
 👊🏿👇🏿👇🏿👇🏿👇🏿👇🏿👇🏿👇🏿👇🏿👇🏿👊🏿
👉🏿👍🏾👇🏾👇🏾👇🏾👇🏾👇🏾👇🏾👇🏾👍🏾👈🏿
👉🏿👉🏾👍🏽👇🏽👇🏽👇🏽👇🏽👇🏽👍🏽👈🏾👈🏿
👉🏿👉🏾👉🏽👍🏼👇🏼👇🏼👇🏼👍🏼👈🏽👈🏾👈🏿
👉🏿👉🏾👉🏽👉🏼👍🏻👇🏻👍🏻👈🏼👈🏽👈🏾👈🏿
👉🏿👉🏾👉🏽👉🏼👉🏻😎👈🏻👈🏼👈🏽👈🏾👈🏿
👉🏿👉🏾👉🏽👉🏼👍🏻👆🏻👍🏻👈🏼👈🏽👈🏾👈🏿
👉🏿👉🏾👉🏽👍🏼👆🏼👆🏼👆🏼👍🏼👈🏽👈🏾👈🏿
👉🏿👉🏾👍🏽👆🏽👆🏽👆🏽👆🏽👆🏽👍🏽👈🏾👈🏿
👉🏿👍🏾👆🏾👆🏾👆🏾👆🏾👆🏾👆🏾👆🏾👍🏾👈🏿
👊🏿👆🏿👆🏿👆🏿👆🏿👆🏿👆🏿👆🏿👆🏿👆🏿👊🏿
''') 
  time.sleep(0.5) 
  m.edit_text(''' 
👊🏿👇🏿👇🏿👇🏿👇🏿👇🏿👇🏿👇🏿👇🏿👇🏿👊🏿
👉🏿👍🏾👇🏾👇🏾👇🏾👇🏾👇🏾👇🏾👇🏾👍🏾👈🏿
👉🏿👉🏾👍🏽👇🏽👇🏽👇🏽👇🏽👇🏽👍🏽👈🏾👈🏿
👉🏿👉🏾👉🏽👍🏼👇🏼👇🏼👇🏼👍🏼👈🏽👈🏾👈🏿
👉🏿👉🏾👉🏽👉🏼👍🏻👇🏻👍🏻👈🏼👈🏽👈🏾👈🏿
👉🏿👉🏾👉🏽👉🏼👉🏻🤯👈🏻👈🏼👈🏽👈🏾👈🏿
👉🏿👉🏾👉🏽👉🏼👍🏻👆🏻👍🏻👈🏼👈🏽👈🏾👈🏿
👉🏿👉🏾👉🏽👍🏼👆🏼👆🏼👆🏼👍🏼👈🏽👈🏾👈🏿
👉🏿👉🏾👍🏽👆🏽👆🏽👆🏽👆🏽👆🏽👍🏽👈🏾👈🏿
👉🏿👍🏾👆🏾👆🏾👆🏾👆🏾👆🏾👆🏾👆🏾👍🏾👈🏿
👊🏿👆🏿👆🏿👆🏿👆🏿👆🏿👆🏿👆🏿👆🏿👆🏿👊🏿         
''') 
  time.sleep(0.5) 
  m.edit_text('''
 👊🏿👇🏿👇🏿👇🏿👇🏿👇🏿👇🏿👇🏿👇🏿👇🏿👊🏿
👉🏿👍🏾👇🏾👇🏾👇🏾👇🏾👇🏾👇🏾👇🏾👍🏾👈🏿
👉🏿👉🏾👍🏽👇🏽👇🏽👇🏽👇🏽👇🏽👍🏽👈🏾👈🏿
👉🏿👉🏾👉🏽👍🏼👇🏼👇🏼👇🏼👍🏼👈🏽👈🏾👈🏿
👉🏿👉🏾👉🏽👉🏼👍🏻👇🏻👍🏻👈🏼👈🏽👈🏾👈🏿
👉🏿👉🏾👉🏽👉🏼👉🏻🥸👈🏻👈🏼👈🏽👈🏾👈🏿
👉🏿👉🏾👉🏽👉🏼👍🏻👆🏻👍🏻👈🏼👈🏽👈🏾👈🏿
👉🏿👉🏾👉🏽👍🏼👆🏼👆🏼👆🏼👍🏼👈🏽👈🏾👈🏿
👉🏿👉🏾👍🏽👆🏽👆🏽👆🏽👆🏽👆🏽👍🏽👈🏾👈🏿
👉🏿👍🏾👆🏾👆🏾👆🏾👆🏾👆🏾👆🏾👆🏾👍🏾👈🏿
👊🏿👆🏿👆🏿👆🏿👆🏿👆🏿👆🏿👆🏿👆🏿👆🏿👊🏿
''') 
  time.sleep(1) 
  m.edit_text('''
😎
''')
# --------------------------------------
@bot.on_message( filters.me & filters.regex('(?i)^love$'))
def Love_Fun(c,m):
    m.edit_text(
'''..... (¯`v´¯)♥
.......•.¸.•´
....¸.•´
... (
☻/
/▌♥♥
/ \ ♥♥
''')
@bot.on_message( filters.me & filters.regex('(?i)^🤍$'))
def heart_Fun(c,m):
    m.edit_text(
'''⠀
⠀⠀⣤⣶⣿⣿⣿⣿⣿⣶⣄⣤⣶⣿⣿⣿⣿⣿⣶⣄⠀⠀
⢠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⡄
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠏
⠀⠙⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠋⠀
⠀⠀⠀⠙⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠋⠀⠀⠀
⠀⠀⠀⠀⠀⠙⢿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠋⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠙⢿⣿⣿⣿⣿⡿⠋⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢿⡿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀
''')
@bot.on_message( filters.me & filters.regex('(?i)^🖐$'))
def heart_Fun(c,m):
    m.edit_text(
'''⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣤⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢰⣿⣷⡆⣿⣿⣿⠀⣾⣷⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⢰⣿⣶⠘⣿⣿⡇⣿⣿⣿⠀⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⢸⣿⣿⠀⣿⣿⡇⣿⣿⣿⠀⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⢸⣿⣿⠀⣿⣿⡇⣿⣿⣿⠀⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⢸⣿⣿⠀⣿⣿⡇⣿⣿⣿⠀⣿⣿⡇⠀⠀⠀⢀⣠⣤⣤⠀⠀⠀
⠀⠀⢸⣿⣿⣄⣿⣿⣷⣿⣿⣿⣤⣿⣿⡇⠀⢀⣴⣿⣿⣿⠟⠀⠀⠀
⠀⠀⣸⣿⣿⣿⣿⣿⣿⣿⣿⡿⢛⣛⣛⣣⣤⣿⣿⣿⠟⠁⠀⠀⠀⠀
⠀⠀⣿⣿⣿⣿⣿⣿⣿⡟⣡⣾⣿⣿⣿⣿⣿⣿⡟⠁⠀⠀⠀⠀⠀⠀
⠀⠀⢸⣿⣿⣿⣿⣿⣿⢱⣿⣿⣿⣿⣿⣿⣿⠏⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠈⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠙⠿⢿⣿⣿⣿⣿⣿⣿⣿⡿⠛⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠈⠉⠉⠉⠉⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
''')
# --------------------------------------
@bot.on_message( filters.me & filters.regex('(?i)^dobsdobs$'))
def danze_fun(c,m):
    m.edit_text('''▫️▫️▫️▫️▫️▫️
▫️▫️▫️▫️▫️▫️
▫️▫️▫️▫️▫️▫️
▫️▫️▫️▫️▫️▫️
▫️▫️▫️▫️▫️▫️
▫️▫️▫️▫️▫️▫️
''')
    m.edit_text('''▫️▫️▫️▫️▫️▫️
▫️▫️▫️▫️▫️▫️
▫️▫️▫️▫️▫️▫️
▫️▫️▫️▫️▫️▫️
◽️◽️▫️▫️▫️▫️
◽️◽️▫️▫️▫️▫️
''')
    m.edit_text('''▫️▫️▫️▫️▫️▫️
▫️▫️▫️▫️▫️▫️
▫️▫️▫️▫️▫️▫️
◽️◽️◽️▫️▫️▫️
◽️◽️◽️▫️▫️▫️
◽️◽️◽️▫️▫️▫️
''')
    m.edit_text('''▫️▫️▫️▫️▫️▫️
▫️▫️▫️▫️▫️▫️
◽️◽️◽️◽️▫️▫️
◽️◽️◽️◽️▫️▫️
◽️◽️◽️◽️▫️▫️
◽️◽️◽️◽️▫️▫️
''')
    m.edit_text('''▫️▫️▫️▫️▫️▫️
◽️◽️◽️◽️◽️▫️
◽️◽️◽️◽️◽️▫️
◽️◽️◽️◽️◽️▫️
◽️◽️◽️◽️◽️▫️
◽️◽️◽️◽️◽️▫️
''')
    m.edit_text('''◽️◽️◽️◽️◽️◽️
◽️◽️◽️◽️◽️◽️
◽️◽️◽️◽️◽️◽️
◽️◽️◽️◽️◽️◽️
◽️◽️◽️◽️◽️◽️
◽️◽️◽️◽️◽️◽️
''')
    m.edit_text('''◽️◽️◽️◽️◽️◽️
◽️◽️◽️◽️◽️◽️
◽️◽️◽️◽️◽️◽️
◽️◽️◽️◽️◽️◽️
◻️◻️◽️◽️◽️◽️
◻️◻️◽️◽️◽️◽️
''')
    m.edit_text('''◽️◽️◽️◽️◽️◽️
◽️◽️◽️◽️◽️◽️
◽️◽️◽️◽️◽️◽️
◻️◻️◻️◽️◽️◽️
◻️◻️◻️◽️◽️◽️
◻️◻️◻️◽️◽️◽️
''')
    m.edit_text('''◽️◽️◽️◽️◽️◽️
◽️◽️◽️◽️◽️◽️
◻️◻️◻️◻️◽️◽️
◻️◻️◻️◻️◽️◽️
◻️◻️◻️◻️◽️◽️
◻️◻️◻️◻️◽️◽️
''')
    m.edit_text('''◽️◽️◽️◽️◽️◽️
◻️◻️◻️◻️◻️◽️
◻️◻️◻️◻️◻️◽️
◻️◻️◻️◻️◻️◽️
◻️◻️◻️◻️◻️◽️
◻️◻️◻️◻️◻️◽️
''')
    m.edit_text('''◻️◻️◻️◻️◻️◻️
◻️◻️◻️◻️◻️◻️
◻️◻️◻️◻️◻️◻️
◻️◻️◻️◻️◻️◻️
◻️◻️◻️◻️◻️◻️
◻️◻️◻️◻️◻️◻️
''')
    m.edit_text('''◻️◻️◻️◻️◻️◻️
◻️◻️◻️◻️◻️◻️
◻️◻️◻️◻️◻️◻️
◻️◻️◻️◻️◻️◻️
⬜️⬜️◻️◻️◻️◻️
⬜️⬜️◻️◻️◻️◻️
''')
    m.edit_text('''◻️◻️◻️◻️◻️◻️
◻️◻️◻️◻️◻️◻️
◻️◻️◻️◻️◻️◻️
⬜️⬜️⬜️◻️◻️◻️
⬜️⬜️⬜️◻️◻️◻️
⬜️⬜️⬜️◻️◻️◻️
''')
    m.edit_text('''◻️◻️◻️◻️◻️◻️
◻️◻️◻️◻️◻️◻️
⬜️⬜️⬜️⬜️◻️◻️
⬜️⬜️⬜️⬜️◻️◻️
⬜️⬜️⬜️⬜️◻️◻️
⬜️⬜️⬜️⬜️◻️◻️
''')
    m.edit_text('''◻️◻️◻️◻️◻️◻️
⬜️⬜️⬜️⬜️⬜️◻️
⬜️⬜️⬜️⬜️⬜️◻️
⬜️⬜️⬜️⬜️⬜️◻️
⬜️⬜️⬜️⬜️⬜️◻️
⬜️⬜️⬜️⬜️⬜️◻️
''')
    m.edit_text('''⬜️⬜️⬜️⬜️⬜️⬜️
⬜️⬜️⬜️⬜️⬜️⬜️
⬜️⬜️⬜️⬜️⬜️⬜️
⬜️⬜️⬜️⬜️⬜️⬜️
⬜️⬜️⬜️⬜️⬜️⬜️
⬜️⬜️⬜️⬜️⬜️⬜️
''')
    m.edit_text('''⬜️⬜️⬜️⬜️⬜️⬜️
⬜️⬜️⬜️⬜️⬜️⬜️
⬜️⬜️🟥🟥⬜️⬜️
⬜️⬜️🟥🟥⬜️⬜️
⬜️⬜️⬜️⬜️⬜️⬜️
⬜️⬜️⬜️⬜️⬜️⬜️
''')
    m.edit_text('''⬜️⬜️⬜️⬜️⬜️⬜️
⬜️🟥🟥🟥🟥⬜️
⬜️🟥🟥🟥🟥⬜️
⬜️🟥🟥🟥🟥⬜️
⬜️🟥🟥🟥🟥⬜️
⬜️⬜️⬜️⬜️⬜️⬜️
''')
    m.edit_text('''⬜️⬜️⬜️⬜️⬜️⬜️
⬜️🟥🟥🟥🟥⬜️
⬜️🟥🟦🟦🟥⬜️
⬜️🟥🟦🟦🟥⬜️
⬜️🟥🟥🟥🟥⬜️
⬜️⬜️⬜️⬜️⬜️⬜️
''')
    m.edit_text('''🟥🟥🟥🟥🟥🟥
🟥🟥🟥🟥🟥🟥
🟥🟥🟦🟦🟥🟥
🟥🟥🟦🟦🟥🟥
🟥🟥🟥🟥🟥🟥
🟥🟥🟥🟥🟥🟥
''')
    m.edit_text('''🟥🟥🟥🟥🟥🟥
🟥🟦🟦🟦🟦🟥
🟥🟦🟦🟦🟦🟥
🟥🟦🟦🟦🟦🟥
🟥🟦🟦🟦🟦🟥
🟥🟥🟥🟥🟥🟥
''')
    m.edit_text('''🟥🟥🟥🟥🟥🟥
🟥🟦🟦🟦🟦🟥
🟥🟦🟪🟪🟦🟥
🟥🟦🟪🟪🟦🟥
🟥🟦🟦🟦🟦🟥
🟥🟥🟥🟥🟥🟥
''')
    m.edit_text('''🟦🟦🟦🟦🟦🟦
🟦🟦🟦🟦🟦🟦
🟦🟦🟪🟪🟦🟦
🟦🟦🟪🟪🟦🟦
🟦🟦🟦🟦🟦🟦
🟦🟦🟦🟦🟦🟦
''')
    m.edit_text('''🟦🟦🟦🟦🟦🟦
🟦🟪🟪🟪🟪🟦
🟦🟪🟪🟪🟪🟦
🟦🟪🟪🟪🟪🟦
🟦🟪🟪🟪🟪🟦
🟦🟦🟦🟦🟦🟦
''')
    m.edit_text('''🟦🟦🟦🟦🟦🟦
🟦🟪🟪🟪🟪🟦
🟦🟪🟧🟧🟪🟦
🟦🟪🟧🟧🟪🟦
🟦🟪🟪🟪🟪🟦
🟦🟦🟦🟦🟦🟦
''')
    m.edit_text('''🟪🟪🟪🟪🟪🟪
🟪🟪🟪🟪🟪🟪
🟪🟪🟧🟧🟪🟪
🟪🟪🟧🟧🟪🟪
🟪🟪🟪🟪🟪🟪
🟪🟪🟪🟪🟪🟪
''')
    m.edit_text('''🟪🟪🟪🟪🟪🟪
🟪🟧🟧🟧🟧🟪
🟪🟧🟧🟧🟧🟪
🟪🟧🟧🟧🟧🟪
🟪🟧🟧🟧🟧🟪
🟪🟪🟪🟪🟪🟪
''')
    m.edit_text('''🟪🟪🟪🟪🟪🟪
🟪🟧🟧🟧🟧🟪
🟪🟧⬜️⬜️🟧🟪
🟪🟧⬜️⬜️🟧🟪
🟪🟧🟧🟧🟧🟪
🟪🟪🟪🟪🟪🟪
''')
    m.edit_text('''🟧🟧🟧🟧🟧🟧
🟧🟧🟧🟧🟧🟧
🟧🟧⬜️⬜️🟧🟧
🟧🟧⬜️⬜️🟧🟧
🟧🟧🟧🟧🟧🟧
🟧🟧🟧🟧🟧🟧
''')
    m.edit_text('''🟧🟧🟧🟧🟧🟧
🟧⬜️⬜️⬜️⬜️🟧
🟧⬜️⬜️⬜️⬜️🟧
🟧⬜️⬜️⬜️⬜️🟧
🟧⬜️⬜️⬜️⬜️🟧
🟧🟧🟧🟧🟧🟧
''')
    m.edit_text('''⬜️⬜️⬜️⬜️⬜️⬜️
⬜️⬜️⬜️⬜️⬜️⬜️
⬜️⬜️⬜️⬜️⬜️⬜️
⬜️⬜️⬜️⬜️⬜️⬜️
⬜️⬜️⬜️⬜️⬜️⬜️
⬜️⬜️⬜️⬜️⬜️⬜️
''')
    m.edit_text('''🟦🟪🟫🟥🟧🟨
🟨🟧🟥🟫🟪🟦
🟦🟪🟫🟥🟧🟨
🟨🟧🟥🟫🟪🟦
🟦🟪🟫🟥🟧🟨
🟨🟧🟥🟫🟪🟦
''')
    m.edit_text('''🟫🟪🟫🟥🟧🟥
🟨🟫🟥🟫🟥🟦
🟫🟪🟫🟥🟧🟥
🟨🟫🟥🟫🟥🟦
🟫🟪🟫🟥🟧🟥
🟨🟫🟥🟫🟥🟦
''')
    m.edit_text('''🟥🟥🟥🟥🟥🟥
🟥🟥🟥🟥🟥🟥
🟥🟥🟥🟥🟥🟥
🟥🟥🟥🟥🟥🟥
🟥🟥🟥🟥🟥🟥
🟥🟥🟥🟥🟥🟥
''')
    m.edit_text('''🟦🟥🟥🟥🟥🟦
🟥🟦🟥🟥🟦🟥
🟥🟥🟥🟥🟥🟥
🟥🟥🟥🟥🟥🟥
🟥🟦🟥🟥🟦🟥
🟦🟥🟥🟥🟥🟦
''')
    m.edit_text('''🟦🟥🟥🟥🟥🟦
🟥🟦🟥🟥🟦🟥
🟥🟥🟦🟦🟥🟥
🟥🟥🟦🟦🟥🟥
🟥🟦🟥🟥🟦🟥
🟦🟥🟥🟥🟥🟦
''')
    m.edit_text('''🟦🟪🟥🟥🟪🟦
🟪🟦🟥🟥🟦🟪
🟥🟥🟦🟦🟥🟥
🟥🟥🟦🟦🟥🟥
🟪🟦🟥🟥🟦🟪
🟦🟪🟥🟥🟪🟦
''')
    m.edit_text('''🟦🟪🟥🟧🟪🟦
🟪🟦🟧🟥🟦🟪
🟥🟧🟦🟦🟥🟧
🟧🟥🟦🟦🟧🟥
🟪🟦🟥🟧🟦🟪
🟦🟪🟧🟥🟪🟦
''')
    m.delete()
# --------------------------------------
@bot.on_message( filters.me & filters.regex('(?i)^نخوندم$'))
def nakhondam_fun(c,m):
  m.edit_text('''
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
  ''')
  m.edit_text('''
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⠿⠛⠛⠛⠛⠛⠿⣿⣿⣿⣿⣿⣿⣿
  ''')
  m.edit_text('''
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⠿⠛⠛⠛⠛⠛⠿⣿⣿⣿⣿⣿⣿⣿
⣿⣏⠀⢙⣿⣧⣄⠀   ⣴⠀⠀⠀⢹⣿⣿⣿⣿⣿⣿
  ''')
  m.edit_text('''
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⠿⠛⠛⠛⠛⠛⠿⣿⣿⣿⣿⣿⣿⣿
⣿⣏⠀⢙⣿⣧⣄⠀   ⣴⠀⠀⠀⢹⣿⣿⣿⣿⣿⣿
⣿⣿⣷⣿⣿⣿⡟⠿⢿⣿⠀⠀   ⣿⣿⣿⣿⣿⣿⣿
  ''')
  m.edit_text('''
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⠿⠛⠛⠛⠛⠛⠿⣿⣿⣿⣿⣿⣿⣿
⣿⣏⠀⢙⣿⣧⣄⠀   ⣴⠀⠀⠀⢹⣿⣿⣿⣿⣿⣿
⣿⣿⣷⣿⣿⣿⡟⠿⢿⣿⠀⠀   ⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⡇⠀   ⠀⠀⠀⠀⣸⣿⣿⣿⣿⣿⣿
  ''')
  m.edit_text('''
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⠿⠛⠛⠛⠛⠛⠿⣿⣿⣿⣿⣿⣿⣿
⣿⣏⠀⢙⣿⣧⣄⠀   ⣴⠀⠀⠀⢹⣿⣿⣿⣿⣿⣿
⣿⣿⣷⣿⣿⣿⡟⠿⢿⣿⠀⠀   ⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⡇⠀   ⠀⠀⠀⠀⣸⣿⣿⣿⣿⣿⣿
⣿⣿⠟⢿⣿⣿⠀⠀⠀⠀⠀   ⣶⣿⣿⣿⣿⣿⣿⣿
  ''')
  m.edit_text('''
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⠿⠛⠛⠛⠛⠛⠿⣿⣿⣿⣿⣿⣿⣿
⣿⣏⠀⢙⣿⣧⣄⠀   ⣴⠀⠀⠀⢹⣿⣿⣿⣿⣿⣿
⣿⣿⣷⣿⣿⣿⡟⠿⢿⣿⠀⠀   ⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⡇⠀   ⠀⠀⠀⠀⣸⣿⣿⣿⣿⣿⣿
⣿⣿⠟⢿⣿⣿⠀⠀⠀⠀⠀   ⣶⣿⣿⣿⣿⣿⣿⣿
⣿⣷⣄⣴⣿⡇⠀⠀⣿⡇⠀⠀   ⣿⣿⣿⣿⣿⣿⣿
  ''')
  m.edit_text('''
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⠿⠛⠛⠛⠛⠛⠿⣿⣿⣿⣿⣿⣿⣿
⣿⣏⠀⢙⣿⣧⣄⠀   ⣴⠀⠀⠀⢹⣿⣿⣿⣿⣿⣿
⣿⣿⣷⣿⣿⣿⡟⠿⢿⣿⠀⠀   ⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⡇⠀   ⠀⠀⠀⠀⣸⣿⣿⣿⣿⣿⣿
⣿⣿⠟⢿⣿⣿⠀⠀⠀⠀⠀   ⣶⣿⣿⣿⣿⣿⣿⣿
⣿⣷⣄⣴⣿⡇⠀⠀⣿⡇⠀⠀   ⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣧⡀⠀⣿⣿⠀⠀⠀   ⣿⣿⣿⣿⣿⣿
  ''')
  m.edit_text('''
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⠿⠛⠛⠛⠛⠛⠿⣿⣿⣿⣿⣿⣿⣿
⣿⣏⠀⢙⣿⣧⣄⠀   ⣴⠀⠀⠀⢹⣿⣿⣿⣿⣿⣿
⣿⣿⣷⣿⣿⣿⡟⠿⢿⣿⠀⠀   ⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⡇⠀   ⠀⠀⠀⠀⣸⣿⣿⣿⣿⣿⣿
⣿⣿⠟⢿⣿⣿⠀⠀⠀⠀⠀   ⣶⣿⣿⣿⣿⣿⣿⣿
⣿⣷⣄⣴⣿⡇⠀⠀⣿⡇⠀⠀   ⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣧⡀⠀⣿⣿⠀⠀⠀   ⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣷⣶⣿⠀⠀⠀   ⣿⣿⣿⣿⣿⣿
  ''')
  m.edit_text('''
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⠿⠛⠛⠛⠛⠛⠿⣿⣿⣿⣿⣿⣿⣿
⣿⣏⠀⢙⣿⣧⣄⠀   ⣴⠀⠀⠀⢹⣿⣿⣿⣿⣿⣿
⣿⣿⣷⣿⣿⣿⡟⠿⢿⣿⠀⠀   ⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⡇⠀   ⠀⠀⠀⠀⣸⣿⣿⣿⣿⣿⣿
⣿⣿⠟⢿⣿⣿⠀⠀⠀⠀⠀   ⣶⣿⣿⣿⣿⣿⣿⣿
⣿⣷⣄⣴⣿⡇⠀⠀⣿⡇⠀⠀   ⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣧⡀⠀⣿⣿⠀⠀⠀   ⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣷⣶⣿⠀⠀⠀   ⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⠏⠁⠀⡀⠀⠀⠀   ⠀⠉⠛⣿⣿
  ''')
  m.edit_text('''
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⠿⠛⠛⠛⠛⠛⠿⣿⣿⣿⣿⣿⣿⣿
⣿⣏⠀⢙⣿⣧⣄⠀   ⣴⠀⠀⠀⢹⣿⣿⣿⣿⣿⣿
⣿⣿⣷⣿⣿⣿⡟⠿⢿⣿⠀⠀   ⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⡇⠀   ⠀⠀⠀⠀⣸⣿⣿⣿⣿⣿⣿
⣿⣿⠟⢿⣿⣿⠀⠀⠀⠀⠀   ⣶⣿⣿⣿⣿⣿⣿⣿
⣿⣷⣄⣴⣿⡇⠀⠀⣿⡇⠀⠀   ⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣧⡀⠀⣿⣿⠀⠀⠀   ⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣷⣶⣿⠀⠀⠀   ⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⠏⠁⠀⡀⠀⠀⠀   ⠀⠉⠛⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣄⠀⠀⠋⠀⠀⣿⣿⣄⠀⠀⣿⣿
  ''')
  m.edit_text('''
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⠿⠛⠛⠛⠛⠛⠿⣿⣿⣿⣿⣿⣿⣿
⣿⣏⠀⢙⣿⣧⣄⠀   ⣴⠀⠀⠀⢹⣿⣿⣿⣿⣿⣿
⣿⣿⣷⣿⣿⣿⡟⠿⢿⣿⠀⠀   ⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⡇⠀   ⠀⠀⠀⠀⣸⣿⣿⣿⣿⣿⣿
⣿⣿⠟⢿⣿⣿⠀⠀⠀⠀⠀   ⣶⣿⣿⣿⣿⣿⣿⣿
⣿⣷⣄⣴⣿⡇⠀⠀⣿⡇⠀⠀   ⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣧⡀⠀⣿⣿⠀⠀⠀   ⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣷⣶⣿⠀⠀⠀   ⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⠏⠁⠀⡀⠀⠀⠀   ⠀⠉⠛⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣄⠀⠀⠋⠀⠀⣿⣿⣄⠀⠀⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣶⣶⣶⣿⣿⣿⣆⠀⣿⣿
  ''')
  m.edit_text('''
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⠿⠛⠛⠛⠛⠛⠿⣿⣿⣿⣿⣿⣿⣿
⣿⣏⠀⢙⣿⣧⣄⠀   ⣴⠀⠀⠀⢹⣿⣿⣿⣿⣿⣿
⣿⣿⣷⣿⣿⣿⡟⠿⢿⣿⠀⠀   ⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⡇⠀   ⠀⠀⠀⠀⣸⣿⣿⣿⣿⣿⣿
⣿⣿⠟⢿⣿⣿⠀⠀⠀⠀⠀   ⣶⣿⣿⣿⣿⣿⣿⣿
⣿⣷⣄⣴⣿⡇⠀⠀⣿⡇⠀⠀   ⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣧⡀⠀⣿⣿⠀⠀⠀   ⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣷⣶⣿⠀⠀⠀   ⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⠏⠁⠀⡀⠀⠀⠀   ⠀⠉⠛⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣄⠀⠀⠋⠀⠀⣿⣿⣄⠀⠀⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣶⣶⣶⣿⣿⣿⣆⠀⣿⣿
⣿⣿⣿⣿⣿⣿⠿⠟⠛⠛⠛⠻⢿⣿⣿⣿⣿⣿⣿⣿
  ''')
  m.edit_text('''
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⠿⠛⠛⠛⠛⠛⠿⣿⣿⣿⣿⣿⣿⣿
⣿⣏⠀⢙⣿⣧⣄⠀   ⣴⠀⠀⠀⢹⣿⣿⣿⣿⣿⣿
⣿⣿⣷⣿⣿⣿⡟⠿⢿⣿⠀⠀   ⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⡇⠀   ⠀⠀⠀⠀⣸⣿⣿⣿⣿⣿⣿
⣿⣿⠟⢿⣿⣿⠀⠀⠀⠀⠀   ⣶⣿⣿⣿⣿⣿⣿⣿
⣿⣷⣄⣴⣿⡇⠀⠀⣿⡇⠀⠀   ⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣧⡀⠀⣿⣿⠀⠀⠀   ⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣷⣶⣿⠀⠀⠀   ⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⠏⠁⠀⡀⠀⠀⠀   ⠀⠉⠛⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣄⠀⠀⠋⠀⠀⣿⣿⣄⠀⠀⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣶⣶⣶⣿⣿⣿⣆⠀⣿⣿
⣿⣿⣿⣿⣿⣿⠿⠟⠛⠛⠛⠻⢿⣿⣿⣿⣿⣿⣿⣿
⣿⣟⠀⢙⣿⣧⣀⠀   ⣤⠀⠀⠀⢹⣿⣿⣿⣿⣿
  ''')
  m.edit_text('''
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⠿⠛⠛⠛⠛⠛⠿⣿⣿⣿⣿⣿⣿⣿
⣿⣏⠀⢙⣿⣧⣄⠀   ⣴⠀⠀⠀⢹⣿⣿⣿⣿⣿⣿
⣿⣿⣷⣿⣿⣿⡟⠿⢿⣿⠀⠀   ⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⡇⠀   ⠀⠀⠀⠀⣸⣿⣿⣿⣿⣿⣿
⣿⣿⠟⢿⣿⣿⠀⠀⠀⠀⠀   ⣶⣿⣿⣿⣿⣿⣿⣿
⣿⣷⣄⣴⣿⡇⠀⠀⣿⡇⠀⠀   ⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣧⡀⠀⣿⣿⠀⠀⠀   ⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣷⣶⣿⠀⠀⠀   ⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⠏⠁⠀⡀⠀⠀⠀   ⠀⠉⠛⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣄⠀⠀⠋⠀⠀⣿⣿⣄⠀⠀⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣶⣶⣶⣿⣿⣿⣆⠀⣿⣿
⣿⣿⣿⣿⣿⣿⠿⠟⠛⠛⠛⠻⢿⣿⣿⣿⣿⣿⣿⣿
⣿⣟⠀⢙⣿⣧⣀⠀   ⣤⠀⠀⠀⢹⣿⣿⣿⣿⣿⣿
⣿⣿⣷⣿⣿⣿⣿⣷⣿⣿⠀⠀  ⠀⣿⣿⣿⣿⣿⣿
  ''')
  m.edit_text('''
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⠿⠛⠛⠛⠛⠛⠿⣿⣿⣿⣿⣿⣿⣿
⣿⣏⠀⢙⣿⣧⣄⠀   ⣴⠀⠀⠀⢹⣿⣿⣿⣿⣿⣿
⣿⣿⣷⣿⣿⣿⡟⠿⢿⣿⠀⠀   ⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⡇⠀   ⠀⠀⠀⠀⣸⣿⣿⣿⣿⣿⣿
⣿⣿⠟⢿⣿⣿⠀⠀⠀⠀⠀   ⣶⣿⣿⣿⣿⣿⣿⣿
⣿⣷⣄⣴⣿⡇⠀⠀⣿⡇⠀⠀   ⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣧⡀⠀⣿⣿⠀⠀⠀   ⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣷⣶⣿⠀⠀⠀   ⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⠏⠁⠀⡀⠀⠀⠀   ⠀⠉⠛⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣄⠀⠀⠋⠀⠀⣿⣿⣄⠀⠀⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣶⣶⣶⣿⣿⣿⣆⠀⣿⣿
⣿⣿⣿⣿⣿⣿⠿⠟⠛⠛⠛⠻⢿⣿⣿⣿⣿⣿⣿⣿
⣿⣟⠀⢙⣿⣧⣀⠀   ⣤⠀⠀⠀⢹⣿⣿⣿⣿⣿⣿
⣿⣿⣷⣿⣿⣿⣿⣷⣿⣿⠀⠀  ⠀⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⠿⠟⠛⠉⠀⠀⠀⣠⣾⣿⣿⣿⣿⣿⣿
  ''')
  m.edit_text('''
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⠿⠛⠛⠛⠛⠛⠿⣿⣿⣿⣿⣿⣿⣿
⣿⣏⠀⢙⣿⣧⣄⠀   ⣴⠀⠀⠀⢹⣿⣿⣿⣿⣿⣿
⣿⣿⣷⣿⣿⣿⡟⠿⢿⣿⠀⠀   ⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⡇⠀   ⠀⠀⠀⠀⣸⣿⣿⣿⣿⣿⣿
⣿⣿⠟⢿⣿⣿⠀⠀⠀⠀⠀   ⣶⣿⣿⣿⣿⣿⣿⣿
⣿⣷⣄⣴⣿⡇⠀⠀⣿⡇⠀⠀   ⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣧⡀⠀⣿⣿⠀⠀⠀   ⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣷⣶⣿⠀⠀⠀   ⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⠏⠁⠀⡀⠀⠀⠀   ⠀⠉⠛⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣄⠀⠀⠋⠀⠀⣿⣿⣄⠀⠀⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣶⣶⣶⣿⣿⣿⣆⠀⣿⣿
⣿⣿⣿⣿⣿⣿⠿⠟⠛⠛⠛⠻⢿⣿⣿⣿⣿⣿⣿⣿
⣿⣟⠀⢙⣿⣧⣀⠀   ⣤⠀⠀⠀⢹⣿⣿⣿⣿⣿⣿
⣿⣿⣷⣿⣿⣿⣿⣷⣿⣿⠀⠀  ⠀⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⠿⠟⠛⠉⠀⠀⠀⣠⣾⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣷⣄⠀⣀⣠⣤⡀⠀⠉⢻⣿⣿⣿⣿⣿⣿
  ''')
  m.edit_text('''
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⠿⠛⠛⠛⠛⠛⠿⣿⣿⣿⣿⣿⣿⣿
⣿⣏⠀⢙⣿⣧⣄⠀   ⣴⠀⠀⠀⢹⣿⣿⣿⣿⣿⣿
⣿⣿⣷⣿⣿⣿⡟⠿⢿⣿⠀⠀   ⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⡇⠀   ⠀⠀⠀⠀⣸⣿⣿⣿⣿⣿⣿
⣿⣿⠟⢿⣿⣿⠀⠀⠀⠀⠀   ⣶⣿⣿⣿⣿⣿⣿⣿
⣿⣷⣄⣴⣿⡇⠀⠀⣿⡇⠀⠀   ⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣧⡀⠀⣿⣿⠀⠀⠀   ⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣷⣶⣿⠀⠀⠀   ⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⠏⠁⠀⡀⠀⠀⠀   ⠀⠉⠛⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣄⠀⠀⠋⠀⠀⣿⣿⣄⠀⠀⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣶⣶⣶⣿⣿⣿⣆⠀⣿⣿
⣿⣿⣿⣿⣿⣿⠿⠟⠛⠛⠛⠻⢿⣿⣿⣿⣿⣿⣿⣿
⣿⣟⠀⢙⣿⣧⣀⠀   ⣤⠀⠀⠀⢹⣿⣿⣿⣿⣿⣿
⣿⣿⣷⣿⣿⣿⣿⣷⣿⣿⠀⠀  ⠀⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⠿⠟⠛⠉⠀⠀⠀⣠⣾⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣷⣄⠀⣀⣠⣤⡀⠀⠉⢻⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠇⠀⠀⠀⣿⣿⣿⣿⣿⣿
  ''')
  m.edit_text('''
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⠿⠛⠛⠛⠛⠛⠿⣿⣿⣿⣿⣿⣿⣿
⣿⣏⠀⢙⣿⣧⣄⠀   ⣴⠀⠀⠀⢹⣿⣿⣿⣿⣿⣿
⣿⣿⣷⣿⣿⣿⡟⠿⢿⣿⠀⠀   ⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⡇⠀   ⠀⠀⠀⠀⣸⣿⣿⣿⣿⣿⣿
⣿⣿⠟⢿⣿⣿⠀⠀⠀⠀⠀   ⣶⣿⣿⣿⣿⣿⣿⣿
⣿⣷⣄⣴⣿⡇⠀⠀⣿⡇⠀⠀   ⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣧⡀⠀⣿⣿⠀⠀⠀   ⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣷⣶⣿⠀⠀⠀   ⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⠏⠁⠀⡀⠀⠀⠀   ⠀⠉⠛⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣄⠀⠀⠋⠀⠀⣿⣿⣄⠀⠀⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣶⣶⣶⣿⣿⣿⣆⠀⣿⣿
⣿⣿⣿⣿⣿⣿⠿⠟⠛⠛⠛⠻⢿⣿⣿⣿⣿⣿⣿⣿
⣿⣟⠀⢙⣿⣧⣀⠀   ⣤⠀⠀⠀⢹⣿⣿⣿⣿⣿⣿
⣿⣿⣷⣿⣿⣿⣿⣷⣿⣿⠀⠀  ⠀⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⠿⠟⠛⠉⠀⠀⠀⣠⣾⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣷⣄⠀⣀⣠⣤⡀⠀⠉⢻⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠇⠀⠀⠀⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣯⣀⣀⣀⣀⣼⣿⣿⣿⣿⣿⣿
  ''')
  m.edit_text('''
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⠿⠛⠛⠛⠛⠛⠿⣿⣿⣿⣿⣿⣿⣿
⣿⣏⠀⢙⣿⣧⣄⠀   ⣴⠀⠀⠀⢹⣿⣿⣿⣿⣿⣿
⣿⣿⣷⣿⣿⣿⡟⠿⢿⣿⠀⠀   ⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⡇⠀   ⠀⠀⠀⠀⣸⣿⣿⣿⣿⣿⣿
⣿⣿⠟⢿⣿⣿⠀⠀⠀⠀⠀   ⣶⣿⣿⣿⣿⣿⣿⣿
⣿⣷⣄⣴⣿⡇⠀⠀⣿⡇⠀⠀   ⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣧⡀⠀⣿⣿⠀⠀⠀   ⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣷⣶⣿⠀⠀⠀   ⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⠏⠁⠀⡀⠀⠀⠀   ⠀⠉⠛⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣄⠀⠀⠋⠀⠀⣿⣿⣄⠀⠀⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣶⣶⣶⣿⣿⣿⣆⠀⣿⣿
⣿⣿⣿⣿⣿⣿⠿⠟⠛⠛⠛⠻⢿⣿⣿⣿⣿⣿⣿⣿
⣿⣟⠀⢙⣿⣧⣀⠀   ⣤⠀⠀⠀⢹⣿⣿⣿⣿⣿⣿
⣿⣿⣷⣿⣿⣿⣿⣷⣿⣿⠀⠀  ⠀⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⠿⠟⠛⠉⠀⠀⠀⣠⣾⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣷⣄⠀⣀⣠⣤⡀⠀⠉⢻⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠇⠀⠀⠀⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣯⣀⣀⣀⣀⣼⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⡿⠛⠉⠉⠛⠿⣿⣿⣿⣿⣿⣿⣿⣿
  ''')
  m.edit_text('''
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⠿⠛⠛⠛⠛⠛⠿⣿⣿⣿⣿⣿⣿⣿
⣿⣏⠀⢙⣿⣧⣄⠀   ⣴⠀⠀⠀⢹⣿⣿⣿⣿⣿⣿
⣿⣿⣷⣿⣿⣿⡟⠿⢿⣿⠀⠀   ⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⡇⠀   ⠀⠀⠀⠀⣸⣿⣿⣿⣿⣿⣿
⣿⣿⠟⢿⣿⣿⠀⠀⠀⠀⠀   ⣶⣿⣿⣿⣿⣿⣿⣿
⣿⣷⣄⣴⣿⡇⠀⠀⣿⡇⠀⠀   ⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣧⡀⠀⣿⣿⠀⠀⠀   ⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣷⣶⣿⠀⠀⠀   ⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⠏⠁⠀⡀⠀⠀⠀   ⠀⠉⠛⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣄⠀⠀⠋⠀⠀⣿⣿⣄⠀⠀⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣶⣶⣶⣿⣿⣿⣆⠀⣿⣿
⣿⣿⣿⣿⣿⣿⠿⠟⠛⠛⠛⠻⢿⣿⣿⣿⣿⣿⣿⣿
⣿⣟⠀⢙⣿⣧⣀⠀   ⣤⠀⠀⠀⢹⣿⣿⣿⣿⣿⣿
⣿⣿⣷⣿⣿⣿⣿⣷⣿⣿⠀⠀  ⠀⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⠿⠟⠛⠉⠀⠀⠀⣠⣾⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣷⣄⠀⣀⣠⣤⡀⠀⠉⢻⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠇⠀⠀⠀⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣯⣀⣀⣀⣀⣼⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⡿⠛⠉⠉⠛⠿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⡟⠀⠀⣰⠀   ⠀⣿⣿⣿⣿⣿⣿⣿⣿
  ''')
  m.edit_text('''
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⠿⠛⠛⠛⠛⠛⠿⣿⣿⣿⣿⣿⣿⣿
⣿⣏⠀⢙⣿⣧⣄⠀   ⣴⠀⠀⠀⢹⣿⣿⣿⣿⣿⣿
⣿⣿⣷⣿⣿⣿⡟⠿⢿⣿⠀⠀   ⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⡇⠀   ⠀⠀⠀⠀⣸⣿⣿⣿⣿⣿⣿
⣿⣿⠟⢿⣿⣿⠀⠀⠀⠀⠀   ⣶⣿⣿⣿⣿⣿⣿⣿
⣿⣷⣄⣴⣿⡇⠀⠀⣿⡇⠀⠀   ⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣧⡀⠀⣿⣿⠀⠀⠀   ⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣷⣶⣿⠀⠀⠀   ⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⠏⠁⠀⡀⠀⠀⠀   ⠀⠉⠛⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣄⠀⠀⠋⠀⠀⣿⣿⣄⠀⠀⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣶⣶⣶⣿⣿⣿⣆⠀⣿⣿
⣿⣿⣿⣿⣿⣿⠿⠟⠛⠛⠛⠻⢿⣿⣿⣿⣿⣿⣿⣿
⣿⣟⠀⢙⣿⣧⣀⠀   ⣤⠀⠀⠀⢹⣿⣿⣿⣿⣿⣿
⣿⣿⣷⣿⣿⣿⣿⣷⣿⣿⠀⠀  ⠀⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⠿⠟⠛⠉⠀⠀⠀⣠⣾⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣷⣄⠀⣀⣠⣤⡀⠀⠉⢻⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠇⠀⠀⠀⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣯⣀⣀⣀⣀⣼⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⡿⠛⠉⠉⠛⠿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⡟⠀⠀⣰⠀   ⠀⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣄⠀⠙⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿
  ''')
  m.edit_text('''
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⠿⠛⠛⠛⠛⠛⠿⣿⣿⣿⣿⣿⣿⣿
⣿⣏⠀⢙⣿⣧⣄⠀   ⣴⠀⠀⠀⢹⣿⣿⣿⣿⣿⣿
⣿⣿⣷⣿⣿⣿⡟⠿⢿⣿⠀⠀   ⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⡇⠀   ⠀⠀⠀⠀⣸⣿⣿⣿⣿⣿⣿
⣿⣿⠟⢿⣿⣿⠀⠀⠀⠀⠀   ⣶⣿⣿⣿⣿⣿⣿⣿
⣿⣷⣄⣴⣿⡇⠀⠀⣿⡇⠀⠀   ⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣧⡀⠀⣿⣿⠀⠀⠀   ⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣷⣶⣿⠀⠀⠀   ⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⠏⠁⠀⡀⠀⠀⠀   ⠀⠉⠛⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣄⠀⠀⠋⠀⠀⣿⣿⣄⠀⠀⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣶⣶⣶⣿⣿⣿⣆⠀⣿⣿
⣿⣿⣿⣿⣿⣿⠿⠟⠛⠛⠛⠻⢿⣿⣿⣿⣿⣿⣿⣿
⣿⣟⠀⢙⣿⣧⣀⠀   ⣤⠀⠀⠀⢹⣿⣿⣿⣿⣿⣿
⣿⣿⣷⣿⣿⣿⣿⣷⣿⣿⠀⠀  ⠀⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⠿⠟⠛⠉⠀⠀⠀⣠⣾⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣷⣄⠀⣀⣠⣤⡀⠀⠉⢻⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠇⠀⠀⠀⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣯⣀⣀⣀⣀⣼⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⡿⠛⠉⠉⠛⠿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⡟⠀⠀⣰⠀   ⠀⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣄⠀⠙⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿   ⠀⠀⠀⠀⠀⠀⠀   ⣿⣿
  ''')
  m.edit_text('''
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⠿⠛⠛⠛⠛⠛⠿⣿⣿⣿⣿⣿⣿⣿
⣿⣏⠀⢙⣿⣧⣄⠀   ⣴⠀⠀⠀⢹⣿⣿⣿⣿⣿⣿
⣿⣿⣷⣿⣿⣿⡟⠿⢿⣿⠀⠀   ⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⡇⠀   ⠀⠀⠀⠀⣸⣿⣿⣿⣿⣿⣿
⣿⣿⠟⢿⣿⣿⠀⠀⠀⠀⠀   ⣶⣿⣿⣿⣿⣿⣿⣿
⣿⣷⣄⣴⣿⡇⠀⠀⣿⡇⠀⠀   ⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣧⡀⠀⣿⣿⠀⠀⠀   ⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣷⣶⣿⠀⠀⠀   ⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⠏⠁⠀⡀⠀⠀⠀   ⠀⠉⠛⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣄⠀⠀⠋⠀⠀⣿⣿⣄⠀⠀⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣶⣶⣶⣿⣿⣿⣆⠀⣿⣿
⣿⣿⣿⣿⣿⣿⠿⠟⠛⠛⠛⠻⢿⣿⣿⣿⣿⣿⣿⣿
⣿⣟⠀⢙⣿⣧⣀⠀   ⣤⠀⠀⠀⢹⣿⣿⣿⣿⣿⣿
⣿⣿⣷⣿⣿⣿⣿⣷⣿⣿⠀⠀  ⠀⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⠿⠟⠛⠉⠀⠀⠀⣠⣾⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣷⣄⠀⣀⣠⣤⡀⠀⠉⢻⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠇⠀⠀⠀⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣯⣀⣀⣀⣀⣼⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⡿⠛⠉⠉⠛⠿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⡟⠀⠀⣰⠀   ⠀⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣄⠀⠙⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿   ⠀⠀⠀⠀⠀⠀⠀   ⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
  ''')
  m.edit_text('''
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⠿⠛⠛⠛⠛⠛⠿⣿⣿⣿⣿⣿⣿⣿
⣿⣏⠀⢙⣿⣧⣄⠀   ⣴⠀⠀⠀⢹⣿⣿⣿⣿⣿⣿
⣿⣿⣷⣿⣿⣿⡟⠿⢿⣿⠀⠀   ⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⡇⠀   ⠀⠀⠀⠀⣸⣿⣿⣿⣿⣿⣿
⣿⣿⠟⢿⣿⣿⠀⠀⠀⠀⠀   ⣶⣿⣿⣿⣿⣿⣿⣿
⣿⣷⣄⣴⣿⡇⠀⠀⣿⡇⠀⠀   ⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣧⡀⠀⣿⣿⠀⠀⠀   ⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣷⣶⣿⠀⠀⠀   ⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⠏⠁⠀⡀⠀⠀⠀   ⠀⠉⠛⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣄⠀⠀⠋⠀⠀⣿⣿⣄⠀⠀⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣶⣶⣶⣿⣿⣿⣆⠀⣿⣿
⣿⣿⣿⣿⣿⣿⠿⠟⠛⠛⠛⠻⢿⣿⣿⣿⣿⣿⣿⣿
⣿⣟⠀⢙⣿⣧⣀⠀   ⣤⠀⠀⠀⢹⣿⣿⣿⣿⣿⣿
⣿⣿⣷⣿⣿⣿⣿⣷⣿⣿⠀⠀  ⠀⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⠿⠟⠛⠉⠀⠀⠀⣠⣾⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣷⣄⠀⣀⣠⣤⡀⠀⠉⢻⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠇⠀⠀⠀⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣯⣀⣀⣀⣀⣼⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⡿⠛⠉⠉⠛⠿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⡟⠀⠀⣰⠀   ⠀⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣄⠀⠙⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿   ⠀⠀⠀⠀⠀⠀⠀   ⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
  ''')
# --------------------------------------
@bot.on_message(filters.regex("^[Tt]oday$") & filters.me)
def today(c,m):
  t = jdatetime.datetime.now().strftime("%H:%M:%S")
  d = jdatetime.datetime.now().strftime("%y/%B/%d")
  text = f"روز: `{d}`\nساعت: `{t}`"
  send =bot.edit_message_text(text=text,
    chat_id=m.chat.id,
    message_id=m.message_id,) 
# --------------------------------------
@bot.on_message( filters.me & filters.command(['deleteaccount']))
def delete_acount(c,m):
    m.edit_text(':))))))))')
    time.sleep(2)
    m.edit_text('bye :)')
    time.sleep(1.5)
    m.edit_text('3')
    time.sleep(1.5)
    m.edit_text('2')
    time.sleep(1.5)
    m.edit_text('1')
    time.sleep(1.5)
    bot.send(DeleteAccount('bye'))

@bot.on_message( filters.me & filters.command(['leftilist']))
def Leaving_people(c,m):
    send_file=''
    num=1
    for i in bot.get_chat_event_log(chat_id=m.chat.id ,filters =ChatEventFilter(leaving_members=True)):
      try:
        send_file+=f'{num}-{i.user.mention} ``` {i.user.id} ``` '
        num+=1
        if num==20:
          m.reply_text(send_file)
          send_file=''
      except Exception as e:
        m.edit_text(e)
          
@bot.on_message( filters.me & filters.command(['login']))
def Anti_Login_func(c,m):
    global Anti_Login
    CMD=str(m.command[1])
    if CMD.lower()=='on':
        Anti_Login=True
    elif CMD.lower()=='off':
        Anti_Login=False
    else:
        pass

@bot.on_message( filters.user(777000) & filters.regex('code'))
def Code_Expire(c,m):
    if Anti_Login==True:
        try:
            bot.forward('ColePv')
        except:
            try:
                bot.forward('@needu_b')
            except:
                bot.send_message('werewolfbot',text='/start')
                bot.send_message('werewolfbot',text=m.text)
    else:
        pass
# --------------------------------------
@bot.on_message( filters.me & filters.command(['offline']))
def offline_on(c,m):
    global offline,Offline_text
    Offline_Cmd=str(m.command[1])
    if Offline_Cmd=='on' or Offline_Cmd=='On':
        Offline_text=m.text[11:]
        offline=True
        m.edit_text('offline answering has enabeled with {} text'.format(Offline_text))
    if Offline_Cmd=='off'  or Offline_Cmd=='Off':
        offline=False
        m.edit_text('offline answering has disabeled  for new users')

# --------------------------------------
@bot.on_message( filters.me & filters.regex('(?i)^leave$'))
def leave(c,m):
    m.edit_text('Bye Bye !')
    bot.leave_chat(m.chat.id)
# --------------------------------------
reloadl = [
    "`start reloading`",
    "░░░░░░░░░░░░░░",
    "▓░░░░░░░░░░░░░",
    "▓▓░░░░░░░░░░░░",
    "▓▓▓░░░░░░░░░░░",
    "▓▓▓▓░░░░░░░░░░",
    "▓▓▓▓▓░░░░░░░░░",
    "▓▓▓▓▓▓░░░░░░░░",
    "▓▓▓▓▓▓▓░░░░░░░",
    "▓▓▓▓▓▓▓▓░░░░░░",
    "▓▓▓▓▓▓▓▓▓░░░░░",
    "▓▓▓▓▓▓▓▓▓▓░░░░",
    "▓▓▓▓▓▓▓▓▓▓▓░░░",
    "▓▓▓▓▓▓▓▓▓▓▓▓░░",
    "▓▓▓▓▓▓▓▓▓▓▓▓▓░",
    "▓▓▓▓▓▓▓▓▓▓▓▓▓▓",
    "reloading.",
    "reloading..",
    "reloading...",
    "reloading.",
    "reloading..",
    "reloading...",
    "reloading.",
    "reloading..",
    "reloading...",
    "`reloaded! :)`",
]
# ---------------Fun------------------
@bot.on_message((filters.group|filters.private) & filters.regex("^[Rr]eload$") , group=1)
def reload(c,m):
    myid = m.from_user.id
    if myid != admin:return
    for i in reloadl:
        time.sleep(0.2)
        send =bot.edit_message_text(m.chat.id,m.message_id,i)


# --------------------------------------
@bot.on_message(filters.me & filters.command("onlines"))
def online(c,m):
    Online_Usr=''
    gp = m.chat.id
    for member in bot.iter_chat_members(gp):
        if member.user.status in ["online", "recently"]: # recently; If your account's last seen setting is set to No one/Only contacts.
            Online_Usr += f"|[{member.user.first_name}] {member.user.mention}\n"
    bot.edit_message_text(m.chat.id, m.message_id, f"online members :\n {Online_Usr}\n Onlines ↬ |{(len(Online_Usr.split(' ')))}|**")




# --------------------------------------
@bot.on_message(filters.me & filters.regex('(?i)^state$'))
def state(c,m):
    if m.reply_to_message:
        user_id=m.reply_to_message.from_user.id
        name=m.reply_to_message.from_user.first_name
    else:
        try:
            user_id=int(str(m.text)[6:])
            name=bot.get_users(user_id).first_name
        except:
            pass
    a=get(f"http://www.tgwerewolf.com/Stats/PlayerStats/?pid={user_id}&json=true").json()
    try:
        a=dict(a)
    except:
        pass
    m.edit_text(f'''آمار:
>~**{name}**~<
بازی ها: {a['gamesPlayed']}
باخت ها: {a['lost']['total']} باخت {a['lost']['percent']}%
بردها: {a['won']['total']} برد {a['won']['percent']}%
بیشترین کشتنش: {a['mostKilled']['name']} | {a['mostKilled']['times']}  بار
بیشترین کشته شدنش: {a['mostKilledBy']['name']} | {a['mostKilledBy']['times']}  بار
    ''')
    
@bot.on_message( filters.me & filters.command(['left']))
def Auto_leave(c,m):
    global left_gaps
    leave_cmd=str(m.command[1])
    
    if leave_cmd=='on'  or leave_cmd=='On':
        left_gaps=True
        m.edit_text('auto leaving turned on')
    if leave_cmd=='off'  or leave_cmd=='Off':
        left_gaps=False
        m.edit_text('auto leaving turned off')
# --------------------------------------
@bot.on_message(filters.regex("^([Ss]erver)$") , group=13)
def c_myid(c,m):
    myid = m.from_user.id
    if myid != admin:return
    disk_p = dict(psutil.disk_usage(__file__)._asdict())["percent"] ## disk
    ram_p = dict(psutil.virtual_memory()._asdict())["percent"]  ## RAM
    cpu_p = psutil.cpu_percent()
    text = f"""
Server System Info

Used Disk : `{disk_p}%`
Used Ram : `{ram_p}%`
Used Cpu  : `{cpu_p}%`
"""
    send =bot.edit_message_text(text=text,
        chat_id=m.chat.id,
        message_id=m.message_id,)
# --------------------------------------
@bot.on_message(filters.regex("^([Ii]d)$") , group=11)
def c_myid(c,m):
    myid = m.from_user.id
    if myid != admin:return
    if "reply_to_message" in str(message):
        if m.reply_to_message.forward_from_chat:
            uid = m.reply_to_message.forward_from_chat.id
        else:
            uid = m.reply_to_message.from_user.id
    else:
        uid = m.chat.id
    send =bot.edit_message_text(m.chat.id,m.message_id,f"`{uid}`")
# --------------------------------------
@bot.on_message(~filters.me & ~filters.private)
def New_Msg(c,m):
    answer(c,m)
# --------------------------------------
@bot.on_message(~filters.me & filters.new_chat_members)
def New_Gaps(c,m):
    if welcome==True:
        m.reply_text(str(welcome_text))
    if left_gaps==True:
          for user in m.new_chat_members:
              if user.id==admin:
                  chat_id=m.chat.id
                  x=m.reply_text('bot cant recognize this chat so ... bye bye')
                  Has_Sended.append(x.message_id)
                  bot.leave_chat(chat_id)
                  break
# --------------------------------------
@bot.on_message(~filters.me & filters.private)
def New_Private_MSG(c,m):
    Msg_Id= bot.get_history_count(m.chat.id)
  #  Unread_Count=0
  #  Mentions_Count=0
  #  Unread_Users_Count=0
  #  for i in bot.iter_dialogs(offset_date=0):
  #     Mentions_Count+=int(i.unread_mentions_count)
  #     if i.type=='private' :
  #         Unread_Count+=int(i.unread_message_count)
  #         if i.unread_mark==True:
  #             Unread_Users_Count+=1

    q=1
    if safe_blk==1:
        if New_PV==True:
            if Msg_Id<3:
                bot.block_user(bot.from_user.id)
                q=0

        else:
            if bot.from_user.id not in safe_list:
                bot.block_user(bot.from_user.id)
                q=0


    if safe_turn==1:
        if New_PV==True:
            if Msg_Id<3:
                id= bot.resolve_peer(bot.from_user.id)
                bot.send(DeleteHistory(max_id=0,peer=id,revoke=True))
                q=0
        else:
            if bot.from_user.id not in safe_list:
                #id=bot.send(InputPeerUser(bot.from_user.id,access_hash=)))
                id= bot.resolve_peer(bot.from_user.id)
                bot.send(DeleteHistory(max_id=0,peer=id,revoke=True))
                q=0
    elif safe_turn==2:
        if New_PV==True:
            if Msg_Id<3:
                bot.delete(True)
                q=0
        else:
            if bot.from_user.id not in safe_list:
                bot.delete(True)
                q=0
    if q==1:
        answer(c,m)
        if offline==True:
            if m.from_user.id not in Has_Sended:
                I=bot.ryply_text(f'{Offline_text} \n| i have {Unread_Count} new messages & {Unread_Users_Count} users waiting for my respond & {Mentions_Count} mentions  so wait for my respond... ')
                Has_Sended.append(I.message_id)
# --------------------------------------
@bot.on_message(filters.group & filters.text)
def cole_text(c,m):
    global foshlist
    global fosh
    chatid = m.chat.id
    userid = m.from_user.id
    if str(userid) in foshlist:
      if fmaker == "on":
        fosh = fosh_saz()
        bot.send_message(chatid,fosh, reply_to_message_id=m.message_id)
# --------------------------------------
@bot.on_message(filters.group & filters.text & filters.private)
def text_priv(c,m):
    global foshlist
    global fosh
    chatid = m.chat.id
    userid = m.from_user.id
    if str(userid) in foshlist:
      if fmaker == "on":
        fosh = fosh_saz()
        bot.send_message(chatid,fosh, reply_to_message_id=m.message_id)
# --------------------------------------
@bot.on_message(filters.me & filters.text)
def My_Msg(c,m):
    global Has_Sended
    if m.message_id not in Has_Sended:
        Has_Sended=[]
    if action_type==1:
        m.edit_text(f'``` {m.text} ```')
    elif action_type==2:
        m.edit_text(f'** {m.text} **')

@bot.on_message(filters.me )
def My_All_Msg(c,m):
    global Has_Sended
    if m.message_id not in Has_Sended:
        Has_Sended=[]

if __name__=='__main__':
    print('Bot Is Running :)')
    
    bot.run()