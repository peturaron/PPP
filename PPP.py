import string
import random

class Encryption():

    def __init__(self,seed):

        random.seed(seed)
        self.seed = seed
        self.encrypted_phrase = ""
        self.true_alphabet = list(string.ascii_lowercase)
        self.rand_alphabet = random.sample(self.true_alphabet,len(self.true_alphabet))

    def encryption(self,message):

        output = ''
        #step1
        for i in range(len(message)):
            output = output + message[i]
            output = output + random.sample(self.true_alphabet,1)[0] #Næ í einn random staf ur index 0 i ehv random lista
        #step2
        self.encrypted_phrase = output[::-1] #reversa strengnum
        #step3
        encrypted_phase_two = list(range(len(self.encrypted_phrase)))
        for i,letter in enumerate(self.encrypted_phrase.lower()):
            if letter in self.true_alphabet:
                index = self.true_alphabet.index(letter)
                encrypted_phase_two[i] = self.rand_alphabet[index]
            else:
                encrypted_phase_two[i] = letter #fyrir kommur eda punkta
        self.encrypted_phrase = ''.join(encrypted_phase_two)
        return self.encrypted_phrase

    def decryption(self,message,seed):
        random.seed(seed)
        session_rand_alphabet = random.sample(self.true_alphabet,len(self.true_alphabet))
        decrypted_message = list(range(len(message)))
        for i,letter in enumerate(message.lower()):
            if letter in self.true_alphabet:
                index = session_rand_alphabet.index(letter)
                decrypted_message[i] = self.true_alphabet[index]
            else:
                decrypted_message[i] = letter
        decrypted_message = ''.join(decrypted_message)[::-1]
        return decrypted_message[::2] #grab every other letter get lika notad for loopu


x = Encryption(10)
quit = ""

while quit != "Y":
    print("Would like to encrypt a message (E) or Decrypt (D)")
    if input != "E":
        i = input()
        if i == 'E':
            print("Hello there agent, please enter a message to encrypt it")
            i = input()
            x.encryption(i)
            print("\nYour encrypted message is the following: ")
            print(x.encrypted_phrase + "\n")

        elif i == 'D':
            print("Please enter a the encrypted message to decrypt it")
            i = input()
            print(x.decryption(i,10))
        print("Do you want to quit (Y/N)")
        quit = input()
