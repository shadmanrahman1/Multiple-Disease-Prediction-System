# 🏥 Multiple Disease Prediction System

A machine learning web application that predicts the likelihood of **Diabetes**, **Heart Disease**, and **Parkinson's Disease** using Streamlit.

## ✨ Features

- **Diabetes Prediction**: Based on health metrics like glucose levels, BMI, blood pressure
- **Heart Disease Prediction**: Uses cardiac indicators and health data
- **Parkinson's Disease Prediction**: Analyzes voice recordings data
- Interactive web interface with real-time predictions
- Input validation and error handling

## 🚀 Quick Start

1. **Clone the repository**
   ```bash
   git clone https://github.com/shadmanrahman1/Multiple-Disease-Prediction-System.git
   cd Multiple-Disease-Prediction-System
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application**
   ```bash
   cd system
   streamlit run app.py
   ```

4. **Open your browser** at `http://localhost:8501`

## 📋 Usage

### Diabetes Prediction
Enter health metrics like:
- Pregnancies, Glucose Level, Blood Pressure
- Skin Thickness, Insulin Level, BMI
- Diabetes Pedigree Function, Age

### Heart Disease Prediction
Enter cardiac indicators like:
- Age, Sex, Chest Pain Type
- Blood Pressure, Cholesterol Level
- ECG Results, Heart Rate, etc.

### Parkinson's Disease Prediction
Enter voice analysis parameters like:
- Fundamental Frequency measures
- Jitter and Shimmer values
- Harmonics and Noise ratios
- Nonlinear complexity measures

## 🛠️ Tech Stack

- **Frontend**: Streamlit
- **ML Models**: Scikit-learn
- **Data Processing**: Pandas, NumPy
- **Model Storage**: Pickle

## 📊 Model Performance

| Disease | Algorithm | Accuracy |
|---------|-----------|----------|
| Diabetes | SVM | ~78% |
| Heart Disease | Random Forest | ~85% |
| Parkinson's | SVM | ~90% |

## 📝 License

MIT License - see [LICENSE](LICENSE) file.

## 🙏 Acknowledgments

- UCI Machine Learning Repository for datasets
- Streamlit team for the framework
- Scikit-learn contributors

---

⚠️ **Disclaimer**: For educational purposes only. Not a substitute for professional medical advice.
