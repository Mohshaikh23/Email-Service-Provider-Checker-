# Email Platform Checker from Domains

This is a simple **Streamlit** web application that checks the email platform (Gmail, Outlook, etc.) associated with a list of domains. The app processes a CSV file uploaded by the user, analyzes the MX records for each domain, and outputs the results, including the identified email platform. Users can then download the results as a CSV file.

## Features

- **Upload CSV**: Upload a CSV file containing domains (with a `Domain` column).
- **Platform Detection**: Automatically detects if the domain uses Gmail (Google Workspace), Outlook (Microsoft 365), or an unknown email platform.
- **Results Display**: View the email platform for each domain directly in the web app.
- **Downloadable Results**: Download the results as a new CSV file.

## Requirements

To run this project, you'll need to install the following Python libraries:

- `streamlit`
- `pandas`
- `dnspython`

You can install the required libraries using pip:

```bash
pip install streamlit pandas dnspython
```

## How to Run the App

1. Clone this repository:

   ```bash
   git clone https://github.com/Mohshaikh23/Email-Service-Provider-Checker-.git
   ```

2. Navigate to the project directory:

   ```bash
   cd dnscheck
   ```

3. Run the Streamlit app:

   ```bash
   streamlit run app.py
   ```

4. Open the provided local URL (e.g., `http://localhost:8501`) in your browser to access the app.

## Usage

1. Upload a CSV file containing a list of domains (with a column named `Domain`).
2. The app will process each domain, checking its MX records.
3. Results will be displayed in a table format.
4. Download the results as a CSV file with an additional column for the detected email platform.

## Example CSV Format

The uploaded CSV file should have a column named `Domain` with the domains you want to check:

```csv
Domain
example1.com
example2.com
example3.com
```

## Example Output

Once processed, the app will generate a CSV file with the following structure:

```csv
Domain,Email Platform
example1.com,Gmail (Google Workspace)
example2.com,Outlook (Microsoft 365)
example3.com,Other/Unknown Platform
```

## Screenshots

![App Interface](screenshots/app-interface.png)

## Contributing

Feel free to submit a pull request or open an issue if you find any bugs or have feature requests.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
