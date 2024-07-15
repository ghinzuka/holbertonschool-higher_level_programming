
def generate_invitations(template, attendees):
    if not isinstance(template, str):
        print("Error :template must be a string")
    if not isinstance(attendees, list) or not all(isinstance(a, dict) for a in attendees):
        print("Error: attendees must be a list of dictionnaires")
    