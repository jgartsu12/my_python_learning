name = 'Seb'
product = 'Python e course'
# f formats to run python code inside of email_content
email_content= f""" 
Hi {name}

Thank you for purchasing {product}

Regards,

Sales Team
"""

print(email_content) 
# str interpolation built for dynamic sys so u dont have to hard code everything and wrap elements like product or name and customize to build sys and run custom