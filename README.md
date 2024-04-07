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
  - Under "APIs & Services" > "Credentials", click "Create Credentials" > "OAuth client ID" for a web application, adding `https://developers.google.com/oauthplayground` under "Authorized redirect URIs".
  - Note your "Client ID" and "Client Secret".
- **OAuth 2.0 Playground**:
  - Visit [OAuth 2.0 Playground](https://developers.google.com/oauthplayground), click the gear icon ⚙️, check "Use your own OAuth credentials", input your credentials.
  - Authorize with `https://mail.google.com/` scope, exchange the authorization code for tokens, and note the "Refresh Token".

#### **3. Cloud Storage Setup**
- **Bucket Creation**:
  - In Cloud Storage, create a bucket, noting its name.
- **Zip File Upload**:
  - Upload your .zip file to the bucket, noting the file name (Including .zip).

#### **4. Script Setup**
- **Receive and Save Script**:
  - Download `paybrush.js` from your email and save it to a directory.
- **Run Script**:
  - Open a terminal, navigate to the script directory, and execute `node paybrush.js`. Input required information when prompted.

#### **5. Deployment**
- **Deploy Function**:
  - Use this command in the terminal within your script's directory:
    ```
    gcloud functions deploy paypalListener --runtime nodejs16 --trigger-http --allow-unauthenticated --entry-point paypalListener --source .
    ```

#### **6. Testing**
- **Simulate PayPal IPN**:
  - Test the function with `curl`, adjusting the URL and email payload as needed:
    ```
    curl -X POST https://us-central1-your-project-id.cloudfunctions.net/paypalListener -H "Content-Type: application/json" -d '{"payer_email": "youremail@example.com"}'
    ```
