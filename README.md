# Paybrush 

Welcome to the quick setup guide for deploying your Paybrush solution. Save your **Client ID**, **Client Secret**, and **Refresh Token** along the way. This straightforward process is designed to get you up and running in about 30 minutes 🙂

#### **1. Environment Setup**
- **Node.js**: Install from [nodejs.org](https://nodejs.org/).
- **Google Cloud SDK**: Install from [cloud.google.com/sdk](https://cloud.google.com/sdk). Homebrew command:
  ```
  brew install --cask google-cloud-sdk
  ```
#### **2. Gmail OAuth2 Authentication Setup**
- **Google Cloud Console**:
  - Open [Google Cloud Console](https://console.cloud.google.com/), select/create a project, enable the Gmail API under "APIs & Services" > "Library".
- **OAuth 2.0 Credentials**:
  - Under "APIs & Services" > "Credentials", click "Create Credentials" > "OAuth client ID". If needed, "Configure Consent Screen" > "External". Enter app name and email then save and continue until complete and publish app. Return to "Credentials", click "Create Credentials" > "OAuth client ID", for a web application, adding `https://developers.google.com/oauthplayground` under "Authorized redirect URIs".
  - Note your "Client ID" and "Client Secret".
- **OAuth 2.0 Playground**:
  - Visit [OAuth 2.0 Playground](https://developers.google.com/oauthplayground), click the gear icon ⚙️, check "Use your own OAuth credentials", input your credentials.
  - Authorize with `https://mail.google.com/` scope, exchange the authorization code for tokens, and note the "Refresh Token". If needed, if "Google hasn’t verified this app", then click "Advanced" > "Go to APP_NAME" > "Continue".
  - ☑️ Check auto-refresh the token

#### **3. Google Drive Share Link Setup**

- **Google Drive File Preparation**:
  - Upload the files or folder containing your digital product to your Google Drive.
  - Right-click the file or folder, select "Get link," then choose "Anyone with the link" under General access.

- **Share Link Generation**:
  - Once the access level is set to "Anyone with the link," copy the shareable link provided by Google Drive.
  - Note this link. You will use it later to customize your script to automatically send it to customers after their purchase.

#### **4. Script Setup**
- **Receive and Save Script**:
  - Download `Paybrush.zip` from the link in your email and unzip the file.
- **Run Script**:
  - Open a terminal, navigate to the script directory, and execute `node paybrush.js`. Input required information when prompted.

#### **5. Deployment**
- **Deploy Function**:
  - Use these commands in the terminal within your script's directory:
    ```
    gcloud init           
    ```
    Replace PROJECT_ID with your Google Cloud project ID:
    ```
    gcloud config set project PROJECT_ID           
    ```
    Deploy your cloud function:
    ```
    gcloud functions deploy paypalListener --runtime nodejs16 --trigger-http --allow-unauthenticated --entry-point paypalListener --source .
    ```
    If there is a permissions error, run this command and redeploy again after. Replace PROJECT_ID with your Google Cloud project ID:
    ```
    gcloud projects add-iam-policy-binding PROJECT_ID \
    --member="serviceAccount:PROJECT_ID@appspot.gserviceaccount.com" \
    --role="roles/artifactregistry.reader"
    ```
    
#### **6. Testing**
- **Simulate PayPal IPN**:
  - Test the function with `curl`. Read the output after deploying under "httpsTrigger" > "url". Adjust the URL after POST and the email payload as needed for this command:
    ```
    curl -X POST https://us-central1-your-project-id.cloudfunctions.net/paypalListener -H "Content-Type: application/json" -d '{"payer_email": "youremail@example.com"}'
    ```

#### **7. Setup PayPal IPN**
- **Get Cloud Function URL**: In Google Cloud Console, under Cloud Functions, find your function `paypalListener` and copy its Trigger URL.
- **Configure IPN in PayPal**:
  - For detailed PayPal IPN setup, visit: [What is Instant Payment Notification or IPN?](https://www.paypal.com/us/cshelp/article/what-is-instant-payment-notification-or-ipn-help188).
  - Paste your function's Trigger URL into the "Notification URL" field.
  - Congratulations, your setup is now complete.

If you have any questions or need support, you can find our contacts at [paybru.sh](https://paybru.sh/).

© 2024 Paybrush
