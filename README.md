# **Drug Prediction Using Machine Learning**

## **Overview**
This project predicts the most suitable drug for a patient based on their medical attributes like age, sex, blood pressure, and cholesterol levels. A Decision Tree Classifier powers the predictions, and a Streamlit-based interface makes it user-friendly.

---

## **Features**
- Predicts drug recommendations based on patient attributes.
- Interactive and easy-to-use Streamlit interface.
- Visualizes the decision tree logic and data insights.

---

## **Technologies Used**
- **Python**: Core language.
- **Pandas, NumPy**: Data preprocessing.
- **Scikit-learn**: Machine learning.
- **Streamlit**: User interface.
- **Matplotlib**: Visualizations.

---

## **Installation**
1. Clone the repository:
   ```bash
   git clone https://github.com/rishikasharma11/drug-prediction.git
   cd drug-prediction

2. Install dependencies:
   ```bash
   pip install -r requirements.txt

3. Run the application:
   ```bash
   streamlit run app.py

4. Open your browser and navigate to:
   ```bash
   http://localhost:8501

---

## **Usage**
1. Launch the Streamlit app.
2. Input the following patient details:
    - **Age**: Patient's age.
    - **Sex**: Select Male or Female.
    - **Blood Pressur**: Choose Low, Normal, or High.
    - **Cholesterol**: Choose Normal or High.
    - **Na_to_K**: Provide the Sodium-to-Potassium ratio.
3. Click the Predict button to get the recommended drug.
4. Explore the visualized decision tree logic for insights.

