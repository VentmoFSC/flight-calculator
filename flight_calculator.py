#flight time calculator, ensuring that the weight is a positive number and calculating flight time based on weight.
def calculate_flight_time(weight_grams): 

    #Ensure weight is a positive number
    #copilot suggested a failsale against negative weight values, no changes needed
    if weight_grams <= 0: 
        raise ValueError("Weight must be a positive number.")

    #calculation to determine flight time based on weight
    #rejected initial copilot calculation as overly complex, simplified the math to a linear calculation
    #Flight time decreases with weight
    flight_time = 180 - (0.1 * weight_grams)  

    #returns flight time
    return max(0, flight_time)  

#Generate a flight time table for weights from 0 to max_weight_grams in increments of step_grams
def flight_time_table(max_weight_grams, step_grams):

    table = []

    #For loop to iterate through weights from 0 to max_weight_grams in increments of step_grams
    #Edited copilot's suggestion to use a for loop instead of a while loop
    for weight in range(0, max_weight_grams + 1, step_grams):

            #Calculate flight time for the current weight
            time = calculate_flight_time(weight)
            table.append((weight, time))

    #Returns the flight time table        
    return table