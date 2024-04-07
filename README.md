# Paybrush

This guide provides a comprehensive overview of setting up and deploying your Paybrush automation solution on Google Cloud Platform (GCP), starting from email receipt to full deployment and operational testing.

### Step 1: Preparing Your Environment
- **Install Python**: Confirm Python is installed on your system. Download it at [python.org](https://www.python.org/).
- **Install Google Cloud SDK**: For deploying applications to GCP, install the Google Cloud SDK from [cloud.google.com/sdk](https://cloud.google.com/sdk). If using Homebrew, run:
    ```bash
    brew install --cask google-cloud-sdk`.
    ```
### Step 2: Receiving and Saving the Script
- **Receive `paybrush.py` Via Email**: Look for an email from Paybrush with the `paybrush.py` setup script attached.
- **Save the Script**: Download and save the script to your preferred working directory on your computer.

### Step 3: Running the Setup Script
- **Open Terminal**: Go to the directory where `paybrush.py` is saved.
    ```bash
    cd path_to_saved_script
    ```
- **Run the `paybrush.py` Script**: Execute the script using Python. It will request information to customize your setup.
    ```bash
    python paybrush.py
    ```
    Alternatively, use `python3 paybrush.py` if your system requires specifying Python 3 explicitly.
- **Enter Required Information**: Input your email address, email password, company name, Google Cloud Storage bucket name, and the ZIP file's name in GCS as prompted.

### Step 4: Deploying to Google Cloud Platform
- **Navigate to the Generated Script**: Find the newly created `main.py` in the same directory.
- **Initialize Google Cloud SDK**: Run `gcloud init` to start the SDK if not already done. This process includes logging in and selecting or creating a GCP project.
- **Deploy to Cloud Functions**: Use the command below, replacing `<function_name>` with your chosen name for the cloud function.
    ```bash
    gcloud functions deploy <function_name> --runtime python39 --trigger-http --entry-point app --source .
    ```
    Be mindful of securing your function, especially for production environments.

- **Verify Deployment**: After deployment, GCP will provide a function URL. Test this endpoint with a simulated PayPal IPN message to confirm functionality.

### Additional Notes
- Ensure environment variables (`EMAIL_ADDRESS`, `EMAIL_PASSWORD`, `GCS_BUCKET_NAME`, `ZIP_FILE_NAME`) are accurately configured in your Cloud Function settings.
- Prioritize security by not embedding sensitive data directly in the script. Instead, use GCP's Secret Manager or environment variables.
- Consistently monitor your Cloud Function's logs and keep dependencies up to date to mitigate potential security vulnerabilities or functional issues.
