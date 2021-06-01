class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        total_tank = 0
        curr_tank = 0 
        starting_station = 0
        for i, station in enumerate(gas):
            
            total_tank = total_tank + gas[i] - cost[i]            
            curr_tank = curr_tank + gas[i] - cost[i]
            
            if curr_tank <0 :
                #go to next station
                starting_station = i + 1
                
                curr_tank = 0 
                
        return starting_station if total_tank >= 0 else -1