from re import search
from os import environ
from twisted.internet import protocol, reactor
from twisted.words.protocols.irc import IRCClient
from datetime import datetime
from requests import get

class Bot(IRCClient):

    nickname = environ['NICKNAME']
    password = environ['PASSWORD']

    def signedOn(self):
        self.join(self.factory.channel, self.factory.key)

    def joined(self, channel):
        print(datetime.utcnow().isoformat() + " - joined: ", channel)

    def privmsg(self, user, channel, msg):
        url_pattern = "(?P<url>https?://[^\s]+)"
        user = user.split('!', 1)[0]
        if msg.startswith('<>'):
            link = dict(song = search(url_pattern, msg).group("url"))
            get(environ['QUEUE_URL'], params=link, verify=False)
            

class BotFactory(protocol.ClientFactory):
    def __init__(self, channel, key):
        self.channel = channel
        self.key = key
    def buildProtocol(self,addr):
        p = Bot()
        p.factory = self
        return p

    def clientConnectionLost(self,connector,reason):
        connector.connect()

    def clientConnectionFailed(self,connector,reason):
        print("connection failed: ", reason)
        reactor.stop()
