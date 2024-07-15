from task_00_intro import generate_invitations
import os

if __name__ == "__main__":
    
    template_file = 'template.txt'
    if os.path.exists(template_file):
        with open(template_file, 'r') as file:
            template_content = file.read()
    else:
        print(f"Error: {template_file} does not exist.")
        template_content = ""

    # List of attendees
    attendees = [
        {"name": "Alice", "event_title": "Python Conference", "event_date": "2023-07-15", "event_location": "New York"},
        {"name": "Bob", "event_title": "Data Science Workshop", "event_date": "2023-08-20", "event_location": "San Francisco"},
        {"name": "Charlie", "event_title": "AI Summit", "event_date": None, "event_location": "Boston"}
    ]

    # Call the function with the template and attendees list
    generate_invitations(template_content, attendees)