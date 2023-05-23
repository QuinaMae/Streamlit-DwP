import streamlit as st
import pandas as pd

def calculate_descriptive_stats(data):
    # Calculate descriptive statistics
    descriptive_stats = data.describe()

    # Add additional statistics if needed
    # descriptive_stats['median'] = data.median()

    return descriptive_stats

def main():
    # Title and description
    st.title("StayOnTrack Calculator")
    st.write("Enter your dataset and calculate descriptive statistics.")

    # File upload
    uploaded_file = st.file_uploader("Upload your dataset (CSV file)", type="csv")

    if uploaded_file is not None:
        # Read the dataset
        data = pd.read_csv(uploaded_file)

        # Display the dataset
        st.subheader("Dataset")
        st.write(data)

        # Calculate descriptive statistics
        descriptive_stats = calculate_descriptive_stats(data)

        # Display the descriptive statistics
        st.subheader("Descriptive Statistics")
        st.write(descriptive_stats)

if __name__ == "__main__":
    main()