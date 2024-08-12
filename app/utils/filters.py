from datetime import datetime

def format_date(date):
  return date.strftime('%m/%d/%y')

def format_url(url):
  return url.replace('http://', '').replace('https://', '').replace('www.', '').split('/')[0].split('?')[0]

def format_plural(amount, singular, plural=None):
    print(f"Debug: Amount received: {amount}")
    if not isinstance(amount, int):
        try:
            amount = int(amount)
        except ValueError:
            raise ValueError("Amount must be an integer or convertible to an integer")
    
    if plural is None:
        plural = singular + 's'
    
    return f"{amount} {singular if amount == 1 else plural}"
