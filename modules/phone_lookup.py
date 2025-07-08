import phonenumbers
from phonenumbers import geocoder, carrier, timezone

def lookup_number(number):
    """
    Parses phone number and extracts region, carrier, timezone, etc.
    Returns structured dictionary even if data is missing.
    """
    try:
        parsed = phonenumbers.parse(number, None)

        if not phonenumbers.is_valid_number(parsed):
            return {"valid": False, "error": "Invalid phone number."}

        # Safely extract info with defaults
        region = geocoder.description_for_number(parsed, "en") or "Unknown"
        sim_carrier = carrier.name_for_number(parsed, "en") or "Unknown"
        timezones = timezone.time_zones_for_number(parsed)
        country_code = parsed.country_code
        national_number = parsed.national_number

        return {
            "valid": True,
            "region": region,
            "carrier": sim_carrier,
            "timezones": list(timezones),
            "country_code": country_code,
            "national_number": national_number
        }

    except Exception as e:
        return {
            "valid": False,
            "error": str(e)
        }
