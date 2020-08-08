##########################################################################################################################
### This program can be converted to ann exe format using the pyinstaler lib, just go to the desired folder and        ###
### pyinstaller --onefile --windowed frontend.py                                                                       ###
### onefile allows only one file of the exe to be made, windowed omits the existence of a command line behind your GUI ###
##########################################################################################################################

from tkinter import *
import backend #backend made using sqlite3

#Create Object of Tkinter class
root = Tk()

#####################################Necessary internal function definitions######################################################
###Because we have bound this function to a widget event, it gets the event parameter
def get_selected_row(event):
    #Implementing try-except block b/c when empty listbox is clicked throws
    # IndexError, so when IndexError occurs,continue with the program through pass
    try:
        global selected_tuple
        #Get index of the list from the listbox of selected row
        index = databox.curselection()[0]
        selected_tuple = databox.get(index) #Gives us the tuple value of index at the cursor 

        #This allows the selected row's tuple values to be displayed in the entry boxes for their specific values 
        e1.delete(0, END)
        e1.insert(END, selected_tuple[1])

        e2.delete(0, END)
        e2.insert(END, selected_tuple[2])

        e3.delete(0, END)
        e3.insert(END, selected_tuple[3])

        e4.delete(0, END)
        e4.insert(END, selected_tuple[4])
    except IndexError:
        pass


#############To be used for the command associated with the View All Button##############
def view_func ():
    databox.delete(0, END) # Deletes the entire content of list box so same contents dont get displayed over and over again 
    for rows in backend.view_all():
        databox.insert(END,rows)


############To be used for the command associated with the Search Button###############
def search_func ():
    databox.delete(0, END) # Deletes the entire content of list box so same contents dont get displayed over and over again 
    #Use get function for the strings because they are of type StringVar
    for rows in backend.Search_Entry(author = author_txt.get(), title =title_txt.get() , isbn =isbn_txt.get() ,year =year_txt.get()):
        databox.insert(END,rows)


############To be used for the command associated with the Add Entry Button###############
def add_func():
    databox.delete(0, END)
    backend.Add_Entry(author = author_txt.get(), title =title_txt.get() , isbn =isbn_txt.get() ,year =year_txt.get())    
    for rows in backend.view_all():
        databox.insert(END, rows)


############To be used for the command associated with the Update Entry Button###############
def update_func():
    backend.update(selected_tuple[0], title_txt.get(), author_txt.get(), year_txt.get(), isbn_txt.get())   
    #For loop to display all current contents of the list that encapsulates all the database data 
    for rows in backend.view_all():
        databox.insert(END, rows)


############To be used for the command associated with the Delete Entry Button###############
def delete_func():
    databox.delete(0, END) # Deletes the entire content of list box so same contents dont get displayed over and over again 
    backend.Delete_Selected(selected_tuple[0])  #Passing the id of the selected row to the Delete Method in the backend 
    for rows in backend.view_all():
        databox.insert(END,rows)

#Program Title
root.title("Bookstore Database Program")

#Creating Labels 
l1=Label( root,text="Title")
l1.grid(row=0,column=0)

l2=Label(root,text="Author")
l2.grid(row=0,column=2)

l3=Label( root,text="Year")
l3.grid(row=1,column=0)

l4=Label( root,text="ISBN")
l4.grid(row=1,column=2)


#Creating entry boxes for Title, Year, Author, ISBN
title_txt = StringVar()
e1 = Entry(root, textvariable=title_txt)
e1.grid(row=0,column=1)

author_txt = StringVar()
e2 = Entry(root, textvariable=author_txt)
e2.grid(row=0,column=3)

year_txt = StringVar()
e3 = Entry(root, textvariable=year_txt)
e3.grid(row=1,column=1)

isbn_txt = StringVar()
e4 = Entry(root, textvariable=isbn_txt)
e4.grid(row=1,column=3)

#Creating Buttons for all options
View_All_Button = Button(root, text ="View All", width = 12, bg= 'yellow', command = view_func) #No need to add (), else py will execute at all times instead of only when button is pressed
Search_Entry_Button = Button(root, text ="Search Entry", width = 12, bg= 'yellow', command = search_func)
Add_Entry_Button = Button(root, text ="Add Entry", bg= 'yellow', width = 12, command = add_func)
Update_Selected_Button = Button(root, text ="Update Selected", bg= 'yellow', width = 12, command= update_func)
Delete_Selected_Button = Button(root, text ="Delete Selected",  bg= 'yellow', width = 12, command= delete_func)
Close_Button = Button(root, text ="Close", bg= 'yellow', width = 12, command= root.destroy)

#Adding Dimension specifications for Buttons
View_All_Button.grid(row = 2, column = 3)
Search_Entry_Button.grid(row = 3, column = 3)
Add_Entry_Button.grid(row = 4, column = 3)
Update_Selected_Button.grid(row = 5, column = 3)
Delete_Selected_Button.grid(row = 6, column = 3)
Close_Button.grid(row = 7, column = 3)

##Adding a scroll box to display database contents 
databox = Listbox(root, height = 6, width = 35)
databox.grid(row =2, column = 0, rowspan = 6 , columnspan= 2)

##Adding Scrolbar for listbox
scrolling = Scrollbar(root)
scrolling.grid(row=2,column=2,rowspan=6)

databox.configure(yscrollcommand=scrolling.set)
scrolling.configure(command=databox.yview)

#uses bind method of lsitbox to apply a certain function of get_selected_row to the cursor
databox.bind('<<ListboxSelect>>', get_selected_row)

mainloop()
