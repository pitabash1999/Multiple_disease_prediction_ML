# Multi-Disease Prediction Web Application

![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=Streamlit&logoColor=white)
![Python](https://img.shields.io/badge/Python-3.12-blue?style=for-the-badge&logo=python)
![Machine Learning](https://img.shields.io/badge/Machine%20Learning-SVM-orange?style=for-the-badge)

A web-based application for predicting multiple diseases (Diabetes, Heart Disease, and Parkinson's Disease) using machine learning models built with Streamlit.

## Overview

This project develops a user-friendly web application that leverages machine learning to provide real-time predictions for three major health conditions:
- Diabetes prediction
- Heart disease prediction
- Parkinson's disease prediction
- Breast cancer classification

The application uses pre-trained Support Vector Machine (SVM) models that have been trained on diverse clinical datasets to deliver accurate predictions based on user-input medical data.

## Features

- **Intuitive Interface**: Simple and clean UI built with Streamlit
- **Multiple Disease Prediction**: Single application for three different disease predictions
- **Real-time Results**: Immediate prediction outputs based on user inputs
- **Machine Learning Models**: SVM-based models trained on clinical datasets
- **Performance Metrics**: Models evaluated using accuracy_score and other relevant metrics

## Technical Requirements

### Hardware
- Computer with 8 GB RAM
- Multi-core processor

### Software
- Python 3.12
- Spyder or Google Colab (for development)

### Libraries
The application uses the following Python libraries:
```
numpy
pandas
scikit-learn
streamlit
pickle
math
os
sys
streamlit_option_menu
```

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/multi-disease-prediction.git
cd multi-disease-prediction
```

2. Create and activate a virtual environment (recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

3. Install the required packages:
```bash
pip install -r requirements.txt
```

## Usage

1. Run the Streamlit application:
```bash
streamlit run app.py
```

2. The application will open in your default web browser

3. Navigate through the different disease prediction sections and input your data

4. View your prediction results instantly

## Project Structure

```
multi-disease-prediction/
├── models/               # Pre-trained machine learning models
├── datasets/             # Training datasets (if included)
├── app.py                # Main Streamlit application file
├── requirements.txt      # Python dependencies
└── README.md             # Project documentation
```

## Contributing

Contributions are welcome! Please fork the repository and create a pull request with your improvements.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- Streamlit for the amazing web application framework
- Scikit-learn for machine learning tools
- All dataset providers and researchers whose work made this possible

---

**Note**: This application is intended for preliminary screening purposes only and should not replace professional medical advice. Always consult with a healthcare provider for medical diagnoses.
