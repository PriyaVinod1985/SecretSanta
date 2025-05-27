import random
from collections import defaultdict
import csv

#This Class contains methods that define the logic of generating employee and secret child pairs. 
class SecretSantaEngine:

    def __init__(self, participants, last_year_pairs = None,last_year_data=None):

        self.all_participants = participants  
        self.name_to_data = {p['Employee_Name']: {
            'Employee_Name': p['Employee_Name'],
            'Employee_EmailID': p.get('Employee_EmailID', '')
        } for p in participants}

        if last_year_data:
            
            for name, extra in last_year_data.items():
                if name in self.name_to_data:
                    if 'Secret_Child_Name' in extra:
                        self.name_to_data[name]['Secret_Child_Name'] = extra['Secret_Child_Name']
                    if 'Secret_Child_EmailID' in extra:
                        self.name_to_data[name]['Secret_Child_EmailID'] = extra['Secret_Child_EmailID']
                else:
                    self.name_to_data[name] = extra
                    
        self.participant_names = [p['Employee_Name'] for p in participants]
        self.unique_names = list(set(self.participant_names))
        self.duplicates_map = self._build_duplicates_map()
        self.last_year = dict(last_year_pairs) if last_year_pairs else {}
        self.final_pairs = []

    def _build_duplicates_map(self):
        """Returns a map of participant name -> list of indices where it appears."""
        index_map = defaultdict(list)
        for name in self.participant_names:
            index_map[name].append(name)
        return index_map
    
    def generate_pairs(self, max_attempts=1000):
        givers = self.unique_names[:]
        receivers = self.unique_names[:]

        attempts = 0
        while attempts < max_attempts:
            random.shuffle(receivers)
            temp_pairs = dict(zip(givers, receivers))

            if self._is_valid(temp_pairs):
                break
            attempts += 1

        if attempts == max_attempts:
               raise RuntimeError("Unable to generate valid Secret Santa pairs without self-assignments.")
            
        self.final_pairs = [ (giver, temp_pairs[giver])
        for giver in self.participant_names
           ]

        return self.final_pairs

    def _is_valid(self, temp_pairs):
        for giver, receiver in temp_pairs.items():
            if giver == receiver:
                return False  
            if self.last_year.get(giver) == receiver:
                return False  
        return True

    def save_pairs_to_csv(self, file_path):
        try:
            unique_pairs = {}
            for giver, receiver in self.final_pairs:
                unique_pairs[giver] = receiver  

            with open(file_path, 'w', newline='') as csvfile:
                fieldnames = ['Employee_Name', 'Employee_EmailID', 'Secret_Child_Name', 'Secret_Child_EmailID']
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                writer.writeheader()
                
                for giver, receiver in unique_pairs.items():
                    giver_data = self.name_to_data.get(giver,{})
                    receiver_data = self.name_to_data.get(receiver,{})
                    writer.writerow({
                        'Employee_Name': giver,
                        'Employee_EmailID': giver_data.get('Employee_EmailID', ''),
                        'Secret_Child_Name': receiver,
                        'Secret_Child_EmailID': receiver_data.get('Employee_EmailID', '')
                    })
                
        except Exception as e:
            raise RuntimeError(f"Failed to save CSV: {e}")
