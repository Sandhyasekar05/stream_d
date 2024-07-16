import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
df=pd.read_csv("F:\heartdispredict\Heart_Disease_Prediction.csv")
st.write(df)
correlation_matrix = df.corr()

# Plot and display the heatmap
st.write("### Correlation Matrix Heatmap")
plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, cmap="coolwarm", fmt=".2f", linewidths=.5)
plt.title("Correlation Matrix")
st.pyplot(plt)

labels = ['Male', 'Female']
sizes = [183, 87]

# Plot
plt.figure(figsize=(8, 6))  # Optional: Adjust the figure size
plt.pie(sizes, labels=labels, autopct='%1.1f%%')
plt.title('Gender Distribution')  # Optional: Add a title
st.pyplot(plt)

#scatter plot
plt.figure(figsize=(8, 6))
sns.scatterplot(data=df,x='Chest pain type',y='Age',hue='Max HR')
plt.title('chest paintype under age')
st.pyplot(plt)


