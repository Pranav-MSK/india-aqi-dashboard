# 🌫️ India Metro Cities — Air Quality Index (2015–2020)

An end-to-end data project analyzing air quality across 9 major Indian metro cities using Python and Tableau.

## 📊 Live Dashboard

🔗 [View on Tableau Public](https://public.tableau.com/views/IndiaMetroCities-AirQualityIndex20152020/Dashboard1)

<div class='tableauPlaceholder' id='viz1778573277790' style='position: relative'><noscript><a href='#'><img alt=' ' src='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;In&#47;IndiaMetroCities-AirQualityIndex20152020&#47;Dashboard1&#47;1_rss.png' style='border: none' /></a></noscript><object class='tableauViz'  style='display:none;'><param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' /> <param name='embed_code_version' value='3' /> <param name='site_root' value='' /><param name='name' value='IndiaMetroCities-AirQualityIndex20152020&#47;Dashboard1' /><param name='tabs' value='yes' /><param name='toolbar' value='yes' /><param name='static_image' value='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;In&#47;IndiaMetroCities-AirQualityIndex20152020&#47;Dashboard1&#47;1.png' /> <param name='animate_transition' value='yes' /><param name='display_static_image' value='yes' /><param name='display_spinner' value='yes' /><param name='display_overlay' value='yes' /><param name='display_count' value='yes' /><param name='language' value='en-US' /></object></div>                <script type='text/javascript'>                    var divElement = document.getElementById('viz1778573277790');                    var vizElement = divElement.getElementsByTagName('object')[0];                    if ( divElement.offsetWidth > 800 ) { vizElement.style.width='100%';vizElement.style.height=(divElement.offsetWidth*0.75)+'px';} else if ( divElement.offsetWidth > 500 ) { vizElement.style.width='100%';vizElement.style.height=(divElement.offsetWidth*0.75)+'px';} else { vizElement.style.width='100%';vizElement.style.minHeight='1700px';vizElement.style.maxHeight=(divElement.offsetWidth*1.77)+'px';}                     var scriptElement = document.createElement('script');                    scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';                    vizElement.parentNode.insertBefore(scriptElement, vizElement);                </script>

---

## 📁 Project Structure

```
aqi-dashboard/
│
├── data/
│   ├── city_day.csv          # Raw dataset (source: Kaggle)
│   └── aqi_metro.csv         # Cleaned dataset used in Tableau
│
├── scripts/
│   └── prepare_data.py       # Data cleaning script
│
└── README.md
```

---

## 🛠️ Tools Used

| Tool | Purpose |
|---|---|
| Python (Pandas) | Data cleaning & preparation |
| Tableau Public | Dashboard & visualizations |

---

## 📦 Data Source

- **Dataset:** [Air Quality Data in India (2015–2020)](https://www.kaggle.com/datasets/rohanrao/air-quality-data-in-india)
- **Source:** Kaggle
- **Raw rows:** ~19,800 across 26 cities
- **After cleaning:** ~9,400 rows across 9 metro cities

---

## 🧹 Data Cleaning Steps

1. Filtered to 9 major metro cities: Delhi, Mumbai, Chennai, Kolkata, Bengaluru, Hyderabad, Ahmedabad, Jaipur, Gurugram
2. Dropped niche pollutant columns: NO, NOx, NH3, Benzene, Toluene, Xylene
3. Removed all rows with null values
4. Final columns retained: `City, Date, PM2.5, PM10, NO2, CO, SO2, O3, AQI, AQI_Bucket`

---

## 📈 Dashboard Views

| Sheet | Chart Type | Insight |
|---|---|---|
| AQI Trend Over Time | Line Chart | Overall AQI decline + COVID-19 lockdown dip (2020) |
| City AQI Ranking | Horizontal Bar | Delhi consistently worst; Bengaluru & Chennai cleanest |
| Pollutant Breakdown | Bar Chart | PM2.5 & PM10 are dominant pollutants in northern cities |
| City AQI Trends | Multi-line Chart | Per-city AQI trends across 5 years |
| Monthly Seasonality | Line Chart | Winter (Oct–Jan) spikes and monsoon (Jun–Aug) dips |

---

## 💡 Key Insights

- **Delhi** has the highest average AQI across all years and all pollutants
- **COVID-19 lockdown (March–May 2020)** caused a visible and significant AQI drop across all cities
- **Winter months (November–January)** see the worst air quality due to crop burning and cold air trapping pollutants
- **Monsoon season (June–August)** brings the cleanest air across all cities
- **Southern cities** (Bengaluru, Chennai, Hyderabad) maintain significantly better air quality year-round

---

## ▶️ How to Run

```bash
# Install dependencies
pip install pandas

# Place city_day.csv in the data/ folder
# Then run:
python scripts/prepare_data.py
```

The cleaned `aqi_metro.csv` will be saved to the `data/` folder, ready to load into Tableau.
