<<<<<<< HEAD
# HealthSymptomChecker
=======
# Health Symptom Checker Expert System

The Health Symptom Checker Expert System is a web-based tool that allows users to enter their symptoms along with basic demographic data (age and sex) to receive a preliminary assessment of potential medical conditions. The system uses a static knowledge base and a simple rule-based scoring system to display treatment recommendations and follow-up questions. It is designed with a responsive, multi-page layout using Flask and Bootstrap.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Deployment](#deployment)
- [Project Structure](#project-structure)
- [Documentation](#documentation)
- [Contributing](#contributing)
- [License](#license)

## Features

- **Responsive Multi-Page Layout:** Uses a shared layout (`base.html`) for consistent headers, footers, and containers across all pages.
- **Dynamic Symptom Input:** Includes auto-suggest functionality for symptom entry, with add/remove capability.
- **Demographic Data Collection:** Collects age and sex for basic personalization of scoring.
- **Rule-Based Analysis:** Matches user-selected symptoms with a static knowledge base to generate a score for each condition.
- **Visual Match Indicators:** Displays match strength using a set of colored squares (e.g., STRONG match, MODERATE match, FAIR match).
- **Treatment Recommendations:** Shows treatment information for each condition (advice is removed per requirement).
- **Follow-Up Questions:** Displays additional follow-up questions if more information is needed.
- **Heroku Deployment Ready:** Includes a Procfile for deployment and uses Gunicorn as the production server.

## Installation

### Prerequisites

- Python 3.x
- pip (Python package installer)
- Git

### Setup Instructions

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/yourusername/HealthSymptomChecker.git
   cd HealthSymptomChecker

2. **Create and Activate a Virtual Environment:**

python3 -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate

3. **Install Dependencies:**

pip install -r requirements.txt


4. **Project Structure:**

HealthSymptomChecker/
├── app.py
├── knowledge_base.json
├── Procfile
├── requirements.txt
├── templates/
│   ├── base.html
│   ├── index.html
│   ├── results.html
│   └── close.html
└── static/
    ├── style.css
    └── logo.png

5. **Run the Application Locally:**

python app.py
Or
flask run

6. **Access the Application:**

Open your browser and navigate to http://127.0.0.1:5000.

7. **Using the App:**

Enter your age and select your sex.
In the symptom input field, type a symptom (e.g., "headache") and choose from the auto-suggest list.
Click the "Add Symptom" button to add the symptom to your list. You can remove any symptom by clicking its "Remove" button.
Once you have selected your symptoms, click the "Analyze Symptoms" button.
The results page will display possible conditions, each with:
A visual match indicator (colored squares).
A match strength label (e.g., STRONG match).
Treatment recommendations.
Any additional follow-up questions if needed.
Use the "New Search" button to clear your selections and start over, or "Close Program" to exit.

8. **Deployment**
Deploying to Heroku
Ensure You Have the Heroku CLI Installed and Are Logged In:
heroku login

9. **Create a Heroku App:**

heroku create your-app-name
Ensure Your Procfile Contains:
web: gunicorn app:app


10. Push Your Code to Heroku:

git push heroku main
Scale the Web Dyno:
heroku ps:scale web=1

11. Open Your App:
heroku open
Project Structure

HealthSymptomChecker/
├── app.py                # Flask application
├── knowledge_base.json   # Static JSON file with conditions, symptoms, treatment, and follow-up questions
├── Procfile              # For Heroku deployment
├── requirements.txt      # Python dependencies
├── templates/            # HTML templates
│   ├── base.html         # Shared layout
│   ├── index.html        # Input page
│   ├── results.html      # Results page
│   └── close.html        # Closing page
└── static/               # Static assets (CSS, images, JS)
    ├── style.css         # Custom CSS
    └── logo.png          # Favicon/logo
    
Documentation
User Manual: Detailed instructions on how to use the system.
System Documentation: Describes the system architecture, design decisions, and limitations.
Contributing
If you'd like to contribute, please fork this repository and submit a pull request with your changes. Follow standard coding practices and include tests and documentation as needed.

>>>>>>> aaec236 (version 1.0 commit for Heroku deployment)
