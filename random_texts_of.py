from twilio.rest import Client
import time, threading
import random

def random_love_note():
    account_sid = ''
    auth_token = ''

    client = Client(account_sid, auth_token)

    partner_name = ''
    txt_messages_to_send = [
        'You are the source of my joy, the center of my world and the whole of my heart.',
        'When I tell you I love you, I am not saying it out of habit, I am reminding you that you are my life.',
        'I don’t need paradise because I found you. I don’t need dreams because I already have you.',
        'You are the last thought in my mind before I drift off to sleep and the first thought when I wake up each morning.',
        'Everywhere I look I am reminded of your love. You are my world.',
        "Love is not about how many days, weeks or months you’ve been together it’s all about how much you love each other every day.",
        'If I know what love is, it is because of you',
        'You are my paradise and I would happily get stranded on you for a lifetime',
        'I can’t stop thinking about you, today... tomorrow... always.',
        'When I look into your eyes I see the mirror of my soul',
        'This is all I want to do with you forever.',
        'Thank you for always being my rainbow after the storm.',
        'I am so totally, completely, overwhelmingly, eye-poppingly, life-changingly, spectacularly, passionately, deliciously in love with you.',
        'God is keeping me alive but you are keeping me in love.',
        'My angel, my life, my entire world, you’re the one that I want, the one that I need, let me be with you always, my love, my everything.',
        'This morning I awoke and was reminded of the preciousness of life because of you.',
        'I love you every step of the way.',
        'Walk with me through life...and I’ll have everything I’ll need for the journey.',
        'I may not be your first date, kiss or love...but I want to be your last everything.',
        'The best feeling is when you look at him...and he is already staring.',
        "And then my soul saw you and it kind of went, 'Oh, there you are. I’ve been looking all over for you'",
        'Together with you is my favorite place to be.',
        'Good morning my love, our two souls aflame, with my man I feel two hearts beat the same.',
        'I am very indecisive and always have trouble picking my favorite anything. But, without a doubt, you are my favorite everything.',
        'I still fall in love with you every day',
        'The sun is up, the sky is blue, today is beautiful and so are you',
        'Thank you, my love, for always making me feel like the most beautiful woman in the world.',
        'Thank God someone threw me away so you could pick me up and love me',
        'If I had a flower for every time I thought of you, I could walk in my garden forever',
        'It is because of you, my angel, that I now understand all of those quotes about love.'
    ]

    random_choice = random.randint(0, len(txt_messages_to_send))
    complete_message = partner_name + ' ' + txt_messages_to_send[random_choice]

    message = client.messages.create(
        to='',
        from_='',
        body= complete_message)
    print('Message Sent. SID: ', message.sid)

    random_seconds_one = 3600
    random_seconds_two = 20000
    random_seconds_to_send = random.randint(random_seconds_one, random_seconds_two)

    threading.Timer(random_seconds_to_send, random_love_note).start()

if __name__ == '__main__':
    random_love_note()