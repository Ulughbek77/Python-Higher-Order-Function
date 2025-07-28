emails = ["ali@gmail.com", "vali@yahoo.com", "sami@gmail.com", "bek@outlook.com"]
gmail_users = list(filter(lambda email: "@gmail.com" in email, emails))
print(gmail_users)  
