# Scanned_receipts_prediction

## Requirements
- Python
- Libraries: Streamlit, Pandas, Statsmodels, etc.

## Installation Steps
### Install Python
- Download Python from [python.org](https://python.org).
- Follow the installation instructions for your OS.

### Set Up the Environment
- Create and activate a virtual environment.
- Windows: Run 'venv\Scripts\activate'
- Mac: Run 'source venv/bin/activate'

### Install Required Libraries
- Run `pip install streamlit pandas statsmodels matplotlib seaborn tensorflow`.

## Downloading Project Files
Ensure you have the following files:
- The Streamlit app script (e.g., `app.py`).
- The trained model file (`model.pkl`).

## Running the App
### Using Streamlit
- Run 'streamlit run web_app.py'

### Using Docker
- Run 'docker build -t chandra/predict .'
- 'docker image ls'
- 'docker run -p 8080:8051 ImageId'

## Using the App
[Select a month from the dropdown menu.
Choose whether you want to see predictions for each day or the average for the month.
Click on "Start Prediction" to view the results.
The app will display the number of scanned receipts predicted for the selected period]

## Troubleshooting
[If you encounter errors related to missing libraries, ensure all required libraries are installed.
If the model file (model.pkl) is not found, ensure it's in the same directory as the Streamlit script or update the script with the correct file path.
For any issues with Python installation or package management, refer to the official Python documentation.]

