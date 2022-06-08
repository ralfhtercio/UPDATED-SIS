from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import displaytable as disp
import displaytable
import SISdatabase



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

class AddCourse:
    def __init__(self, frame, table):

        self.add_course_frame = frame
        self.course_table = table

        self.course_id = StringVar()

        self.add_course_id_entry = Entry(self.add_course_frame, textvariable=self.course_id, highlightthickness=2,
                                         highlightbackground="#33539E", font=("Bahnschrift SemiBold Condensed", 18))
        self.add_course_text = Text(self.add_course_frame, highlightthickness=2, highlightbackground="#33539E",
                                    font=("Bahnschrift SemiBold Condensed", 18))

        course_id_label = Label(self.add_course_frame, text="COURSE CODE", font=("Bahnschrift SemiBold Condensed", 17),
                                bg="#33539E", fg="white")
        course_id_label.place(x=10, y=50, width=110, height=35)
        self.add_course_id_entry.place(x=120, y=50, width=200, height=35)
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

        course_id_label = Label(self.edit_course_frame, text="COURSE CODE", font=("Bahnschrift SemiBold Condensed", 17),
                                bg="#33539E", fg="white")
        course_id_label.place(x=10, y=50, width=110, height=35)
        self.edit_course_id_entry.place(x=120, y=50, width=200, height=35)
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

class DashboardGUI:
    def __init__(self, frame):
        self.dashboard_cont_frame = frame


        self.bg_frame = Frame(self.dashboard_cont_frame, bg="#E9B7D4")

        self.stud_list_label = Label(self.dashboard_cont_frame, bg="#33539E", fg="#E9B7D4",
                                     text="  LIST OF STUDENTS", font=("Bahnschrift SemiBold Condensed", 15, "bold"), anchor="w")
        self.stud_list_frame = Frame(self.dashboard_cont_frame, bg="#E9B7D4", highlightbackground="#33539E",
                                     highlightthickness=2)

        self.course_label = Label(self.dashboard_cont_frame, bg="#33539E", fg="#E9B7D4",
                                  text="  LIST OF COURSES", font=("Bahnschrift SemiBold Condensed", 15, "bold"), anchor="w")
        self.course_list_frame = Frame(self.dashboard_cont_frame, bg="#E9B7D4", highlightbackground="#33539E",
                                       highlightthickness=2)

        scroll_x_stud_list = Scrollbar(self.stud_list_frame, orient=HORIZONTAL)
        scroll_y_stud_list = Scrollbar(self.stud_list_frame, orient=VERTICAL)

        scroll_x_course_list = Scrollbar(self.course_list_frame, orient=HORIZONTAL)
        scroll_y_course_list = Scrollbar(self.course_list_frame, orient=VERTICAL)
        self.student_table = ttk.Treeview(self.stud_list_frame, xscrollcommand=scroll_x_stud_list.set,
                                          yscrollcommand=scroll_y_stud_list.set, columns=("id_no", "name",
                                                                                          "course_code", "year",
                                                                                          "gender"))
        scroll_x_stud_list.pack(side=BOTTOM, fill=X)
        scroll_y_stud_list.pack(side=RIGHT, fill=Y)
        scroll_x_stud_list.config(command=self.student_table.xview)
        scroll_y_stud_list.config(command=self.student_table.yview)
        self.student_table.heading("id_no", text="ID Number")
        self.student_table.heading("name", text="Name")
        self.student_table.heading("course_code", text="Course Code")
        self.student_table.heading("year", text="Year")
        self.student_table.heading("gender", text="Gender")
        self.student_table['show'] = 'headings'
        self.student_table.column("id_no", width=70)
        self.student_table.column("name", width=190)
        self.student_table.column("course_code", width=100)
        self.student_table.column("year", width=70)
        self.student_table.column("gender", width=70)

        self.student_table.pack(fill=BOTH, expand=1)

        self.course_table = ttk.Treeview(self.course_list_frame, xscrollcommand=scroll_x_course_list.set,
                                         yscrollcommand=scroll_y_course_list.set, columns=("course_code",
                                                                                           "course"))
        scroll_x_course_list.pack(side=BOTTOM, fill=X)
        scroll_y_course_list.pack(side=RIGHT, fill=Y)
        scroll_x_course_list.config(command=self.course_table.xview)
        scroll_y_course_list.config(command=self.course_table.yview)
        self.course_table.heading("course_code", text="Course Code")
        self.course_table.heading("course", text="Course")
        self.course_table['show'] = 'headings'
        self.course_table.column("course_code", width=50)
        self.course_table.column("course", width=200)

        self.course_table.pack(fill=BOTH, expand=1)

        self.max_student_img = PhotoImage(file=r"images\max.png").subsample(5, 5)
        self.max_course_img = PhotoImage(file=r"images\max.png").subsample(5, 5)
        self.max_student_button = Button(self.dashboard_cont_frame, command=self.max_student_table, relief=FLAT,
                                         bg="#33539E", activebackground="#33539E", image=self.max_student_img)
        self.max_course_button = Button(self.dashboard_cont_frame, command=self.max_course_table, relief=FLAT,
                                        bg="#33539E", activebackground="#33539E", image=self.max_course_img)

        self.min_image = PhotoImage(file=r"images\min.png").subsample(5, 5)
        self.min_button = Button(self.dashboard_cont_frame, command=self.default_layout, relief=FLAT,
                                 fg="#E9B7D4", bg="#33539E", activeforeground="#E9B7D4", activebackground="#33539E",
                                 image=self.min_image)
        self.min_button.photo = self.min_image

        self.default_layout()
        disp.display_student_table(self.student_table)
        disp.display_course_table(self.course_table)

    def default_layout(self):
        self.min_button.place_forget()
        self.max_student_button.place(x=530, y=30, height=30, width=30)
        self.max_course_button.place(x=840, y=30, height=30, width=30)
        self.bg_frame.place(x=10, y=190, height=350, width=880)
        self.stud_list_label.place_configure(x=20, y=30, width=550, height=30)
        self.stud_list_frame.place_configure(x=20, y=60, width=550, height=500)
        self.course_label.place_configure(x=580, y=30, width=300, height=30)
        self.course_list_frame.place_configure(x=580, y=60, width=300, height=500)



    def max_student_table(self):
        self.hide_widgets()
        self.stud_list_label.place_configure(x=20, y=30, width=860, height=30)
        self.stud_list_frame.place_configure(x=20, y=60, width=860, height=500)
        self.min_button.place(x=840, y=30, height=30, width=30)

    def max_course_table(self):
        self.hide_widgets()
        self.course_label.place_configure(x=20, y=30, width=860, height=30)
        self.course_list_frame.place_configure(x=20, y=60, width=860, height=500)
        self.min_button.place(x=840, y=30, height=30, width=30)

    def hide_widgets(self):
        self.stud_list_label.place_forget()
        self.stud_list_frame.place_forget()
        self.max_student_button.place_forget()
        self.max_course_button.place_forget()
        self.course_list_frame.place_forget()
        self.course_label.place_forget()

class StudentGUI:
    def __init__(self, frame):
        self.student_cont_frame = frame

        self.search_stud = StringVar()

        self.add_button_img = PhotoImage(file=r"images\addstudent.png").subsample(1, 1)
        self.edit_button_img = PhotoImage(file=r"images\editstudent.png").subsample(1, 1)
        self.delete_button_img = PhotoImage(file=r"images\deletestudent.png").subsample(1, 1)
        self.srch_img = PhotoImage(file=r"images\searchbuttonimg.png").subsample(1, 1)

        add_student_btn = Button(self.student_cont_frame, bg="#33539E", image=self.add_button_img,
                                 command=self.add_student)
        add_student_btn.photo = self.add_button_img
        add_student_btn.place(x=70, y=50, width=70, height=70)

        edit_student_btn = Button(self.student_cont_frame, bg="#33539E", image=self.edit_button_img,
                                  command=self.edit_student)
        edit_student_btn.photo = self.edit_button_img
        edit_student_btn.place(x=150, y=50, width=70, height=70)

        delete_student_btn = Button(self.student_cont_frame, bg="#33539E", image=self.delete_button_img,
                                    command=self.delete_student)
        delete_student_btn.photo = self.delete_button_img
        delete_student_btn.place(x=230, y=50, width=70, height=70)

        search_code_label = Label(self.student_cont_frame, font=("Bahnschrift SemiBold Condensed", 11, "bold"), bg="#33539E", fg="white",
                                  text="Student ID:")
        search_code_label.place(x=370, y=85, width=80, height=35)
        self.search_student_bar_entry = Entry(self.student_cont_frame, textvariable=self.search_stud,
                                              font=("Bahnschrift SemiBold Condensed", 15, "bold"), highlightthickness=2,
                                              highlightbackground="#33539E")
        self.search_student_bar_entry.place(x=450, y=85, width=395, height=35)
        self.search_stud.trace("w", lambda name, index, mode, sv=self.search_stud: self.search_student())

        search_student_lbl = Label(self.student_cont_frame, image=self.srch_img)
        search_student_lbl.photo = self.srch_img
        search_student_lbl.place(x=845, y=85, width=35, height=35)

        self.stud_list_label = Label(self.student_cont_frame, bg="#33539E", fg="white", anchor='w',
                                     text="   LIST OF STUDENTS", font=("Bahnschrift SemiBold Condensed", 15, "bold"))

        self.stud_list_frame = Frame(self.student_cont_frame, bg="white", highlightbackground="#33539E",
                                     highlightthickness=2)

        self.stud_list_label.place_configure(x=370, y=140, width=510, height=30)
        self.stud_list_frame.place_configure(x=370, y=170, width=510, height=370)

        scroll_x_stud_list = Scrollbar(self.stud_list_frame, orient=HORIZONTAL)
        scroll_y_stud_list = Scrollbar(self.stud_list_frame, orient=VERTICAL)
        self.student_table = ttk.Treeview(self.stud_list_frame, xscrollcommand=scroll_x_stud_list.set,
                                          yscrollcommand=scroll_y_stud_list.set, columns=("id_no", "name",
                                                                                          "course_code", "year",
                                                                                          "gender"))
        scroll_x_stud_list.pack(side=BOTTOM, fill=X)
        scroll_y_stud_list.pack(side=RIGHT, fill=Y)
        scroll_x_stud_list.config(command=self.student_table.xview)
        scroll_y_stud_list.config(command=self.student_table.yview)
        self.student_table.heading("id_no", text="ID Number")
        self.student_table.heading("name", text="Name")
        self.student_table.heading("course_code", text="Course")
        self.student_table.heading("year", text="Year")
        self.student_table.heading("gender", text="Gender")
        self.student_table['show'] = 'headings'
        self.student_table.column("id_no", width=70)
        self.student_table.column("name", width=170)
        self.student_table.column("course_code", width=70)
        self.student_table.column("year", width=60)
        self.student_table.column("gender", width=60)

        self.student_table.pack(fill=BOTH, expand=1)

        self.heading_label = Label(self.student_cont_frame, bg="#33539E", fg="white", anchor='w',
                                   font=("Bahnschrift SemiBold Condensed", 15, "bold"))
        self.heading_label.place(x=10, y=140, width=340, height=30)

        self.features_frame = Frame(self.student_cont_frame, bg="#E9B7D4", highlightbackground="#E9B7D4",
                                    highlightthickness=2)
        self.add_student_frame = Frame(self.student_cont_frame, bg="#E9B7D4", highlightbackground="#E9B7D4",
                                       highlightthickness=2)
        self.edit_student_frame = Frame(self.student_cont_frame, bg="#E9B7D4", highlightbackground="#E9B7D4",
                                        highlightthickness=2)

        self.default_layout()
        disp.display_student_table(self.student_table)

    def default_layout(self):
        self.heading_label.config(text="  FEATURES")
        self.hide_widgets()
        self.features_frame.place(x=10, y=170, width=340, height=370)

        add_button_nav = Button(self.features_frame, command=self.add_student,
                                activebackground="#33539E", fg="white", activeforeground="#E9B7D4", bg="#33539E",
                                text=" ADD STUDENT", image=self.add_button_img, compound="left", anchor="w",
                                font=("Bahnschrift SemiBold Condensed", 20, "bold")
                                )
        add_button_nav.place(x=20, y=40, width=290, height=70)
        edit_button_nav = Button(self.features_frame, font=("Bahnschrift SemiBold Condensed", 20, "bold"), command=self.edit_student,
                                 activebackground="#33539E", fg="white", activeforeground="#E9B7D4", bg="#33539E",
                                 text=" EDIT STUDENT", image=self.edit_button_img, compound="left", anchor="w",
                                 )
        edit_button_nav.place(x=20, y=120, width=290, height=70)
        delete_button_nav = Button(self.features_frame, command=self.delete_student,
                                   activebackground="#33539E", fg="white", activeforeground="#E9B7D4", bg="#33539E",
                                   text=" DELETE STUDENT", image=self.delete_button_img, compound="left", anchor="w",
                                   font=("Bahnschrift SemiBold Condensed", 20, "bold")
                                   )
        delete_button_nav.place(x=20, y=200, width=290, height=70)

    def hide_widgets(self):
        self.features_frame.place_forget()
        self.add_student_frame.place_forget()
        self.edit_student_frame.place_forget()
        
    def add_student(self):
        self.heading_label.config(text="  ADD STUDENT")
        self.hide_widgets()
        self.add_student_frame.place(x=10, y=170, width=340, height=370)
        AddStudent(self.add_student_frame, self.student_table, self.search_student_bar_entry.get())

    def edit_student(self):
        self.heading_label.config(text="  EDIT STUDENT")
        self.hide_widgets()
        self.edit_student_frame.place(x=10, y=170, width=340, height=370)
        EditStudent(self.edit_student_frame, self.student_table)

    def delete_student(self):
        cursor_row = self.student_table.focus()
        contents = self.student_table.item(cursor_row)
        rows = contents['values']
        if rows == "":
            messagebox.showerror("Error", "Select a student first!")
        else:
            if messagebox.askyesno("Delete Student", "Do you wish to delete this student?"):
                SISdatabase.delete_student_rec(rows[0])
                messagebox.showinfo("Success", "Student deleted in database!")
                disp.display_student_table(self.student_table)
                self.default_layout()
                return
            else:
                return

    def search_student(self):
        result = SISdatabase.search_student_rec(self.search_stud.get().upper())
        self.student_table.delete(*self.student_table.get_children())
        if not result:
            return
        else:
            for x in result:
                self.student_table.insert('', 0, values=(x[0], x[1], x[3], x[2], x[4]))

class CoursesGUI:
    def __init__(self, frame):
        self.courses_cont_frame = frame

        self.search_course_id = StringVar()

        self.add_button_img = PhotoImage(file=r"images\addcourse.png").subsample(1, 1)
        self.edit_button_img = PhotoImage(file=r"images\editcourse.png").subsample(1, 1)
        self.delete_button_img = PhotoImage(file=r"images\deletecourse.png").subsample(1, 1)
        self.srch_img = PhotoImage(file=r"images\searchbuttonimg.png").subsample(1, 1)

        add_course_btn = Button(self.courses_cont_frame, image=self.add_button_img,
                                bg="#33539E", command=self.add_course)
        add_course_btn.photo = self.add_button_img
        add_course_btn.place(x=70, y=50, width=70, height=70)

        edit_course_btn = Button(self.courses_cont_frame, image=self.edit_button_img, bg="#33539E",
                                 command=self.edit_course)
        edit_course_btn.photo = self.edit_button_img
        edit_course_btn.place(x=150, y=50, width=70, height=70)

        delete_course_btn = Button(self.courses_cont_frame, image=self.delete_button_img, bg="#33539E",
                                   command=self.delete_course)
        delete_course_btn.photo = self.delete_button_img
        delete_course_btn.place(x=230, y=50, width=70, height=70)

        search_code_label = Label(self.courses_cont_frame, font=("Bahnschrift SemiBold Condensed", 11, "bold"), bg="#33539E", fg="white",
                                  text="Course CODE:")
        search_code_label.place(x=370, y=85, width=80, height=35)
        self.search_course_bar_entry = Entry(self.courses_cont_frame, textvariable=self.search_course_id,
                                             font=("Bahnschrift SemiBold Condensed", 15, "bold"), highlightthickness=2,
                                             highlightbackground="#33539E")
        self.search_course_bar_entry.place(x=450, y=85, width=395, height=35)
        self.search_course_id.trace("w", lambda name, index, mode, sv=self.search_course_id: self.search_course())
        search_course_lbl = Label(self.courses_cont_frame, image=self.srch_img)
        search_course_lbl.photo = self.srch_img
        search_course_lbl.place(x=845, y=85, width=35, height=35)

        courselist_label = Label(self.courses_cont_frame, bg="#33539E", fg="white",
                                 text="   LIST OF COURSES",
                                 font=("Bahnschrift SemiBold Condensed", 15, "bold"), anchor='w')
        courselist_label.place(x=370, y=140, width=510, height=30)

        self.course_list_frame = Frame(self.courses_cont_frame, bg="white", highlightbackground="#33539E",
                                       highlightthickness=2)
        self.course_list_frame.place(x=370, y=170, width=510, height=370)

        scroll_x_course_list = Scrollbar(self.course_list_frame, orient=HORIZONTAL)
        scroll_y_course_list = Scrollbar(self.course_list_frame, orient=VERTICAL)
        self.course_table = ttk.Treeview(self.course_list_frame, xscrollcommand=scroll_x_course_list.set,
                                         yscrollcommand=scroll_y_course_list.set, columns=("course_code",
                                                                                           "course"))
        scroll_x_course_list.pack(side=BOTTOM, fill=X)
        scroll_y_course_list.pack(side=RIGHT, fill=Y)
        scroll_x_course_list.config(command=self.course_table.xview)
        scroll_y_course_list.config(command=self.course_table.yview)
        self.course_table.heading("course_code", text="Course Code")
        self.course_table.heading("course", text="Course")
        self.course_table['show'] = 'headings'
        self.course_table.column("course_code", width=120)
        self.course_table.column("course", width=390)

        self.course_table.pack(fill=BOTH, expand=1)

        self.heading_label = Label(self.courses_cont_frame, bg="#33539E", fg="white", anchor='w',
                                   text="", font=("Bahnschrift SemiBold Condensed", 15, "bold"))
        self.heading_label.place(x=10, y=140, width=340, height=30)

        self.features_frame = Frame(self.courses_cont_frame, bg="#E9B7D4", highlightbackground="#E9B7D4",
                                    highlightthickness=2)
        self.add_course_frame = Frame(self.courses_cont_frame, bg="#E9B7D4", highlightbackground="#E9B7D4",
                                      highlightthickness=2)
        self.edit_course_frame = Frame(self.courses_cont_frame, bg="#E9B7D4", highlightbackground="#E9B7D4",
                                       highlightthickness=2)

        self.default_layout()
        disp.display_course_table(self.course_table)

    def default_layout(self):
        self.heading_label.config(text="   FEATURES")
        self.hide_widgets()
        self.features_frame.place(x=10, y=170, width=340, height=370)

        add_button_nav = Button(self.features_frame, command=self.add_course,
                                activebackground="#33539E", fg="white", activeforeground="#E9B7D4", bg="#33539E",
                                text=" ADD COURSE", image=self.add_button_img, compound="left", anchor="w",
                                font=("Bahnschrift SemiBold Condensed", 20, "bold")
                                )
        add_button_nav.place(x=20, y=40, width=290, height=70)
        edit_button_nav = Button(self.features_frame, font=("Bahnschrift SemiBold Condensed", 20, "bold"), command=self.edit_course,
                                 activebackground="#33539E", fg="white", activeforeground="#E9B7D4", bg="#33539E",
                                 text=" EDIT COURSE", image=self.edit_button_img, compound="left", anchor="w",
                                 )
        edit_button_nav.place(x=20, y=120, width=290, height=70)
        delete_button_nav = Button(self.features_frame, command=self.delete_course,
                                   activebackground="#33539E", fg="white", activeforeground="#E9B7D4", bg="#33539E",
                                   text=" DELETE COURSE", image=self.delete_button_img, compound="left", anchor="w",
                                   font=("Bahnschrift SemiBold Condensed", 20, "bold")
                                   )
        delete_button_nav.place(x=20, y=200, width=290, height=70)

    def hide_widgets(self):
        self.features_frame.place_forget()
        self.add_course_frame.place_forget()
        self.edit_course_frame.place_forget()

    def add_course(self):
        self.heading_label.config(text="  ADD COURSE")
        self.hide_widgets()
        self.add_course_frame.place(x=10, y=170, width=340, height=370)
        AddCourse(self.add_course_frame, self.course_table)

    def edit_course(self):
        self.heading_label.config(text="  EDIT COURSE")
        self.hide_widgets()
        self.edit_course_frame.place(x=10, y=170, width=340, height=370)
        EditCourse(self.edit_course_frame, self.course_table)

    def delete_course(self):
        cursor_row = self.course_table.focus()
        contents = self.course_table.item(cursor_row)
        rows = contents['values']
        if rows == "":
            messagebox.showerror("Error", "Select course first")
            return
        else:
            if messagebox.askyesno("Delete Course", "Do you wish to delete this course? Some students might be enrolled"
                                                    " in this course."):
                if SISdatabase.delete_course_rec(rows[0]):
                    disp.display_course_table(self.course_table)
                    messagebox.showinfo("Success", "Course deleted in database")
                    self.default_layout()
                return
            else:
                return

    def search_course(self):
        result = SISdatabase.search_course_rec(self.search_course_id.get().upper())
        self.course_table.delete(*self.course_table.get_children())
        if not result:
            return
        else:
            for x in result:
                self.course_table.insert('', 0, values=(x[0], x[1]))

class SIS:
    def __init__(self, frame):
        # creates database table for students and courses
        SISdatabase.data()

        self.frame = frame
        self.frame.title("Student Information System")
        self.frame.geometry("1200x680+63+8")
        self.frame.resizable(False, False)
        self.frame.iconbitmap(r"images\logosis.ico")

        # background frames
        bg_frame = Frame(self.frame, bg="#33539E")
        bg_frame.place(x=0, y=0, width=1200, height=680)

        # navigation frame
        self.nav_frame = Frame(bg_frame, bg="#33539E")
        self.nav_frame.place(x=3, y=3, width=260, height=674)

        # contents frame
        self.right_frame = Frame(bg_frame, bg="#7FACD6")
        self.right_frame.place(x=266, y=0, width=940, height=680)

        self.SISlogopic = PhotoImage(file=r"images\sislabellogo.png").subsample(2, 2)
        icon_pic_lbl = Label(self.nav_frame, image=self.SISlogopic)
        icon_pic_lbl.photo = self.SISlogopic
        icon_pic_lbl.place(x=5, y=10, width=250, height=180)

        self.dashboard_img = PhotoImage(file=r"images\dashboardimg.png")
        self.student_img = PhotoImage(file=r"images\studimg.png")
        self.course_img = PhotoImage(file=r"images\courseimg.png")
        self.about_img = PhotoImage(file=r"images\aboutimg.png")

        dashbrd_nav_button = Button(self.nav_frame, command=self.dashboard_frame_gui, relief=FLAT,
                                    activebackground="#33539E", activeforeground="#E9B7D4", fg="#7FACD6", bg="#33539E",
                                    image=self.dashboard_img, text="   HOME PAGE",
                                    font=("Bahnschrift SemiBold Condensed", 17, "bold"), anchor="w", compound="left")
        dashbrd_nav_button.place(x=0, y=200, width=260, height=50)
        stud_nav_button = Button(self.nav_frame, command=self.student_frame_gui, relief=FLAT,
                                 activebackground="#33539E", activeforeground="#E9B7D4", fg="#7FACD6", bg="#33539E",
                                 image=self.student_img, text="   STUDENTS",
                                 font=("Bahnschrift SemiBold Condensed", 17, "bold"), anchor="w", compound="left")
        stud_nav_button.place(x=0, y=250, width=260, height=50)
        course_nav_button = Button(self.nav_frame, command=self.courses_frame_gui, relief=FLAT,
                                   activebackground="#33539E", activeforeground="#E9B7D4", fg="#7FACD6", bg="#33539E",
                                   image=self.course_img, text="   COURSES",
                                   font=("Bahnschrift SemiBold Condensed", 17, "bold"), anchor="w", compound="left")
        course_nav_button.place(x=0, y=300, width=260, height=50)
       

        self.dashboard_cont_frame = Frame(self.right_frame, bg="#E9B7D4", highlightbackground="#33539E",
                                          highlightthickness=2)
        self.student_cont_frame = Frame(self.right_frame, bg="#E9B7D4", highlightbackground="#33539E",
                                        highlightthickness=2)
        self.courses_cont_frame = Frame(self.right_frame, bg="#E9B7D4", highlightbackground="#33539E",
                                        highlightthickness=2)
        self.about_cont_frame = Frame(self.right_frame, bg="#E9B7D4", highlightbackground="#33539E",
                                      highlightthickness=2)

        self.head_bldsgn_img = PhotoImage(file=r"images\label_design.png")
        self.heading_label = Label(self.right_frame, text="",
                                   bg="#33539E", fg="#E9B7D4",
                                   anchor="w", font=("Bahnschrift SemiBold Condensed", 20, "bold"))
        self.heading_lbldsgn = Label(self.right_frame, image=self.head_bldsgn_img, bg="#33539E",
                                     fg="#E9B7D4", anchor='sw')
        self.heading_label.place(x=20, y=50, width=900, height=50)
        self.heading_lbldsgn.place(x=800, y=50, width=120, height=50)

        self.dashboard_frame_gui()

    def hide_widgets(self):
        self.dashboard_cont_frame.place_forget()
        self.student_cont_frame.place_forget()
        self.courses_cont_frame.place_forget()
        self.about_cont_frame.place_forget()

    def dashboard_frame_gui(self):
        self.heading_label.config(text="  HOME PAGE ")
        self.hide_widgets()
        self.dashboard_cont_frame.place(x=20, y=100, width=900, height=570)
        DashboardGUI(self.dashboard_cont_frame)

    def student_frame_gui(self):
        self.heading_label.config(text="  STUDENTS")
        self.hide_widgets()
        self.student_cont_frame.place(x=20, y=100, width=900, height=570)
        StudentGUI(self.student_cont_frame)

    def courses_frame_gui(self):
        self.heading_label.config(text="  COURSES")
        self.hide_widgets()
        self.courses_cont_frame.place(x=20, y=100, width=900, height=570)
        CoursesGUI(self.courses_cont_frame)

 


root = Tk()
ob = SIS(root)
root.mainloop()
