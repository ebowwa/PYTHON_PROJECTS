from core.resume_generator import ResumePDF, load_data  # Corrected import statement

# Load the resume data from a JSON file
data = load_data('data/resume.json')

# Create a ResumePDF instance and generate the PDF
resume_pdf = ResumePDF(data)
resume_pdf.generate_pdf()