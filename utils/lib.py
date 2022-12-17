from phe import paillier
import shamirs

from utils import config
from utils import database

class Tool:
    def __init__(self, secret_number_list=[], encrypted_number_list=[], decrypted_number_list=[], share_list=[], header_list=[]):
        self.secret_number_list    = secret_number_list
        self.encrypted_number_list = encrypted_number_list
        self.decrypted_number_list = decrypted_number_list
        self.share_list = share_list
        self.header_list = header_list
        self.database = database.DatabaseService()

        key = self.getKey()

        self.public_key  = key[0]
        self.private_key = key[1]
    
    @property
    def secret_number_list(self):
        return self._secret_number_list
    
    @secret_number_list.setter
    def secret_number_list(self, val):
        self._secret_number_list = val
        return

    @property
    def encrypted_number_list(self):
        return self._encrypted_number_list
    
    @encrypted_number_list.setter
    def encrypted_number_list(self, val):
        self._encrypted_number_list = val
        return

    @property
    def decrypted_number_list(self):
        return self._decrypted_number_list

    @decrypted_number_list.setter
    def decrypted_number_list(self, val):
        self._decrypted_number_list = val
        return

    @property
    def share_list(self):
        return self._share_list
    
    @share_list.setter
    def share_list(self, val):
        self._share_list = val
        return

    @property
    def header_list(self):
        return self._header_list

    @header_list.setter
    def header_list(self, val):
        self._header_list = val
        return

    @property
    def database(self):
        return self._database

    @database.setter
    def database(self, val):
        self._database = database.DatabaseService()
        return
        
    def getKey(self):
        public_key, private_key = paillier.generate_paillier_keypair()
        keyring = paillier.PaillierPrivateKeyring()
        keyring.add(private_key)
        return (public_key, private_key)
    
    def updateSecretNumberList(self, secret_number_list):
        self.secret_number_list = secret_number_list
        return

    def updateHeaderList(self, header_list):
        self.header_list = header_list
        return
    
    def encrytedData(self):
        self.encrypted_number_list = [self.public_key.encrypt(x).ciphertext() for x in self.secret_number_list]
        return
    
    def decryptedData(self):
        encrypted_number_list = [paillier.EncryptedNumber(self.public_key, x, 0) for x in self.encrypted_number_list]
        self.decrypted_number_list = [self.private_key.decrypt(x) for x in encrypted_number_list]
        return
    
    def splitData(self):
        for num in self.encrypted_number_list:
            self.share_list.append(shamirs.shares(num, quantity=config.N, threshold=config.T, modulus=config.MODULUS))
        return

    def storeSplitData(self, id): # Bug
        for i in range(config.N):
            data_pack = {}
            data_pack["id"] = id
            for j in range(len(self.share_list)):
                data_pack[str(self.header_list[j])] = self.share_list[j]
            
            database._write(data_pack, i)
        return
    
    def uploadData(self, data_pack):
        headers = list(data_pack.keys())
        self.updateHeaderList(headers)
        data = list(data_pack.values())[1:]
        self.updateSecretNumberList(data)

        self.encrytedData()
        self.splitData()
        self.storeSplitData(data[0])

        self.database._peek_all()
        return