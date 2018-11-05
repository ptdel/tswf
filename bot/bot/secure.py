from os.path import dirname, realpath
from twisted.internet import ssl
from OpenSSL import SSL

keys = ''.join([dirname(realpath(__file__)), "/keys/"])

class CtxFactory(ssl.ClientContextFactory):

    def getContext(self):
        self.method = SSL.SSLv23_METHOD
        ctx = ssl.ClientContextFactory.getContext(self)
        ctx.use_certificate_file(keys + 'cert.pem')
        ctx.use_privatekey_file(keys + 'cert.key')
        return ctx
