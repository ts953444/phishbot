from simplegmail import Gmail

class colors:
    RED = '\033[31m'
    ENDC = '\033[m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'


print(colors.YELLOW + "                           __    _      __    __          __")
print(colors.YELLOW + " __                 ____  / /_  (_)____/ /_  / /_  ____  / /_")
print(colors.YELLOW + "/o \\/    __        / __ \\/ __ \\/ / ___/ __ \\/ __ \\/ __ \\/ __/")
print(colors.YELLOW + "\\__/\\   /o \\/     / /_/ / / / / (__  ) / / / /_/ / /_/ / /_  ")
print(colors.YELLOW + "        \\__/\\    / .___/_/ /_/_/____/_/ /_/_.___/\\____/\\__/  ")
print(colors.YELLOW + "                /_/ ")

recipient = input(colors.GREEN + 'Enter destination email address:\n' + colors.ENDC)

gmail = Gmail()

params = {
  'to': recipient,
  'sender': 'John Hacker <ts953444@gmail.com>',
  'subject': 'Please helps!',
  'msg_html': '<h1>Woah, my first email!</h1><br /><a href=http://3.19.16.86/>check this</a>This is an HTML email.<br />John Haxor, VP, Global Operations<br /><<font color="red">Toyota Financial Services</font>',
  #"msg_plain": "Hi\nThis is a plain text email.",
  #"attachments": ["path/to/something/cool.pdf", "path/to/image.jpg", "path/to/script.py"],
  #'signature': True  # use my account signature
}
message = gmail.send_message(**params)