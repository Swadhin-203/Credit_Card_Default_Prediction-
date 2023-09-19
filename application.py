# Import necessary libraries
import streamlit as st
import pandas as pd
from src.pipelines.prediction_pipeline import predict
import warnings
warnings.filterwarnings("ignore")

# Define the Streamlit app


def main():

    st.title("Credit Card Fraud Detection")

    # Display an image from a URL
    st.image('https://images.pexels.com/photos/259200/pexels-photo-259200.jpeg',
             caption='Credit Card Frauds', use_column_width=True)

    # Create a file uploader widget
    uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

    if uploaded_file is not None:
        # Read the uploaded file
        df = pd.read_csv(uploaded_file)

        # Display the uploaded data
        st.subheader("Uploaded Data")
        st.write(df)

        # Perform predictions
        predictions = predict(df)
        final = pd.concat([df['ID'], pd.Series(predictions).map(
            {0: 'loyal', 1: 'defaulter'})], axis=1)

        # Display the predictions
        st.subheader("Predictions")
        st.write(final)


# Run the app
if __name__ == '__main__':
    main()
