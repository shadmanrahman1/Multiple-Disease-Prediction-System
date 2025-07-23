# 🏥 Multiple Disease Prediction System

A comprehensive machine learning-powered web application that predicts the likelihood of three major diseases: **Diabetes**, **Heart Disease**, and **Parkinson's Disease**. Built with Streamlit and powered by trained ML models for accurate health predictions.

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Streamlit](https://img.shields.io/badge/Streamlit-1.0+-red.svg)
![Scikit-learn](https://img.shields.io/badge/Scikit--learn-Latest-orange.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)

## 🌟 Features

### 🩺 Disease Prediction Modules
- **Diabetes Prediction**: Predicts diabetes risk based on health metrics like glucose levels, BMI, blood pressure, etc.
- **Heart Disease Prediction**: Assesses cardiovascular health using various cardiac indicators
- **Parkinson's Disease Prediction**: Analyzes voice recordings data to detect Parkinson's disease

### 🎯 Key Highlights
- **Interactive Web Interface**: User-friendly Streamlit-based GUI
- **Real-time Predictions**: Instant results with confidence scores
- **Multiple Input Validation**: Error handling for invalid inputs
- **Organized UI**: Sectioned input fields for better user experience
- **Responsive Design**: Works on desktop and mobile devices

## 🏗️ Project Structure

```
Multiple_Disease_prediction/
├── 📁 Diabetes/
│   ├── diabetes_app_streamlit.py          # Standalone diabetes prediction app
│   ├── Diabetes_EDA.ipynb                 # Exploratory Data Analysis
│   ├── Diabetes_prediction.ipynb          # Model training notebook
│   ├── diabetes_predictive_system.py      # Core prediction logic
│   ├── diabetes_trained_model.sav         # Trained diabetes model
│   └── diabetes.csv                       # Training dataset
├── 📁 Heart/
│   ├── heart_disease_data.csv             # Heart disease dataset
│   ├── heart_disease_EDA.ipynb            # Exploratory Data Analysis
│   ├── heart_disease_prediction.ipynb     # Model training notebook
│   └── heart_trained_model.sav            # Trained heart disease model
├── 📁 Parkinson/
│   ├── parkinson_disease_prediction.ipynb # Model training notebook
│   ├── parkinson_EDA.ipynb                # Exploratory Data Analysis
│   ├── parkinson_trained_model.sav        # Trained Parkinson's model
│   ├── parkinsons.data                    # Training dataset
│   └── parkinsons.names                   # Dataset description
├── 📁 system/
│   ├── app.py                             # Main Streamlit application
│   ├── diabetes_trained_model.sav         # Model files
│   ├── heart_trained_model.sav
│   └── parkinson_trained_model.sav
└── README.md                              # Project documentation
```

## 🚀 Quick Start

### Prerequisites
- Python 3.8 or higher
- pip package manager

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/Multiple_Disease_prediction.git
   cd Multiple_Disease_prediction
   ```

2. **Install required packages**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application**
   ```bash
   cd system
   streamlit run app.py
   ```

4. **Open your browser**
   - The app will automatically open at `http://localhost:8501`

## 📋 Usage Guide

### 🩺 Diabetes Prediction
**Required Inputs:**
- Number of Pregnancies
- Glucose Level
- Blood Pressure
- Skin Thickness
- Insulin Level
- BMI (Body Mass Index)
- Diabetes Pedigree Function
- Age

### ❤️ Heart Disease Prediction
**Required Inputs:**
- Age, Sex, Chest Pain Type
- Resting Blood Pressure
- Serum Cholesterol Level
- Fasting Blood Sugar
- Resting ECG Results
- Maximum Heart Rate Achieved
- Exercise Induced Angina
- ST Depression
- Slope of Peak Exercise ST Segment
- Number of Major Vessels
- Thalassemia Test Result

### 🧠 Parkinson's Disease Prediction
**Voice Analysis Parameters:**
- **Fundamental Frequency**: MDVP:Fo(Hz), MDVP:Fhi(Hz), MDVP:Flo(Hz)
- **Jitter Measures**: MDVP:Jitter(%), MDVP:Jitter(Abs), MDVP:RAP, MDVP:PPQ, Jitter:DDP
- **Shimmer Measures**: MDVP:Shimmer, MDVP:Shimmer(dB), Shimmer:APQ3, Shimmer:APQ5, MDVP:APQ, Shimmer:DDA
- **Harmonics & Noise**: NHR, HNR
- **Nonlinear Measures**: RPDE, DFA, D2, PPE
- **Spectral Measures**: spread1, spread2

## 🔬 Machine Learning Models

### Model Performance
| Disease | Algorithm | Accuracy | Features |
|---------|-----------|----------|----------|
| Diabetes | Support Vector Machine | ~78% | 8 clinical features |
| Heart Disease | Random Forest | ~85% | 13 cardiac indicators |
| Parkinson's | SVM/Random Forest | ~90% | 22 voice features |

### Training Process
Each model was trained using:
1. **Data Preprocessing**: Cleaning, normalization, feature scaling
2. **Exploratory Data Analysis**: Statistical analysis and visualization
3. **Feature Engineering**: Selection of most relevant features
4. **Model Training**: Cross-validation and hyperparameter tuning
5. **Model Evaluation**: Performance metrics and validation

## 📊 Datasets

### Sources
- **Diabetes**: Pima Indians Diabetes Database
- **Heart Disease**: Cleveland Heart Disease Database
- **Parkinson's**: UCI ML Repository Parkinson's Dataset

### Data Quality
- All datasets have been preprocessed and cleaned
- Missing values handled appropriately
- Features scaled and normalized for optimal model performance

## 🛠️ Technologies Used

- **Frontend**: Streamlit, streamlit-option-menu
- **Backend**: Python, Scikit-learn
- **Data Processing**: Pandas, NumPy
- **Visualization**: Matplotlib, Seaborn
- **Model Persistence**: Pickle
- **Development**: Jupyter Notebooks

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

### Development Setup
1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- UCI Machine Learning Repository for datasets
- Streamlit team for the amazing framework
- Scikit-learn contributors
- Healthcare professionals who validated the approach

---

⭐ **Star this repository if you found it helpful!**

> **Disclaimer**: This application is for educational and research purposes only. It should not be used as a substitute for professional medical advice, diagnosis, or treatment. Always consult with qualified healthcare professionals for medical concerns.
