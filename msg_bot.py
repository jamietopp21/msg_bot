import re

import random as rand_module

from fuck import get_fuck
from define_word import get_definition
import os.path
import os

import requests
from bs4 import BeautifulSoup
from fbchat import log, Client
from fbchat.client import *

word_list =[
    'random word'
]

# Subclass fbchat.Client and override required methods
class ToppBot(Client):
    def onMessage(self, author_id, message_object, thread_id, thread_type, **kwargs):

        if message_object.text is not None:

            if thread_type == ThreadType.GROUP:
                group_participants = list(self.fetchGroupInfo(thread_id)[thread_id].participants)
                group_participants.remove(self.uid)


            if author_id != self.uid:
                msg_text = message_object.text

                send_this = message_object

                if re.match('!doggo', msg_text):
                    req = json.loads(requests.get('https://dog.ceo/api/breeds/image/random').text)
                    url = req['message']

                    self.sendRemoteImage(url, message=Message(text=''), thread_id=thread_id, thread_type=thread_type)

                elif re.match('!imgay', msg_text):
                    send_this.text = f'seriously mate'
                    self.send(send_this, thread_id=thread_id, thread_type=thread_type)

                elif re.match('!fox', msg_text):
                    req = json.loads(requests.get('https://randomfox.ca/floof/').text)
                    url = req['image']

                    self.sendRemoteImage(url, message=Message(text=''), thread_id=thread_id, thread_type=thread_type)


                elif re.match('!checkserver', msg_text):
                    send_this.text = f'I\'m working!'
                    self.send(send_this, thread_id=thread_id, thread_type=thread_type)

                elif re.match('!choosefood', msg_text):
                    foods = [
                        'Nandos',
                        'McDonalds',
                        'Pizza Plus',
                        'Subway',
                        'VIP Pizza',
                        'Spoons',
                        'Taco Bell',
                        'Burger King',
                        'Grubbs',
                        'Buddies',
                        'Fillets',
                        'Pizza Express',
                        'Casa Brazil',
                        'Coast to Coast',
                        'Pizza Hut',
                        'Meat Liquor',
                        'GBK',
                        'Home Food!',
                        'Supermarket',
                        'Starve'
                    ]

                    choice = rand_module.choice(foods)
                    send_this.text = f'{choice}!'
                    self.send(send_this, thread_id=thread_id, thread_type=thread_type)


                elif re.match('!trivia', msg_text):

                    r = requests.get('https://opentdb.com/api.php?amount=1').json()

                    question = r['results'][0]['question']
                    correct = r['results'][0]['correct_answer']
                    choices = r['results'][0]['incorrect_answers']

                    choices.append(correct)

                    rand_module.shuffle(choices)

                    correct_index = choices.index(correct) + 1


                    send_this.text = question.replace('&quot;', '"').replace('&#039;', "'")
                    self.send(send_this, thread_id=thread_id, thread_type=thread_type)
                    
                    letters = ['a','b','c','d']

                    for x in range(0,len(choices)):
                        send_this.text = f'{letters[x]}) {choices[x]}'
                        self.send(send_this, thread_id=thread_id, thread_type=thread_type)


                    time.sleep(10)

                    send_this.text = f'The answer was: {correct}!'
                    self.send(send_this, thread_id=thread_id, thread_type=thread_type)

                    

                elif re.match('!urmomgay', msg_text):                    
                    send_this.text = f'no u'
                    self.send(send_this, thread_id=thread_id, thread_type=thread_type)
    

                elif re.match('!canigetayeet', msg_text):
                    e = 'E'*rand_module.randint(2,30)                   
                    send_this.text = f'Y{e}T'
                    self.send(send_this, thread_id=thread_id, thread_type=thread_type)


                elif re.match('!cato', msg_text):
                    req = requests.get('http://thecatapi.com/api/images/get?format=xml').text
                    
                    cat_url = re.search('<url>(.*)<\/url>',req).group(1)
                    self.sendRemoteImage(cat_url, message=Message(text=''), thread_id=thread_id, thread_type=thread_type)


                elif re.match('!pick (.*) or (.*)', msg_text):
                    rnd_choice = rand_module.randint(1,2)

                    choice = re.match('!pick (.*) or (.*)', msg_text).group(rnd_choice)
                    send_this.text = f'I\'ve picked: {choice}'
                    self.send(send_this, thread_id=thread_id, thread_type=thread_type)

                elif re.match('!whoshould (.*)\\?',msg_text):
                    task = re.match('!whoshould (.*)\\?',msg_text).group(1)
                    slave = rand_module.choice(group_participants)
                    send_this.text = f'{self.fetchUserInfo(slave)[slave].name} should {task}'
                    self.send(send_this, thread_id=thread_id, thread_type=thread_type)
                
                elif re.match('!fuckyou (.*)', msg_text):
                    send_this.text = get_fuck(re.match('!fuckyou (.*)', msg_text).group(1).strip().capitalize())
                    self.send(send_this, thread_id=thread_id, thread_type=thread_type)

                elif re.match('!define (.*)',msg_text):
                    defi = re.match('!define (.*)',msg_text).group(1).lower().strip()
                    send_this.text = get_definition(defi)
                    self.send(send_this, thread_id=thread_id, thread_type=thread_type)


                elif re.match('!bills £(\d+.\d\d)', msg_text):
                    split_this = float(re.match('!bills £(\d+.\d\d)', msg_text).group(1))
                    split_this = split_this/len(group_participants)
                    split_this = round(split_this,2)
                    split_this = str(split_this)
                    if split_this[-2:] == '.0':
                        split_this = split_this + '0'
                    send_this.text = f'Pay £{split_this} each!'

                    self.send(send_this, thread_id=thread_id, thread_type=thread_type)
                
                elif re.match('!snap', msg_text):
                    
                    victims = []
                    kill = len(group_participants)/2
                    if kill != int(kill):
                        if rand_module.randint(0,1) == 0:
                            kill = kill + 0.5
                        else:
                            kill = kill - 0.5
                    kill = int(kill)

                    for victim in rand_module.sample(group_participants,kill):
                        send_this.text = f'Thanos killed {self.fetchUserInfo(victim)[victim].name}!'
                        self.send(send_this, thread_id=thread_id, thread_type=thread_type)
                        self.removeUserFromGroup(victim,thread_id=thread_id)
                        victims.append(victim)

                    send_this.text = f'The rest of you survived, for now. The others will be back soon #TheyreInTheSoulStone.'
                    self.send(send_this, thread_id=thread_id, thread_type=thread_type)

                    time.sleep(5)

                    for victim in victims:
                        self.addUsersToGroup(victim,thread_id=thread_id)

                    
                elif re.match('!russianroulette', msg_text):
                    gun = []

                    send_this.text = 'Loading Gun...'
                    self.send(send_this, thread_id=thread_id, thread_type=thread_type)
                    time.sleep(0.3)
            

                    for x in range(0,len(group_participants)-1):
                        gun.append(0)
                    gun.append(1)

                    rand_module.shuffle(gun)
                    rand_module.shuffle(group_participants)


                    for x in range(0,len(gun)):
                        time.sleep(1)
                        if gun[x] == 0:
                            send_this.text = '*click*'
                            self.send(send_this, thread_id=thread_id, thread_type=thread_type)
                            time.sleep(0.2)

                            send_this.text = f'{self.fetchUserInfo(group_participants[x])[group_participants[x]].name} survived'
                            self.send(send_this, thread_id=thread_id, thread_type=thread_type)
                        
                        if gun[x] == 1:
                            victim = group_participants[x]
                            send_this.text = '*BANG*'
                            self.send(send_this, thread_id=thread_id, thread_type=thread_type)
                            time.sleep(0.2)
                            send_this.text = f'{self.fetchUserInfo(group_participants[x])[group_participants[x]].name} died #rip'
                            self.send(send_this, thread_id=thread_id, thread_type=thread_type)
                            self.removeUserFromGroup(victim,thread_id=thread_id)
                            break


                    time.sleep(5)
                    self.addUsersToGroup(victim,thread_id=thread_id)



                elif re.match('!sendnudes', msg_text):
                    self.sendRemoteImage('https://thumbs.dreamstime.com/b/funny-nudes-figures-18698635.jpg', message=Message(text=''), thread_id=thread_id, thread_type=thread_type)
                

                elif re.match('!important (.*)',msg_text):
                    #if a json file with the name thread_id_important doesn't exist, then create one
                    filename = f'{thread_id}_important.json'

                    if not os.path.isfile(filename):
                        important_json = open(filename,'w')
                        save_json = '{'+thread_id+'[]}'
                        save_json = json.loads(save_json)
                        important_json.write(json.dump(save_json))
                        important_json.close()

                
                elif re.match('!whatsimportant?',msg_text):
                    filename = f'{thread_id}_important.json'

                    if not os.path.isfile(filename):
                        send_this.text = 'Nothing saved!'
                        self.send(send_this, thread_id=thread_id, thread_type=thread_type)

                


                #print(f'{message_object.text} in thread {thread_id} which is {thread_type}')

                #self.send(message_object, thread_id=thread_id, thread_type=thread_type)

client = ToppBot(os.environ.get('MSGBOT_EMAIL'),os.environ.get('MSGBOT_PASSWORD'))
client.listen()
print('yeet!')