from flask import Flask, render_template, request, send_file
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit-form', methods=['POST'])
def submit_form():
    name = request.form['name']
    email = request.form['email']
    message = request.form['message']
    
    # Here you would typically save this information to a database
    # or send an email. For this example, we'll just print it.
    print(f"Received message from {name} ({email}): {message}")
    
    return 'OK', 200

@app.route('/download-resume')
def download_resume():
    # Replace 'path/to/your/resume.pdf' with the actual path to your resume file
    resume_path = 'path/to/your/resume.pdf'
    return send_file(resume_path, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)