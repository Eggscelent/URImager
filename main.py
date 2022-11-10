#V0.12

from tkinter import *
import tkinter
from tkinter import filedialog as fd
import customtkinter
from PIL import Image, ImageDraw, ImageFont, ImageOps, ImageTk
import os

customtkinter.set_appearance_mode("Dark")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("green")  # Themes: "blue" (standard), "green", "dark-blue"

app = customtkinter.CTk()

w = 400 # width for the Tk root
h = 450 # height for the Tk root

# get screen width and height
ws = app.winfo_screenwidth() # width of the screen
hs = app.winfo_screenheight() # height of the screen

# calculate x and y coordinates for the Tk root window
x = (ws/2) - (w/2)
y = (hs/2) - (h/2)

# set the dimensions of the screen
# and where it is placed
app.geometry('%dx%d+%d+%d' % (w, h, x, y))
app.geometry('%dx%d+%d+%d' % (w, h, x, y))
app.title("URImager")

imageextensions = [".jpg", ".JPG", ".png", ".PNG", ".jpeg", ".JPEG"]
progressbar_1 = ""

# update progress bar percentage and textvariable for status
def update(progressvar, textvar):
    progressbar_1.set(progressvar)
    message.configure(text=textvar)
    app.update() # update tkinter main display

def disable():
    input1.configure(state=DISABLED)
    input2.configure(state=DISABLED)
    switch_1.configure(state=DISABLED)
    button_1.configure(state=DISABLED)
    button_2.configure(state=DISABLED)
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
    #win = filedialog.askdirectory(initialdir="C:/", title="Select photo folder.")

        #if not win:
            #update(0.01, "Folder not selected!")

    def selectfolder():
        global win
        win = fd.askdirectory(initialdir="C:/", title="Select photo folder.")
        folder.configure(text=win)
        app.update()

        if not win:
            folder.configure(text="No folder selected...")
            app.update()

    def urtoimage():

        update(0.01, "Starting")
        imagecount = 0
        imageroot = win
        patient_ur = input1.get()
        patient_ur_repeat = input2.get()
        orientation = switch_1.get()

        update(0.02, "Reading Files")
        path = (imageroot + "/appended")

        if patient_ur == patient_ur_repeat and len(patient_ur) == 7 and orientation == 1:
            disable()

            update(0.03, "Creating List")
            imageList = os.listdir(imageroot)
            lengthList = len(os.listdir(imageroot))
            existence = 1

            isExist = os.path.exists(path)
            if not isExist:
                update(0.4, "Making directory")
                existence = 0
                os.makedirs(path)

            progressbartotal = lengthList - existence
            progressbarsum = 0
            increments = 1 / progressbartotal

            for extension in imageextensions:
                for img in imageList:
                    if img.endswith(extension):
                        progressbarsum += increments
                        imagecount = 1 + imagecount
                        update(progressbarsum, ("Processing " + img))
                        isoimage = Image.open(os.path.join(imageroot, img))
                        im = ImageOps.exif_transpose(isoimage)
                        draw = ImageDraw.Draw(im)
                        #fontsize = 2
                        #img_fraction = 0.40
                        print(img)

                        #font = ImageFont.truetype("arial.ttf", fontsize)

                        #while font.getsize(patient_ur)[0] < img_fraction * im.size[0]:
                           # fontsize += 1
                            #print(fontsize)
                            #font = ImageFont.truetype("arial.ttf", fontsize)

                        #fontsize -= 1
                        font = ImageFont.truetype("arial.ttf", 260)

                        x, y = (0, 0)
                        w, h = font.getsize(patient_ur)

                        draw.rectangle((x, y, x + w, y + h), fill="white")
                        draw.text((x, y), patient_ur, fill='black', font=font)

                        im.save(path + "/append_" + img)
                else:
                    update(1, "Finished! " + str(imagecount) + " images processed.")
        else:
            update(0, "Failed! \n *Mismatching patientUR. \n *Insufficient integers. \n *Orientation not ticked.")

frame_1 = customtkinter.CTkFrame(master=app, bg="grey")
frame_1.pack(pady=20, padx=60, fill="both", expand=True)

label=Label(master=frame_1, text="", font='Courier 11 bold', bg="#2E2E2E", foreground="white")
label.pack()

label=Label(master=frame_1, text="Patient UR", font='Courier 11 bold', bg="#2E2E2E", foreground="white")
label.pack()

input1 = customtkinter.CTkEntry(master=frame_1, validate="all", validatecommand=(core.reg, '%P'))
input1.pack(pady=10, padx=10)

label=Label(master=frame_1, text="Confirm Patient UR", font='Courier 11 bold', bg="#2E2E2E", foreground="white")
label.pack()

input2 = customtkinter.CTkEntry(master=frame_1, validate="all", validatecommand=(core.reg, '%P'))
input2.pack(pady=10, padx=10)

switch_1 = customtkinter.CTkSwitch(master=frame_1, text="Correct Orientation?")
switch_1.pack(pady=10, padx=10)

button_1 = customtkinter.CTkButton(master=frame_1, command=core.selectfolder, text="Select Folder")
button_1.pack(pady=10, padx=10)

folder = Label(master=frame_1, text="No folder selected...", bg="#2E2E2E", foreground="white")
folder.pack(pady=10, padx=10)

button_2 = customtkinter.CTkButton(master=frame_1, command=core.urtoimage, text="Start")
button_2.pack(pady=10, padx=10)

message = Label(master=frame_1, text="Waiting for input...", bg="#2E2E2E", foreground="white")
message.pack()

progressbar_1 = customtkinter.CTkProgressBar(master=frame_1, orient=HORIZONTAL)
progressbar_1.pack(pady=10, padx=10)
progressbar_1.set(0)

app.resizable(False, False)

if __name__ == "__main__":
    app.mainloop()