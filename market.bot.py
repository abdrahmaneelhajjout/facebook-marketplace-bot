# -*- coding: utf-8 -*-

from fbchat import Client
from fbchat.models import *
from config import *
from time import sleep
import random
import re


class MarketBot(Client):

    def __init__(self, email, password):
        super().__init__(email, password)
        self.conversation_status = {}  # Track conversation status

    def onMessage(self, author_id, message_object, thread_id, thread_type, **kwargs):

        if author_id != self.uid:
            message_text = message_object.text.lower()

            if message_text in message_mappings:
                sleep(random.randrange(5, 15))
                self.markAsDelivered(thread_id, message_object.uid)
                self.markAsRead(thread_id)
                self.setTypingStatus(
                    TypingStatus.TYPING, thread_id=thread_id, thread_type=thread_type)
                sleep(random.randrange(10, 25))
                response = message_mappings[message_text]

                # Send each line as a separate message
                for line in response.splitlines():
                    self.send(Message(text=line), thread_id=thread_id,
                              thread_type=thread_type)

            else:
                if thread_id not in self.conversation_status:
                    self.conversation_status[thread_id] = "first"
                    # Perform actions for the first message (e.g., greeting)
                    sleep(random.randrange(5, 15))
                    self.markAsDelivered(thread_id, message_object.uid)
                    self.markAsRead(thread_id)
                    self.setTypingStatus(
                        TypingStatus.TYPING, thread_id=thread_id, thread_type=thread_type)
                    sleep(random.randrange(10, 25))
                    response = message_mappings[message_text]

                    # Send each line as a separate message
                    for line in response.splitlines():
                        self.send(Message(text=line),
                                  thread_id=thread_id, thread_type=thread_type)

            if message_object.text.find('livr') >= 0:
                sleep(random.randrange(5, 15))
                self.markAsDelivered(thread_id, message_object.uid)
                self.markAsRead(thread_id)
                self.setTypingStatus(
                    TypingStatus.TYPING, thread_id=thread_id, thread_type=thread_type)
                sleep(random.randrange(10, 25))
                self.send(Message(text=deliver_message),
                          thread_id=thread_id, thread_type=thread_type)

            if (message_object.text.find('etat') >= 0) or (message_object.text.find('état') >= 0):
                sleep(random.randrange(5, 15))
                self.markAsDelivered(thread_id, message_object.uid)
                self.markAsRead(thread_id)
                self.setTypingStatus(
                    TypingStatus.TYPING, thread_id=thread_id, thread_type=thread_type)
                sleep(random.randrange(10, 20))
                self.send(Message(text=status_phone_message),
                          thread_id=thread_id, thread_type=thread_type)

            if (message_object.text.find('adresse') >= 0):
                sleep(random.randrange(5, 15))
                self.markAsDelivered(thread_id, message_object.uid)
                self.markAsRead(thread_id)
                self.setTypingStatus(
                    TypingStatus.TYPING, thread_id=thread_id, thread_type=thread_type)
                sleep(random.randrange(10, 20))
                self.send(Message(text=shop_adress_message),
                          thread_id=thread_id, thread_type=thread_type)

            if message_object.text.lower() == "ok":
                sleep(random.randrange(5, 15))
                self.markAsDelivered(thread_id, message_object.uid)
                self.markAsRead(thread_id)
                self.reactToMessage(message_object.uid, MessageReaction.YES)


client = MarketBot(email, password)
client.listen()
