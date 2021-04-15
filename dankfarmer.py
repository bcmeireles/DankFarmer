import requests
import random
import time

commands = ["work", "daily", "weekly", "monthly", "fish", "hunt", "beg", "use padlock"]
sell = ["boar", "deer", "duck", "fish", "rarefish", "rabbit", "skunk", "bread", "pizza", "cookie"]
pet_actions = ["feed", "pat", "wash"]

channelid = ''
token = ''

def run_commands():
    for command in commands:
        r = requests.post(f"https://discord.com/api/v8/channels/{channelid}/messages", headers={
            "Authorization":token
        }, data={
            "content":f"pls {command}"
        })
        time.sleep(5)
    other_commands()

def other_commands():
    r = requests.post(f"https://discord.com/api/v8/channels/{channelid}/messages", headers={
        "Authorization":token
    }, data={
        "content":"pls highlow"
    })
    time.sleep(5)

    r = requests.post(f"https://discord.com/api/v8/channels/{channelid}/messages", headers={
        "Authorization":token
    }, data={
        "content":"high"
    })
    time.sleep(5)

    r = requests.post(f"https://discord.com/api/v8/channels/{channelid}/messages", headers={
        "Authorization":token
    }, data={
        "content":"pls pm"
    })
    time.sleep(5)

    r = requests.post(f"https://discord.com/api/v8/channels/{channelid}/messages", headers={
        "Authorization":token
    }, data={
        "content":"f"
    })
    time.sleep(5)

    r = requests.post(f"https://discord.com/api/v8/channels/{channelid}/messages", headers={
        "Authorization":token
    }, data={
        "content":"pls use bank"
    })
    time.sleep(5)

    r = requests.post(f"https://discord.com/api/v8/channels/{channelid}/messages", headers={
        "Authorization":token
    }, data={
        "content":"1"
    })
    time.sleep(5)
    sell_commands()



def sell_commands():
    for item in sell:
        r = requests.post(f"https://discord.com/api/v8/channels/{channelid}/messages", headers={
            "Authorization":token
        }, data={
            "content":f"pls sell {item} all"
        })
        time.sleep(5)
    deposit()


def pet_commands():
    for action in pet_actions:
        r = requests.post(f"https://discord.com/api/v8/channels/{channelid}/messages", headers={
            "Authorization":token
        }, data={
            "content":f"pls pet {action}"
        })
        time.sleep(5)


def deposit():
    r = requests.post(f"https://discord.com/api/v8/channels/{channelid}/messages", headers={
            "Authorization":token
        }, data={
            "content":f"pls dep all"
        })

while True:
    run_commands()
    run_commands()
    run_commands()
    run_commands()
    run_commands()
    pet_commands()