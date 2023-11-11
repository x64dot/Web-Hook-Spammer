import requests
import colorama

class WebhookSpammer:
    def __init__(self, webhook, content, username, amount = 30):
        self.webhook = webhook
        self.amount = amount
        self.content = content
        self.username = username

    def Spammer(self):
        count = 0
        loss = 0 
        json_data = {"content" : self.content, "username" : self.username}

        for _  in range(self.amount):
            try:
                count += 1
                print(f"[+] Spam message sent! count = {count}.")
                send_data = requests.post(self.webhook, json = json_data)
            except:
                loss += 1
                print("[-] Spam message may have not been sent! Due to connection issues.")
        
        print(colorama.Fore.GREEN + f"\n[+] Successful messages sent: {count}." + colorama.Fore.RED + f"\n[!] unsuccessful messages sent: {loss}." + colorama.Style.RESET_ALL)
        exit(0)



print()

WEBHOOK = input("Enter discord webhook: ")

try:
    connection = requests.get(WEBHOOK)

    if connection.status_code == 200:
        print(colorama.Fore.GREEN + "[+] Discord connection works!" + colorama.Style.RESET_ALL)

    else:
        print(colorama.Fore.RED + "[!] Discord connection does not work!" + colorama.Style.RESET_ALL)
        exit(0)

except requests.exceptions.MissingSchema:
    print(colorama.Fore.RED + "[!] Enter a valid discord webhook!" + colorama.Style.RESET_ALL)

print("Press enter to use the default amount of messages to be sent.")

try:
    AMOUNT = int(input("Amount of messages to be sent(Default: 30): "))

except ValueError:
    CONTENT = input("What message should be sent? ")
    print("\n")
    USERNAME = input("What username should be used? ")

    Obj = WebhookSpammer(WEBHOOK,CONTENT,USERNAME)
    Obj.Spammer()


CONTENT = input("What message should be sent? ")
USERNAME = input("What username should be used? ")


Obj = WebhookSpammer(WEBHOOK,CONTENT,USERNAME,AMOUNT)
Obj.Spammer()


