# 🌱 Ikigai-Based Mental Health & Productivity Correlator for Students

---

## 📌 Overview
Students’ mental health challenges often remain unnoticed until they escalate into burnout, anxiety, or academic failure. Most existing solutions are reactive, medicalized, or disconnected from students’ daily academic routines.

This project presents a **preventive, explainable, and ethical web-based system** that analyzes students’ everyday habits using data science and machine learning to provide early awareness of stress, productivity, and life balance through the **Ikigai framework**.

### ⚠️ Disclaimer
This system is **not a medical diagnostic tool**.  
It is intended solely for **awareness, self-reflection, and preventive well-being support**.

---

## 🎯 Objectives
1. Identify early stress and burnout patterns in students  
2. Encourage balanced routines using behavioral data  
3. Translate the Ikigai philosophy into measurable indicators  
4. Provide explainable, ethical, and preventive insights  

---

## 💡 Solution Approach
The system analyzes simple daily habit inputs:

- Sleep hours  
- Study hours  
- Screen time  
- Physical activity  
- Self-reported mood  

Using a **three-layer scoring methodology**, the platform:
- Normalizes raw behavioral data  
- Computes weighted stress and productivity scores  
- Applies machine learning as a supporting signal, reinforced with rule-based safety overrides  

The Ikigai framework — *What you love, What you are good at, What the world needs, and What you can be paid for* — is operationalized into measurable behavioral pillars, allowing students to visualize balance between mental well-being and academic effort.

---

## 🧮 Scoring Methodology (Explainable & Ethical)

### 🔹 Layer 1: Behavioral Normalization (0–100 Scale)
Raw inputs are converted into normalized scores so different units can be compared fairly.

- **Sleep Score**: Optimal sleep (7–8 hrs) scores highest  
- **Study Score**: Balanced study hours score higher than extremes  
- **Screen Time Score**: Inverted scoring to penalize overuse  
- **Physical Activity Score**: Rewards consistent movement  
- **Mood Score**: Scaled from self-reported mood (1–5)  

---

### 🔹 Layer 2: Stress & Productivity Analysis
Weighted scoring based on common psychological findings:

- Sleep and mood have higher influence than screen time  

Produces:
- **Stress Risk Score**  
- **Stress Level** (Low / Medium / High)  
- **Productivity Score**  

---

### 🔹 Layer 3: ML Validation & Safety Checks
A machine learning model (Decision Tree / Logistic Regression) is used **only as a supporting tool**.

To ensure ethical responsibility, **rule-based safety overrides** are applied:
- Very low sleep or mood never results in “Low stress”  
- Extreme patterns override ML predictions to prevent underestimation  
- Rule-based logic always has final authority over ML output  

---

## 🌸 Ikigai Balance Computation
The Ikigai philosophy is translated into four measurable pillars:

- **Love**: Mood + Physical activity  
- **Good At**: Study consistency  
- **Need**: Recovery balance (sleep vs stress)  
- **Value**: Productivity score  

The final **Ikigai Balance Score** reflects overall harmony between effort and well-being.

---

## 🛠️ Technology Stack
- **Frontend**: HTML, CSS, JavaScript, Dynamic UI with real-time API integration  
- **Backend**: Flask (Python)  
- **REST APIs**: `/predict`, `/ikigai`  
- **Machine Learning**: Pandas, Scikit-learn  
- **Data**: Synthetic CSV dataset (behavioral patterns)  

---

## 🧩 System Architecture

1. Student Input (Daily Habits)

2. Web Frontend (Form-based UI)

3. Flask Backend (REST APIs)

4. Behavior Normalization Engine

5. Stress & Productivity Scoring

6. ML Model (Support Only)

7. Rule-Based Ethical Overrides

8. Ikigai Balance Computation

9. Explainable Results Dashboard

Each stage is designed to be transparent, interpretable, and ethically responsible, ensuring users understand how outputs are generated.

---

## 🚀 Future Scope
- Real-time habit tracking instead of manual input  
- Personalized long-term well-being recommendations  
- Integration with wearable health and fitness devices  
- College-wide anonymous stress analytics dashboards  
- Longitudinal trend analysis across semesters  

---

## 👤 Target Users
- College and university students (18–25 years)  
- Students facing academic pressure, screen overuse, stress, or burnout risk  

---

## 🏁 Conclusion
The **Ikigai-Based Mental Health & Productivity Correlator for Students** demonstrates how **ethical, explainable, and preventive data science** can proactively support student well-being.

By focusing on **awareness rather than diagnosis**, and combining behavioral science with responsible machine learning, this project provides a scalable foundation for future educational and wellness platforms aimed at building sustainable and balanced student lifestyles.

---

## 🤝 Contributor
- **Prachi Patil** (@pracheyyy)


