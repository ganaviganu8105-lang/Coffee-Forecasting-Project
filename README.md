# Coffee-Forecasting-Project
Coffee Forecasting Project ☕
Data-Driven Forecasting & Peak Demand Prediction for Afficionado Coffee Roasters
📌 Project Overview
This project focuses on analyzing coffee sales transaction data and forecasting future customer demand using data analytics and time-series forecasting techniques.
The system helps businesses:
Predict future coffee demand
Analyze revenue trends
Identify peak business hours
Understand category-level product demand
Improve inventory and staff planning
The project was developed using Python, Pandas, Streamlit, and forecasting methodologies.
🎯 Objectives
Forecast hourly coffee demand
Predict daily revenue trends
Identify peak customer activity hours
Perform category-level demand analysis
Build an interactive Streamlit dashboard
Support data-driven business decision-making
🛠️ Technologies Used
Python
Pandas
NumPy
Streamlit
Scikit-learn
Time-Series Forecasting
Git & GitHub
📂 Project Structure
Plain text
Coffee-Forecasting-Project/
│
├── app/                    # Streamlit dashboard
├── data/
│   ├── raw/                # Raw dataset
│   ├── processed/          # Cleaned and processed data
│   └── forecast/           # Forecast outputs
│
├── notebooks/              # Jupyter notebooks
├── outputs/plots/          # Generated graphs and plots
├── src/                    # Source code files
│   ├── preprocessing.py
│   ├── time_series.py
│   ├── features.py
│   ├── models.py
│   ├── evaluation.py
│   └── peak_detection.py
│
├── requirements.txt
└── README.md
⚙️ Project Workflow
1. Data Preprocessing
Cleaned raw coffee sales data
Created datetime features
Generated revenue column
Handled missing values
2. Time-Series Construction
Hourly demand aggregation
Daily revenue aggregation
Category-level demand creation
3. Feature Engineering
Created:
Lag features
Rolling averages
Hour-based features
Day-of-week indicators
4. Forecasting Models
Implemented:
Naive Forecast Model
Moving Average Forecast Model
5. Model Evaluation
Evaluation metrics used:
MAE (Mean Absolute Error)
RMSE (Root Mean Square Error)
MAPE (Mean Absolute Percentage Error)
6. Dashboard Visualization
Interactive Streamlit dashboard includes:
Store-wise forecasting
Revenue analysis
Peak hours analysis
Category demand analysis
📊 Dashboard Features
✅ Store Selection
✅ Forecast Model Selection
✅ Hourly Demand Forecast
✅ Daily Revenue Forecast
✅ Peak Hours Analysis
✅ Category-Level Demand Analysis
📈 Key Insights
Morning hours show highest coffee demand
Coffee category contributes maximum sales
Revenue patterns fluctuate across time periods
Forecasting helps improve operational planning
🚀 How to Run the Project
Install Dependencies
Bash
pip install -r requirements.txt
Run Preprocessing
Bash
python src/preprocessing.py
Run Time-Series Processing
Bash
python src/time_series.py
Run Feature Engineering
Bash
python src/features.py
Run Forecasting Model
Bash
python src/models.py
Run Evaluation
Bash
python src/evaluation.py
Launch Streamlit Dashboard
Bash
streamlit run app/app.py
📌 Future Enhancements
ARIMA & Prophet forecasting models
Real-time analytics integration
Cloud deployment
Advanced machine learning models
Automated business recommendations
👩‍💻 Developed By
Ganavi
MCA – Presidency University
📄 License
This project is developed for academic and internship purposes.
