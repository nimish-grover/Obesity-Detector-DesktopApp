import tkinter as tk
import gui as text_detector


root = tk.Tk()
root.geometry("225x200")
root.title("Obesity Detector")
root.minsize(225,200)
root.maxsize(225,200)

root.configure(bg="lightblue")


#-------------------------------------------------------------------------------------------------------------------
label = tk.Label(root,text="Obesity Detector",font=("Arial",20,"bold"),bg="lightblue",foreground="black")
label.grid(row=0,column=1)

label = tk.Label(root,text="       ",font=("Arial",20,"bold"),bg="lightblue",foreground="black")
label.grid(row=1,column=1)

#-------------------------------------------------------------------------------------------------------------------

text_button = tk.Button(root, text='Text Based Detection',command='call_text')
text_button.grid(row=2, column=0, columnspan=2)

label = tk.Label(root,text="       ",font=("Arial",20,"bold"),bg="lightblue",foreground="black")
label.grid(row=3,column=1)

#-------------------------------------------------------------------------------------------------------------------
image_button = tk.Button(root, text='Image Based Detection')
image_button.grid(row=4, column=0, columnspan=2)

label = tk.Label(root,text="       ",font=("Arial",20,"bold"),bg="lightblue",foreground="black")
label.grid(row=5,column=1)




def call_text():
    new=tk.Toplevel(root)
    text_detector.run_detector()

root.mainloop()