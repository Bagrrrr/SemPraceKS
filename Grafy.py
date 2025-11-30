import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

dataset = {}
whyset = {}
ratingset = {}
with open(r"C:\Users\Uživatel\OneDrive\Plocha\SemPraceKS\data.txt", "r", encoding="utf-8") as f:
    for i in range(3):
        school = f.readline() # reads
        nums = f.readline()
        why = f.readline()
        rating = f.readline()

        why = why.strip().split() # prepares
        nums = nums.strip().split()
        rating = rating.strip().split()

        dataset[school.strip()] = list(map(int, nums)) # saves in dicts
        whyset[school.strip()] = list(map(int, why))
        ratingset[school.strip()] = list(map(int, rating))





st.header("používáte mobilní aplikaci eDoklady?") #yes/no pie charts
cols = st.columns(3)
for i, (school, values) in enumerate(dataset.items()):
    if i >= 3:
        break
    if len(values) >= 3: 
        second_value = values[1]
        third_value = values[2]
        pie_data = [second_value, third_value]
        labels = ['Ano', 'Ne']

        fig, ax = plt.subplots()
        ax.pie(pie_data, labels=labels, autopct='%1.1f%%', startangle=90)
        ax.axis('equal')

        cols[i].subheader(f"Graf pro {school.strip()}")
        cols[i].pyplot(fig)
        cols[i].text(f"ze {values[0]} studentů")
        
st.markdown("---")
st.header("kde jste se s aplikací setkali?")
options = ["Neznám", "Od přátel", "Od rodiny", "Z sociálních médií", "Z rádia či televize", "Na Úřadu"]
cols = st.columns(3)
for i, (school, values) in enumerate(whyset.items()):
    if i >= 3:
        break
    with cols[i]:
        st.subheader(f"Graf pro {school.strip()}")
        bar_data = (values + [0]*6)[:6]
        bar_labels = options[:len(bar_data)]
        colors = ['#4C72B0','#DD8452','#55A868','#C44E52','#8172B2','#937860'][:len(bar_data)]

        fig, ax = plt.subplots(figsize=(4, 3))
        ax.bar(bar_labels, bar_data, color=colors)
        ax.set_ylabel('Počet studentů')
        ax.set_title('Kde jste na aplikaci narazili?')
        ax.set_ylim(0, max(bar_data) * 1.2 if max(bar_data) > 0 else 1)
        plt.setp(ax.get_xticklabels(), rotation=30, ha='right')
        fig.tight_layout()

        cols[i].pyplot(fig)
        cols[i].text(f"ze {dataset[school][0]} studentů")

st.markdown("---")
st.header("hodnocení stavu digitalizace ČR (1-10)")
rating_labels = [str(i) for i in range(1, 11)]
cols = st.columns(3)
for i, (school, values) in enumerate(ratingset.items()):
    if i >= 3:
        break
    with cols[i]:
        st.subheader(f"Hodnocení pro {school.strip()}")
        bar_data = (values + [0] * 10)[:10]
        colors = plt.cm.Blues(np.linspace(0.35, 0.9, 10))

        fig, ax = plt.subplots(figsize=(6, 3))
        ax.bar(rating_labels, bar_data, color=colors)
        ax.set_xlabel("Hodnocení (1-10)")
        ax.set_ylabel("Počet hlasů")
        ax.set_title("Distribuce hodnocení")
        ax.set_ylim(0, max(bar_data) * 1.2 if max(bar_data) > 0 else 1)
        plt.setp(ax.get_xticklabels(), rotation=0, ha='center')
        fig.tight_layout()

        cols[i].pyplot(fig)
        cols[i].text(f"Celkem hlasů: {sum(bar_data)}")