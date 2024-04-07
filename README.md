# Paybrush

Here are the detailed instructions for a user to download the `paybrush.py` setup script from GitHub, run the script, and then deploy the generated script to Google Cloud Platform (GCP) from their terminal.

### Step 1: Preparing Your Environment

1. **Install Git**: Ensure Git is installed on your system to clone the repository. You can download it from [git-scm.com](https://git-scm.com/).
2. **Install Python**: Ensure Python is installed on your system. You can download it from [python.org](https://www.python.org/).
3. **Install Google Cloud SDK**: Install the Google Cloud SDK from [cloud.google.com/sdk](https://cloud.google.com/sdk) to deploy the application to GCP.

### Step 2: Downloading the Script from GitHub

1. **Clone the GitHub Repository**: Open your terminal and clone the repository containing `paybrush.py` using Git. Enter the following command in your terminal:
   ```bash
   git clone https://github.com/paybrush/paybrush.git
   ```
2. **Navigate to the Repository Directory**: Change into the directory that contains the cloned repository:
   ```bash
   cd paybrush
   ```

### Step 3: Running the Setup Script

1. **Run the `paybrush.py` Script**: Execute the setup script using Python. This script will prompt you for various inputs required to customize the application.
   ```bash
   python paybrush.py
   ```
2. **Enter Required Information**: When prompted, enter your email address, email password, company name, Google Cloud Storage bucket name, and the name of the ZIP file stored in GCS.

### Step 4: Deploying to Google Cloud Platform

1. **Navigate to the Generated Script**: Once the setup script completes, it will generate a new Python file named `<company_name>_paybrush.py`. Navigate to this file in your terminal.
   ```bash
   cd path_to_generated_script
   ```

2. **Initialize Google Cloud SDK**: If you haven't already initialized the Google Cloud SDK, do so by running:
   ```bash
   gcloud init
   ```
   Follow the on-screen instructions to log in and set up your GCP project.

3. **Deploy to Cloud Functions**: Deploy the generated script as a Google Cloud Function. Replace `<function_name>` with a name for your cloud function, and set the `--trigger-http` flag to create an HTTP-triggered function.
   ```bash
   gcloud functions deploy <function_name> --runtime python39 --trigger-http --allow-unauthenticated --entry-point main --source .
   ```
   **Note:** The `--allow-unauthenticated` flag allows anyone to trigger your function. For production, consider removing this flag and securing your function.

4. **Verify Deployment**: After the deployment completes, GCP will provide you with a URL for your deployed function. You can test this URL by sending a POST request simulating an IPN message from PayPal.

### Additional Notes

- Ensure that the environment variables (e.g., `EMAIL_ADDRESS`, `EMAIL_PASSWORD`, `GCS_BUCKET_NAME`, and `ZIP_FILE_NAME`) are correctly set in your Cloud Function's settings.
- For security reasons, avoid hardcoding sensitive information like email passwords directly into the script. Use GCP's Secret Manager or environment variables configured through the Cloud Console.
- Regularly update your dependencies and review your Cloud Function's logs for any unexpected errors or security issues.

This guide provides a comprehensive overview of deploying a customized PayBrush application to GCP, starting from downloading the script from GitHub, running the setup script, and finally deploying the customized application to Google Cloud Functions.
