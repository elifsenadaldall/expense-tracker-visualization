# Expense Tracker with Visualization

## **Overview**
The Expense Tracker with Visualization is a Python-based web application designed to help users effectively manage their income and expenses. With features such as data storage, filtering, and interactive visualizations, this project aims to make financial management simple and insightful. The application allows users to input transactions, filter data by date, and visualize spending patterns through charts and graphs.

---

## **Author**
- **Elif Sena Daldal**

---

## **Key Features**
- **Add Income and Expenses**: Easily record financial transactions.
- **Interactive Visualizations**:
  - Pie Chart for category-based spending.
  - Line Graph for expense trends over time.
  - Bar Chart for income distribution by category.
- **Data Filtering**: View financial data by year and month.
- **User-Friendly Interface**: Built using Streamlit for quick and easy navigation.

---

## **Technologies Used**
- **Python 3.9**: Core programming language.
- **Pandas**: Data handling and analysis.
- **Plotly**: Interactive data visualizations.
- **Streamlit**: Web application framework.

---

## **How to Run the Project**

### Prerequisites
Ensure you have Python 3.9 installed on your system.

### Steps
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/Expense-Tracker-Visualization.git
   cd Expense-Tracker-Visualization
   ```

2. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Application**:
   ```bash
   streamlit run tracker.py
   ```

4. **Open the App**:
   - The application will automatically open in your default web browser.
   - If not, copy and paste the URL provided in the terminal (e.g., `http://localhost:8501`) into your browser.

### Additional Notes
- Ensure the `expenses.csv` file is in the same directory as `tracker.py`.
- Modify the `expenses.csv` file to suit your initial data needs.

---

## **Results and Insights**
The Expense Tracker effectively visualized financial data, enabling users to:
- Identify major spending categories like Rent and Food.
- Observe expense trends over time to identify patterns and spikes.
- Analyze income sources for better financial planning.

---

## **Challenges and Solutions**
### **Challenges**
- Managing inconsistent date formats in CSV files.
- Designing intuitive visualizations.
- Handling missing or malformed data entries.

### **Solutions**
- Used robust error-handling techniques for date parsing.
- Leveraged Plotly for dynamic and user-friendly visualizations.
- Implemented data validation checks to handle incomplete or incorrect entries.

---

## **Future Enhancements**
1. **Multi-Currency Support**: Add support for transactions in multiple currencies with automatic conversion.
2. **Mobile Application**: Develop a mobile-friendly version for accessibility on smartphones.
3. **Budget Planning**: Enable users to set budgets and get alerts for overspending.
4. **AI-Driven Insights**: Incorporate machine learning to provide predictive analytics and personalized financial recommendations.

---

## **References**
1. [Python Documentation](https://docs.python.org/3.11/)
2. [Pandas Documentation](https://pandas.pydata.org/pandas-docs/stable/user_guide/)
3. [Plotly Documentation](https://plotly.com/python/plotly-express/)
4. [Streamlit Documentation](https://docs.streamlit.io/)

---

## **License**
This project is licensed under the MIT License - see the LICENSE file for details.

---



