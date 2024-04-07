# Paybrush

This guide details the process of deploying your customized Paybrush solution on Google Cloud Platform (GCP), from initial script setup to deployment and testing, with an added focus on setting up Gmail OAuth2 for email functionalities.

### **Step 1: Preparing Your Environment**
- **Install Node.js:** Ensure Node.js is installed on your system. Download from [nodejs.org](https://nodejs.org/).
- **Install Google Cloud SDK:** Download and install the Google Cloud SDK from [cloud.google.com/sdk](https://cloud.google.com/sdk). For Homebrew users:
  ```sh
  brew install --cask google-cloud-sdk
  ```

### **Step 2: Setting Up Gmail OAuth2 Authentication**
**OAuth 2.0 Setup:**
1. **Google Cloud Console Setup:**
   - Go to the [Google Cloud Console](https://console.cloud.google.com/).
   - Choose or create a project.
   - Navigate to "APIs & Services" > "Library", search for "Gmail API", and enable it.

2. **Create OAuth 2.0 Credentials:**
   - In "APIs & Services" > "Credentials", click "Create Credentials" > "OAuth client ID".
   - Select "Web application" and set up the consent screen with the required information.
   - Under "Authorized redirect URIs", add `https://developers.google.com/oauthplayground` for testing.
   - Copy your "Client ID" and "Client Secret". You will use this later to customize your script.

**OAuth 2.0 Playground for Tokens:**
1. **Authorize APIs:**
   - Visit the [OAuth 2.0 Playground](https://developers.google.com/oauthplayground).
   - Click the gear icon ⚙️ in the top right corner, check the box for "Use your own OAuth credentials", and enter your copied Client ID and Client Secret from earlier.
   - Input `https://mail.google.com/` in "Input your own scopes" and click "Authorize APIs".

2. **Exchange Authorization Code for Tokens:**
   - After authorization, click "Exchange authorization code for tokens" in Step 2 of the Playground.
   - Copy the "Refresh Token". You will use this later to customize your script.

**Integration:**
- Use the "Refresh Token" along with your "Client ID" and "Client Secret" in your application for authenticating email requests with Nodemailer.

**Note:**
- Securely store the "Client Secret" and "Refresh Token" as they provide access to your Google account.

**Uploading a Zip File to Google Cloud Storage**

1. **Create a Cloud Storage Bucket:**
   - Navigate to the Cloud Storage section in the Google Cloud Console.
   - Click on "Create Bucket."
   - Enter the bucket name, choose a location, and configure other settings as needed.
   - Click "Create" to create the bucket.
   - Copy the bucket name. You will use this later to customize your script.

2. **Upload Zip File to Bucket:**
   - Select the bucket you just created.
   - Click on the "Upload files" button.
   - Choose the zip file from your local system and upload it to the bucket.
   - Once uploaded, the zip file will be available in your Cloud Storage bucket.
   - Copy the zip file name (Including .zip). You will use this later to customize your script.

### **Step 3: Receiving and Saving the Script**
- **Receive `paybrush.js` Via Email:** Look for an email from Paybrush with the `paybrush.js` setup script.
- **Save the Script:** Download and save the script to a preferred directory on your computer.

### **Step 4: Running the Setup Script**
- **Navigate to Script Directory:** Open a terminal and change to the directory where you saved `paybrush.js`.
  ```sh
  cd path_to_saved_script
  ```
- **Execute `paybrush.js`:** Run the setup script using Node.js. This script will prompt for inputs required to customize the application.
  ```sh
  node paybrush.js
  ```
- **Enter Required Information:** Input your Gmail address, OAuth2 credentials (Client ID, Client Secret, Refresh Token), company name, Google Cloud Storage bucket name, and ZIP file name.

### Step 5: Deploying to Google Cloud Platform

After finalizing your `function.js` script, you're ready to deploy it to Google Cloud Platform as a Cloud Function. This allows your code to be triggered via HTTP requests, such as those you might simulate from PayPal for testing or real transactions.

**Access Generated Script**:
- `paybrush.js` creates a new JavaScript file, `function.js`, in the same directory.

**Initialize Google Cloud SDK**:
- If not already done, initialize the SDK by opening your terminal and running:
  ```sh
  gcloud init
  ```
- Follow the prompts to authenticate and select your Google Cloud project.

**Deploy Your Function**:
- Deploy your function to Google Cloud Functions using the Google Cloud CLI with the following command. Ensure you're in the directory containing your `function.js` file.
  ```sh
  gcloud functions deploy paypalListener --runtime nodejs16 --trigger-http --allow-unauthenticated --entry-point paypalListener --source .
  ```
- This command deploys your function named `paypalListener` with Node.js 16 as the runtime. The `--trigger-http` flag specifies that the function will be triggered by HTTP requests, and `--allow-unauthenticated` allows it to be invoked without authentication (note: consider your authentication requirements for production use).

#### Testing Your Cloud Function

After deployment, you can simulate a PayPal IPN message to your function to test its behavior. Use `curl` to send a POST request mimicking a PayPal payment notification:

```sh
curl -X POST https://us-central1-your-project-id.cloudfunctions.net/paypalListener \
-H "Content-Type: application/json" \
-d '{"payer_email": "youremail@example.com"}'
```

- Replace `https://us-central1-your-project-id.cloudfunctions.net/paypalListener` with the actual URL provided after deploying your Cloud Function.
- Modify the JSON payload (`-d` option) as needed to simulate different IPN messages from PayPal.

#### **Additional Notes**
- **Secure Configuration:** Use GCP's Secret Manager or environment variables to manage sensitive information securely.
- **Monitor and Update:** Regularly check your Cloud Run service's logs and update dependencies to mitigate vulnerabilities.
