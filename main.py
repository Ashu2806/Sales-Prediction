import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

# Step 1: Load the dataset
df = pd.read_csv("car_purchasing.csv", encoding='ISO-8859-1')

# Step 2: Drop unused columns
df = df.drop(['customer name', 'customer e-mail', 'country', 'gender'], axis=1)

# Step 3: Rename columns for consistency
df.columns = ['Age', 'Annual_Salary', 'Credit_Card_Debt', 'Net_Worth', 'Amount_Paid']

# Step 4: Define features and target
X = df.drop(['Amount_Paid'], axis=1)
y = df['Amount_Paid']

# Step 5: Split the dataset
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Step 6: Feature scaling
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Step 7: Train the model
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train_scaled, y_train)

# Step 8: Predict
y_pred = model.predict(X_test_scaled)

# Step 9: Evaluate the model
mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print("Model Evaluation Metrics:")
print(f"Mean Absolute Error (MAE): {mae:.2f}")
print(f"Mean Squared Error (MSE): {mse:.2f}")
print(f"R² Score: {r2:.2f}")

# Step 10: Visualization – Salary vs. Purchase Amount
df['Salary_Range'] = pd.cut(df['Annual_Salary'], bins=5)
grouped = df.groupby('Salary_Range')['Amount_Paid'].mean().reset_index()

plt.figure(figsize=(10, 6))
bars = plt.bar(grouped['Salary_Range'].astype(str), grouped['Amount_Paid'], color='#4c72b0')
plt.title('Average Amount Paid by Salary Range', fontsize=14, weight='bold')
plt.xlabel('Annual Salary Range', fontsize=12)
plt.ylabel('Average Amount Paid', fontsize=12)
plt.xticks(rotation=45)

# Add bar labels
for bar in bars:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, yval + 5000, f'{yval:.0f}', ha='center', fontsize=10)

plt.tight_layout()
plt.savefig("amount_paid_by_salary_range.png")  # Saves the figure
plt.show()
