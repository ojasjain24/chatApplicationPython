from tkinter import *
import loginPage
from client import Client
import time
from threading import Thread

root = Tk()
c1=Client(loginPage.getvals())

def getvals():
    c1.send_message((Msgvalue.get()))

root.geometry("500x400")
Label(root, text="GROUP CHAT", font="comicsansms 15 bold", pady=15).pack()

Msgvalue = StringVar()

widget=Button(root, text="send", command=getvals)
widget.bind("<Enter>",getvals())
widget.pack(side = BOTTOM,anchor='se')

MsgEntry = Entry(root, textvariable=Msgvalue, font="comicsansms 12 bold",bg='#99FF99').pack(side = BOTTOM,anchor='sw', fill="x", padx=36)

def update_messages():
    """
    updates the local list of messages
    :return: None
    """

    scrollbar = Scrollbar(root)
    scrollbar.pack(side=RIGHT, fill=Y)
    listbox = Text(root, wrap =WORD, yscrollcommand=scrollbar.set, background="#CCFFCC", fg="black", selectbackground="#003300",
                      highlightcolor="#0033CC")

    msgs = []
    run = True
    while run:

        time.sleep(0.1)  # update every 1/10 of a second
        new_messages = c1.get_messages()  # get any new messages from client
        msgs.extend(new_messages)  # add to local list of messages

        for msg in new_messages:  # display new messages
            print(msg)
            #title_label = Label(text=str(msg), bg="#CCFFCC", fg="black", padx=34, pady=5, font="comicsansms 9 bold",borderwidth=3,wraplength=300, relief=SUNKEN)
            #title_label.pack(side=TOP)

            listbox.insert(END, str(msg)+'\n\n')
            listbox.pack(fill=BOTH, padx=36)
            scrollbar.config(command=listbox.yview)

            if msg == "{quit}":
                root.destroy()
                run = False
                break

Thread(target=update_messages).start()

root.mainloop()
