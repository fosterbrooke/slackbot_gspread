import gspread
from oauth2client.service_account import ServiceAccountCredentials
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError

# Setup the credentials for Google Sheets
# scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
scope = ["https://www.googleapis.com/auth/spreadsheets.readonly"]
creds = ServiceAccountCredentials.from_json_keyfile_name('./credential.json', scope)
client = gspread.authorize(creds)

# Open the Google Sheet by ID and get the data
spreadsheet_id = ''
sheet = client.open_by_key(spreadsheet_id).sheet1
slack_ids = sheet.col_values(1)  # Assumes Slack IDs are in the first column

# Setup the Slack client
slack_token = ''
client = WebClient(token=slack_token)

# Define your custom message
message = "Hello, this is a custom message!"

# Send messages to each Slack ID
for slack_id in slack_ids:
    try:
        response = client.chat_postMessage(
            channel=slack_id,
            text=message
        )
        print(f"Message sent to {slack_id}: {response['ok']}")
    except SlackApiError as e:
        print(f"Error sending message to {slack_id}: {e.response['error']}")