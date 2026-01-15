import streamlit as st
import matplotlib.pyplot as plt
import matplotlib as mpl

st.set_page_config(page_title="Grafy")  # Nastavení názvu stránky

st.markdown(
    """
    <style>
    html, body, .stApp, .stApp .main, .stApp .block-container { background-color: #f8f9fa !important; }

    .stApp, .stApp * { color: #0f1720 !important; }
    .stApp a { color: #0b67ff !important; }

    .stApp h1, .stApp h2, .stApp h3, .stApp h4 { color: #0b1220 !important; }

    .stButton button, button, input, textarea, select { background-color: #ffffff !important; color: #0f1720 !important; }
    </style>
    """,
    unsafe_allow_html=True,
) # Vlastní CSS pro světlý režim


st.title("Digitalizace státní správy z pohledu studentů VŠ")

st.write("Kryštof Šejhar, 8.M, Gymnázium Christiana Dopplera")

st.write("Cíl šetření: Analýza postojů, míry informovanosti a spokojenosti studentů" \
" vysokých škol s nabídkou digitálních služeb v České republice.")

st.subheader("Metodologie sběru dat")
st.write("Sběr dat proběhl formou přímého oslovování studentů před budovami vysokých škol. " \
"Tato metoda terénního šetření byla zvolena pro zajištění vysoké relevance vzorku a možnost " \
"okamžitého vysvětlení případných nejasností v otázkách. Celkem bylo tímto způsobem v průběhu " \
"prosince 2025 získáno 320 validních vzorků od studentů různých studijních oborů.")

st.header("Vizualizace výsledků")

st.subheader("Využívání digitálních služeb státní správy")
st.write("První graf se zaměřuje na dvě stěžejní platformy digitální státní správy, mobilní aplikaci eDoklady" \
" a Portál občana. Srovnává výsledky mého šetření mezi studenty s oficiálními daty za celou ČR. U studentů je" \
" patrné výrazně vyšší povědomí a využívání těchto služeb, což může být ovlivněno jejich větší technickou" \
" zdatností a potřebou efektivního řešení administrativních úkonů.")

mpl.rcParams['figure.facecolor'] = '#f8f9fa' 
mpl.rcParams['axes.facecolor'] = '#f8f9fa'
mpl.rcParams['savefig.facecolor'] = '#f8f9fa'
mpl.rcParams['font.size'] = 8
mpl.rcParams['axes.titlesize'] = 9
mpl.rcParams['axes.labelsize'] = 8
mpl.rcParams['xtick.labelsize'] = 7
mpl.rcParams['ytick.labelsize'] = 7
mpl.rcParams['legend.fontsize'] = 7 # Nastavení velikostí

with open(r"data.txt", "r", encoding="utf-8") as f:
    data = f.readlines() # Načtení dat ze souboru

Používá = int(data[2].strip())
Nepoužívá = int(data[4].strip()) # data k prvnímu grafu


col1, col2 = st.columns(2) # Vytvoření dvou sloupců pro grafy

FIGSIZE = (2.5, 2.5)  # Velikost grafů

with col1:
    st.header("Studenti")
    fig = plt.figure(figsize=FIGSIZE)
    ax = fig.add_axes([0.1, 0.1, 0.8, 0.8])  
    ax.pie([Používá, Nepoužívá], labels=["Používá", "Nepoužívá"], autopct="%1.1f%%", startangle=63,
           labeldistance=1.15, pctdistance=0.55, textprops={'color': '#0f1720', 'fontsize': 7}, radius=0.6, center=(0, 0)) # Vytvoření prvního grafu
    ax.set_aspect('equal')
    ax.set_xlim(-0.75, 0.75)
    ax.set_ylim(-0.75, 0.75)
    ax.autoscale(False)
    st.pyplot(fig) # Zobrazení prvního grafu




with col2:
    st.header("Česká republika")
    labels = ["Používá", "Nepoužívá"]
    values = [2050000, 10900000 - 2050000]
    fig2 = plt.figure(figsize=FIGSIZE)
    ax2 = fig2.add_axes([0.1, 0.1, 0.8, 0.8])
    ax2.pie(values, labels=labels, autopct='%1.1f%%', startangle=90,
            labeldistance=1.15, pctdistance=0.55, textprops={'color': '#0f1720', 'fontsize': 7}, radius=0.6, center=(0, 0)) # Vytvoření druhého grafu
    ax2.set_aspect('equal')
    ax2.set_xlim(-0.75, 0.75)
    ax2.set_ylim(-0.75, 0.75)
    ax2.autoscale(False)
    st.pyplot(fig2) # Zobrazení druhého grafu



st.write("---")
st.header("Odkud se studenti dozvídají o digitalizaci státní správy?")
st.write("Pro druhý graf jsem zjišťoval, kde se studenti o digitalizaci dozvídají. Tato " \
"data jsou klíčová pro pochopení, zda státní informační kampaň zasahuje i akademickou půdu. " \
"Výsledky potvrzují předpoklad, že pro studenty jsou klíčové [např. sociální sítě, online " \
"zpravodajství nebo aplikace]. Tento trend jasně odděluje studenty od většinové populace, " \
"která ve velké míře stále čerpá z tradičních médií (televize, tisk).")
labels_odkud = ["Neznal", "Přátelé a rodina", "Sociální Média", "Rádio", "Úřad"]
values_odkud = [
    int(data[8].strip()),
    int(data[10].strip()),
    int(data[12].strip()),
    int(data[14].strip()),
    int(data[16].strip()),
] # data k třetímu grafu
fig3, ax3 = plt.subplots(figsize=(4, 2.5))
ax3.pie(values_odkud, labels=labels_odkud, autopct='%1.1f%%', startangle=90,
        labeldistance=1.15, pctdistance=0.55, textprops={'color': '#0f1720', 'fontsize': 7}, radius=0.6) # Vytvoření třetího grafu
ax3.axis('equal')
fig3.tight_layout()
st.pyplot(fig3) # Zobrazení třetího grafu


st.write("---")
st.subheader("Hodnocení digitalizace státní správy studenty VŠ")
st.write("Poslední graf zobrazuje rozložení hodnocení digitalizace státní správy studenty " \
"vysokých škol na škále od 1 do 10. Z grafu je patrné, že většina studentů hodnotí " \
"digitalizaci v rozmezí 5 až 8, což naznačuje mírnou spokojenost, ale také prostor pro zlepšení.") 
labels_1_10 = [str(i) for i in range(1, 11)]
values_1_10 = [
    int(data[20].strip()),
    int(data[22].strip()),
    int(data[24].strip()),
    int(data[26].strip()),
    int(data[28].strip()),
    int(data[30].strip()),
    int(data[32].strip()),
    int(data[34].strip()),
    int(data[36].strip()),
    int(data[38].strip()),
] # data k čtvrtému grafu

fig4, ax4 = plt.subplots(figsize=(4, 2))  
bars = ax4.bar(labels_1_10, values_1_10, color='tab:blue')
ax4.set_xlabel('Hodnocení (1-10)', fontsize=7)
ax4.set_ylabel('Počet studentů', fontsize=7)
ax4.set_title('Hodnocení digitalizace státní správy studenty VŠ', fontsize=8)
ax4.set_ylim(0, max(120, max(values_1_10) * 1.05))
ax4.tick_params(axis='x', labelsize=6)
ax4.tick_params(axis='y', labelsize=6)  # nastavení čtvrtého grafu
for bar in bars:
    height = bar.get_height()
    ax4.annotate(f"{int(height)}",
                 xy=(bar.get_x() + bar.get_width() / 2, height),
                 xytext=(0, 1),  
                 textcoords="offset points",
                 ha='center', va='bottom', fontsize=6) # vytvoření čtvrtého grafu s hodnotami nad sloupci
fig4.tight_layout()
st.pyplot(fig4) # Zobrazení čtvrtého grafu

total_responses = sum(values_1_10)

weighted_sum = sum(r * count for r, count in zip(range(1, 11), values_1_10))
mean_rating = weighted_sum / total_responses
st.write(f"**Průměrné hodnocení digitalizace státní správy studenty VŠ:** {mean_rating:.2f} / 10") # Výpočet a zobrazení průměrného hodnocení

st.write("---")
st.subheader("Zdroje")
st.write("https://www.cesko.digital/")
st.write("https://publico.cz/cesko/digitalni-obcanky-800-tisic-cechu-volby#:~:text=Sn%C4%9Bmovn%C3%AD%20volby%20otestuj%C3%AD%20digit%C3%A1ln%C3%AD%20ob%C4%8Danky.%20M%C3%A1%20je%20u%C5%BE%20p%C5%99es%20800%20tis%C3%ADc%20%C4%8Cech%C5%AF%20%7C%20PUBLICO.")



