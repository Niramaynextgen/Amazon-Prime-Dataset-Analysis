import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(
    page_title="Amazon Prime Dashboard",
    page_icon="🎥",
    layout="wide",
)

with st.sidebar:
    st.image(
        "https://upload.wikimedia.org/wikipedia/commons/thumb/1/11/Amazon_Prime_Video_logo.svg/2560px-Amazon_Prime_Video_logo.svg.png",
        use_container_width=True)
    st.markdown("---✨Project Details✨---")
    st.info(
        "This dashboard visualizes the cleaned Amazon Prime Dataset, showcasing trends in content type, ratings and release years.")
    st.header("Data Settings")
    uploaded_file = st.file_uploader("Upload your cleaned CSV file", type=['csv'])


st.title(" 🎞️ Amazon Prime Video Content Analysis 🎞️ ")
st.markdown("---")


with st.expander("ℹ️ About Amazon Prime Video"):
    st.markdown("""
        **History & Key Facts:**
        * **Launch:** Originally launched as **Amazon Unbox** on September 7, 2006.
        * **Evolution:** Rebranded as *Amazon Instant Video* in 2011 before becoming **Prime Video**.
        * **Global Reach:** Now available in over 200 countries with over **200 million** subscribers.
        """)


@st.cache_data
def load_data(file):
    if file is not None:
        try:
            return pd.read_csv(file)
        except Exception as e:
            st.error(f"Error Loading File: {e}")
            return None
    return None


df = load_data(uploaded_file)

if df is not None:
    st.subheader("📂 Processed Dataset")
    st.dataframe(df)

    st.markdown("---")
    st.subheader("📊 Content Analytics")

    row1_col1, row1_col2 = st.columns(2)

    with row1_col1:
        st.markdown("#### 1. Movies vs. TV Shows")
        count = df['type'].value_counts()

        fig1, ax1 = plt.subplots(figsize=(6, 4))
        ax1.bar(count.index, count.values, color=['skyblue', 'gold'])  # Changed 'colour' to 'color'
        ax1.set_ylabel("Count")
        ax1.grid(axis='y', linestyle='--', alpha=0.5)
        st.pyplot(fig1)

    with row1_col2:
        st.markdown("#### 2. Content Release by Year")
        release = df['release_year'].value_counts()

        fig2, ax2 = plt.subplots(figsize=(6, 4))
        ax2.scatter(release.index, release.values, color='darkorange', alpha=0.6)
        ax2.set_xlabel("Release Year")
        ax2.set_ylabel("Number of Titles")
        ax2.grid(True, linestyle='--', alpha=0.5)
        st.pyplot(fig2)

    st.markdown("---")

    row2_col1, row2_col2 = st.columns(2)

    with row2_col1:
        st.markdown("#### 3. Count of Titles by Rating")
        rating_counts = df['rating'].value_counts()
        my_colors = ['orange', 'green', 'blue', 'purple', 'coral', 'cyan', 'red', 'lime', 'teal', 'yellow', 'violet',
                     'pink', 'indigo']

        fig3, ax3 = plt.subplots(figsize=(6, 4))
        ax3.barh(rating_counts.index, rating_counts, color=my_colors[:len(rating_counts)])
        ax3.set_xlabel("Count")
        ax3.invert_yaxis()
        ax3.grid(axis='x', linestyle='--', alpha=0.5)
        st.pyplot(fig3)

    with row2_col2:
        st.markdown("#### 4. Top 5 Ratings Share")
        pie_data = df['rating'].value_counts()
        top_5 = pie_data[:5]
        other_count = pie_data[5:].sum()
        final_pie_data = pd.concat([top_5, pd.Series({'Others': other_count})])

        fig4, ax4 = plt.subplots(figsize=(6, 4))
        ax4.pie(final_pie_data.values, labels=final_pie_data.index, autopct='%1.1f%%', startangle=140)
        st.pyplot(fig4)

    st.markdown("---")
    st.markdown("#### 🌐 Explore More")
    st.link_button("Go to Amazon Prime Video", "https://www.primevideo.com/")

else:
    st.warning("👈 Please upload your cleaned Amazon Prime CSV file in the sidebar to start the analysis.")