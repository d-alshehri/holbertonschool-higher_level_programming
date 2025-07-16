import os

def generate_invitations(template, attendees):
    # Check for valid input types
    if not isinstance(template, str):
        print("Error: Template must be a string.")
        return

    if not isinstance(attendees, list) or not all(isinstance(a, dict) for a in attendees):
        print("Error: Attendees must be a list of dictionaries.")
        return

    # Check for empty inputs
    if template.strip() == "":
        print("Template is empty, no output files generated.")
        return

    if not attendees:
        print("No data provided, no output files generated.")
        return

    # Generate files
    for index, attendee in enumerate(attendees, start=1):
        content = template
        for key in ["name", "event_title", "event_date", "event_location"]:
            value = attendee.get(key)
            content = content.replace(f"{{{key}}}", str(value) if value else "N/A")

        output_filename = f"output_{index}.txt"
        with open(output_filename, 'w') as file:
            file.write(content)
