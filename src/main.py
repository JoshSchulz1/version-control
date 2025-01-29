import datetime

# Get current date and time
now = datetime.datetime.now()
formatted_time = now.strftime("%Y-%m-%d %H:%M:%S")

# Write to version.md
with open("version.md", "w") as file:
    file.write(f"Current date and time: {formatted_time}")
