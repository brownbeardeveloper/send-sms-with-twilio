Setup Instructions

To get the Twilio text message app working, follow the steps below:
1. Create a Twilio Account

    Go to Twilio's website and sign up for an account.
    After signing up, navigate to your Twilio Console to access your Account SID and Auth Token.

2. Obtain the Messaging Service SID

    In the Twilio Console, go to Messaging and create a new Messaging Service. You will need this Messaging Service SID to send messages.

3. Create a .env File

    In the root of your project, create a .env file.
    Add the following values to the .env file:
    
    TWILIO_AUTH_TOKEN=your_auth_token_here
    TWILIO_ACCOUNT_SID=your_account_sid_here
    MESSAGING_SERVICE_SID=your_messaging_service_sid_here
    MY_PHONE_NUMBER=your_phone_number_here
