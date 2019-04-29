# -*- coding: UTF-8 -*-
from wxpy import *
import time
import random

bot = Bot(cache_path=True)

girl_friend = bot.friends().search(u"七七七", sex=FEMALE)[0]



#girl_friend.send("Hello, testing...")

#mom = bot.friends().search(u"杨秀娟", sex=FEMALE)[0]

# 打印来自其他好友、群聊和公众号的消息
@bot.register()
def print_others(msg):
    print(msg)

# 回复 my_friend 的消息 (优先匹配后注册的函数!)
#@bot.register(mom)
#def reply_my_friend(msg):
    #return 'received: {} ({})'.format(msg.text, msg.type)

# 自动接受新的好友请求
@bot.register(msg_types=FRIENDS)
def auto_accept_friends(msg):
    # 接受好友请求
    new_friend = msg.card.accept()
    # 向新的好友发送消息
    new_friend.send('哈哈，我自动接受了你的好友请求')
    
    
# 回复 my_friend 的消息 (优先匹配后注册的函数!)
@bot.register(girl_friend)
def reply_my_friend(msg):
    time.sleep(random.randint(0,20))
    answer = ""
    if "想你" in msg.text and "不想你".find(msg.text) < 0:
        
        miss_you = ["我也想妳鸭☆","好想好想好想妳\n想抱抱妳","想死妳啦!","不要太想我哦，马上就肥来了！♥","快肥来了啦!",
                "么么么么么么么达", "想妳想妳，虽然这些是预录好的，但我真的好想妳..","抱抱妳，要乖哦", "不要太担心哦","爱你哦★",
                "我也好想见妳", "老婆又想我了，开心☄", "爱老婆", "老婆今天干麻了?", "老婆，我也想你",
                "想老婆，想跟老婆一起玩...", "老婆要一直想我哦>口<", "我也想妳","想我就看照片吧","么么，我也想你啦","♥ ♥ ♥ "]
        
        num = random.randint(0,20)
        answer = miss_you[num]
        return answer
    
    




embed()
