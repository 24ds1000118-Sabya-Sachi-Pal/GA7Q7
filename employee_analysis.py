# employee_analysis.py
# Author: 24ds1000118@ds.study.iitm.ac.in

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# -------------------------------
# 1. Load Employee Data
# -------------------------------
data = """employee_id,department,region,performance_score,years_experience,satisfaction_rating
EMP001,Marketing,North America,94.77,12,3.5
EMP002,Sales,North America,69.99,2,4
EMP003,Operations,Africa,65.12,8,4.7
EMP004,Finance,Africa,62.69,15,3.5
EMP005,Operations,Asia Pacific,85.06,4,3.2
EMP006,R&D,Europe,91.25,10,4.6
EMP007,R&D,Asia Pacific,87.40,6,4.8
EMP008,Sales,North America,72.55,3,3.9
EMP009,Marketing,Europe,78.30,7,4.1
EMP010,R&D,North America,88.90,5,4.5
"""

# Load into pandas
from io import StringIO
df = pd.read_csv(StringIO(data))

# -------------------------------
# 2. Frequency Count for R&D
# -------------------------------
rd_count = df[df['department'] == 'R&D'].shape[0]
print("Frequency count for R&D department:", rd_count)

# -------------------------------
# 3. Create Histogram of Departments
# -------------------------------
plt.figure(figsize=(8,6))
sns.histplot(df['department'], discrete=True, color="skyblue", edgecolor="black")
plt.title("Distribution of Employees Across Departments")
plt.xlabel("Department")
plt.ylabel("Frequency")

# -------------------------------
# 4. Save the visualization
# -------------------------------
# Save as PNG image
plt.savefig("employee_department_analysis.png", dpi=300, bbox_inches='tight')

# Also create a simple HTML file with the image embedded
html_content = f"""
<!DOCTYPE html>
<html>
<head>
    <title>Employee Department Analysis</title>
    <style>
        body {{ font-family: Arial, sans-serif; margin: 40px; }}
        .container {{ max-width: 800px; margin: 0 auto; }}
        .result {{ background-color: #f0f0f0; padding: 20px; margin: 20px 0; border-radius: 5px; }}
        img {{ max-width: 100%; height: auto; }}
    </style>
</head>
<body>
    <div class="container">
        <h1>Employee Department Analysis</h1>
        <div class="result">
            <h2>R&D Department Frequency Count</h2>
            <p>Number of employees in R&D department: <strong>{rd_count}</strong></p>
        </div>
        <div class="result">
            <h2>Distribution of Employees Across Departments</h2>
            <img src="employee_department_analysis.png" alt="Department Distribution Chart">
        </div>
    </div>
</body>
</html>
"""

with open("employee_department_analysis.html", "w") as f:
    f.write(html_content)

print("✅ Visualization saved as employee_department_analysis.png")
print("✅ Analysis report saved as employee_department_analysis.html")
