def current_users(events):
  # Sort the events by date
  events.sort(key=get_event_date)

  # Create a dictionary to store the machines and their users
  machines = {}

  # Iterate through the events
  for event in events:
    # If the machine is not in the dictionary, add it
    if event.machine not in machines:
      machines[event.machine] = set()

    # If the event is a login, add the user to the set for that machine
    if event.type == "login":
      machines[event.machine].add(event.user)

    # If the event is a logout, remove the user from the set for that machine
    elif event.type == "logout":
      machines[event.machine].remove(event.user)

  # Return the dictionary of machines and users
  return machines

# Generate a report of the current users on each machine
def generate_report(machines):
  # Iterate through the machines and users
  for machine, users in machines.items():
    # If there are any users on the machine, print a report
    if len(users) > 0:
      # Join the users into a comma-separated string
      user_list = ", ".join(users)

      # Print the report
      print("{}: {}".format(machine, user_list))

#### Logged users

def get_event_date(event):
  return event.date

def current_users(events):
  events.sort(key=get_event_date)
  machines = {}
  for event in events:
    if event.machine not in machines:
      machines[event.machine] = set()
    if event.type == "login":
      machines[event.machine].add(event.user)
    elif event.type == "logout":
      machines[event.machine].remove(event.user)
  return machines

def generate_report(machines):
  for machine, users in machines.items():
    if len(users) > 0:
      user_list = ", ".join(users)
      print("{}: {}".format(machine, user_list))

class Event:
  def __init__(self, event_date, event_type, machine_name, user):
    self.date = event_date
    self.type = event_type
    self.machine = machine_name
    self.user = user

events = [
  Event('2020-01-21 12:45:46', 'login', 'myworkstation.local', 'jordan'),
  Event('2020-01-22 15:53:42', 'logout', 'webserver.local', 'jordan'),
  Event('2020-01-21 18:53:21', 'login', 'webserver.local', 'lane'),
  Event('2020-01-22 10:25:34', 'logout', 'myworkstation.local', 'jordan'),
  Event('2020-01-21 08:20:01', 'login', 'webserver.local', 'jordan'),
  Event('2020-01-23 11:24:35', 'login', 'mailserver.local', 'chris'),
]

users = current_users(events)
print(users)

generate_report(users)

# in the course shoud write this: 
# {'webserver.local': {'lane'}, 'myworkstation.local': set(), 'mailserver.local': {'chris'}}
# webserver.local: lane
# mailserver.local: chris