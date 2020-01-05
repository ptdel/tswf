from os import environ
from bot import BotFactory
from twisted.internet import reactor
from secure import CtxFactory

if __name__ == "__main__":
    f = BotFactory("#dailyprog", "")
    reactor.connectSSL(environ["IRC_SERVER"], 6697, f, CtxFactory())
    reactor.run()
