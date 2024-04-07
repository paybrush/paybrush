# Paybrush

This guide outlines the process of setting up and deploying your Paybrush automation solution on Google Cloud Platform (GCP), leveraging Node.js for your application's backend.

### Step 1: Preparing Your Environment

- **Install Node.js**: Ensure Node.js is installed on your system. You can download it from [nodejs.org](https://nodejs.org/).
- **Install Google Cloud SDK**: To deploy applications to GCP, you need the Google Cloud SDK. Download and install it from [cloud.google.com/sdk](https://cloud.google.com/sdk). For Homebrew users:
  ```bash
  brew install --cask google-cloud-sdk
  ```

### Step 2: Setting Up Your Project

- **Receive Your Setup Script Via Email**: Check your email for a message from Paybrush, which will include the `index.js` (formerly `paybrush.py`) as an attachment.
- **Save the Script**: Download and save the `index.js` file to a directory on your computer where you wish to work.

### Step 3: Configuring Your Application

- **Open Your Terminal**: Navigate to the directory where `index.js` is saved.
  ```bash
  cd path_to_saved_script
  ```
- **Install Dependencies**: Before running your script, install necessary Node.js packages.
  ```bash
  npm install express @google-cloud/storage nodemailer body-parser
  ```
- **Customize Your Setup**: Modify `index.js` as needed to include your actual email credentials, Google Cloud Storage bucket name, and ZIP file name.

### Step 4: Deploying to Google Cloud Run

- **Initialize Google Cloud SDK**:
  ```bash
  gcloud init
  ```
  Follow the instructions to log in and set up your GCP project.

- **Containerize Your Application**: Create a `Dockerfile` in the same directory as your `index.js`.
  
- **Build and Push the Docker Image**:
  ```bash
  docker build -t gcr.io/your_project_id/my_paybrush .
  docker push gcr.io/your_project_id/my_paybrush
  ```

- **Deploy to Google Cloud Run**:
  ```bash
  gcloud run deploy my_paybrush --image gcr.io/your_project_id/my_paybrush --platform managed --region your_region --allow-unauthenticated
  ```

  Replace `your_project_id` and `your_region` with your Google Cloud project ID and desired region, respectively.

### Additional Notes

- **Environment Variables**: Ensure that environment variables for `EMAIL_ADDRESS`, `EMAIL_PASSWORD`, `GCS_BUCKET_NAME`, and `ZIP_FILE_NAME` are correctly configured in your deployment settings or code.
  
- **Security**: Avoid embedding sensitive data directly in your script. Use environment variables or GCP's Secret Manager for managing sensitive information securely.

- **Monitoring and Updates**: Regularly monitor your application's logs and update dependencies to address any potential security issues or functional improvements.
