from tkinter import *
import customtkinter
from PIL import Image, ImageDraw, ImageFont, ImageOps
import os
import ctypes

myappid = 'URImager' # arbitrary string
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)

customtkinter.set_appearance_mode("dark")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"

app = customtkinter.CTk()
app.geometry("400x400")
app.title("URImager")
#app.iconbitmap('icon.ico')

def urtoimage(m):
    imageroot = input3.get()
    patient_ur = input1.get()
    patient_ur_repeat = input2.get()
    orientation = switch_1.get()

    if len(patient_ur) == 7:
        #images = glob.glob(imageroot + r"\*.jpg")
        path = (imageroot + "/appended")

        if patient_ur == patient_ur_repeat:

            if orientation == 1:

                imageList = os.listdir(imageroot)
                lengthList = len(os.listdir(imageroot))

                print(imageList)
                print(lengthList)

                isExist = os.path.exists(path)
                if not isExist:
                    os.makedirs(path)


                for img in imageList:
                    if img.endswith((".jpg", ".JPG", ".png", ".jpeg")):
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

                        im.save(path + "/Edited_" + img)
                        print("UR to Image Successful!")
                else:
                    return
                #os.system("pause")
            elif orientation == 0:
                messagebox.showerror("Error", "Ensure all images have been orientated appropriately...")
                return
        else:
            messagebox.showerror("Error", "Mismatching patientUR! Please try again...")
            return
    else:
        messagebox.showerror("Error", "UR number must be 7 numbers... Please try again")
        return

frame_1 = customtkinter.CTkFrame(master=app)
frame_1.pack(pady=20, padx=60, fill="both", expand=True)

input1 = customtkinter.CTkEntry(master=frame_1, placeholder_text="Patient UR")
input1.pack(pady=12, padx=10)

input2 = customtkinter.CTkEntry(master=frame_1, placeholder_text="Confirm Patient UR")
input2.pack(pady=12, padx=10)

input3 = customtkinter.CTkEntry(master=frame_1, placeholder_text="Working Directory")
input3.pack(pady=12, padx=10)

switch_1 = customtkinter.CTkSwitch(master=frame_1, text="Correct Orientation?")
switch_1.pack(pady=12, padx=10)

button_1 = customtkinter.CTkButton(master=frame_1, command=urtoimage, text="Start")
button_1.pack(pady=12, padx=10)

app.resizable(False,False)

if __name__ == "__main__":
    app.mainloop()