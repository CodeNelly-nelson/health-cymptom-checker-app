from flask import Flask, render_template, request, redirect, url_for
import json

app = Flask(__name__)

# Load knowledge base from file.
with open('knowledge_base.json', 'r') as file:
    knowledge_base = json.load(file)

# Support both "conditions" and "diseases" keys.
if "conditions" in knowledge_base:
    conditions = knowledge_base["conditions"]
elif "diseases" in knowledge_base:
    conditions = knowledge_base["diseases"]
else:
    conditions = []

# Load follow-up questions if present.
follow_up_questions = knowledge_base.get("follow_up_questions", {})

def extract_symptom_list():
    """Extract a unique, sorted list of symptoms from the knowledge base."""
    symptoms_set = set()
    for condition in conditions:
        cond_symptoms = condition.get('symptoms', {})
        if isinstance(cond_symptoms, dict):
            symptoms_set.update([s.lower() for s in cond_symptoms.keys()])
        elif isinstance(cond_symptoms, list):
            symptoms_set.update([s.lower() for s in cond_symptoms])
    return sorted(list(symptoms_set))

@app.route('/', methods=['GET'])
def index():
    """Render the input page with demographics and symptom selection."""
    symptom_list = extract_symptom_list()
    return render_template('index.html', symptom_list=symptom_list)

@app.route('/analyze', methods=['POST'])
def analyze():
    """Process the submitted form, analyze the symptoms, and render the results page."""
    # Retrieve the hidden JSON string containing the selected symptoms.
    symptoms_json = request.form.get('symptoms_json', '[]')
    try:
        user_symptoms = json.loads(symptoms_json)
    except Exception:
        user_symptoms = []
    user_symptoms = [sym.strip() for sym in user_symptoms if sym.strip()]
    
    # Retrieve demographic information.
    user_age = request.form.get('userAge', None)
    user_sex = request.form.get('userSex', None)
    
    # Initialize scores for each condition.
    condition_scores = {}
    for condition in conditions:
        condition_scores[condition['name']] = 0

    # 1. Basic scoring: count matching symptoms.
    for symptom in user_symptoms:
        for cond in conditions:
            cond_symptoms = cond.get('symptoms', {})
            if isinstance(cond_symptoms, dict):
                weight = cond_symptoms.get(symptom, 0)
            elif isinstance(cond_symptoms, list):
                sym_list = [s.lower() for s in cond_symptoms]
                weight = 1 if symptom in sym_list else 0
            else:
                weight = 0
            condition_scores[cond['name']] += weight

    # 2. Personalized adjustment: Increase score for some conditions if age >= 65.
    try:
        age = int(user_age)
        if age >= 65:
            if "Influenza (Flu)" in condition_scores:
                condition_scores["Influenza (Flu)"] += 1
            if "COVID-19" in condition_scores:
                condition_scores["COVID-19"] += 1
    except (ValueError, TypeError):
        pass

    # Build results list.
    results = []
    for cond in conditions:
        name = cond['name']
        score = condition_scores[name]
        if score > 0:
            # Remove advice from the results; only treatment info is kept.
            treatment = cond.get('treatment', 'No treatment info available')
            results.append({
                "name": name,
                "score": score,
                "treatment": treatment,
                "follow_up_needed": []  # For future follow-up questions if needed.
            })
    # Sort results by descending score.
    results.sort(key=lambda x: x['score'], reverse=True)
    
    # Convert raw scores to percentage likelihood relative to highest score.
    if results:
        max_score = max(result["score"] for result in results)
        for r in results:
            ratio = r["score"] / max_score
            if ratio >= 0.75:
                r["strength"] = "STRONG match"
            elif ratio >= 0.4:
                r["strength"] = "MODERATE match"
            else:
                r["strength"] = "FAIR match"
            # Example: Add a follow-up question for Influenza if applicable.
            if "Influenza" in r["name"]:
                r["follow_up_needed"].append("How severe are your flu symptoms? (Mild, Moderate, Severe)")
    else:
        results = []

    return render_template('results.html', results=results)

@app.route('/close')
def close():
    """Render a simple closing page."""
    return render_template('close.html')

if __name__ == '__main__':
    app.run(debug=True)
