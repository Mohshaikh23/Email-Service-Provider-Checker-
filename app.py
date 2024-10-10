import streamlit as st
import dns.resolver
import pandas as pd
import csv
import io

# Function to check the platform based on MX records
def check_email_platform(domain, timeout=10):
    try:
        # Querying MX records for the domain with an increased timeout
        mx_records = dns.resolver.resolve(domain, 'MX', lifetime=timeout)
        for mx in mx_records:
            mail_server = str(mx.exchange).lower()
            
            # Check if Gmail (Google Workspace)
            if 'google.com' in mail_server:
                return 'Gmail (Google Workspace)'
            # Check if Outlook (Microsoft 365)
            elif 'outlook.com' in mail_server or 'hotmail.com' in mail_server:
                return 'Outlook (Microsoft 365)'
        
        return 'Other/Unknown Platform'
    
    except (dns.resolver.NoAnswer, dns.resolver.NXDOMAIN):
        return 'Domain Not Found or No Email Setup'
    except dns.resolver.LifetimeTimeout:
        return 'Timeout Occurred - DNS Query Too Slow'

# Streamlit app layout
st.title("Email Platform Checker from Domains")

# Upload the CSV file
uploaded_file = st.file_uploader("Upload a CSV file with a 'Domain' column", type=["csv"])

if uploaded_file is not None:
    # Read the CSV file into a DataFrame
    df = pd.read_csv(uploaded_file)
    
    # Check if the necessary 'Domain' column exists
    if 'Domain' not in df.columns:
        st.error("The uploaded CSV does not have a 'Domain' column. Please upload a valid file.")
    else:
        # Check email platforms for each domain
        st.write("Processing the domains...")
        df['Email Platform'] = df['Domain'].apply(check_email_platform)
        
        # Display the results
        st.write("Results:")
        st.dataframe(df)
        
        # Create a download link for the processed CSV file
        output = io.StringIO()
        df.to_csv(output, index=False)
        processed_file = output.getvalue().encode('utf-8')
        output.close()

        st.download_button(
            label="Download Results as CSV",
            data=processed_file,
            file_name='email_platform_results.csv',
            mime='text/csv'
        )
