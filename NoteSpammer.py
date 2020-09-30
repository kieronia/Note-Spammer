from navmenu import Menu
import pyPrivnote as pn
import os
from colorama import Fore, init, Style
from throwbin import ThrowBin

tb = ThrowBin()






def throwbin():
    counter = int(1)
    input(f"{Fore.RED}[!] Press enter to continue!\n[>] ")#when pressing enter on the menu, it normally records that enter as an input, ruining 'enter to quit' systems etc - this is a blank input that'll catch the spare input...
    os.system("title Ready To Create Throwbin Notes!")
    os.system("cls")
    throwbinmessagecontent = input(f"{Fore.CYAN}[+] Throwbin Message Content?\n[>]{Fore.WHITE} ")
    throwbintitle = input(f"{Fore.CYAN}[+] Throwbin Title ?\n[>]{Fore.WHITE} ")
    amountofthrowbins = int(input(f"{Fore.CYAN}[+] Throwbin Count To Make?\n[>]{Fore.WHITE} "))
    messagelinkoriginal = tb.post(
    title=throwbintitle,
    text=throwbinmessagecontent,
    syntax="text"
)
    print(f"{Fore.GREEN}[+] {messagelinkoriginal.link} - Original Link Made!")
    linkchain = tb.post(
    title=throwbintitle,
    text=messagelinkoriginal.link,
    syntax="text"
)
    print(f"{Fore.GREEN}[{counter}] {linkchain.link}")
    counter = counter + 1
    for i in range(amountofthrowbins-1):
        linkchain = tb.post(
        title=throwbintitle,
        text=linkchain.link,
        syntax="text"
)
        os.system(f"title Made [{counter}] Out Of {amountofthrowbins} Messages - {linkchain.link}")
        print(f"{Fore.GREEN}[{counter}] {linkchain.link}")
        counter = counter + 1

    linkchain = tb.post(
    title=throwbintitle,
    text=linkchain.link,
    syntax="text"
)
    os.system(f"title [+] All created - Final Link {linkchain.link} [+]")
    print(f"{Fore.GREEN}[{counter}] {linkchain.link} - FINAL CREATED")
    throwbin()
        

def privnote():
    counter = int(1)
    input(f"{Fore.RED}[!] Press enter to continue!\n[>] ")#when pressing enter on the menu, it normally records that enter as an input, ruining 'enter to quit' systems etc - this is a blank input that'll catch the spare input...
    os.system("title Ready To Create Privnotes!")
    os.system("cls")
    privnotemessagecontent = input(f"{Fore.CYAN}[+] Privnote Message Content?\n[>]{Fore.WHITE} ")
    amountofprivnotes = int(input(f"{Fore.CYAN}[+] Privnote Count To Make?\n[>]{Fore.WHITE} "))
    originalmessagelink = pn.create_note(privnotemessagecontent)
    print(f"{Fore.GREEN}[+] {originalmessagelink} - Original Link Made!")
    chainlink = pn.create_note(originalmessagelink) 
    print(f"{Fore.GREEN}[{counter}] {chainlink}")
    for i in range(amountofprivnotes-1):
        chainlink = pn.create_note(chainlink)
        os.system(f"title Made [{counter}] Out Of {amountofprivnotes} Messages - {chainlink}")
        print(f"{Fore.GREEN}[{counter}] {chainlink}")
        counter = counter + 1

    chainlink = pn.create_note(chainlink)
    os.system(f"title [+] All created - Final Link {chainlink} [+]")
    print(f"{Fore.GREEN}[{counter}] {chainlink} - FINAL CREATED")
    privnote()


prefix = """
This tool repeatedly creates notes with 
the note services [pastebin] and [throwbin]
It puts a message of choice in the first link.
It then puts that link in another note, 
and puts that note link in a new note etc.
People get hyped and have curiousity
for the note contents, hence will probably
waste their time going through them XD
NavMenu from https://github.com/zoony1337/NavMenu
"""

suffix = """
Select a note service.
"""

def backtomenu(): #was gonna try loop but meh harder then that
    Menu.display(prefix=prefix, indent=5, color='yellow', suffix=suffix, options={
        'Privnote Chain': privnote,
        'Throwbin Chain': throwbin
    })
os.system("title Ready to chain notes!")
backtomenu()
