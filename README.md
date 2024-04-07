# Paybrush

This guide details the process of deploying your customized Paybrush solution on Google Cloud Platform (GCP), from initial script setup to deployment and testing, with an added focus on setting up Gmail OAuth2 for email functionalities.

#### **Step 1: Preparing Your Environment**
- **Install Node.js:** Ensure Node.js is installed on your system. Download from [nodejs.org](https://nodejs.org/).
- **Install Google Cloud SDK:** Download and install the Google Cloud SDK from [cloud.google.com/sdk](https://cloud.google.com/sdk). For Homebrew users:
  ```sh
  brew install --cask google-cloud-sdk
  ```

#### **Step 2: Setting Up Gmail OAuth2 Authentication**

**OAuth 2.0 Setup:**
1. **Google Cloud Console Setup:**
   - Go to the [Google Cloud Console](https://console.cloud.google.com/).
   - Choose or create a project.
   - Navigate to "APIs & Services" > "Library", search for "Gmail API", and enable it.

2. **Create OAuth 2.0 Credentials:**
   - In "APIs & Services" > "Credentials", click "Create Credentials" > "OAuth client ID".
   - Select "Web application" and set up the consent screen with the required information.
   - Under "Authorized redirect URIs", add `https://developers.google.com/oauthplayground` for testing.
   - Note your "Client ID" and "Client Secret".

**OAuth 2.0 Playground for Tokens:**
1. **Authorize APIs:**
   - Visit the [OAuth 2.0 Playground](https://developers.google.com/oauthplayground).
   - Input `https://mail.google.com/` in "Input your own scopes" and click "Authorize APIs".

2. **Exchange Authorization Code for Tokens:**
   - After authorization, click "Exchange authorization code for tokens" in Step 2 of the Playground.
   - Copy the "Refresh Token" and "Access Token" (optional).

**Integration:**
- Use the "Refresh Token" along with your "Client ID" and "Client Secret" in your application for authenticating email requests with Nodemailer.

**Note:**
- Securely store the "Client Secret" and "Refresh Token" as they provide access to your Google account.

#### **Step 3: Receiving and Saving the Script**
- **Receive `paybrush.js` Via Email:** Look for an email from Paybrush with the `paybrush.js` setup script.
- **Save the Script:** Download and save the script to a preferred directory on your computer.

#### **Step 4: Running the Setup Script**
- **Navigate to Script Directory:** Open a terminal and change to the directory where you saved `paybrush.js`.
  ```sh
  cd path_to_saved_script
  ```
- **Execute `paybrush.js`:** Run the setup script using Node.js. This script will prompt for inputs required to customize the application.
  ```sh
  node paybrush.js
  ```
- **Enter Required Information:** Input your Gmail address, OAuth2 credentials (Client ID, Client Secret, Refresh Token), company name, Google Cloud Storage bucket name, and ZIP file name.

#### **Step 5: Deploying to Google Cloud Platform**
- **Access Generated Script:** `paybrush.js` creates a new JavaScript file, `my_paybrush.js`, in the same directory.
- **Initialize Google Cloud SDK:** If not already done, initialize the SDK:
  ```sh
  gcloud init
  ```
- **Deploy to Cloud Run:** Use the Google Cloud CLI to deploy the generated script. Note: Deployment steps may vary based on the specifics of your project and the authentication method chosen for Google Cloud Run.
- **Verify Deployment:** Access the URL provided by GCP to ensure the service is operational.

#### **Additional Notes**
- **Secure Configuration:** Use GCP's Secret Manager or environment variables to manage sensitive information securely.
- **Monitor and Update:** Regularly check your Cloud Run service's logs and update dependencies to mitigate vulnerabilities.
