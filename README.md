# Paybrush

This guide outlines deploying your customized Paybrush solution on GCP, from receiving the script via email to deployment and testing.

### Step 1: Preparing Your Environment

1. **Install Node.js**: Ensure Node.js is installed on your system. You can download it from nodejs.org.

2. **Install Google Cloud SDK**: Install the Google Cloud SDK from cloud.google.com/sdk to deploy the application to GCP. To run with Homebrew:
   ```
   brew install --cask google-cloud-sdk
   ```

### Step 2: Receiving and Saving the Script

1. **Receive paybrush.js Via Email**: Check your email for a message from Paybrush containing the `paybrush.js` setup script as an attachment.

2. **Save the Script**: Download the attachment and save it to a directory on your computer where you wish to work with the script.

### Step 3: Running the Setup Script

1. **Open Your Terminal**: Navigate to the directory where you saved `paybrush.js`.
   ```
   cd path_to_saved_script
   ```

2. **Run the paybrush.js Script**: Execute the setup script using Node.js. This script will prompt you for various inputs required to customize the application.
   ```
   node paybrush.js
   ```

3. **Enter Required Information**: When prompted, enter your email address, email password, company name, Google Cloud Storage bucket name, and the name of the ZIP file stored in GCS.

### Step 4: Deploying to Google Cloud Platform

1. **Navigate to the Generated Script**: The setup script generates a new JavaScript file named `my_paybrush.js` in the same directory.

2. **Initialize Google Cloud SDK**: If you haven't already done so, initialize the Google Cloud SDK by running:
   ```
   gcloud init
   ```
   Follow the instructions to log in and set up your GCP project.

3. **Deploy to Cloud Run**: Deploy the generated script as a Google Cloud Run service using the following command:
   ```
   gcloud run deploy my-paybrush --image=gcr.io/your_project_id/my_paybrush --platform=managed --region=us-central1
   ```
   Replace `your_project_id` with your actual GCP project ID.

4. **Verify Deployment**: GCP will provide a URL for your deployed service upon completion. Test this URL with a simulated PayPal IPN message to ensure everything is working as expected.

### Additional Notes

- Make sure the environment variables (`EMAIL_ADDRESS`, `EMAIL_PASSWORD`, `GCS_BUCKET_NAME`, `ZIP_FILE_NAME`) are correctly set in your Cloud Run service's settings.
- For security, avoid hardcoding sensitive information. Utilize GCP's Secret Manager or environment variables for configuration.
- Regularly review your Cloud Run service's logs and update dependencies to address any issues or vulnerabilities.
