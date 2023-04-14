from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
from tkinter import messagebox
import json
import pandas as pd


class Login:
    def __init__(self, root):
        self.root = root
        self.root.title("Login System")
        self.root.geometry("1100x700+100+50")
        self.root.resizable(True, True)

        def main_page():
            # Login Frame
            frame_login = Frame(self.root, bg="white")
            frame_login.place(x=330, y=150, width=500, height=400)

            # Title & subtitle
            Label(frame_login, text="Sample Text", font=("Impact", 35, "bold"), fg="#6162FF", bg="white").place(
                x=90, y=30)
            Label(frame_login, text="sample text", font=("Goudy old style", 15, "bold"), fg="#1d1d1d",
                  bg="white").place(x=90, y=100)

            # Username
            Label(frame_login, text="Username", font=("Goudy old style", 15, "bold"), fg="grey", bg="white").place(
                x=90, y=140)
            self.username = Entry(frame_login, font=(
                "Goudy old style", 15), bg="#E7E6E6")
            self.username.place(x=90, y=170, width=320, height=35)

            # Password
            Label(frame_login, text="Password", font=("Goudy old style", 15, "bold"), fg="grey",
                  bg="white").place(x=90, y=210)
            self.password = Entry(frame_login, show='*', font=(
                "Goudy old style", 15), bg="#E7E6E6")
            self.password.place(x=90, y=240, width=320, height=35)

            Button(frame_login, cursor="hand2", text="Login", bd=0, command=logging_in,
                   font=("Goudy old style", 15), bg="#6162FF", fg="white").place(x=90, y=320, width=180,
                                                                                 height=40)

        def End_Page():
            # Login Frame
            frame_login = Frame(self.root, bg="white")
            frame_login.place(x=330, y=150, width=500, height=400)

            Label(frame_login, text="emergency", font=("Goudy old style", 15, "bold"), fg="grey", bg="white").place(
                x=90, y=20)
            emergency = Entry(frame_login, font=(
                "Goudy old style", 15), bg="#E7E6E6")
            emergency.place(x=90, y=50, width=320, height=30)
            Label(frame_login, text="description", font=("Goudy old style", 15, "bold"), fg="grey", bg="white").place(
                x=90, y=80)
            description = Entry(frame_login, font=(
                "Goudy old style", 15), bg="#E7E6E6")
            description.place(x=90, y=110, width=320, height=60)
            Label(frame_login, text="area", font=("Goudy old style", 15, "bold"), fg="grey", bg="white").place(
                x=90, y=170)
            area = Entry(frame_login, font=(
                "Goudy old style", 15), bg="#E7E6E6")
            area.place(x=90, y=200, width=320, height=30)
            Label(frame_login, text="start date", font=("Goudy old style", 15, "bold"), fg="grey", bg="white").place(
                x=90, y=230)
            start = Entry(frame_login, font=(
                "Goudy old style", 15), bg="#E7E6E6")
            start.place(x=90, y=260, width=320, height=30)
            Label(frame_login, text="end date", font=("Goudy old style", 15, "bold"), fg="grey", bg="white").place(
                x=90, y=290)
            end = Entry(frame_login, font=(
                "Goudy old style", 15), bg="#E7E6E6")
            end.place(x=90, y=320, width=320, height=30)

            def save():

                messagebox.showinfo('Message title', 'save is ok')
                emergency1 = emergency.get()
                print(emergency1)
                description1 = description.get()
                print(description1)
                area1 = area.get()
                print(area1)
                start1 = start.get()
                print(start1)
                end1 = end.get()
                print(end1)
                data = {"emergency": emergency1, "description": description1,
                        "area": area1, "start": start1, "end": end1, }

                with open('./data.json', 'r+', encoding='utf8') as data1:
                    tmp = json.load(data1)
                    tmp.append(data)
                    data1.seek(0)
                    json.dump(tmp, data1)
                emergency.delete(0, END)
                description.delete(0, END)
                area.delete(0, END)
                start.delete(0, END)
                end.delete(0, END)

            btn1 = Button(frame_login, cursor="hand2", text="Save",   bd=0,  # command=self.check_function
                          font=("Goudy old style", 13), bg="#90fc03", fg="white", command=save)
            btn1.place(x=90, y=360, width=60, height=30)

            def listpage():
                def edit():
                    frame_edit = Frame(self.root, bg="white")
                    frame_edit.place(x=330, y=150, width=500, height=400)

                    Label(frame_edit,  text="emergency", font=("Goudy old style", 15, "bold"), fg="grey", bg="white").place(
                        x=90, y=20)
                    emergencyEdit = Entry(frame_edit, font=(
                        "Goudy old style", 15), bg="#E7E6E6")
                    emergencyEdit.place(x=90, y=50, width=320, height=30)
                    Label(frame_edit, text="description", font=("Goudy old style", 15, "bold"), fg="grey", bg="white").place(
                        x=90, y=80)
                    descriptionEdit = Entry(frame_edit, font=(
                        "Goudy old style", 15), bg="#E7E6E6")
                    descriptionEdit.place(x=90, y=110, width=320, height=60)
                    Label(frame_edit, text="area", font=("Goudy old style", 15, "bold"), fg="grey", bg="white").place(
                        x=90, y=170)
                    areaEdit = Entry(frame_edit, font=(
                        "Goudy old style", 15), bg="#E7E6E6")
                    areaEdit.place(x=90, y=200, width=320, height=30)
                    Label(frame_edit, text="start date", font=("Goudy old style", 15, "bold"), fg="grey", bg="white").place(
                        x=90, y=230)
                    startEdit = Entry(frame_edit, font=(
                        "Goudy old style", 15), bg="#E7E6E6")
                    startEdit.place(x=90, y=260, width=320, height=30)
                    Label(frame_edit, text="end date", font=("Goudy old style", 15, "bold"), fg="grey", bg="white").place(
                        x=90, y=290)
                    endEdit = Entry(frame_edit, font=(
                        "Goudy old style", 15), bg="#E7E6E6")
                    endEdit.place(x=90, y=320, width=320, height=30)

                    def edit_save():
                        emergency2 = emergencyEdit.get()
                        description2 = descriptionEdit.get()
                        area2 = areaEdit.get()
                        start2 = startEdit.get()
                        end2 = endEdit.get()
                        data = {"emergency": emergency2, "description": description2,
                                "area": area2, "start": start2, "end": end2, }
                        print(data)
                        with open('./data.json', 'r') as f:
                            jsonData = json.load(f)
                            jsonData[int(selected_item)
                                     ]['emergency'] = data['emergency']
                            jsonData[int(selected_item)
                                     ]['description'] = data['description']
                            jsonData[int(selected_item)
                                     ]['area'] = data['area']
                            jsonData[int(selected_item)
                                     ]['start'] = data['start']
                            jsonData[int(selected_item)
                                     ]['end'] = data['end']
                            with open('./data.json', 'w') as ff:
                                ff.seek(0)
                                json.dump(jsonData, ff)

                    btn3 = Button(frame_edit, text='OK', command=edit_save)
                    btn3.place(x=90, y=360, width=60, height=30)

                    btn4 = Button(frame_edit, text='Back', command=listpage)
                    btn4.place(x=200, y=360, width=60, height=30)

                    # Get selected item to Edit
                    selected_item = myList.selection()[0]
                    with open('./data.json', 'r') as f:
                        jsonData = json.load(f)
                        emergency_edit = jsonData[int(
                            selected_item)]['emergency']
                        print(emergency_edit)
                        description_edit = jsonData[int(
                            selected_item)]['description']
                        print(description_edit)
                        area_edit = jsonData[int(
                            selected_item)]['area']
                        print(area_edit)
                        start_edit = jsonData[int(
                            selected_item)]['start']
                        print(start_edit)
                        end_edit = jsonData[int(
                            selected_item)]['end']
                        print(end_edit)
                    emergencyEdit.insert(0, emergency_edit)
                    descriptionEdit.insert(0, description_edit)
                    areaEdit.insert(0, area_edit)
                    startEdit.insert(0, start_edit)
                    endEdit.insert(0, end_edit)

                def delete():
                    # Get selected item to Delete
                    selected_item = myList.selection()[0]
                    myList.delete(selected_item)

                with open('./data.json', 'r') as f:
                    jsonData = json.load(f)
                    # messagebox.showinfo('Message title', 'list is ok')
                    # List Frame
                    frame_list = Frame(self.root, bg="white")
                    frame_list.place(x=330, y=150, width=500, height=400)
                    myList = ttk.Treeview(frame_list)
                    myList['columns'] = (
                        'Emergency', 'Description', 'Area', 'Start', 'End', 'Action')
                    myList.column('#0', width=0, stretch=NO)
                    myList.column('Emergency', width=100, stretch=NO)
                    myList.column('Description', width=100, stretch=NO)
                    myList.column('Area', width=100, stretch=NO)
                    myList.column('Start', width=100, stretch=NO)
                    myList.column('End', width=100, stretch=NO)
                    myList.heading('#0', text='', anchor=CENTER)
                    myList.heading(
                        'Emergency', text='Emergency', anchor=CENTER)
                    myList.heading(
                        'Description', text='Description', anchor=CENTER)
                    myList.heading('Area', text='Area', anchor=CENTER)
                    myList.heading('Start', text='Start', anchor=CENTER)
                    myList.heading('End', text='End', anchor=CENTER)
                    for id, row in enumerate(jsonData):
                        myList.insert(parent='', index='end', iid=id, text='',
                                      values=(row['emergency'], row['description'], row['area'], row['start'], row['end']))
                    myList.pack()
                    edit_btn = Button(frame_list, text="Edit", command=edit)
                    edit_btn.place(x=90, y=280, width=80, height=30)
                    del_btn = Button(frame_list, text="Delete", command=delete)
                    del_btn.place(x=210, y=280, width=80, height=30)
                    back_btn = Button(
                        frame_list, text="Back", command=End_Page)
                    back_btn.place(x=330, y=280, width=80, height=30)

            btn2 = Button(frame_login, cursor="hand2", text="List",   bd=0,
                          font=("Goudy old style", 13), bg="#03fceb", fg="white", command=listpage)
            btn2.place(x=190, y=360, width=60, height=30)
            btn_logout = Button(frame_login, cursor="hand2", text="Logout",   bd=0,
                                font=("Goudy old style", 13), bg="#eb34db", fg="white", command=main_page)
            btn_logout.place(x=290, y=360, width=60, height=30)

        def listpage_detail():
            def edit():
                frame_edit = Frame(self.root, bg="white")
                frame_edit.place(x=330, y=150, width=500, height=400)

                Label(frame_edit,  text="emergency", font=("Goudy old style", 15, "bold"), fg="grey", bg="white").place(
                    x=90, y=20)
                emergencyEdit = Entry(frame_edit, font=(
                    "Goudy old style", 15), bg="#E7E6E6")
                emergencyEdit.place(x=90, y=50, width=320, height=30)
                Label(frame_edit, text="description", font=("Goudy old style", 15, "bold"), fg="grey", bg="white").place(
                    x=90, y=80)
                descriptionEdit = Entry(frame_edit, font=(
                    "Goudy old style", 15), bg="#E7E6E6")
                descriptionEdit.place(x=90, y=110, width=320, height=60)
                Label(frame_edit, text="area", font=("Goudy old style", 15, "bold"), fg="grey", bg="white").place(
                    x=90, y=170)
                areaEdit = Entry(frame_edit, font=(
                    "Goudy old style", 15), bg="#E7E6E6")
                areaEdit.place(x=90, y=200, width=320, height=30)
                Label(frame_edit, text="start date", font=("Goudy old style", 15, "bold"), fg="grey", bg="white").place(
                    x=90, y=230)
                startEdit = Entry(frame_edit, font=(
                    "Goudy old style", 15), bg="#E7E6E6")
                startEdit.place(x=90, y=260, width=320, height=30)
                Label(frame_edit, text="end date", font=("Goudy old style", 15, "bold"), fg="grey", bg="white").place(
                    x=90, y=290)
                endEdit = Entry(frame_edit, font=(
                    "Goudy old style", 15), bg="#E7E6E6")
                endEdit.place(x=90, y=320, width=320, height=30)

                def edit_save():
                    emergency2 = emergencyEdit.get()
                    description2 = descriptionEdit.get()
                    area2 = areaEdit.get()
                    start2 = startEdit.get()
                    end2 = endEdit.get()
                    data = {"emergency": emergency2, "description": description2,
                            "area": area2, "start": start2, "end": end2, }
                    print(data)
                    with open('./data.json', 'r') as f:
                        jsonData = json.load(f)
                        jsonData[int(selected_item)
                                 ]['emergency'] = data['emergency']
                        jsonData[int(selected_item)
                                 ]['description'] = data['description']
                        jsonData[int(selected_item)
                                 ]['area'] = data['area']
                        jsonData[int(selected_item)
                                 ]['start'] = data['start']
                        jsonData[int(selected_item)
                                 ]['end'] = data['end']
                        with open('./data.json', 'w') as ff:
                            ff.seek(0)
                            json.dump(jsonData, ff)

                btn3 = Button(frame_edit, text='OK', command=edit_save)
                btn3.place(x=90, y=360, width=60, height=30)

                # Get selected item to Edit
                selected_item = myList.selection()[0]
                with open('./data.json', 'r') as f:
                    jsonData = json.load(f)
                    emergency_edit = jsonData[int(
                        selected_item)]['emergency']
                    print(emergency_edit)
                    description_edit = jsonData[int(
                        selected_item)]['description']
                    print(description_edit)
                    area_edit = jsonData[int(
                        selected_item)]['area']
                    print(area_edit)
                    start_edit = jsonData[int(
                        selected_item)]['start']
                    print(start_edit)
                    end_edit = jsonData[int(
                        selected_item)]['end']
                    print(end_edit)
                emergencyEdit.insert(0, emergency_edit)
                descriptionEdit.insert(0, description_edit)
                areaEdit.insert(0, area_edit)
                startEdit.insert(0, start_edit)
                endEdit.insert(0, end_edit)
                # print(jsonData[int(selected_item)]['description'])
                # for item in jsonData:
                #     if item.id == selected_item:
                #         print(jsonData['description'])
                # myList.item(selected_item, text="Emergency",
                #             values=("Emergency"))

            with open('./data.json', 'r') as f:
                jsonData = json.load(f)
                # messagebox.showinfo('Message title', 'list is ok')
                # List Frame
                frame_list = Frame(self.root, bg="white")
                frame_list.place(x=330, y=150, width=500, height=400)
                myList = ttk.Treeview(frame_list)
                myList['columns'] = (
                    'Emergency', 'Description', 'Area', 'Start', 'End', 'Action')
                myList.column('#0', width=0, stretch=NO)
                myList.column('Emergency', width=100, stretch=NO)
                myList.column('Description', width=100, stretch=NO)
                myList.column('Area', width=100, stretch=NO)
                myList.column('Start', width=100, stretch=NO)
                myList.column('End', width=100, stretch=NO)
                myList.heading('#0', text='', anchor=CENTER)
                myList.heading(
                    'Emergency', text='Emergency', anchor=CENTER)
                myList.heading(
                    'Description', text='Description', anchor=CENTER)
                myList.heading('Area', text='Area', anchor=CENTER)
                myList.heading('Start', text='Start', anchor=CENTER)
                myList.heading('End', text='End', anchor=CENTER)
                for id, row in enumerate(jsonData):
                    myList.insert(parent='', index='end', iid=id, text='',
                                  values=(row['emergency'], row['description'], row['area'], row['start'], row['end']))
                myList.pack()

        # Login Frame
        Frame_login = Frame(self.root, bg="white")
        Frame_login.place(x=330, y=150, width=500, height=400)

        # Title & subtitle
        Label(Frame_login, text="Sample text", font=("Impact", 35, "bold"), fg="#6162FF", bg="white").place(x=90,
                                                                                                            y=30)
        Label(Frame_login, text="sample text", font=("Goudy old style", 15, "bold"), fg="#1d1d1d",
              bg="white").place(x=90, y=100)

        # Username
        Label(Frame_login, text="Username", font=("Goudy old style", 15, "bold"), fg="black", bg="white").place(
            x=90, y=140)
        self.username = Entry(Frame_login, font=(
            "Goudy old style", 15), bg="#E7E6E6")
        self.username.place(x=90, y=170, width=320, height=35)

        # Password
        Label(Frame_login, text="Password", font=("Goudy old style", 15, "bold"), fg="black",
              bg="white").place(x=90, y=210)
        self.password = Entry(Frame_login, show='*', font=(
            "Goudy old style", 15), bg="#E7E6E6")
        self.password.place(x=90, y=240, width=320, height=35)

        def logging_in():
            username = self.username.get()
            print(username)
            password = self.password.get()
            print(password)
            data = {"username": username, "password": password}
            with open('accounts.json', 'r+') as cred_file:
                table_json = json.load(cred_file)

            add = True

            for acc in table_json["accounts"]:
                if data["username"] == acc["username"] and data["password"] == acc["password"]:
                    if data["username"] == "Admin":
                        messagebox.showinfo(" ", "Admin Logged In")
                        add = False
                        End_Page()
                    if data["username"] == "Vo":
                        messagebox.showinfo(" ", "Volunteer Logged In")
                        add = False
                        listpage_detail()
            if add:
                messagebox.showerror(
                    "Error", "ID or Password are wrong , please try again")

        # Button
        Button(Frame_login, cursor="hand2", text="Login", command=logging_in,  bd=0,  # command=self.check_function
               font=("Goudy old style", 15), bg="#6162FF", fg="white").place(x=90, y=320, width=180, height=40)


root = Tk()
# Open Image
bg_pic = Image.open(r"bg.jpg")
# Resized Image
# resized = bg_pic.resize((1199, 850), Image.ANTIALIAS)

bg = ImageTk.PhotoImage(bg_pic)
label_bgImage = Label(root, image=bg)
label_bgImage.place(x=0, y=0)
obj = Login(root)
root.mainloop()
