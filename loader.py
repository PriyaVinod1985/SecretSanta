import csv

#This Class contains methods that loads current year employees as well as
#last years employees and pairings from given csv file

class ParticipantLoader:
    @staticmethod
    def load_from_csv(file_path):
        try:
            with open(file_path, newline='') as csvfile:
                reader = csv.DictReader(csvfile)
                required_headers = {'Employee_Name', 'Employee_EmailID'}
                if not required_headers.issubset(reader.fieldnames):
                    raise ValueError(f"CSV missing required headers: {required_headers - set(reader.fieldnames)}")
                participants = []
                for row in reader:
                    name = row.get('Employee_Name', '').strip()
                    email = row.get('Employee_EmailID', '').strip()
                    if name:
                        participants.append({
                            'Employee_Name': name,
                            'Employee_EmailID': email
                        })
                

            if len(participants) < 2:
                raise ValueError("Need at least 2 participants.")

            return participants
        
        except Exception as e:
            raise RuntimeError(f"Failed to load participants: {e}")


    @staticmethod
    def load_previous_pairs(file_path):
        try:
            with open(file_path, newline='') as csvfile:
                reader = csv.DictReader(csvfile)
                pairs = []
                name_to_data = {}

                for row in reader:
                    giver = row.get('Employee_Name','').strip()
                    receiver = row.get('Secret_Child_Name', '').strip()

                    pairs.append((giver, receiver))

                    # Collect giver and receiver data (only once per person)
                    if giver not in name_to_data:
                        name_to_data[giver] = {
                            'Employee_Name': giver,
                            'Employee_EmailID': row.get('Employee_EmailID', '').strip(),
                        }
                    if receiver not in name_to_data:
                        name_to_data[receiver] = {
                            'Employee_Name': receiver,
                            'Employee_EmailID': row.get('Secret_Child_EmailID', '').strip(),
                        }
                
                return pairs,name_to_data
                
        except Exception as e:
            raise RuntimeError(f"Failed to load previous year pairs: {e}")
