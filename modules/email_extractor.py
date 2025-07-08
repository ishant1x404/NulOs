import random

# Predefined fake profiles for known numbers
KNOWN_PROFILES = {
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

# Fallback random name pools
RANDOM_NAMES = ["Anjali Patel", "Ravi Kumar", "Sana Shaikh", "Mohit Rathi", "Neha Verma", "Kunal Joshi"]
RANDOM_COMPANIES = ["Infosys", "Google", "Amazon", "HCL", "Flipkart", "Freelancer"]

def extract_identity(number):
    """
    Simulates identity extraction using known database or randomized values.
    Designed to be replaced with real scraping logic in NulOs v2.0.
    """
    if number in KNOWN_PROFILES:
        return KNOWN_PROFILES[number]

    # Generate realistic dummy data
    name = random.choice(RANDOM_NAMES)
    company = random.choice(RANDOM_COMPANIES)
    username = name.lower().replace(" ", "")
    email = f"{username}{random.randint(10,99)}@gmail.com"
    source = f"https://search-results.fake/{username}"

    return {
        "name": name,
        "email": email,
        "company": company,
        "source": source
    }

# 📌 FOR V2.0: Add actual scraping here
# def extract_real_identity(number):
#     # 1. Search email leaks databases
#     # 2. Search Pastebin, GitHub, social media
#     # 3. Use real patterns or regex
#     pass
