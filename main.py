from tkinter import *
from tkinter import filedialog
import customtkinter
from PIL import Image, ImageDraw, ImageFont, ImageOps
import os
import ctypes
import time

myappid = 'URImager' # arbitrary string
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)
#comment
customtkinter.set_appearance_mode("Dark")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("green")  # Themes: "blue" (standard), "green", "dark-blue"

app = customtkinter.CTk()
app.geometry("400x400")
app.title("URImager")

win = "finished"
imageformats = [".jpg", ".JPG", ".png", ".PNG", ".jpeg", ".JPEG"]


def update(progressvar, textvar):
    progressbar_1.set(progressvar)
    message.configure(text=textvar)
    app.update()

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
        update(0.01, "Starting")
        imageroot = core.win
        patient_ur = int(input1.get())
        patient_ur_repeat = int(input2.get())
        orientation = switch_1.get()


        update(0.02, "Reading Files")
        print(isinstance(patient_ur, int))
        #images = glob.glob(imageroot + r"\*.jpg")
        path = (imageroot + "/appended")
        patient_ur = str(patient_ur)
        patient_ur_repeat = str(patient_ur_repeat)

        if patient_ur == patient_ur_repeat and len(str(patient_ur)) == 7:

            if orientation == 1:
                update(0.03, "Creating List")
                imageList = os.listdir(imageroot)
                lengthList = len(os.listdir(imageroot))
                existence = 1
                print(imageList)


                isExist = os.path.exists(path)
                if not isExist:
                    update(0.4, "Making directory")
                    existence = 0
                    os.makedirs(path)
                progressbartotal = lengthList - existence
                progressbarsum = 0
                increments = 1 / progressbartotal

                for img in imageList:
                    if img.endswith((".jpg", ".JPG", ".png", ".PNG", ".jpeg", ".JPEG")): #come back later and implement a list for formats
                        progressbarsum += increments
                        update(progressbarsum, ("Processing " + img))
                        isoimage = Image.open(os.path.join(imageroot, img))
                        im = ImageOps.exif_transpose(isoimage)
                        draw = ImageDraw.Draw(im)
                        fontsize = 1
                        img_fraction = 0.20
                        print(img)

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

                        im.save(path + "/mani_" + img)
                else:
                    update(1, "Finished!")
                #os.system("pause")
            elif orientation == 0:
                update(0, "Failed! \n Ensure all images are \n orientated appropriately.")
                return
        else:
            update(0, "Failed! \n Mismatching patientUR. \n Or insufficient integers.")
            return

def slider_callback(value):
    progressbar_1.set(value)

#Application Display Component
#Draw main application
frame_1 = customtkinter.CTkFrame(master=app, bg="grey")
frame_1.pack(pady=20, padx=60, fill="both", expand=True)

label=Label(master=frame_1, text="Patient UR", font='Courier 11 bold', bg="#2E2E2E", foreground="white")
label.pack()

#PatientUR input1
input1 = customtkinter.CTkEntry(master=frame_1, validate="all", validatecommand=(core.reg, '%P'))
input1.pack(pady=10, padx=10)

label=Label(master=frame_1, text="Confirm Patient UR", font='Courier 11 bold', bg="#2E2E2E", foreground="white")
label.pack()

#PatientUR input2
input2 = customtkinter.CTkEntry(master=frame_1, validate="all", validatecommand=(core.reg, '%P'))
input2.pack(pady=10, padx=10)

#Orientational switch
switch_1 = customtkinter.CTkSwitch(master=frame_1, text="Correct Orientation?")
switch_1.pack(pady=10, padx=10)

#Start button
button_1 = customtkinter.CTkButton(master=frame_1, command=core.urtoimage, text="Start")
button_1.pack(pady=10, padx=10)

#FilePath display label
label=Label(master=frame_1, text=core.win, bg="#2E2E2E", foreground="white")
label.pack(pady=10, padx=10)

message = Label(master=frame_1, text="Waiting for input...", bg="#2E2E2E", foreground="white")
message.pack()

progressbar_1 = customtkinter.CTkProgressBar(master=frame_1, orient=HORIZONTAL)
progressbar_1.pack(pady=10, padx=10)
progressbar_1.set(0)

app.resizable(False, False)
app.mainloop()