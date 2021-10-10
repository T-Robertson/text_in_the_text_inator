import os
import random

class Word_crypto():
    def self(self):
        self.word_list = []
        self.key = ''


    def init(self):
        self.self()
        while True:
            x = input('Select Operation: (read ,recover ,write ,insert key) ')
            if x == 'read':
                self.read_text()
            if x == 'recover':
                self.recover_text()
            if x == 'insert key':
                self.key = input('Please input key: ')
                self.recover_text()
            if x == 'write':
                self.write_message()
            elif x != 'read' and x != 'write' and x != 'insert key' and x != 'recover':
                print('Input not valid')
        
    def read_text(self):
        print('read text')
        with open('passage.txt', 'r') as file:
            for words in file.read().split(' '):
                if words.__contains__('\n'):
                    file.read().split('\n')
                else:
                    self.word_list.insert(0,words)
            print(self.word_list)

    def recover_text(self):
        write_text = ""
        message_text = ""
        word = ""
        print("Discovering message")
        if self.key == '':
            for words in self.word_list:
                x = random.randrange(0, len(self.word_list))
                word = self.word_list[x]
                write_text = ' '.join((write_text,word))
            with open('message.txt', 'w') as file:
                file.write(write_text)
        else:
            key = list(self.key.split(' '))
            print("Key added")  
            for number in key:
                word = self.word_list[int(number)]
                message_text = ' '.join((message_text,word))
            with open('message.txt', 'w') as file:
                file.write(message_text)
    
    def write_message(self):
        message_input = input('Enter message : ')
        message = list(message_input.split(' '))
        write_key = ''
        if len(message) > 0:
            for x in message:
                number = self.word_list.index(x)
                write_key = ' '.join((write_key,format(number)))
            print(write_key)

            
def main():
    bot = Word_crypto()
    bot.init()

if __name__ == '__main__':
    main()
