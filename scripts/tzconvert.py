from datetime import datetime
import pytz

# 🔁 Abbreviations to full tz database names
ABBREVIATION_MAP = {
    "CET": "Europe/Paris",  # Central European Time
    "IST": "Asia/Kolkata",  # India Standard Time
    "EST": "US/Eastern",  # Eastern Standard Time
    "CST": "US/Central",  # Central Standard Time
    "MST": "US/Mountain",  # Mountain Standard Time
    "PST": "US/Pacific",  # Pacific Standard Time
    "AKST": "US/Alaska",  # Alaska Standard Time
    "HST": "US/Hawaii",  # Hawaii Standard Time
    "BRT": "America/Sao_Paulo",  # Brazil
    "ART": "America/Argentina/Buenos_Aires",  # Argentina
    "CLT": "America/Santiago",  # Chile
    "GMT": "Europe/London",  # GMT/London
    "AEST": "Australia/Sydney",  # Australian Eastern
    "NZST": "Pacific/Auckland",  # New Zealand Standard Time
}

# 🌍 Friendly name map
COMMON_TIMEZONES = {
    "UTC": "UTC",
    "New York": "US/Eastern",
    "Chicago": "US/Central",
    "Denver": "US/Mountain",
    "Los Angeles": "US/Pacific",
    "Anchorage": "US/Alaska",
    "Honolulu": "US/Hawaii",
    "Mexico City": "America/Mexico_City",
    "Santiago": "America/Santiago",
    "Buenos Aires": "America/Argentina/Buenos_Aires",
    "São Paulo": "America/Sao_Paulo",
    "London": "Europe/London",
    "Paris/Berlin": "Europe/Paris",
    "Moscow": "Europe/Moscow",
    "Tokyo": "Asia/Tokyo",
    "Kolkata": "Asia/Kolkata",
    "Beijing": "Asia/Shanghai",
    "Sydney": "Australia/Sydney",
    "Auckland": "Pacific/Auckland"
}


# 🔎 Resolve input (abbreviation or friendly name) to a valid pytz timezone
def resolve_timezone(tz_input):
    tz_input = tz_input.strip()

    # Try abbreviation
    if tz_input.upper() in ABBREVIATION_MAP:
        return ABBREVIATION_MAP[tz_input.upper()]

    # Try friendly names (case-insensitive)
    for label, tz in COMMON_TIMEZONES.items():
        if tz_input.lower() == label.lower():
            return tz

    # Assume it's already a valid pytz timezone
    return tz_input


# 🌐 Print friendly timezone list
def list_timezones():
    print("📍 Common Timezones:")
    for city, tz in COMMON_TIMEZONES.items():
        print(f" - {city}: {tz}")
    print("\n💡 Tip: You can also use abbreviations like 'CET', 'IST', 'EST', or full names like 'Asia/Tokyo'.")


# 🔄 Time conversion logic
def convert_timezone(date_str, from_zone_str, to_zone_str):
    try:
        naive_datetime = datetime.strptime(date_str, "%Y-%m-%d %H:%M")
        from_zone = pytz.timezone(from_zone_str)
        to_zone = pytz.timezone(to_zone_str)
        from_datetime = from_zone.localize(naive_datetime)
        to_datetime = from_datetime.astimezone(to_zone)

        print(f"\n✅ Converted Time: {to_datetime.strftime('%Y-%m-%d %H:%M (%Z%z)')}")
    except Exception as e:
        print(f"❌ Error: {e}")


# 🚀 Main interface
def main():
    print("=== 🌐 Universal Time Converter ===")
    list_timezones()

    date_str = input("\n🕒 Enter date and time (YYYY-MM-DD HH:MM): ").strip()
    from_input = input("🌍 Enter source timezone (e.g., CET, US/Eastern, Mexico City): ").strip()
    to_input = input("🌏 Enter target timezone (e.g., IST, Asia/Kolkata, Tokyo): ").strip()

    from_zone = resolve_timezone(from_input)
    to_zone = resolve_timezone(to_input)

    convert_timezone(date_str, from_zone, to_zone)


if __name__ == "__main__":
    main()
