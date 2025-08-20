import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Your email (for verification)
email = "24ds1000118@ds.study.iitm.ac.in"

# Sample dataset (small version for demo, can expand to 100 rows)
data = {
    "employee_id": ["EMP001","EMP002","EMP003","EMP004","EMP005","EMP006","EMP007","EMP008","EMP009","EMP010"],
    "department": ["Marketing","Sales","Operations","Finance","Operations","R&D","R&D","Marketing","Sales","R&D"],
    "region": ["North America","North America","Africa","Africa","Asia Pacific","Asia Pacific","Europe","Europe","North America","Europe"],
    "performance_score": [94.77,69.99,65.12,62.69,85.06,77.45,90.12,55.32,70.44,82.99],
    "years_experience": [12,2,8,15,4,6,10,3,5,11],
    "satisfaction_rating": [3.5,4,4.7,3.5,3.2,4.1,4.8,2.9,3.7,4.5]
}

# Load into DataFrame
df = pd.DataFrame(data)

# Frequency count for R&D department
rd_count = df[df['department'] == 'R&D'].shape[0]
print("Frequency count for R&D department:", rd_count)

# Create histogram
plt.figure(figsize=(8, 6))
sns.countplot(data=df, x="department", palette="viridis")
plt.title("Department Distribution of Employees")
plt.xlabel("Department")
plt.ylabel("Count")

# Save plot as image
plt.savefig("department_histogram.png")

# Now embed both the plot and the email into an HTML file
with open("employee_department_analysis.html", "w") as f:
    f.write(f"""
    <html>
    <head><title>Employee Department Analysis</title></head>
    <body>
        <h1>Employee Performance Analysis</h1>
        <p><b>Email for verification:</b> {email}</p>
        <p>Frequency count for R&D department: {rd_count}</p>
        <img src="department_histogram.png" alt="Department Histogram">
    </body>
    </html>
    """)

print("HTML file generated: employee_department_analysis.html")
