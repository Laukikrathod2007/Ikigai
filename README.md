# 🌸 Ikigai  
### *Mental Health & Productivity Companion for Students*

Ikigai is a **web-based, preventive well-being platform** designed to help students understand the balance between their **mental health and productivity** using daily habit data and the Ikigai philosophy.

Rather than reacting after burnout or academic failure, this system focuses on **early awareness, self-reflection, and sustainable routines** — in an ethical, explainable, and non-medical way.

---

## 🚨 Problem Statement

Students’ mental health challenges often remain unnoticed until they escalate into:
- Burnout  
- Chronic stress  
- Anxiety  
- Academic decline  

Most existing solutions are:
- Reactive instead of preventive  
- Medicalized rather than student-friendly  
- Disconnected from everyday routines  

There is a need for a **simple, habit-based awareness system** that fits naturally into a student’s daily life.

---

## 💡 Proposed Solution

Ikigai analyzes **daily behavioral inputs** such as:

- 🛌 Sleep duration  
- 📚 Study hours  
- 📱 Screen time  
- 🏃 Physical activity  
- 😌 Self-reported mood  

Using **data science and machine learning**, the system:
- Estimates **stress risk**
- Calculates **productivity**
- Visualizes **Ikigai balance**
- Provides **personalized improvement suggestions**

⚠️ *The system is not a medical diagnostic tool.*

---

## 🎯 Objectives

- Identify early signs of stress and burnout  
- Encourage healthier and more balanced routines  
- Translate Ikigai philosophy into measurable indicators  
- Ensure transparency, explainability, and ethical design  

---

## 🧠 Ikigai in This Project

Ikigai traditionally represents balance between four aspects of life.  
In this system, they are mapped to measurable behaviors:

| Ikigai Pillar | Interpretation in System |
|--------------|--------------------------|
| ❤️ What you love | Mood & physical activity |
| 🎓 What you are good at | Study consistency |
| 🌍 What you need | Sleep quality & low stress |
| 💼 What gives value | Productivity score |

This allows students to understand **why** their routine feels imbalanced — not just *how stressed* they are.

---

## ⚙️ System Architecture


### Flow Explanation
1. Student enters daily habit data through the web interface  
2. Frontend sends data as JSON to the Flask backend  
3. Backend:
   - Normalizes inputs
   - Calculates stress, productivity, and Ikigai scores
   - Applies ML model with safety rules  
4. Results and insights are visualized on the dashboard  

---

## 📊 Scoring Methodology (Explainable & Safe)

### 🔹 Layer 1: Normalization (0–100 Scale)

Different inputs (hours, minutes, ratings) are converted into a common scale to ensure fairness and interpretability.

- Optimal sleep → higher score  
- Excessive screen time → lower score  
- Better mood → higher score  

---

### 🔹 Layer 2: Weighted Scoring

Not all habits affect mental health equally.

- **Stress Score** emphasizes sleep and mood  
- **Productivity Score** emphasizes study and rest  
- **Ikigai Score** represents overall balance  

Scores are calculated using transparent, rule-based formulas.

---

### 🔹 Layer 3: Machine Learning with Safety Rules

A machine learning model (Logistic Regression / Decision Tree) supports pattern detection.

**Safety overrides ensure risk is never underestimated**, for example:
- Extremely low sleep or mood always increases stress level  

This guarantees ethical and responsible output.

---

## 🖥️ Key Features

- Simple daily habit input  
- Stress risk classification (Low / Medium / High)  
- Productivity scoring  
- Ikigai balance visualization  
- Personalized routine suggestions  
- Fully explainable, non-diagnostic design  

---

## 🛠️ Technology Stack

**Frontend**
- React  
- Tailwind CSS  

**Backend**
- Flask (Python)  

**Machine Learning**
- Pandas  
- Scikit-learn  

**Data**
- Synthetic CSV dataset  

**Visualization**
- Chart.js / Recharts  

---

## 👤 Target Users

- College and university students (18–25 years)  
- Students facing academic pressure or high screen usage  

---

## 🚀 Future Scope

- Real-time habit tracking  
- Long-term personalized recommendations  
- Integration with wearable health data  
- Anonymous, college-level stress analytics  

---

## ⚖️ Ethical Disclaimer

This application **does not diagnose mental health conditions**.

It is intended only for:
- Awareness  
- Self-reflection  
- Preventive well-being support  

For medical or psychological concerns, professional guidance should be sought.

---

## 🏁 Conclusion

Ikigai demonstrates how **responsible data science and human-centered design** can support student well-being proactively.

By combining daily habit analysis with the Ikigai framework, the platform encourages students to view **productivity and mental health as interconnected**, not conflicting goals.

The project provides a scalable foundation for future educational and wellness-focused platforms.

---

⭐ *Built for awareness, balance, and sustainable growth.*
