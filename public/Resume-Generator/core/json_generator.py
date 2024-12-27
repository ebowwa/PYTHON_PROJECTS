import json
import tkinter as tk
from tkinter import ttk

# Define the initial JSON data
json_data = {
    "name": "Insert_Name_Here",
    "contact_info": {
        "email": "example@email.com",
        "phone": "123-456-7890",
        "linkedin": "linkedin.com/in/example"
    },
    "summary": "A brief summary of your background and qualifications.",
    "experiences": [
        {
            "title": "Job Title",
            "company": "Company Name",
            "location": "City, State",
            "dates": "Start Date - End Date",
            "description": "Describe your responsibilities and achievements in this role."
        }
    ],
    "skills": {
        "skill_1": "Skill 1",
        "skill_2": "Skill 2",
        "skill_3": "Skill 3"
    },
    "education": [
        {
            "institution": "University Name",
            "degree": "Degree Name"
        },
        {
            "institution": "School Name",
            "description": "Additional educational information."
        }
    ]
}

def save_json():
    global json_data
    json_data = {
        "name": name_entry.get() if name_entry.get() else "Insert_Name_Here",
        "contact_info": {
            "email": email_entry.get() if email_entry.get() else "example@email.com",
            "phone": phone_entry.get() if phone_entry.get() else "123-456-7890",
            "linkedin": linkedin_entry.get() if linkedin_entry.get() else "linkedin.com/in/example"
        },
        "summary": summary_text.get("1.0", tk.END).strip() if summary_text.get("1.0", tk.END).strip() else "A brief summary of your background and qualifications.",
        "experiences": [
            {
                "title": exp_title_entry.get() if exp_title_entry.get() else "Job Title",
                "company": exp_company_entry.get() if exp_company_entry.get() else "Company Name",
                "location": exp_location_entry.get() if exp_location_entry.get() else "City, State",
                "dates": exp_dates_entry.get() if exp_dates_entry.get() else "Start Date - End Date",
                "description": exp_description_text.get("1.0", tk.END).strip() if exp_description_text.get("1.0", tk.END).strip() else "Describe your responsibilities and achievements in this role."
            }
        ],
        "skills": {
            "skill_1": skill1_entry.get() if skill1_entry.get() else "Skill 1",
            "skill_2": skill2_entry.get() if skill2_entry.get() else "Skill 2",
            "skill_3": skill3_entry.get() if skill3_entry.get() else "Skill 3"
        },
        "education": [
            {
                "institution": edu1_institution_entry.get() if edu1_institution_entry.get() else "University Name",
                "degree": edu1_degree_entry.get() if edu1_degree_entry.get() else "Degree Name"
            },
            {
                "institution": edu2_institution_entry.get() if edu2_institution_entry.get() else "School Name",
                "description": edu2_description_text.get("1.0", tk.END).strip() if edu2_description_text.get("1.0", tk.END).strip() else "Additional educational information."
            }
        ]
    }

    with open("data/resume.json", "w") as f:
        json.dump(json_data, f, indent=4)

    print("JSON data saved to resume.json")

root = tk.Tk()
root.title("Resume Editor")

# Name
name_label = ttk.Label(root, text="Name:")
name_label.grid(row=0, column=0, padx=10, pady=10)
name_entry = ttk.Entry(root)
name_entry.grid(row=0, column=1, padx=10, pady=10)
name_entry.insert(0, "Insert_Name_Here")

# Contact Info
email_label = ttk.Label(root, text="Email:")
email_label.grid(row=1, column=0, padx=10, pady=10)
email_entry = ttk.Entry(root)
email_entry.grid(row=1, column=1, padx=10, pady=10)
email_entry.insert(0, "example@email.com")

phone_label = ttk.Label(root, text="Phone:")
phone_label.grid(row=2, column=0, padx=10, pady=10)
phone_entry = ttk.Entry(root)
phone_entry.grid(row=2, column=1, padx=10, pady=10)
phone_entry.insert(0, "123-456-7890")

linkedin_label = ttk.Label(root, text="LinkedIn:")
linkedin_label.grid(row=3, column=0, padx=10, pady=10)
linkedin_entry = ttk.Entry(root)
linkedin_entry.grid(row=3, column=1, padx=10, pady=10)
linkedin_entry.insert(0, "linkedin.com/in/example")

# Summary
summary_label = ttk.Label(root, text="Summary:")
summary_label.grid(row=4, column=0, padx=10, pady=10)
summary_text = tk.Text(root, height=3, width=30)
summary_text.grid(row=4, column=1, padx=10, pady=10)
summary_text.insert(tk.END, "A brief summary of your background and qualifications.")

# Experiences
exp_title_label = ttk.Label(root, text="Experience Title:")
exp_title_label.grid(row=5, column=0, padx=10, pady=10)
exp_title_entry = ttk.Entry(root)
exp_title_entry.grid(row=5, column=1, padx=10, pady=10)
exp_title_entry.insert(0, "Job Title")

exp_company_label = ttk.Label(root, text="Company:")
exp_company_label.grid(row=6, column=0, padx=10, pady=10)
exp_company_entry = ttk.Entry(root)
exp_company_entry.grid(row=6, column=1, padx=10, pady=10)
exp_company_entry.insert(0, "Company Name")

exp_location_label = ttk.Label(root, text="Location:")
exp_location_label.grid(row=7, column=0, padx=10, pady=10)
exp_location_entry = ttk.Entry(root)
exp_location_entry.grid(row=7, column=1, padx=10, pady=10)
exp_location_entry.insert(0, "City, State")

exp_dates_label = ttk.Label(root, text="Dates:")
exp_dates_label.grid(row=8, column=0, padx=10, pady=10)
exp_dates_entry = ttk.Entry(root)
exp_dates_entry.grid(row=8, column=1, padx=10, pady=10)
exp_dates_entry.insert(0, "Start Date - End Date")

exp_description_label = ttk.Label(root, text="Description:")
exp_description_label.grid(row=9, column=0, padx=10, pady=10)
exp_description_text = tk.Text(root, height=3, width=30)
exp_description_text.grid(row=9, column=1, padx=10, pady=10)
exp_description_text.insert(tk.END, "Describe your responsibilities and achievements in this role.")

# Skills
skill1_label = ttk.Label(root, text="Skill 1:")
skill1_label.grid(row=10, column=0, padx=10, pady=10)
skill1_entry = ttk.Entry(root)
skill1_entry.grid(row=10, column=1, padx=10, pady=10)
skill1_entry.insert(0, "Skill 1")

skill2_label = ttk.Label(root, text="Skill 2:")
skill2_label.grid(row=11, column=0, padx=10, pady=10)
skill2_entry = ttk.Entry(root)
skill2_entry.grid(row=11, column=1, padx=10, pady=10)
skill2_entry.insert(0, "Skill 2")

skill3_label = ttk.Label(root, text="Skill 3:")
skill3_label.grid(row=12, column=0, padx=10, pady=10)
skill3_entry = ttk.Entry(root)
skill3_entry.grid(row=12, column=1, padx=10, pady=10)
skill3_entry.insert(0, "Skill 3")

# Education
edu1_institution_label = ttk.Label(root, text="Education 1 Institution:")
edu1_institution_label.grid(row=13, column=0, padx=10, pady=10)
edu1_institution_entry = ttk.Entry(root)
edu1_institution_entry.grid(row=13, column=1, padx=10, pady=10)
edu1_institution_entry.insert(0, "University Name")

edu1_degree_label = ttk.Label(root, text="Education 1 Degree:")
edu1_degree_label.grid(row=14, column=0, padx=10, pady=10)
edu1_degree_entry = ttk.Entry(root)
edu1_degree_entry.grid(row=14, column=1, padx=10, pady=10)
edu1_degree_entry.insert(0, "Degree Name")

edu2_institution_label = ttk.Label(root, text="Education 2 Institution:")
edu2_institution_label.grid(row=15, column=0, padx=10, pady=10)
edu2_institution_entry = ttk.Entry(root)
edu2_institution_entry.grid(row=15, column=1, padx=10, pady=10)
edu2_institution_entry.insert(0, "School Name")

edu2_description_label = ttk.Label(root, text="Education 2 Description:")
edu2_description_label.grid(row=16, column=0, padx=10, pady=10)
edu2_description_text = tk.Text(root, height=3, width=30)
edu2_description_text.grid(row=16, column=1, padx=10, pady=10)
edu2_description_text.insert(tk.END, "Additional educational information.")

save_button = ttk.Button(root, text="Save", command=save_json)
save_button.grid(row=17, column=0, columnspan=2, padx=10, pady=10)

root.mainloop()