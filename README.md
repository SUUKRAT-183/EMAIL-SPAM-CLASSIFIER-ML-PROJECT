# EMAIL-SPAM-CLASSIFIER-ML-PROJECT

## Overview
This project implements a Machine Learning–based Email Spam Classification system.  
The model classifies emails as **Spam** or **Ham (Not Spam)** using supervised learning techniques.

The training and evaluation of models are performed in a Jupyter Notebook, and a simple Streamlit application is provided to demonstrate the classification workflow.

---

## Dataset
- Source: Kaggle (Email Spam Classification Dataset)
- The dataset used was **already pre-vectorized**, containing numerical features suitable for direct model training.
- No additional text vectorization was required during training.

---

## Models Used
The following machine learning models were trained and evaluated:
- Support Vector Machine (SVM)
- Gaussian Naive Bayes (GNB)
- Bernoulli Naive Bayes (BNB)
- Multinomial Naive Bayes (MNB)

Performance comparison was done using accuracy,precision and confusion matrices.

---

## Technologies Used

### Programming Language
- **Python**  
  The core language used for scripting the entire workflow, from data processing to model training and deployment.

---

### Machine Learning & Modeling
- **Scikit-learn**  
  Used to implement machine learning algorithms such as **Support Vector Machine (SVM)**, **Naive Bayes**, and **Random Forest**, perform train–test splits, and evaluate model performance using metrics like accuracy and confusion matrices.

---

### Data Manipulation & Analysis
- **Pandas**  
  Used for loading the dataset, creating data frames, and managing structured data.
- **NumPy**  
  Used for efficient numerical computations and handling multi-dimensional arrays.

---

### Data Visualization
- **Matplotlib / Seaborn**  
  Used to generate static plots and heatmaps (e.g., confusion matrices) to visualize and compare model performance.

---

### Development Environment
- **Google Colab**  
  A cloud-based Jupyter Notebook environment used for writing code, training models, and leveraging free CPU/GPU resources.

---

### Web Framework & Deployment
- **Streamlit**  
  Used to build an interactive web application (`app.py`) that allows users to input email text and receive real-time spam classification results.


## Working Model Images 

SPAM
<img width="1810" height="828" alt="Screenshot 2026-01-12 234326" src="https://github.com/user-attachments/assets/4fbd7b09-35c8-45fb-8a8a-e633e74c6b39" />

---

HAM
<img width="1846" height="810" alt="Screenshot 2026-01-12 234250" src="https://github.com/user-attachments/assets/b4a2914b-6e09-455e-b766-5240e4c85e6d" />
