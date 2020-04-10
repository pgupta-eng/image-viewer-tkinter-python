from tkinter import * 
from PIL import ImageTk,Image
from win32com.client import Dispatch
#window = tkinter.Tk()
#window.title("Edureka")
#icon =  tkinter.PhotoImage(file = "C:\Users\Ajit Gupta\Downloads\images.jpg")
root = Tk()
root.title('places')



#label = tkinter.Label(window, image = icon)
#label.pack()
#window.mainloop()

my_image1 = ImageTk.PhotoImage(Image.open("images/download1.png"))
my_image2 = ImageTk.PhotoImage(Image.open("images/download3.png"))
my_image3 = ImageTk.PhotoImage(Image.open("images/download3.png"))
my_image4 = ImageTk.PhotoImage(Image.open("images/download4.png"))
my_image5 = ImageTk.PhotoImage(Image.open("images/download5.png"))
my_image6 = ImageTk.PhotoImage(Image.open("images/download6.png"))
my_image7 = ImageTk.PhotoImage(Image.open("images/download7.png"))
my_image8 = ImageTk.PhotoImage(Image.open("images/download8.png"))
my_image9 = ImageTk.PhotoImage(Image.open("images/download9.jpg"))
my_image10 = ImageTk.PhotoImage(Image.open("images/download10.jpg"))
image_list = [my_image1, my_image2, my_image3, my_image4, my_image5, my_image7, my_image8, my_image9, my_image10]
my_label = Label(image=my_image1)
my_label.grid(row=0, column=0, columnspan=3)
def forward(image_number):
	global my_label
	global button_forward
	global button_back
	my_label.grid_forget()#internal function to get rid of already existing photo
	my_label = Label(image=image_list[image_number-1])
	button_forward = Button(root, text=">>", command=lambda:forward(image_number+1))
	button_back = Button(root, text="<<", command=lambda:forward(image_number-1))
	my_label.grid(row=0, column=0, columnspan=3)
	button_back.grid(row=1, column=0)
	button_forward.grid(row=1, column=1)

	
def back():
	global my_label
	global button_forward
	global button_back

	
#my_button = Button(root, text = "Click me", command=my_click)
button_back = Button(root, text = "<<", command=back)
button_forward = Button(root, text = ">>", command=lambda:forward(2))#inorder to go to the next image
button_quit = Button(root, text = "quit", command=root.quit)
#my_button.pack()
button_back.grid(row=1, column=0)
button_forward.grid(row=1, column=1)
button_quit.grid(row=1, column=2)

root.mainloop()