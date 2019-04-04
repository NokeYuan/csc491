# from Crypto.Hash import SHA256
# from Crypto.PublicKey import RSA
# from Crypto import Random
#
# # Creat public key
# key = DSA.generate(2048 ,Random.new().read)
# f = open("public_key.pem", "w")
# f.write(key.publickey().export_key("PEM").decode('utf-8'))
#
# # #sign the data to be secured
# message = "Hello"
# hash_obj = SHA256.new(message.encode('utf-8'))
# signer = DSS.new(key, 'fips-186-3')
# signature = signer.sign(hash_obj)
# #
# # # Load the public key
# f = open("public_key.pem", "r")
# hash_obj = SHA256.new(message.encode('utf-8'))
# pub_key = DSA.import_key(f.read())
#
# # # Verify the authenticity of the message
# if pub_key.verify(hash_obj, signature):
#     print ("OK")
# else:
#     print ("Incorrect signature")

from Crypto.PublicKey import RSA
from Crypto import Random
import ast
from Crypto.Cipher import PKCS1_OAEP

#generate public and private key
random_generator = Random.new().read
key = RSA.generate(1024, random_generator)
publickey = key.publickey()
encryptor = PKCS1_OAEP.new(publickey)

#check if is legal move
legal_move = ['up','right','left','down']
myinput = input("Please specify a command\n")
while myinput not in legal_move:
    myinput = input("Not valid , try again!\n")
else:

    print("\nValid command!")

#encrypt this
this = myinput.encode('UTF-8')
encrypted = encryptor.encrypt(this)


print('\n')
print ('encrypted message:', encrypted)
print('\n')


#decrypt this
f = open('encryption.txt', 'r')
message = f.read()
decryptor = PKCS1_OAEP.new(key)
decrypted = decryptor.decrypt(ast.literal_eval(str(encrypted)))
print ('decrypted message', decrypted)
print('\n')




















