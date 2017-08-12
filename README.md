This piece of code allows you to use Twilo's API to send a random message of your choosing to a pre-defined number.

You must have a Twilio account to use.

The following fields must be filled in:
account_sid = ''(from Twilio)
auth_token = '' (from Twilio)
partner_name = '' (the name of the person to address the text)
to='' (the person's phone number)
from_='' (your Twilio phone number)
random_seconds_one = 3600 (the min. seconds to pass before sending a message)
random_seconds_two = 20000 (the max. seconds to pass before sending a message)

You may edit the list, txt_messages_to_send, with a list of messages of your choosing. The Python script will choose a random message
to send.
