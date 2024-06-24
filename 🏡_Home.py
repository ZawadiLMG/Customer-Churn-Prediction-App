import streamlit as st
#from streamlit_option_menu import option_menu

st.set_page_config(
    page_title = "Home Page",
    page_icon = "🏡",
    layout = 'wide'
)

# Title and introduction
st.markdown('<h1 style="text-align: left;"><b>Customer Churn Predictor</b></h1>', unsafe_allow_html=True)
st.sidebar.success("Select a page above")
st.subheader("Predict Churn, Ensure Customer Loyalty")

st.write(""" 
Welcome to the "Telcom Churn Predictor", an innovative application designed to help telecommunication companies proactively retain their customers. Understanding and anticipating customer 
churn is crucial for maintaining a loyal customer base.""")
st.write("""This project leverages advanced data analytics to predict customer churn, providing actionable insights to reduce turnover and enhance customer satisfaction.
By harnessing the power of predictive modeling, businesses can identify at-risk customers and implement targeted retention strategies, ultimately driving long-term growth and stability.""")

# Image
#image_url = "https://media.istockphoto.com/id/1481095189/photo/businesswoman-analyzes-profitability-of-working-company-with-digital-virtual-screen-graphics.webp?s=1024x1024&w=is&k=20&c=K_zLxKkGr0RN_VGR_KdS6OcM1ClvkfbL6bK5df7DiT4="
# image_url = "https://pixabay.com/illustrations/customer-family-magnifying-glass-563967/"
# st.markdown(f'<img src="{image_url}" alt="Telecommunication Networks" width="800" height="300">', unsafe_allow_html=True)


# st.write("""**Key Features:**
# - **Accurate Prediction:** Utilize predictive modeling to anticipate customer churn with precision.
# - **Data-Driven Decisions:** Leverage comprehensive customer data to inform strategic initiatives.
# - **Proactive Retention:** Take preemptive measures to retain valuable customers and foster long-term loyalty.
# - **Data Upload and Integration:** Seamlessly upload customer data from various sources in CSV format. Integrate with existing databases and CRM systems for real-time data analysis.
# """)

# Footer
st.write("### Contact:")

st.write("*Gmail*: mumbualoyce@gmail.com")

st.markdown("""
*LinkedIn*:  [LinkedIn](https://www.linkedin.com/in/loyce-mumbua/)
""")

st.markdown("""
*Medium Article*:  [Medium Article](https://medium.com/@mumbualoyce/telkom-company-customer-churn-prediction-985b95b6501a)
""")

st.markdown("""
*GitHub Repository*:  [GitHub Repository](https://github.com/ZawadiLMG/Customer-Churn-Prediction.git)
""")