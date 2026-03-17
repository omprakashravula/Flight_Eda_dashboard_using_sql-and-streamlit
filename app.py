import streamlit as st
from ddhelper import DB
import plotly.graph_objects as go
import matplotlib.pyplot as plt
import plotly.express as px
db=DB()
st.sidebar.title('flight analysis')
user_option=st.sidebar.selectbox('menu',['select one','check flight','analtics'])

if user_option=='check flight':
    st.title('check flight')
    col1,col2=st.columns(2)
    city = db.fetch_city_names()
    with col1:
        source=st.selectbox('source',sorted(city))
    with col2:
        destination=st.selectbox('destination',sorted(city))
    if st.button('search'):
        data=db.fetch_all_flights(source,destination)
        st.dataframe(data)
elif user_option=='analtics':
    airline,frequency=db.fetch_airline_frequency()
    fig=go.Figure(
        go.Pie(
            labels=airline,
            values=frequency,
        ))
    st.header('pie chart')
    st.plotly_chart(fig)

    #avg prie for each air line
    airline, avg_price = db.fetch_airline_avg_price()
    fig, ax = plt.subplots()
    ax.bar(airline, avg_price)
    plt.xlabel('Airline')
    plt.ylabel('Average Price')
    plt.xticks(rotation=90)
    plt.title('airline avg price')
    plt.show()
    st.pyplot(fig)

    #most busy city with flights
    city,frequency1=db.busy_airport()
    fig=px.bar(x=city,y=frequency1)
    plt.xlabel('City')
    plt.ylabel('Frequency')
    st.plotly_chart(fig,theme='streamlit',use_container_width=True)

    # daily flight lineplot
    date,frequency2=db.daily_frequency()
    fig = px.line(x=date, y=frequency2)
    plt.xlabel('Date')
    plt.ylabel('Frequency')
    st.plotly_chart(fig, theme='streamlit', use_container_width=True)

else:
    def show_about_page():
        # Header Section with an emoji
        st.title("✈️ Flight Data Analytics & Search")
        st.markdown("---")

        # Column layout for a "Quick Stats" or "Features" look
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric(label="Airlines Tracked", value="10+")
        with col2:
            st.metric(label="Analysis Types", value="Time & Market")
        with col3:
            st.metric(label="Search Speed", value="Instant")

        st.markdown("### 📊 Project Overview")
        st.write(
            """
            Welcome to the **Flight Analysis Portal**. This application is designed to help 
            travelers and data enthusiasts visualize flight trends and find the best routes 
            between major Indian cities. 

            Whether you are looking for the cheapest airline or the most frequent flights 
            to Delhi, our dashboard provides real-time insights from our flight datasets.
            """
        )

        # Adding a clean "Key Features" section
        st.markdown("### 🚀 Key Features")
        features = {
            "Real-time Search": "Filter flights by source and destination instantly.",
            "Market Share Analysis": "Visualize which airlines dominate specific routes using interactive Pie Charts.",
            "Time Series Tracking": "Monitor flight frequency over time with Plotly Line Charts.",
            "Stopover Insights": "Identify direct vs. connecting flights to optimize travel time."
        }

        for feature, description in features.items():
            st.markdown(f"- **{feature}**: {description}")

        st.info(
            "💡 **Tip:** Use the sidebar menu on the left to toggle between the Search Engine and Data Analytics views!")


    # Logic to call the function
    show_about_page()