from tkinter import *
from tkinter import ttk
from tkinter import messagebox

import SISdatabase
import displaytable


class AddStudent:
    def __init__(self, frame, table, searchentry):
        self.add_student_frame = frame
        self.student_table = table
        self.searchEntry = searchentry

        self.id_no = StringVar()
        self.name = StringVar()
        self.course = StringVar()
        self.year = StringVar()
        self.gender = StringVar()

        self.add_name_entry = Entry(self.add_student_frame, textvariable=self.name, highlightthickness=2,
                                    highlightbackground="#33539E", font=("Bahnschrift SemiBold Condensed", 18))

        self.add_id_entry = Entry(self.add_student_frame, textvariable=self.id_no, highlightthickness=2,
                                  highlightbackground="#33539E", font=("Bahnschrift SemiBold Condensed", 18))
        self.add_year_combo = ttk.Combobox(self.add_student_frame, textvariable=self.year, font=("Bahnschrift SemiBold Condensed", 18),
                                           values=[
                                               "1st Year",
                                               "2nd Year",
                                               "3rd Year",
                                               "4th Year",
                                               "5th Year"])
        self.add_course_id_entry = Entry(self.add_student_frame, textvariable=self.course, highlightthickness=2,
                                         highlightbackground="#33539E", font=("Bahnschrift SemiBold Condensed", 18))
        self.add_gender_combo = ttk.Combobox(self.add_student_frame, textvariable=self.gender, font=("Bahnschrift SemiBold Condensed", 18),
                                             values=["Male", "Female", "Other"])

        name_label = Label(self.add_student_frame, text="NAME", font=("Bahnschrift SemiBold Condensed", 17), bg="#33539E",
                           fg="white")
        name_label.place(x=10, y=20, width=80, height=35)
        self.add_name_entry.place(x=90, y=20, width=235, height=35)
        name_format = Label(self.add_student_frame, text="Last Name, First Name, M.I", font=("Bahnschrift SemiBold Condensed", 8),
                            fg="#33539E", bg="white")
        name_format.place(x=95, y=56, height=20)
        id_no_label = Label(self.add_student_frame, text="ID NO.", font=("Bahnschrift SemiBold Condensed", 17), bg="#33539E",
                            fg="white")
        id_no_label.place(x=10, y=80, width=80, height=35)
        self.add_id_entry.place(x=90, y=80, width=235, height=35)
        year_label = Label(self.add_student_frame, text="YEAR", font=("Bahnschrift SemiBold Condensed", 17), bg="#33539E",
                           fg="white")
        year_label.place(x=10, y=125, width=80, height=35)
        self.add_year_combo.place(x=90, y=125, width=235, height=35)
        course_id_label = Label(self.add_student_frame, text="COURSE ID", font=("Bahnschrift SemiBold Condensed", 17), bg="#33539E",
                                fg="white")
        course_id_label.place(x=10, y=170, width=80, height=35)
        self.add_course_id_entry.place(x=90, y=170, width=235, height=35)
        gender_label = Label(self.add_student_frame, text="GENDER", font=("Bahnschrift SemiBold Condensed", 17), bg="#33539E",
                             fg="white")
        gender_label.place(x=10, y=215, width=80, height=35)
        self.add_gender_combo.place(x=90, y=215, width=235, height=35)

        add_info_button = Button(self.add_student_frame, command=self.add_student, text="ADD",
                                 bg="#33539E", fg="white", activebackground="#33539E", activeforeground="#FA9412",
                                 font=("Bahnschrift SemiBold Condensed", 15))
        add_info_button.place(x=175, y=300, width=70, height=30)
        clear_info_button = Button(self.add_student_frame, command=self.clear_data, text="CLEAR",
                                   bg="#33539E", fg="white", activebackground="#33539E", activeforeground="#FA9412",
                                   font=("Bahnschrift SemiBold Condensed", 15))
        clear_info_button.place(x=255, y=300, width=70, height=30)

    def clear_data(self):
        self.add_id_entry.delete(0, END)
        self.add_name_entry.delete(0, END)
        self.add_course_id_entry.delete(0, END)
        self.add_year_combo.delete(0, END)
        self.add_gender_combo.delete(0, END)

    def add_student(self):
        if messagebox.askyesno("Add Student", "Do you want to add the student in the database"):
            if not SISdatabase.info_checker(self.id_no.get(), self.name.get().upper(), self.year.get(),
                                            self.course.get().upper(), self.gender.get().upper()):
                return
            else:
                if SISdatabase.add_student_rec(self.id_no.get(), self.name.get().upper(), self.year.get(),
                                               self.course.get().upper(), self.gender.get()):
                    messagebox.showinfo("Success", "Student added to database")
                    self.clear_data()
                    displaytable.display_student_table(self.student_table)
                else:
                    return

class EditStudent:
    def __init__(self, frame, table):
        self.edit_student_frame = frame
        self.student_table = table

        self.id_no = StringVar()
        self.name = StringVar()
        self.course = StringVar()
        self.year = StringVar()
        self.gender = StringVar()

        self.rows = []

        # Edit
        self.edit_name_entry = Entry(self.edit_student_frame, textvariable=self.name, highlightthickness=2,
                                     highlightbackground="#33539E", font=("Bahnschrift SemiBold Condensed", 18))
        self.edit_id_entry = Entry(self.edit_student_frame, textvariable=self.id_no, highlightthickness=2,
                                   highlightbackground="#33539E", font=("Bahnschrift SemiBold Condensed", 18))
        self.edit_year_combo = ttk.Combobox(self.edit_student_frame, textvariable=self.year, font=("Bahnschrift SemiBold Condensed", 18),
                                            values=[
                                                "1st Year",
                                                "2nd Year",
                                                "3rd Year",
                                                "4th Year",
                                                "5th Year"])
        self.edit_course_entry = Entry(self.edit_student_frame, textvariable=self.course, font=("Bahnschrift SemiBold Condensed", 18),
                                       highlightthickness=2, highlightbackground="#33539E")
        self.edit_gender_combo = ttk.Combobox(self.edit_student_frame, textvariable=self.gender,
                                              font=("Bahnschrift SemiBold Condensed", 18),
                                              values=["Male", "Female", "Other"])

        # attributes on edit student feature
        name_label = Label(self.edit_student_frame, text="NAME", font=("Bahnschrift SemiBold Condensed", 17), bg="#33539E",
                           fg="white")
        name_label.place(x=10, y=20, width=80, height=35)
        self.edit_name_entry.place(x=90, y=20, width=235, height=35)
        name_format = Label(self.edit_student_frame, text="Last Name, First Name, M.I", font=("Bahnschrift SemiBold Condensed", 8),
                            fg="#33539E", bg="white")
        name_format.place(x=95, y=56, height=20)
        id_no_label = Label(self.edit_student_frame, text="ID NO.", font=("Bahnschrift SemiBold Condensed", 17), bg="#33539E",
                            fg="white")
        id_no_label.place(x=10, y=80, width=80, height=35)
        self.edit_id_entry.place(x=90, y=80, width=235, height=35)
        year_label = Label(self.edit_student_frame, text="YEAR", font=("Bahnschrift SemiBold Condensed", 17), bg="#33539E",
                           fg="white")
        year_label.place(x=10, y=125, width=80, height=35)
        self.edit_year_combo.place(x=90, y=125, width=235, height=35)
        course_label = Label(self.edit_student_frame, text="COURSE ID", font=("Bahnschrift SemiBold Condensed", 17), bg="#33539E",
                             fg="white")
        course_label.place(x=10, y=170, width=80, height=35)
        self.edit_course_entry.place(x=90, y=170, width=235, height=35)
        gender_label = Label(self.edit_student_frame, text="GENDER", font=("Bahnschrift SemiBold Condensed", 17), bg="#33539E",
                             fg="white")
        gender_label.place(x=10, y=215, width=80, height=35)
        self.edit_gender_combo.place(x=90, y=215, width=235, height=35)

        update_info_button = Button(self.edit_student_frame, command=self.update_student, text="UPDATE",
                                    bg="#33539E", fg="white", activebackground="#33539E", activeforeground="#FA9412",
                                    font=("Bahnschrift SemiBold Condensed", 15))
        update_info_button.place(x=175, y=300, width=70, height=30)
        clear_info_button = Button(self.edit_student_frame, command=self.clear_data, text="CLEAR",
                                   bg="#33539E", fg="white", activebackground="#33539E", activeforeground="#FA9412",
                                   font=("Bahnschrift SemiBold Condensed", 15))
        clear_info_button.place(x=255, y=300, width=70, height=30)
        self.student_table.bind("<ButtonRelease-1>", self.select_student)

    def update_student(self):
        if not self.rows:
            messagebox.showerror("Error", "Choose a student from the table first")
            return
        elif not SISdatabase.info_checker(self.id_no.get(), self.name.get().upper(), self.year.get(),
                                          self.course.get().upper(), self.gender.get().upper()):
            return
        else:
            if messagebox.askyesno("Update Course", "Do you wish to update the student information?"):
                if SISdatabase.update_student_rec(self.rows[0], self.id_no.get(), self.name.get().upper(),
                                                  self.year.get(), self.course.get().upper(),
                                                  self.gender.get()):
                    messagebox.showinfo("Success", "Information on student has been updated!")
                    self.clear_data()
                    self.rows = []
                    displaytable.display_student_table(self.student_table)

    def clear_data(self):
        self.edit_id_entry.delete(0, END)
        self.edit_name_entry.delete(0, END)
        self.edit_year_combo.delete(0, END)
        self.edit_course_entry.delete(0, END)
        self.edit_gender_combo.delete(0, END)

    def select_student(self, ev):
        cursor_row = self.student_table.focus()
        contents = self.student_table.item(cursor_row)
        self.rows = contents['values']
        self.clear_data()
        if not self.rows:
            return
        else:
            self.edit_name_entry.insert(0, self.rows[1])
            self.edit_id_entry.insert(0, self.rows[0])
            self.edit_year_combo.insert(0, self.rows[3])
            self.edit_course_entry.insert(0, self.rows[2])
            self.edit_gender_combo.insert(0, self.rows[4])
