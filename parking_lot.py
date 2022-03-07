from datetime import datetime

class Car:
    def __init__(self,vehicle_number,color):
        self.vehicle_number =vehicle_number
        
    def __str__(self):
        return "Car [Vehicle_number=" + self.vehicle_number + "]"
    
    def get_vehicle_number(self):
        return self.vehicle_number
   
   
    
class ParkingLot:
    def __init__(self,total_lots):
        self.total_lots = total_lots
        self.available_lots = []
        self.parking_lots = {}
        self.record = []
        # All the empty slots will be indicated by -1
        for i in range(0,total_lots):
            self.available_lots.append(-1)
                             

    def find_empty_lot(self):
        try:
            slot = self.available_lots.index(-1)
            return slot
        except:
            return -1
        
    def park_car(self,car):
        slot = self.find_empty_lot()
        if(slot == -1):
            return "No Empty Lot Available"
        else:
            self.available_lots[slot]=car
            vehicle_number = car.get_vehicle_number()
            self.parking_lots[vehicle_number] = {}
            self.parking_lots[vehicle_number]['slot'] = slot
            self.parking_lots[vehicle_number]['entry_time'] = datetime.now()
            return "Sucess"
            
            
            
    def leave(self,car):
        try:
            vehicle_number = car.get_vehicle_number()
            slot = self.parking_lots[vehicle_number]['slot']
            self.record.append(
                {
                    'slot' : slot,
                    'vehicle_number':vehicle_number,
                    'entry_time' :self.parking_lots[vehicle_number]['entry_time'],
                    'exit_time' : datetime.now()
                }
            )
            self.available_lots[slot] = -1
            self.parking_lots.pop(vehicle_number)
            return "Success"
        except:
            return "No car to remove"
        
    def get_availbe_lots(self):
        result = []
        for i in range(0,len(self.available_lots)):
            if self.available_lots[i] == -1:
                result.append(i)
        return result ,len(result)
    
    def get_all_cars(self):
        result = []
        for i in range(0,len(self.available_lots)):
            if(self.available_lots[i] != -1):
                result.append(self.available_lots[i])
        return result , len(result)
        
    def get_history_record(self):
        return self.record
            
            