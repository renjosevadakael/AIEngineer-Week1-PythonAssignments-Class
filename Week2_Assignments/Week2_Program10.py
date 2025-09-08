""" Assignment Details: 
 
Create a Python program to manage bug records using a class and a dictionary. 
 
Requirements: 
a) Create a class named BugTracker. 
b) Inside the class, maintain an attribute bugs as a dictionary, where each key is a bug ID and the 
value is another dictionary containing details (description, severity, status). 
c) Implement the following methods: 
1. add_bug(bug_id, description, severity) → adds a new bug with status "Open". 
2. update_status(bug_id, new_status) → updates the status of a given bug (e.g., Open 
→ In Progress → Closed). 
3. list_all_bugs() → prints details of all bugs in a readable format. 
d) In the main section (if __name__ == "__main__":): 
o Create a BugTracker object. 
o Add at least three bugs with different IDs, descriptions, and severities. 
o Update the status of one bug to "In Progress" and another to "Closed". 
o Display all bugs with their details. 
bugs = {
    "BUG001": {
        "description": "Login button not working",
        "severity": "High",
        "status": "Open"
    },
    "BUG002": {
        "description": "Typo in homepage title",
        "severity": "Low",
        "status": "Open"
    },
    ...
}



"""


class BugTracker:
    def __init__(self):
        #Dictonary bugs:{bug_id:{description, severity, status}}
        self.bugs={}
    def add_bug(self,bug_id, description, severity):
        self.bugs[bug_id]={
            "description" :description,
            "severity":severity,
            "status":"Open"
        }
    def update_status(self,bug_id, new_status):
        if bug_id in self.bugs:
            self.bugs[bug_id]["status"]=new_status
        else:
            print("Bug Id {bug_id} not found")
    def list_all_bugs(self):
        for bug_id,details in self.bugs.items():
            print(f"Bug Id :{bug_id}")
            print(f"Description :{details["description"]}")
            print(f"Severity :{details["severity"]}")
            print(f"Status:{details["status"]}")
            print("---" * 30)

    
if __name__ == "__main__":
   # Create a BugTracker object
    tracker = BugTracker()

    # Add three bugs
    tracker.add_bug("BUG001", "Login button not working", "High")
    tracker.add_bug("BUG002", "Typo in homepage title", "Low")
    tracker.add_bug("BUG003", "Crash on file upload", "Critical")

    # Update statuses
    tracker.update_status("BUG001", "In Progress")
    tracker.update_status("BUG003", "Closed")

    # Display all bugs
    tracker.list_all_bugs()


