import os


def generate_invitations(template, attendees):
    if not isinstance(template, str):
        print("Error :template must be a string")
        return
    
    if not isinstance(attendees, list) or not all(isinstance(attendee, dict) for attendee in attendees):
        print("Error: attendees must be a list of dictionnaires")
        return
    
    if not template.strip():
        print("Template is empty, no output files generated.")
        return
    
    if not attendees:
        print("Template is empty, no output files generated.")
        return
    
    for x, attendee in enumerate(attendees, start=1):
        content = template
        content = content.replace("{name}", attendee.get("name")if attendee.get("name") is not None else "N/A")
        content = content.replace("{event_title}", attendee.get("event_title")if attendee.get("event_title") is not None else "N/A")
        content = content.replace("{event_date}", attendee.get("event_date")if attendee.get("event_date") is not None else "N/A")
        content = content.replace("{event_location}", attendee.get("event_location")if attendee.get("event_location") is not None else "N/A")
        
        output_file = f"output_{x}.txt"
        
        if os.path.exists(output_file):
            print(f"Error: {output_file} already exists. Skipping.")
            continue
        
        try:
            with open(output_file, 'w') as file:
                file.write(content)
            print(f"Generated {output_file}")
        except Exception as e:
            print(f"Error writ0ing to {output_file}: {e}")