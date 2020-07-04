from Crypto.Cipher import DES
 
# Reading plaintext-ciphertext pairs
content = open("secret.dat",'rb').read()
IV = content[:8]
enc_txt = content[8:]
print(len(enc_txt))
# Weak key list
key = ["0"*16, "F"*16, "0101010101010101", "FEFEFEFEFEFEFEFE", "E0E0E0E0F1F1F1F1", "1F1F1F1F0E0E0E0E"]
key += ["0000000000000000", "FFFFFFFFFFFFFFFF", "E1E1E1E1F0F0F0F0", "1E1E1E1E0F0F0F0F"]

for i in key:
    key_obj = DES.new(bytes.fromhex(i),  DES.MODE_OFB, IV)
    key_obj = DES.new(bytes.fromhex(i),  DES.MODE_ECB)
    # Taking one ciphertext from file
    ct = content #[:16]
    # Corresponding plaintext from file
    #pt = pt_ct_list[0][18:].decode("hex")
    # Potential plaintext
    pt = key_obj.decrypt(ct)
    print(pt)
    #if pot_pt == pt:
    #    print "Key: ", i