
def convert_date_format(date_str):
    # Assumes input is in "YYYY-MM-DD"
    try:
        parts = date_str.split('-')
        if len(parts) != 3:
            raise ValueError
        yyyy, mm, dd = parts
        if len(yyyy) != 4 or len(mm) != 2 or len(dd) != 2:
            raise ValueError
        return f"{dd}-{mm}-{yyyy}"
    except Exception:
        return "Invalid input"

