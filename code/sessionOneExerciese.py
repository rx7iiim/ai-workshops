emails = [
    "Win a free iPhone now! Click this link!",
    "Meeting tomorrow at 10 AM.",
    "Limited offer!!! Get 90%,discount!",
    "Please find attached the project report.",
    "You won a lottery! Claim your prize now!",
    "Let's schedule our weekly sync-up.",
    "Exclusive deal just for you!",
    "Your flight ticket is confirmed.",
    "Earn money fast with this trick!",
    "See you at the office today."
]

spam_keywords = ['free', 'offer', 'iphone', 'link', 'lottery', '!!!', 'earn', 'deal', 'discount']

for email in emails:
    text = email.lower()
    is_spam = False

    for word in spam_keywords:
        if word in text:
            is_spam = True
            break

    if is_spam:
        print(email, "SPAM")
    else:
        print(email, " NOT SPAM")
