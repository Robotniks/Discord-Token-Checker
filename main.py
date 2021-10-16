import colorama 
import requests,os 
from threading import Thread 
from colorama.ansi import Fore,Style 


try:
    os.system('title Token Checker')
    os.system('color')
except: 
    pass    
    

class Log:
    def err(str):
        print(f'{Style.BRIGHT}[{Fore.LIGHTRED_EX} ERROR {Fore.RESET}]: {str}')

    def succ(str): 
        print(f'{Style.BRIGHT}[{Fore.LIGHTGREEN_EX} SUCCESS {Fore.RESET}]: {str}')

    def print(str):
        print(f'{Style.BRIGHT}[{Fore.LIGHTBLUE_EX} CONSOLE {Fore.RESET}]: {str}')   


class Check():
    def __init__(self,token):
        self.token = token 
        self.headers = {'Authorization':self.token}

    def start(self):
        
        reqobj = requests.get('https://discordapp.com/api/v9/guild-events',headers=self.headers)
        if reqobj.status_code == 200:
            return 'valid'

        elif reqobj.status_code == 401:
            return 'invalid'

        elif reqobj.status_code == 403:
            return 'locked'


Log.print('Everything is setup. Program will now start checking Tokens')

def main():
    valid = 0
    invalid = 0
    locked = 0
    total = 0

    with open('tokens.txt','r') as tokens:
        for token in tokens.read().split('\n'):
            checkit = Check(token).start()
            total +=1
            if checkit == 'valid':
                valid +=1
                
                
                with open('output/valid.txt','a') as f:
                    f.write(f'{token}\n')

                Log.succ(f'Found a valid token. There are now {valid} tokens that are valid!')

            elif checkit == 'invalid':
                invalid +=1
                with open('output/invalid.txt','a') as f:
                    f.write(f'{token}\n')

                Log.err(f'Found an invalid token. There are now {invalid} tokens that are invalid!')    

            elif checkit == 'locked':
                locked +=1
                with open('output/locked.txt','a') as f:
                    f.write(f'{token}\n')

                Log.err(f'Found a locked a token. There are now {locked} tokens that are locked')    
    

    Log.print('All tokens have been checked,you may find your result in the "output" folder')
    Log.print(f'Valid Tokens: {valid} Invalid Tokens: {invalid} Locked Tokens: {locked} Total: {total}')


if __name__ == "__main__":
    main()


