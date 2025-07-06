import phonenumbers
from phonenumbers import geocoder, carrier

def lookup_number(number):
    try:
        # Parse the number (e.g., "+919876543210")
        parsed_number = phonenumbers.parse(number)

        # Get country/location (like "Madhya Pradesh")
        region = geocoder.description_for_number(parsed_number, "en")

        # Get carrier (like "Airtel")
        service_provider = carrier.name_for_number(parsed_number, "en")

        # Get country code (like "IN")
        country_code = parsed_number.country_code
        national_number = parsed_number.national_number

        return {
            "region": region,
            "carrier": service_provider,
            "country_code": country_code,
            "national_number": national_number,
            "valid": phonenumbers.is_valid_number(parsed_number)
        }

    except Exception as e:
        return {
            "error": str(e),
            "valid": False
        }
