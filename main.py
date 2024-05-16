import tkinter as tk
from tkinter import messagebox, simpledialog
from datetime import datetime

class DrivingSchoolApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Driving School")
        self.geometry("400x250")
        self.configure(bg="white")  # Set background color to white

        # Initialize dictionary to store booked lessons and progress
        self.booked_lessons = {}
        self.progress = {}

        self.create_interface()

        # Bind window resize event
        self.bind("<Configure>", self.on_window_resize)

    def create_interface(self):
        self.create_buttons()

    def create_buttons(self):
        self.label = tk.Label(self, text="Welcome to Driving School", font=("Arial", 18), fg="#333", bg="#f0f0f0")
        self.label.place(relx=0.5, rely=0.1, anchor=tk.CENTER)

        # Create a frame for buttons
        self.button_frame = tk.Frame(self, bg="#f0f0f0")
        self.button_frame.place(relx=0.5, rely=0.3, anchor=tk.CENTER)

        buttons_info = [
            ("Student Sign-in", self.student_sign_in),
            ("Book a Lesson", self.book_lesson_window),
            ("View Schedule", self.view_schedule_window),
            ("View Progress", self.view_progress_window),
            ("Quit", self.quit)
        ]

        for i, (text, command) in enumerate(buttons_info):
            button = tk.Button(self.button_frame, text=text, command=command, bg="#007bff", fg="white", padx=10, pady=5)
            button.grid(row=0, column=i, padx=10, pady=5)

    def on_window_resize(self, event):
        # Calculate 5% increase in button size
        width_increment = self.winfo_width() // 5
        height_increment = self.winfo_height() // 5

        # Adjust button sizes
        new_width = self.button_frame.winfo_width() + width_increment
        new_height = self.button_frame.winfo_height() + height_increment
        self.button_frame.config(width=new_width, height=new_height)

    def student_sign_in(self):
        sign_in_window = StudentSignIn(self)
        self.center_window(sign_in_window)

    def book_lesson_window(self):
        book_lesson_window = BookLessonWindow(self)
        self.center_window(book_lesson_window)

    def view_schedule_window(self):
        self.view_schedule()

    def view_progress_window(self):
        view_progress_window = ViewProgressWindow(self)
        self.center_window(view_progress_window)

    def book_lesson(self):
        lesson_date = simpledialog.askstring("Book Lesson", "Enter lesson date (YYYY-MM-DD):")
        if lesson_date:
            try:
                lesson_date_obj = datetime.strptime(lesson_date, "%Y-%m-%d")
                day_of_week = lesson_date_obj.strftime("%A")
                if not hasattr(self, 'booked_lessons'):
                    self.booked_lessons = {}
                self.booked_lessons[lesson_date] = day_of_week
                self.progress[lesson_date] = 0  # Initialize progress for the lesson
                messagebox.showinfo("Book Lesson", f"Lesson booked for {lesson_date} ({day_of_week})")
            except ValueError:
                messagebox.showerror("Error", "Invalid date format. Please use YYYY-MM-DD.")

    def view_schedule(self):
        # Check if there are any booked lessons
        if hasattr(self, 'booked_lessons') and self.booked_lessons:
            # Create a schedule string based on booked lessons with days of the week
            schedule = "Booked Lessons:\n"
            for lesson_date, day_of_week in self.booked_lessons.items():
                schedule += f"{lesson_date} ({day_of_week})\n"
            messagebox.showinfo("View Schedule", schedule)
        else:
            messagebox.showinfo("View Schedule", "No booked lessons.")

    def view_progress(self):
        # Create a progress report based on booked lessons
        progress_report = "Lesson Progress:\n"
        for lesson_date, progress in self.progress.items():
            progress_report += f"{lesson_date}: {progress}% complete\n"
        if progress_report == "Lesson Progress:\n":
            progress_report += "No lessons in progress."
        messagebox.showinfo("View Progress", progress_report)

    def center_window(self, window):
        window.update_idletasks()
        window.geometry("+{}+{}".format(
            self.winfo_x() + (self.winfo_width() - window.winfo_width()) // 2,
            self.winfo_y() + (self.winfo_height() - window.winfo_height()) // 2,
        ))

class StudentSignIn(tk.Toplevel):
    def __init__(self, master):
        super().__init__(master)
        self.title("Student Sign-in")
        self.geometry("300x200")
        self.configure(bg="#f0f0f0")  # Set background color to white

        self.create_sign_in_form()

    def create_sign_in_form(self):
        self.email_label = tk.Label(self, text="Email:", bg="#f0f0f0")
        self.email_label.grid(row=0, column=0, padx=10, pady=5)
        self.email_entry = tk.Entry(self)
        self.email_entry.grid(row=0, column=1, padx=10, pady=5)

        self.password_label = tk.Label(self, text="Password:", bg="#f0f0f0")
        self.password_label.grid(row=1, column=0, padx=10, pady=5)
        self.password_entry = tk.Entry(self, show="*")
        self.password_entry.grid(row=1, column=1, padx=10, pady=5)

        self.sign_in_button = tk.Button(self, text="Sign In", command=self.sign_in, bg="#28a745", fg="white")
        self.sign_in_button.grid(row=2, columnspan=2, padx=10, pady=10)

    def sign_in(self):
        email = self.email_entry.get()
        password = self.password_entry.get()
        if email and password:
            # Placeholder for sign-in verification
            messagebox.showinfo("Sign In", "Sign-in Successfully.")
        else:
            messagebox.showerror("Error", "Please fill in all fields.")

class BookLessonWindow(tk.Toplevel):
    def __init__(self, master):
        super().__init__(master)
        self.title("Book Lesson")
        self.geometry("300x150")
        self.configure(bg="#f0f0f0")  # Set background color to white

        self.create_book_lesson_form()

    def create_book_lesson_form(self):
        lesson_date_label = tk.Label(self, text="Lesson Date:", bg="#f0f0f0")
        lesson_date_label.grid(row=0, column=0, padx=10, pady=5)
        self.lesson_date_entry = tk.Entry(self)
        self.lesson_date_entry.grid(row=0, column=1, padx=10, pady=5)

        book_button = tk.Button(self, text="Book", command=self.book_lesson, bg="#dc3545", fg="white")
        book_button.grid(row=1, columnspan=2, padx=10, pady=10)

    def book_lesson(self):
        lesson_date = self.lesson_date_entry.get()
        if lesson_date:
            try:
                lesson_date_obj = datetime.strptime(lesson_date, "%Y-%m-%d")
                day_of_week = lesson_date_obj.strftime("%A")
                if not hasattr(self.master, 'booked_lessons'):
                    self.master.booked_lessons = {}
                self.master.booked_lessons[lesson_date] = day_of_week
                self.master.progress[lesson_date] = 0  # Initialize progress for the lesson
                messagebox.showinfo("Book Lesson", f"Lesson booked for {lesson_date} ({day_of_week})")
            except ValueError:
                messagebox.showerror("Error", "Invalid date format. Please use YYYY-MM-DD.")
        else:
            messagebox.showerror("Error", "Please enter a lesson date.")

class ViewScheduleWindow(tk.Toplevel):
    def __init__(self, master):
        super().__init__(master)
        self.title("View Schedule")
        self.geometry("300x150")
        self.configure(bg="#f0f0f0")  # Set background color to white

        self.create_view_schedule()

    def create_view_schedule(self):
        if hasattr(self.master, 'booked_lessons'):
            self.schedule_label = tk.Label(self, text="Booked Lessons:", bg="#f0f0f0")
            self.schedule_label.pack(pady=10)

            self.schedule_text = tk.Text(self, height=5, width=30, bg="white", fg="#333")
            self.schedule_text.pack()

            for lesson_date, day_of_week in self.master.booked_lessons.items():
                self.schedule_text.insert(tk.END, f"{lesson_date} ({day_of_week})\n")
        else:
            messagebox.showinfo("View Schedule", "No booked lessons.")

class ViewProgressWindow(tk.Toplevel):
    def __init__(self, master):
        super().__init__(master)
        self.title("View Progress")
        self.geometry("300x150")
        self.configure(bg="#f0f0f0")  # Set background color to white

        self.create_view_progress()

    def create_view_progress(self):
        progress_form = ViewProgressForm(self)
        progress_form.pack(expand=True, fill="both")

class ViewProgressForm(tk.Frame):
    def __init__(self, master):
        super().__init__(master, bg="#f0f0f0")

        self.progress_label = tk.Label(self, text="Lesson Progress:", bg="#f0f0f0")
        self.progress_label.pack(pady=10)

        self.progress_text = tk.Text(self, height=5, width=30, bg="white", fg="#333")
        self.progress_text.pack()

        for lesson_date, progress in master.master.progress.items():
            self.progress_text.insert(tk.END, f"{lesson_date}: {progress}% complete\n")

if __name__ == "__main__":
    root = DrivingSchoolApp()
    root.mainloop()
