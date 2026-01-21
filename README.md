# Email Spam Classifier using Machine Learning

## Overview
This project implements a machine learning–based email spam classification system.
The objective is to classify emails as **Spam** or **Ham (Not Spam)** using supervised
learning techniques with a strong emphasis on precision.

All model training, evaluation, and analysis are performed in a Jupyter Notebook.

---

## Dataset
- **Source:** Kaggle (Email Spam Classification Dataset)
- The dataset is **pre-vectorized**, where each email is represented using numerical
  word-frequency features.
- Since the data was already vectorized, no additional text preprocessing or feature
  extraction was required.

---

## Models Used
The following machine learning models were trained and evaluated:

- **Bernoulli Naive Bayes (BNB)**
- **Gaussian Naive Bayes (GNB)**
- **Multinomial Naive Bayes (MNB)**
- **Support Vector Machine (SVM)**

Model performance was compared using:
- Accuracy  
- Precision  
- Confusion Matrix  

Among all evaluated models, **Support Vector Machine (SVM)** demonstrated the best
overall precision and was selected as the final model.

---

## Workflow
1. Dataset loading and inspection  
2. Train–test split  
3. Model training  
4. Model evaluation using standard classification metrics  
5. Final model selection and serialization using Pickle  

---

## Technologies Used

### Programming Language
- **Python** – Core language used for implementing the complete machine learning workflow.

### Machine Learning & Evaluation
- **Scikit-learn** – Used for implementing Naive Bayes variants and Support Vector Machine (SVM),
  performing train–test splits, and evaluating models using accuracy, precision, and
  confusion matrices.

### Data Handling
- **Pandas** – Used for dataset loading and data manipulation.  
- **NumPy** – Used for numerical operations and array handling.

### Data Visualization
- **Matplotlib**
- **Seaborn**  
Used for plotting confusion matrices and visual comparison of model performance.

### Development Environment
- **Google Colab** – Cloud-based Jupyter Notebook environment used for development,
  training, and evaluation.

---

## Model Persistence
The final trained **SVM model** was saved using Python’s `pickle` module as
`spam_classifier.pkl`.  
This allows the trained model to be reused later without retraining.

---

## Repository Contents
- `Email_Spam_Detection.ipynb` – Main notebook containing data analysis, model training,
  and evaluation  
- `spam_classifier.pkl` – Serialized trained SVM model  
- `requirements.txt` – Python dependencies  
- `PPT/` – Project presentation files  

---

## Conclusion
This project demonstrates the effectiveness of classical machine learning algorithms
for email spam classification. Through comparative evaluation, SVM was identified as
the most suitable model due to its higher precision and reliable generalization
performance.

---

*This project was developed for academic and learning purposes.*
