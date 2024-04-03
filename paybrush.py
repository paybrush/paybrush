import os

def main():
    print("Welcome to the PayBrush setup wizard.")
    email_address = input("Enter your email address: ")
    email_password = input("Enter your email password: ")
    company_name = input("Enter your company name: ").replace(" ", "_")
    gcs_bucket_name = input("Enter your Google Cloud Storage bucket name: ")
    zip_file_name = input("Enter the name of your ZIP file stored in GCS: ")
    
    template = f"""import os
import smtplib
from email.message import EmailMessage
from flask import Flask, request, jsonify
from google.cloud import storage

app = Flask(__name__)

# Environment variables
EMAIL_ADDRESS = "{email_address}"
EMAIL_PASSWORD = "{email_password}"
GCS_BUCKET_NAME = "{gcs_bucket_name}"
ZIP_FILE_NAME = "{zip_file_name}"

@app.route('/paypal_listener', methods=['POST'])
def paypal_listener():
    # Extract the payer's email from PayPal IPN data
    email_address = request.form['payer_email']
    process_payment_and_send_email(email_address)
    return jsonify({{'status': 'success'}}), 200

def send_email_with_attachment(recipient_email, attachment_path):
    # Create email message with attachment
    msg = EmailMessage()
    msg['Subject'] = 'Your Purchase from {company_name}'
    msg['From'] = EMAIL_ADDRESS
    msg['To'] = recipient_email
    msg.set_content('Attached is the ZIP file you purchased.')

    # Attach the ZIP file
    with open(attachment_path, 'rb') as f:
        file_data = f.read()
        file_name = os.path.basename(f.name)
    msg.add_attachment(file_data, maintype='application', subtype='zip', filename=file_name)

    # Send the email via SMTP
    with smtplib.SMTP_SSL('smtp.protonmail.com', 465) as smtp:
        smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        smtp.send_message(msg)

def process_payment_and_send_email(email_address):
    # Download the ZIP file from GCS and send it via email
    source_blob_name = ZIP_FILE_NAME
    destination_file_name = '/tmp/' + ZIP_FILE_NAME
    
    storage_client = storage.Client()
    bucket = storage_client.bucket(GCS_BUCKET_NAME)
    blob = bucket.blob(source_blob_name)
    blob.download_to_filename(destination_file_name)

    send_email_with_attachment(email_address, destination_file_name)

if __name__ == "__main__":
    app.run()
    """
    
    # Generate a new file with the user's configuration
    filename = f"{company_name}_paybrush.py"
    with open(filename, "w") as file:
        file.write(template)
    
    print(f"Setup complete. Your custom script has been saved as {filename}")

if __name__ == "__main__":
    main()
