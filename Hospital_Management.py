import ttkbootstrap as tb
from ttkbootstrap.constants import *
import tkinter as tk
from tkinter import ttk

# Initialize window
app = tb.Window(themename="flatly")
app.title("🏥 Hospital Management System")
app.geometry("1050x700")

# -------------- Data Storage (In-memory) -------------- #
patients_data = []
doctors_data = [
    {"name": "Dr. Smith", "specialty": "Cardiology", "avatar": "👨‍⚕️"},
    {"name": "Dr. Johnson", "specialty": "Neurology", "avatar": "👩‍⚕️"},
    {"name": "Dr. Lee", "specialty": "Orthopedics", "avatar": "👨‍⚕️"},
    {"name": "Dr. Kim", "specialty": "Dermatology", "avatar": "👩‍⚕️"},
    {"name": "Dr. Clark", "specialty": "Pediatrics", "avatar": "👨‍⚕️"},
    {"name": "Dr. Martinez", "specialty": "General Surgery", "avatar": "👩‍⚕️"},
    {"name": "Dr. Brown", "specialty": "Ophthalmology", "avatar": "👨‍⚕️"},
    {"name": "Dr. Taylor", "specialty": "Psychiatry", "avatar": "👩‍⚕️"},
    {"name": "Dr. Wilson", "specialty": "Radiology", "avatar": "👨‍⚕️"},
    {"name": "Dr. Moore", "specialty": "Endocrinology", "avatar": "👩‍⚕️"},
]
appointments_data = []
staff_data = []
beds_data = {
    "total_beds": 50,
    "occupied_beds": 30,
    "empty_beds": 20
}

# -------------- Sidebar -------------- #
sidebar = tb.Frame(app, bootstyle="light", width=200)
sidebar.pack(side=LEFT, fill=Y)

menu_items = [
    ("🏠", "Home"),
    ("➕", "Add Patients"),  # Add Patients
    ("👤", "View Patients"),  # View Patients
    ("🩺", "Doctors"),
    ("📅", "Appointments"),
    ("💳", "Billing"),
    ("👥", "Staff"),
    ("🛏️", "Beds")
]

frames = {}

def show_frame(name):
    for f in frames.values():
        f.place_forget()

    frames[name].place(relx=0.19, rely=0.08, relwidth=0.8, relheight=0.88)
    frames[name].tkraise()

def create_sidebar():
    for icon, label in menu_items:
        btn = tb.Button(sidebar, text=f"{icon} {label}", bootstyle="light", width=20,
                        command=lambda l=label: show_frame(l))
        btn.pack(pady=10, padx=10)

create_sidebar()

# -------------- Top Bar -------------- #
topbar = tb.Frame(app, bootstyle="primary")
topbar.place(relx=0.19, rely=0, relwidth=0.81, height=50)

title = tb.Label(topbar, text="Hospital Management System", font=("Segoe UI", 18), bootstyle="inverse-light")
title.pack(padx=20, pady=5, anchor="w")

# -------------- Home Page -------------- #
home_frame = tb.Frame(app, bootstyle="light")
home_label = tb.Label(home_frame, text="Welcome 👋", font=("Segoe UI", 20), bootstyle="primary")
home_label.pack(pady=30)

frames["Home"] = home_frame


# -------------- Add Patients Page -------------- #
def add_patient():
    name = patient_name_entry.get()
    age = patient_age_entry.get()
    gender = patient_gender_var.get()
    contact = patient_contact_entry.get()
    disease = patient_disease_entry.get()

    if name and age and gender and contact and disease:
        patient = {
            "name": name,
            "age": age,
            "gender": gender,
            "contact": contact,
            "disease": disease
        }
        patients_data.append(patient)

        # Save to hospital.txt
        with open("hospital.txt", "a") as file:
            file.write(f"{name},{age},{gender},{contact},{disease}\n")

        # Clear input fields
        patient_name_entry.delete(0, tk.END)
        patient_age_entry.delete(0, tk.END)
        patient_contact_entry.delete(0, tk.END)
        patient_disease_entry.delete(0, tk.END)
        patient_gender_var.set("")

        update_patient_list()

# Main Frame without Scrollbar
patient_frame = tb.Frame(app, bootstyle="light")
frames["Add Patients"] = patient_frame

# Title
pt_title = tb.Label(patient_frame, text="➕ Add Patient", font=("Segoe UI", 18))
pt_title.pack(pady=10)

# Name
patient_name_label = tb.Label(patient_frame, text="Name", font=("Segoe UI", 12))
patient_name_label.pack(pady=5)
patient_name_entry = tb.Entry(patient_frame, bootstyle="secondary")
patient_name_entry.pack(pady=5)

# Age
patient_age_label = tb.Label(patient_frame, text="Age", font=("Segoe UI", 12))
patient_age_label.pack(pady=5)
patient_age_entry = tb.Entry(patient_frame, bootstyle="secondary")
patient_age_entry.pack(pady=5)

# Gender
patient_gender_label = tb.Label(patient_frame, text="Gender", font=("Segoe UI", 12))
patient_gender_label.pack(pady=5)
patient_gender_var = tk.StringVar()
gender_male_rb = tb.Radiobutton(patient_frame, text="Male", value="Male", variable=patient_gender_var, bootstyle="secondary")
gender_female_rb = tb.Radiobutton(patient_frame, text="Female", value="Female", variable=patient_gender_var, bootstyle="secondary")
gender_male_rb.pack(pady=5)
gender_female_rb.pack(pady=5)

# Contact Number
patient_contact_label = tb.Label(patient_frame, text="Contact Number", font=("Segoe UI", 12))
patient_contact_label.pack(pady=5)
patient_contact_entry = tb.Entry(patient_frame, bootstyle="secondary")
patient_contact_entry.pack(pady=5)

# Disease
patient_disease_label = tb.Label(patient_frame, text="Disease", font=("Segoe UI", 12))
patient_disease_label.pack(pady=5)
patient_disease_entry = tb.Entry(patient_frame, bootstyle="secondary")
patient_disease_entry.pack(pady=5)

# Add Button
add_patient_button = tb.Button(patient_frame, text="Add Patient", bootstyle="primary", command=add_patient)
add_patient_button.pack(pady=20)

# List Frame
patient_list_frame = tb.Frame(patient_frame, bootstyle="light")
patient_list_frame.pack(pady=10, fill="both", expand=True)

# -------------- View Patients Page -------------- #
def update_patient_list():
    for widget in patient_list_frame.winfo_children():
        widget.destroy()
    for patient in patients_data:
        # Create a frame for each patient's details
        patient_frame = tb.Frame(patient_list_frame, bootstyle="secondary", padding=10)
        patient_frame.pack(pady=5, fill=X)

        # Display patient details
        tb.Label(patient_frame, text=f"Name: {patient['name']}", font=("Segoe UI", 14)).pack(anchor="w", padx=10)
        tb.Label(patient_frame, text=f"Age: {patient['age']}", font=("Segoe UI", 14)).pack(anchor="w", padx=10)
        tb.Label(patient_frame, text=f"Gender: {patient['gender']}", font=("Segoe UI", 14)).pack(anchor="w", padx=10)
        tb.Label(patient_frame, text=f"Contact: {patient['contact']}", font=("Segoe UI", 14)).pack(anchor="w", padx=10)
        tb.Label(patient_frame, text=f"Disease: {patient['disease']}", font=("Segoe UI", 14)).pack(anchor="w", padx=10)



view_patient_frame = tb.Frame(app, bootstyle="light")
frames["View Patients"] = view_patient_frame

view_pt_title = tb.Label(view_patient_frame, text="👤 View Patients", font=("Segoe UI", 18))
view_pt_title.pack(pady=10)

patient_list_frame = tb.Frame(view_patient_frame, bootstyle="light")
patient_list_frame.pack(pady=10, fill="both", expand=True)

# When the "View Patients" page is shown, update the patient list
update_patient_list()


# -------------- Doctors Page -------------- #
def update_doctor_list():
    for widget in doctor_list_frame.winfo_children():
        widget.destroy()
    for doctor in doctors_data:
        doctor_frame = tb.Frame(doctor_list_frame, bootstyle="secondary", padding=10)
        doctor_frame.pack(pady=5, fill=X)

        # Display doctor details
        tb.Label(doctor_frame, text=f"Name: {doctor['name']}", font=("Segoe UI", 14)).pack(anchor="w", padx=10)
        tb.Label(doctor_frame, text=f"Specialty: {doctor['specialty']}", font=("Segoe UI", 14)).pack(anchor="w", padx=10)
        tb.Label(doctor_frame, text=f"Avatar: {doctor['avatar']}", font=("Segoe UI", 14)).pack(anchor="w", padx=10)


doctor_frame = tb.Frame(app, bootstyle="light")
frames["Doctors"] = doctor_frame

doctor_title = tb.Label(doctor_frame, text="🩺 Doctors", font=("Segoe UI", 18))
doctor_title.pack(pady=10)

# Creating canvas and scrollbar for the doctors section
doctor_canvas = tk.Canvas(doctor_frame)
doctor_scrollbar = ttk.Scrollbar(doctor_frame, orient="vertical", command=doctor_canvas.yview)
doctor_canvas.configure(yscrollcommand=doctor_scrollbar.set)

doctor_scrollable_frame = tb.Frame(doctor_canvas, bootstyle="light")
doctor_scrollable_frame.bind(
    "<Configure>", lambda e: doctor_canvas.configure(scrollregion=doctor_canvas.bbox("all"))
)

doctor_canvas.create_window((0, 0), window=doctor_scrollable_frame, anchor="nw")

doctor_scrollbar.pack(side="right", fill="y")
doctor_canvas.pack(side="left", fill="both", expand=True)

doctor_list_frame = doctor_scrollable_frame
update_doctor_list()


# -------------- Appointments Page -------------- #
def add_appointment():
    patient_name = appointment_patient_name.get()
    doctor_name = appointment_doctor_name.get()
    date = appointment_date.get()
    if patient_name and doctor_name and date:
        appointments_data.append({"patient": patient_name, "doctor": doctor_name, "date": date})
        appointment_patient_name.delete(0, tk.END)
        appointment_doctor_name.delete(0, tk.END)
        appointment_date.delete(0, tk.END)
        update_appointment_list()


def update_appointment_list():
    for widget in appointment_list_frame.winfo_children():
        widget.destroy()
    for appointment in appointments_data:
        tb.Label(appointment_list_frame,
                 text=f"Patient: {appointment['patient']} - Doctor: {appointment['doctor']} - Date: {appointment['date']}",
                 font=("Segoe UI", 14)).pack(pady=5)


appt_frame = tb.Frame(app, bootstyle="light")
frames["Appointments"] = appt_frame

appt_title = tb.Label(appt_frame, text="📅 Appointments", font=("Segoe UI", 18))
appt_title.pack(pady=10)

appointment_patient_name_label = tb.Label(appt_frame, text="Patient Name", font=("Segoe UI", 12))
appointment_patient_name_label.pack(pady=5)

appointment_patient_name = tb.Entry(appt_frame, bootstyle="secondary")
appointment_patient_name.pack(pady=5)

appointment_doctor_name_label = tb.Label(appt_frame, text="Doctor Name", font=("Segoe UI", 12))
appointment_doctor_name_label.pack(pady=5)

appointment_doctor_name = tb.Entry(appt_frame, bootstyle="secondary")
appointment_doctor_name.pack(pady=5)

appointment_date_label = tb.Label(appt_frame, text="Appointment Date", font=("Segoe UI", 12))
appointment_date_label.pack(pady=5)

appointment_date = tb.Entry(appt_frame, bootstyle="secondary")
appointment_date.pack(pady=5)

add_appointment_button = tb.Button(appt_frame, text="Add Appointment", bootstyle="primary", command=add_appointment)
add_appointment_button.pack(pady=20)

appointment_list_frame = tb.Frame(appt_frame, bootstyle="light")
appointment_list_frame.pack(pady=10, fill="both", expand=True)


# -------------- Billing Page -------------- #
# Global list to store bills
bills_data = []

def add_bill():
    patient_name = bill_patient_name.get()
    amount = bill_amount.get()
    if patient_name and amount:
        bill_data = {"patient": patient_name, "amount": amount}
        bills_data.append(bill_data)  # ✅ Use bills_data, not appointments_data
        bill_patient_name.delete(0, tk.END)
        bill_amount.delete(0, tk.END)
        update_bill_list()

def update_bill_list():
    for widget in bill_list_frame.winfo_children():
        widget.destroy()
    for bill in bills_data:  # ✅ Use bills_data here
        tb.Label(bill_list_frame, text=f"Patient: {bill['patient']} - Amount: ₹{bill['amount']}",
                 font=("Segoe UI", 14)).pack(pady=5)

# Frame for Billing
bill_frame = tb.Frame(app, bootstyle="light")
frames["Billing"] = bill_frame

bill_title = tb.Label(bill_frame, text="💳 Billing", font=("Segoe UI", 18))
bill_title.pack(pady=10)

bill_patient_name_label = tb.Label(bill_frame, text="Patient Name", font=("Segoe UI", 12))
bill_patient_name_label.pack(pady=5)

bill_patient_name = tb.Entry(bill_frame, bootstyle="secondary")
bill_patient_name.pack(pady=5)

bill_amount_label = tb.Label(bill_frame, text="Amount", font=("Segoe UI", 12))
bill_amount_label.pack(pady=5)

bill_amount = tb.Entry(bill_frame, bootstyle="secondary")
bill_amount.pack(pady=5)

add_bill_button = tb.Button(bill_frame, text="Add Bill", bootstyle="primary", command=add_bill)
add_bill_button.pack(pady=20)

bill_list_frame = tb.Frame(bill_frame, bootstyle="light")
bill_list_frame.pack(pady=10, fill="both", expand=True)

# Show home frame
show_frame("Home")


# Fixing the issue with 'Staff' section

# -------------- Staff Page -------------- #
def update_staff_list():
    for widget in staff_list_frame.winfo_children():
        widget.destroy()
    for staff in staff_data:
        staff_frame = tb.Frame(staff_list_frame, bootstyle="secondary", padding=10)
        staff_frame.pack(pady=5, fill=X)

        # Display staff details
        tb.Label(staff_frame, text=f"Name: {staff['name']}", font=("Segoe UI", 14)).pack(anchor="w", padx=10)
        tb.Label(staff_frame, text=f"Role: {staff['role']}", font=("Segoe UI", 14)).pack(anchor="w", padx=10)


staff_frame = tb.Frame(app, bootstyle="light")
frames["Staff"] = staff_frame  # Ensure the 'Staff' frame is added to the frames dictionary

staff_title = tb.Label(staff_frame, text="👥 Staff", font=("Segoe UI", 18))
staff_title.pack(pady=10)

# Creating canvas and scrollbar for the staff section
staff_canvas = tk.Canvas(staff_frame)
staff_scrollbar = ttk.Scrollbar(staff_frame, orient="vertical", command=staff_canvas.yview)
staff_canvas.configure(yscrollcommand=staff_scrollbar.set)

staff_scrollable_frame = tb.Frame(staff_canvas, bootstyle="light")
staff_scrollable_frame.bind(
    "<Configure>", lambda e: staff_canvas.configure(scrollregion=staff_canvas.bbox("all"))
)

staff_canvas.create_window((0, 0), window=staff_scrollable_frame, anchor="nw")

staff_scrollbar.pack(side="right", fill="y")
staff_canvas.pack(side="left", fill="both", expand=True)

staff_list_frame = staff_scrollable_frame
update_staff_list()  # Update the staff list once the frame is created


# -------------- Updating 'show_frame' function -------------- #
def show_frame(name):
    for f in frames.values():
        f.place_forget()

    # Ensure the 'Staff' frame is added and shown correctly
    if name in frames:
        frames[name].place(relx=0.19, rely=0.08, relwidth=0.8, relheight=0.88)
        frames[name].tkraise()
    else:
        print(f"Frame '{name}' not found.")

# The rest of the code remains the same.

# -------------- Beds Page -------------- #

# Sample list of beds (could be loaded from a database or file)
beds_data = [{"bed_id": 1, "status": "Available"}, {"bed_id": 2, "status": "Occupied"}]


# Function to update the beds list in the UI
def update_beds_list():
    for widget in beds_list_frame.winfo_children():
        widget.destroy()

    for bed in beds_data:
        bed_frame = tb.Frame(beds_list_frame, bootstyle="secondary", padding=10)
        bed_frame.pack(pady=5, fill=X)

        tb.Label(bed_frame, text=f"Bed ID: {bed['bed_id']}", font=("Segoe UI", 14)).pack(anchor="w", padx=10)
        tb.Label(bed_frame, text=f"Status: {bed['status']}", font=("Segoe UI", 14)).pack(anchor="w", padx=10)


# Initialize Beds Page
beds_frame = tb.Frame(app, bootstyle="light")
frames["Beds"] = beds_frame  # Ensure the 'Beds' frame is added to the frames dictionary

beds_title = tb.Label(beds_frame, text="🛏️ Beds", font=("Segoe UI", 18))
beds_title.pack(pady=10)

# Creating canvas and scrollbar for the beds section
beds_canvas = tk.Canvas(beds_frame)
beds_scrollbar = ttk.Scrollbar(beds_frame, orient="vertical", command=beds_canvas.yview)
beds_canvas.configure(yscrollcommand=beds_scrollbar.set)

beds_scrollable_frame = tb.Frame(beds_canvas, bootstyle="light")
beds_scrollable_frame.bind(
    "<Configure>", lambda e: beds_canvas.configure(scrollregion=beds_canvas.bbox("all"))
)

beds_canvas.create_window((0, 0), window=beds_scrollable_frame, anchor="nw")

beds_scrollbar.pack(side="right", fill="y")
beds_canvas.pack(side="left", fill="both", expand=True)

beds_list_frame = beds_scrollable_frame
update_beds_list()  # Update the beds list once the frame is created


# Function to add a new bed
def add_bed(bed_id, status="Available"):
    new_bed = {"bed_id": bed_id, "status": status}
    beds_data.append(new_bed)
    update_beds_list()


# Function to remove a bed
def remove_bed(bed_id):
    global beds_data
    beds_data = [bed for bed in beds_data if bed["bed_id"] != bed_id]
    update_beds_list()


# Sample functions to add and remove beds
add_bed(3)  # Adding a bed with ID 3
remove_bed(2)  # Removing bed with ID 2


# -------------- Updating 'show_frame' function -------------- #
def show_frame(name):
    for f in frames.values():
        f.place_forget()

    # Ensure the 'Beds' frame is added and shown correctly
    if name in frames:
        frames[name].place(relx=0.19, rely=0.08, relwidth=0.8, relheight=0.88)
        frames[name].tkraise()
    else:
        print(f"Frame '{name}' not found.")


# The rest of the code remains the same.


# Run the app
app.mainloop()
