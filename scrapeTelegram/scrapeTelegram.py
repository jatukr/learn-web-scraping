from telethon.sync import TelegramClient
from telethon.tl.functions.messages import GetDialogsRequest
from telethon.tl.types import InputPeerEmpty
import csv

api_id = 1779804
api_hash = 'e320a33e11a7289fcdf4ed89431f4de2'
phone = '+6285733085591'
client = TelegramClient(phone, api_id, api_hash)

client.connect()
if not client.is_user_authorized():
    client.send_code_request(phone)
    client.sign_in(phone, input('Enter the code : '))

chats = []
last_date = None
chunk_size = 200
groups = []

result = client(GetDialogsRequest(
            offset_date=last_date,
            offset_id=0,
            offset_peer=InputPeerEmpty(),
            limit=chunk_size,
            hash=0
        ))
print('Check 1 : ', result.chats)
chats.extend(result.chats)
print('Check 2 : ', chats)

for chat in chats:
    try:
        if chat.megagroup:
            groups.append(chat)
    except:
        continue

"""
print('Choose a group to scrape members from : ')
i = 0
for g in groups:
    print(str(i) + '-' + g.title)
    i += 1

g_index = input('Enter a number: ')
target_group = groups[int(g_index)]

print('Fetching Member....')
all_participants = []
all_participants = client.get_participants(target_group, aggressive=True)

print('Saving In File...')
with open('member_gosc.csv', 'w', encoding='UTF-8') as f:
    writer = csv.writer(f, delimiter=',', lineterminator='\n')
    writer.writerow(['username', 'user_id', 'access hash', 'name', 'group', 'group id'])
    for user in all_participants:
        if user.username:
            username = user.username
        else:
            username = ''
        if user.first_name:
            first_name = user.first_name
        else:
            first_name = ''
        if user.last_name:
            last_name = user.last_name
        else:
            last_name = ''
        name = (first_name + ' ' + last_name).strip()
        writer.writerow([username, user.id, user.access_hash, name, target_group.title, target_group.id])
print('Members scraped successfully.')
"""