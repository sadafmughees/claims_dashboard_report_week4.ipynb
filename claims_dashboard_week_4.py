#!/usr/bin/env python
# coding: utf-8

# # NHS Claims Analytics Dashboard
# 
# Week 4 – Production Ready Dashboard

# In[1]:


import pandas as pd

df = pd.read_csv("claims_demo.csv")
df.head()


# ## Key Performance Indicators (KPIs)

# In[2]:


total_claims = len(df)
total_amount = df["Claim_Amount_GBP"].sum()
avg_processing = df["Processing_Time_Days"].mean()
approved_claims = (df["Status"] == "Approved").sum()

print("Total Claims:", total_claims)
print("Total Claim Amount (£):", round(total_amount, 2))
print("Average Processing Time (Days):", round(avg_processing, 2))
print("Approved Claims:", approved_claims)


# ## Import Visualization Libraries

# In[3]:


import matplotlib.pyplot as plt
import seaborn as sns

plt.style.use("default")


# ## Claims by Type

# In[4]:


claim_type = df.groupby("Claim_Type")["Claim_Amount_GBP"].sum()

plt.figure(figsize=(8,5))
claim_type.plot(kind="bar")
plt.title("Claims Amount by Type")
plt.ylabel("Amount (£)")
plt.show()


# ## Claim Status Distribution

# In[5]:


df["Status"].value_counts().plot(
    kind="pie",
    autopct="%1.1f%%",
    figsize=(6,6)
)
plt.title("Claim Status Distribution")
plt.ylabel("")
plt.show()


# ## Average Processing Time by Claim Type

# In[6]:


avg_time = df.groupby("Claim_Type")["Processing_Time_Days"].mean()

plt.figure(figsize=(8,5))
avg_time.plot(kind="bar")
plt.title("Average Processing Time by Claim Type")
plt.ylabel("Days")
plt.show()


# ## NHS Theme Configuration

# In[7]:


NHS_BLUE = "#005EB8"
NHS_DARK_BLUE = "#003087"
NHS_LIGHT_GREY = "#E8EDEE"

print("NHS Theme Loaded Successfully")


# ## Enhanced NHS Styled Chart

# In[8]:


claim_type = df.groupby("Claim_Type")["Claim_Amount_GBP"].sum()

plt.figure(figsize=(10,5))
claim_type.plot(kind="bar")

plt.title("NHS Claims Amount by Type", color=NHS_DARK_BLUE)
plt.xlabel("Claim Type")
plt.ylabel("Amount (£)")

plt.show()


# ## Export Dashboard Summary to PDF

# In[9]:


get_ipython().system('pip install reportlab -q')


# In[10]:


from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet


# In[11]:


pdf = SimpleDocTemplate("NHS_Claims_Report.pdf")

styles = getSampleStyleSheet()

content = []

content.append(
    Paragraph("NHS Claims Analytics Report", styles['Title'])
)

content.append(Spacer(1,12))

content.append(
    Paragraph(f"Total Claims: {total_claims}", styles['Normal'])
)

content.append(
    Paragraph(
        f"Total Claim Amount: £{total_amount:,.2f}",
        styles['Normal']
    )
)

content.append(
    Paragraph(
        f"Average Processing Time: {avg_processing:.2f} Days",
        styles['Normal']
    )
)

pdf.build(content)

print("PDF Generated Successfully")


# ## Production Logging

# In[12]:


import logging

logging.basicConfig(
    filename="dashboard.log",
    level=logging.INFO
)

logging.info("Dashboard Started")

print("Logging Enabled")


# ## PostgreSQL Integration Template

# In[13]:


# Future Production Database Connection

from sqlalchemy import create_engine

DATABASE_URL = (
    "postgresql://username:password@localhost:5432/claims_db"
)

print("PostgreSQL Template Added")


# ## Week 4 Dashboard Completion Summary
# 
# Features Implemented:
# 
# - NHS Branding
# - KPI Monitoring
# - Claims Analytics Visualizations
# - PDF Export Capability
# - Production Logging
# - PostgreSQL Migration Template
# - Production-Ready Dashboard Structure

# In[ ]:




