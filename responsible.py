import ed25519

class Account():

    def __init__(self):
        '''
        账号对象
        '''
        self.signing_key, self.verifying_key = ed25519.create_keypair()
        self.PublicKey = self.verifying_key.to_ascii(encoding="hex")
        self.PrivateKey = self.signing_key.to_ascii(encoding="hex")
        self.SigningKey = self.signing_key
        self.VerifiyingKey = self.verifying_key
        self.userName = str(self.PublicKey)[2:-1]
        self.signingKey = str(self.PrivateKey)[2:-1]

