# modules/email_extractor.py

import random

def extract_identity(number):
    # Realistic mock data for known numbers
    known_data = {
        "+919876543210": {
            "name": "Rahul Mehta",
            "email": "rahul.mehta92@gmail.com",
            "company": "TCS",
            "source": "https://www.linkedin.com/in/rahulmehta"
        },
        "+918888888888": {
            "name": "Priya Sharma",
            "email": "priya.s@gmail.com",
            "company": "Wipro",
            "source": "https://github.com/priyasharma"
        },
        "+917654321098": {
            "name": "Aman Verma",
            "email": "aman.v@outlook.com",
            "company": "Freelancer",
            "source": "https://pastebin.com/raw/xyz987"
        }
    }

    if number in known_data:
        return known_data[number]

    # Random fallback
    names = ["Anjali Patel", "Ravi Kumar", "Sana Shaikh", "Mohit Rathi"]
    companies = ["Infosys", "Google", "HCL", "Startups", "Amazon"]
    name = random.choice(names)
    company = random.choice(companies)
    username = name.lower().replace(" ", "")
    email = f"{username}{random.randint(10,99)}@gmail.com"
    source = f"https://search-results.fake/{username}"

    return {
        "name": name,
        "email": email,
        "company": company,
        "source": source
    }
