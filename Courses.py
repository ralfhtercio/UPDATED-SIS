from tkinter import *
from tkinter import messagebox
import SISdatabase

import displaytable as disp
import displaytable


class AddCourse:
    def __init__(self, frame, table):

        self.add_course_frame = frame
        self.course_table = table

        self.course_id = StringVar()

        self.add_course_id_entry = Entry(self.add_course_frame, textvariable=self.course_id, highlightthickness=2,
                                         highlightbackground="#33539E", font=("Bahnschrift SemiBold Condensed", 18))
        self.add_course_text = Text(self.add_course_frame, highlightthickness=2, highlightbackground="#33539E",
                                    font=("Bahnschrift SemiBold Condensed", 18))

        course_id_label = Label(self.add_course_frame, text="COURSE ID", font=("Bahnschrift SemiBold Condensed", 17),
                                bg="#33539E", fg="white")
        course_id_label.place(x=10, y=50, width=80, height=35)
        self.add_course_id_entry.place(x=90, y=50, width=235, height=35)
        course_label = Label(self.add_course_frame, text="COURSE NAME", font=("Bahnschrift SemiBold Condensed", 17),
                             bg="#33539E", fg="white")
        course_label.place(x=10, y=100, width=110, height=35)
        self.add_course_text.place(x=10, y=135, width=315, height=125)

        add_info_button = Button(self.add_course_frame, command=self.add_course, text="ADD",
                                 bg="#33539E", fg="white", activebackground="#33539E", activeforeground="#FA9412",
                                 font=("Bahnschrift SemiBold Condensed", 15))
        add_info_button.place(x=175, y=300, width=70, height=30)
        clear_info_button = Button(self.add_course_frame, command=self.clear_data, text="CLEAR",
                                   bg="#33539E", fg="white", activebackground="#33539E", activeforeground="#FA9412",
                                   font=("Bahnschrift SemiBold Condensed", 15))
        clear_info_button.place(x=255, y=300, width=70, height=30)

    def clear_data(self):
        self.add_course_id_entry.delete(0, END)
        self.add_course_text.delete(1.0, END)

    def add_course(self):
        if self.add_course_id_entry.get() == "" or self.add_course_text.get(1.0, END) == "":
            messagebox.showerror("Error", "Please fill all fields")
            return

        else:
            if messagebox.askyesno("Add Course", "Do you wish to add the course to database?"):
                if SISdatabase.add_course_rec(self.course_id.get().upper(),
                                              self.add_course_text.get(1.0, END).upper().replace("\n", "")):
                    messagebox.showinfo("Success", "Course added to database.")
                    self.clear_data()
                    displaytable.display_course_table(self.course_table)
                else:
                    return
            else:
                return

class EditCourse:
    def __init__(self, frame, table):
        self.edit_course_frame = frame
        self.course_table = table

        self.rows = []

        self.course_id = StringVar()

        self.edit_course_id_entry = Entry(self.edit_course_frame, textvariable=self.course_id, highlightthickness=2,
                                          highlightbackground="#33539E", font=("Bahnschrift SemiBold Condensed", 18))
        self.edit_course_text = Text(self.edit_course_frame, highlightthickness=2, highlightbackground="#33539E",
                                     font=("Bahnschrift SemiBold Condensed", 18))

        course_id_label = Label(self.edit_course_frame, text="COURSE ID", font=("Bahnschrift SemiBold Condensed", 17),
                                bg="#33539E", fg="white")
        course_id_label.place(x=10, y=50, width=80, height=35)
        self.edit_course_id_entry.place(x=90, y=50, width=235, height=35)
        course_label = Label(self.edit_course_frame, text="COURSE NAME", font=("Bahnschrift SemiBold Condensed", 17),
                             bg="#33539E", fg="white")
        course_label.place(x=10, y=100, width=110, height=35)
        self.edit_course_text.place(x=10, y=135, width=315, height=125)

        update_info_button = Button(self.edit_course_frame, command=self.update_course, text="UPDATE",
                                    bg="#33539E", fg="white", activebackground="#33539E", activeforeground="#FA9412",
                                    font=("Bahnschrift SemiBold Condensed", 15))
        update_info_button.place(x=175, y=300, width=70, height=30)
        clear_info_button = Button(self.edit_course_frame, command=self.clear_data, text="CLEAR",
                                   bg="#33539E", fg="white", activebackground="#33539E", activeforeground="#FA9412",
                                   font=("Bahnschrift SemiBold Condensed", 15))
        clear_info_button.place(x=255, y=300, width=70, height=30)
        self.course_table.bind("<ButtonRelease-1>", self.select_course)

    def update_course(self):
        if not self.rows:
            messagebox.showerror("Error", "Choose a course from the table first")
        elif self.edit_course_id_entry.get() == "" or self.edit_course_text.get(1.0, END) == "":
            messagebox.showerror("Error", "Please fill all fields")
            return
        else:
            if messagebox.askyesno("Update Course", "Do you wish to update the course information? Some students might"
                                                    " be enrolled in this course?"):
                if SISdatabase.update_course_rec(self.rows[0], self.course_id.get().upper(),
                                                 self.edit_course_text.get(1.0, END).upper().replace("\n", "")):
                    messagebox.showinfo("Success", "Information on course has been updated!")
                    self.clear_data()
                    self.rows = []
                    disp.display_course_table(self.course_table)
                return
            else:
                return

    def clear_data(self):
        self.edit_course_id_entry.delete(0, END)
        self.edit_course_text.delete(1.0, END)

    def select_course(self, ev):
        cursor_row = self.course_table.focus()
        contents = self.course_table.item(cursor_row)
        self.rows = contents['values']
        self.clear_data()
        self.edit_course_id_entry.insert(0, self.rows[0])
        self.edit_course_text.insert(END, self.rows[1])
