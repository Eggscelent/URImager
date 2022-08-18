from tkinter import *
from tkinter import filedialog
import customtkinter
from PIL import Image, ImageDraw, ImageFont, ImageOps
import os
import ctypes

#TO DO:
#Fix ability to submit letters in input
#Implement proper 7 number limit

myappid = 'URImager' # arbitrary string
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)
#comment
customtkinter.set_appearance_mode("dark")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"

app = customtkinter.CTk()
app.geometry("400x400")
app.title("URImager")
app.iconbitmap('favicon.ico')

class core:
    win = filedialog.askdirectory(initialdir="C:/", title="Select photo folder.")
    if not win:
        win = "Folder not selected!"

    def urtoimage():
        imageroot = dialog.win
        patient_ur = int(input1.get())
        patient_ur_repeat = int(input2.get())
        orientation = switch_1.get()

        if len(str(patient_ur)) == 7 and isinstance(patient_ur, int) == True:
            print(isinstance(patient_ur, int))
            #images = glob.glob(imageroot + r"\*.jpg")
            path = (imageroot + "/appended")
            patient_ur = str(patient_ur)
            patient_ur_repeat = str(patient_ur_repeat)

            if patient_ur == patient_ur_repeat:

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
                        if img.endswith((".jpg", ".JPG", ".png", ".jpeg")):
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
                        win = "finished"
                    #os.system("pause")
                elif orientation == 0:
                    message.configure(text="Failed! \n Ensure all images are \n orientated appropriately.")
                    return
            else:
                message.configure(text="Failed! \n Mismatching patientUR.")
                return
        else:
            message.configure(text="Failed! \n PatientUR must be 7 numbers.")
            return

#Application Display Component
#Draw main application
frame_1 = customtkinter.CTkFrame(master=app)
frame_1.pack(pady=20, padx=60, fill="both", expand=True)

#vcmd = (frame_1.register(callback))

#w = Entry(frame_1, validate='all', validatecommand=(vcmd, '%P'))
#w.pack()

def callback(frame_1, P):
    if str.isdigit(P) or str(P) == "":
        return True
    else:
        return False

#PatientUR input1
input1 = customtkinter.CTkEntry(master=frame_1, placeholder_text="Patient UR")
input1.pack(pady=12, padx=10)

#PatientUR input2
input2 = customtkinter.CTkEntry(master=frame_1, placeholder_text="Confirm Patient UR")
input2.pack(pady=12, padx=10)

#FilePath display label
label=Label(master=frame_1, text=dialog.win, font='Courier 11 bold')
label.pack()

label1=Label(master=frame_1, text=dialog.win, font='Courier 11 bold')
label1.pack()

#Orientational switch
switch_1 = customtkinter.CTkSwitch(master=frame_1, text="Correct Orientation?")
switch_1.pack(pady=12, padx=10)

#Start button
button_1 = customtkinter.CTkButton(master=frame_1, command=application(), text="Start")
button_1.pack(pady=12, padx=10)

while True:
    message = Label(master=frame_1, text="Waiting for input...", font='Courier 11 bold')
    message.pack()
    app.resizable(False, False)
    app.mainloop()