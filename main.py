from tkinter import *
from tkinter import filedialog
import customtkinter
from PIL import Image, ImageDraw, ImageFont, ImageOps
import os
import ctypes

myappid = 'URImager' # arbitrary string
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)
#comment
customtkinter.set_appearance_mode("dark")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"

app = customtkinter.CTk()
app.geometry("400x400")
app.title("URImager")
app.iconbitmap('favicon.ico')

win = "finished"
imageformats = [".jpg", ".JPG", ".png", ".PNG", ".jpeg", ".JPEG"]

class core:
    def correct(char):
        if len(str(char)) == 0:
            return True
        elif char.isdigit() and len(str(char)) <= 7:
            return True
        else:
            return False

    reg = app.register(correct)

    win = filedialog.askdirectory(initialdir="C:/", title="Select photo folder.")
    if not win:
        win = "Folder not selected!"

    def urtoimage():
        imageroot = core.win
        patient_ur = int(input1.get())
        patient_ur_repeat = int(input2.get())
        orientation = switch_1.get()

        print(isinstance(patient_ur, int))
        #images = glob.glob(imageroot + r"\*.jpg")
        path = (imageroot + "/appended")
        patient_ur = str(patient_ur)
        patient_ur_repeat = str(patient_ur_repeat)

        if patient_ur == patient_ur_repeat and len(str(patient_ur)) == 7:

            if orientation == 1:

                imageList = os.listdir(imageroot)
                lengthList = len(os.listdir(imageroot))

                print(imageList)
                print(lengthList)

                isExist = os.path.exists(path)
                if not isExist:
                    os.makedirs(path)
                win = "starting"
                message.configure(text="Starting!")
                for img in imageList:
                    if img.endswith((".jpg", ".JPG", ".png", ".PNG", ".jpeg", ".JPEG")): #come back later and implement a list for formats
                        win = "importing"
                        isoimage = Image.open(os.path.join(imageroot, img))
                        im = ImageOps.exif_transpose(isoimage)
                        draw = ImageDraw.Draw(im)
                        fontsize = 1
                        img_fraction = 0.20
                        print(img)

                        win = "processing"

                        font = ImageFont.truetype("arial.ttf", fontsize)
                        while font.getsize(patient_ur)[0] < img_fraction * im.size[0]:
                            fontsize += 1
                            font = ImageFont.truetype("arial.ttf", fontsize)

                        fontsize -= 1
                        font = ImageFont.truetype("arial.ttf", fontsize)

                        x, y = (0, 0)
                        w, h = font.getsize(patient_ur)

                        draw.rectangle((x, y, x + w, y + h), fill="white")
                        draw.text((x, y), patient_ur, fill='black', font=font)

                        win = "saving"

                        im.save(path + "/mani_" + img)
                        print("UR to Image Successful!")
                else:
                    message.configure(text="Finished!")
                #os.system("pause")
            elif orientation == 0:
                message.configure(text="Failed! \n Ensure all images are \n orientated appropriately.")
                return
        else:
            message.configure(text="Failed! \n Mismatching patientUR. \n Or insufficient integers.")
            return

#Application Display Component
#Draw main application
frame_1 = customtkinter.CTkFrame(master=app)
frame_1.pack(pady=20, padx=60, fill="both", expand=True)

label=Label(master=frame_1, text="Patient UR", font='Courier 11 bold')
label.pack()

#PatientUR input1
input1 = customtkinter.CTkEntry(master=frame_1, validate="all", validatecommand=(core.reg, '%P'))
input1.pack(pady=12, padx=10)

label=Label(master=frame_1, text="Confirm Patient UR", font='Courier 11 bold')
label.pack()

#PatientUR input2
input2 = customtkinter.CTkEntry(master=frame_1, validate="all", validatecommand=(core.reg, '%P'))
input2.pack(pady=12, padx=10)

label=Label(master=frame_1, text="Working Directory", font='Courier 11 bold')
label.pack()

#FilePath display label
label=Label(master=frame_1, text=core.win, bg="grey")
label.pack()

#Orientational switch
switch_1 = customtkinter.CTkSwitch(master=frame_1, text="Correct Orientation?")
switch_1.pack(pady=12, padx=10)

#Start button
button_1 = customtkinter.CTkButton(master=frame_1, command=core.urtoimage, text="Start")
button_1.pack(pady=12, padx=10)

message = Label(master=frame_1, text="Waiting for input...")
message.pack()

while True:
    app.resizable(False, False)
    app.mainloop()