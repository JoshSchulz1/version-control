import datetime


now = datetime.datetime.utcnow()

# Help from chatgpt to manually adjust to current timezone
timezone_offset = datetime.timedelta(hours=-8)
local_time = now + timezone_offset

formatted_time = local_time.strftime("%Y-%m-%d %H:%M:%S")


with open("version.md", "w") as file:
    file.write(f"Current date and time: {formatted_time}")

