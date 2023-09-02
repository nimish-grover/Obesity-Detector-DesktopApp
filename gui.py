import tkinter as tk
import joblib
import text_detector
import image_detector
from tkinter import messagebox
from tkinter import filedialog

global sel_gen,sel_fam,sel_smoke,sel_mtrans,age_entry,height_entry,weight_entry,label1,label2

joblib.dump(text_detector.clf,'obesity-text.joblib')
joblib.dump(image_detector.model,'obesity-image.joblib')
text = joblib.load('obesity-text.joblib')
image = joblib.load('obesity-image.joblib')

def take_input():
    ch = sel_choice.get()
    return choice(ch)

def choice(ch):

    if ch == 'Text Detector':
        return run_text_detector()
    elif ch == 'Image Detector':
        return run_image_detector()
    else:
        return error()

def error():

    messagebox.showerror('Error','Choose Valid Model')


def get_input():
    # -------------------------------------------------------------------------------------------------------------------
    gender = sel_gen.get()

    famhistory=sel_fam.get()

    smoke = sel_smoke.get()

    mtrans = sel_mtrans.get()

    Age = float(age_entry.get())

    Height = float(height_entry.get())

    Weight = float(weight_entry.get())

    print("Gender:",gender)
    print('Age: ',Age)
    print('Height: ',Height)
    print('Weight: ',Weight)
    print('Family history:',famhistory)
    print('Smoke:',smoke)
    print('Mode of transport:',mtrans)


    return predict_obese(Age,Height,Weight,gender,famhistory,smoke,mtrans)

    # -------------------------------------------------------------------------------------------------------------------


def predict_obese(Age,Height,Weight,gender,famhistory,smoke,mtrans):
    # -------------------------------------------------------------------------------------------------------------------
    if gender == "Male":
        gender = 1
    else:
        gender = 0

    # -------------------------------------------------------------------------------------------------------------------
    if famhistory == "Yes":
        famhistory = 1
    else:
        famhistory = 0

    # -------------------------------------------------------------------------------------------------------------------
    if smoke == "Yes":
        smoke = 1
    else:
        smoke = 0

    # -------------------------------------------------------------------------------------------------------------------
    if mtrans == "Public_Transportation":
        mtrans = 3
    elif mtrans == "Walking":
        mtrans = 4
    elif mtrans == "Automobile":
        mtrans = 0
    elif mtrans == "Motorbike":
        mtrans = 2
    else:
        mtrans = 1

    # -------------------------------------------------------------------------------------------------------------------

    prediction = text.predict([[Age,Height,Weight,gender,famhistory,smoke,mtrans]])

    label1.config(text="Prediction :-" + text_detector.pred_list[int(prediction)])


def run_text_detector():
    global sel_gen, sel_fam, sel_smoke, sel_mtrans, age_entry, height_entry, weight_entry, label1

    root = tk.Toplevel(win)
    root.transient(win)
    root.geometry("500x650")
    root.title("Obesity Detector")
    root.minsize(500,650)
    root.maxsize(600,1000)

    root.configure(bg="lightblue")



    #-------------------------------------------------------------------------------------------------------------------
    label = tk.Label(root,text="Obesity Detector",font=("Arial",20,"bold"),bg="lightblue",foreground="black")
    label.grid(row=0,column=1)

    #-------------------------------------------------------------------------------------------------------------------
    label = tk.Label(root,text="       ",font=("Arial",20,"bold"),bg="lightblue",foreground="black")
    label.grid(row=1,column=1)

    #-------------------------------------------------------------------------------------------------------------------
    age_label = tk.Label(root, text='Age:',font=("Arial",10,"bold"),bg="lightblue",foreground="black")
    age_label.grid(row=2, column=0)
    age_entry = tk.Entry(root)
    age_entry.grid(row=2, column=1)

    #-------------------------------------------------------------------------------------------------------------------
    label = tk.Label(root,text="       ",font=("Arial",20,"bold"),bg="lightblue",foreground="black")
    label.grid(row=3,column=1)

    #-------------------------------------------------------------------------------------------------------------------
    height_label = tk.Label(root, text='Height (m):',font=("Arial",10,"bold"),bg="lightblue",foreground="black")
    height_label.grid(row=4, column=0)
    height_entry = tk.Entry(root)
    height_entry.grid(row=4, column=1)

    #-------------------------------------------------------------------------------------------------------------------
    label = tk.Label(root,text="       ",font=("Arial",20,"bold"),bg="lightblue",foreground="black")
    label.grid(row=5,column=1)

    #-------------------------------------------------------------------------------------------------------------------
    weight_label = tk.Label(root, text='Weight (kg):',font=("Arial",10,"bold"),bg="lightblue",foreground="black")
    weight_label.grid(row=6, column=0)
    weight_entry = tk.Entry(root)
    weight_entry.grid(row=6, column=1)

    #-------------------------------------------------------------------------------------------------------------------
    label = tk.Label(root,text="       ",font=("Arial",20,"bold"),bg="lightblue",foreground="black")
    label.grid(row=7,column=1)

    #-------------------------------------------------------------------------------------------------------------------
    gender_label = tk.Label(root, text='Gender:',font=("Arial",10,"bold"),bg="lightblue",foreground="black")
    gender_label.grid(row=8, column=0)
    option_gen=["Select","Male","Female"]
    sel_gen = tk.StringVar()
    sel_gen.set(option_gen[0])
    option_menu = tk.OptionMenu(root,sel_gen,*option_gen)
    option_menu.grid(row=8, column=1)

    #-------------------------------------------------------------------------------------------------------------------
    label = tk.Label(root,text="       ",font=("Arial",20,"bold"),bg="lightblue",foreground="black")
    label.grid(row=9,column=1)

    #-------------------------------------------------------------------------------------------------------------------
    fam_label = tk.Label(root, text='Family History with overweight?',font=("Arial",10,"bold"),bg="lightblue",foreground="black")
    fam_label.grid(row=10, column=0)
    option_fam=["Select","yes","no"]
    sel_fam = tk.StringVar()
    sel_fam.set(option_fam[0])
    option_menu = tk.OptionMenu(root,sel_fam,*option_fam)
    option_menu.grid(row=10, column=1)

    #-------------------------------------------------------------------------------------------------------------------
    label = tk.Label(root,text="       ",font=("Arial",20,"bold"),bg="lightblue",foreground="black")
    label.grid(row=11,column=1)

    #-------------------------------------------------------------------------------------------------------------------
    smoke_label = tk.Label(root, text='Do you Smoke?',font=("Arial",10,"bold"),bg="lightblue",foreground="black")
    smoke_label.grid(row=12, column=0)
    option_smoke=["Select","yes","no"]
    sel_smoke = tk.StringVar()
    sel_smoke.set(option_smoke[0])
    option_menu = tk.OptionMenu(root,sel_smoke,*option_smoke)
    option_menu.grid(row=12, column=1)

    #-------------------------------------------------------------------------------------------------------------------
    label = tk.Label(root,text="       ",font=("Arial",20,"bold"),bg="lightblue",foreground="black")
    label.grid(row=13,column=1)

    #-------------------------------------------------------------------------------------------------------------------
    mtrans_label = tk.Label(root, text='Your mode of transport',font=("Arial",10,"bold"),bg="lightblue",foreground="black")
    mtrans_label.grid(row=14, column=0)
    option_mtrans=["Select","Walking","AutoMobile","Motorbike","Pubic_Transportation"]
    sel_mtrans = tk.StringVar()
    sel_mtrans.set(option_mtrans[0])
    option_menu = tk.OptionMenu(root,sel_mtrans,*option_mtrans)
    option_menu.grid(row=14, column=1)

    #-------------------------------------------------------------------------------------------------------------------
    label = tk.Label(root,text="       ",font=("Arial",20,"bold"),bg="lightblue",foreground="black")
    label.grid(row=15,column=1)




    submit_button = tk.Button(root, text='Submit', command=get_input)
    submit_button.grid(row=16, column=0, columnspan=2)

    #-------------------------------------------------------------------------------------------------------------------
    label = tk.Label(root,text="       ",font=("Arial",20,"bold"),bg="lightblue",foreground="black")
    label.grid(row=17,column=1)

    label1 = tk.Label(root,text="",font=("Arial",15,"bold"),bg="lightblue",foreground="black")
    label1.grid(row=18,column=1)

    root.mainloop()


def run_image_detector():
    global label2
    root = tk.Toplevel(win)
    root.transient(win)
    #root.wm_attributes("-topmost",1)
    root.geometry("275x200")
    root.title("Obesity Detector")
    root.minsize(275,200)
    root.maxsize(275,200)
    root.configure(bg="lightblue")

    # -------------------------------------------------------------------------------------------------------------------
    label = tk.Label(root, text="Obesity Detector", font=("Arial", 20, "bold"), bg="lightblue", foreground="black")
    label.grid(row=0, column=1)

    # -------------------------------------------------------------------------------------------------------------------
    label = tk.Label(root, text="       ", font=("Arial", 20, "bold"), bg="lightblue", foreground="black")
    label.grid(row=1, column=1)

    # -------------------------------------------------------------------------------------------------------------------

    btn = tk.Button(root, text='Select Image', command=open_file)
    btn.grid(row=2,column=1)

    #-------------------------------------------------------------------------------------------------------------------
    label = tk.Label(root,text="       ",font=("Arial",20,"bold"),bg="lightblue",foreground="black")
    label.grid(row=3,column=1)

    label2 = tk.Label(root,text="",font=("Arial",15,"bold"),bg="lightblue",foreground="black")
    label2.grid(row=4,column=1)

    root.mainloop()


def open_file():
    file = filedialog.askopenfile(mode='r',filetypes = [('JPEG files', '*.jpg *.jpeg'),('PNG files', '*.png')])
    print("file accessed")
    return predict(file)

def predict(file):

    prediction = list(image.predict(file.name, confidence=40, overlap=30))
    if prediction[0]['class'] == '1':
        prediction = "Not Obese"
    else:
        prediction = "Obese"

    label2.config(text="Prediction :-" + prediction)


#-------------------------------------------------------------------------------------------------------------------
win = tk.Tk()
win.geometry("350x300")
win.title("Obesity Detector")
win.minsize(350, 250)
win.maxsize(350, 250)
win.configure(bg="lightblue")
# -------------------------------------------------------------------------------------------------------------------
label = tk.Label(win, text="Obesity Detector", font=("Arial", 20, "bold"), bg="lightblue", foreground="black")
label.grid(row=0, column=0)

# -------------------------------------------------------------------------------------------------------------------
label = tk.Label(win, text="       ", font=("Arial", 20, "bold"), bg="lightblue", foreground="black")
label.grid(row=1, column=1)

# -------------------------------------------------------------------------------------------------------------------

choice_label = tk.Label(win, text='Choose the detector:', font=("Arial", 10, "bold"), bg="lightblue", foreground="black")
choice_label.grid(row=2, column=0)
option_choice = ["Select", "Text Detector", "Image Detector"]
sel_choice = tk.StringVar()
sel_choice.set(option_choice[0])
option_menu = tk.OptionMenu(win, sel_choice, *option_choice)
option_menu.grid(row=2, column=1)
# -------------------------------------------------------------------------------------------------------------------
label = tk.Label(win, text="       ", font=("Arial", 20, "bold"), bg="lightblue", foreground="black")
label.grid(row=3, column=1)

# -------------------------------------------------------------------------------------------------------------------
submit_button = tk.Button(win, text='Submit',command=take_input)
submit_button.grid(row=4, column=0, columnspan=2)

win.mainloop()
