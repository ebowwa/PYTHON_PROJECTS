from flask import Flask, request, jsonify
import json

app = Flask(__name__)

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

@app.route('/save', methods=['POST'])
def save_json():
    """
    Save JSON data to resume.json

    Request JSON structure:
    {
        "name": "string",
        "contact_info": {
            "email": "string",
            "phone": "string",
            "linkedin": "string"
        },
        "summary": "string",
        "experiences": [
            {
                "title": "string",
                "company": "string",
                "location": "string",
                "dates": "string",
                "description": "string"
            }
        ],
        "skills": {
            "skill_1": "string",
            "skill_2": "string",
            "skill_3": "string"
        },
        "education": [
            {
                "institution": "string",
                "degree": "string"
            },
            {
                "institution": "string",
                "description": "string"
            }
        ]
    }
    """
    global json_data
    json_data = request.get_json()

    with open("data/resume.json", "w") as f:
        json.dump(json_data, f, indent=4)

    return jsonify({"message": "JSON data saved to resume.json"})

if __name__ == '__main__':
    app.run(debug=True)
