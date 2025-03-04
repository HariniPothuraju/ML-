import statistics
def calculate_mean(data):
  return sum(data)/len(data)
def calculate_median(data):
  sorted_data=sorted(data)
  n=len(data)
  if(n%2==0):
   middle1=sorted_data[n//2-1]
   middle2=sorted_data[n//2]
   return (middle1+middle2)/2
  else:
      return sorted_data[n//2]
def calculate_mode(data):
    return statistics.mode(data)
def calculate_varience(data):
    mean_value=calculate_mean(data)
    squared_value=sum((x-mean_value)**2 for x in data)
    return squared_value/len(data)
def calculate_standard_deviation(data):
    varience_value=calculate_varience(data)
    return varience_value**0.5
data=[27,38,29,16,27,63]
mean_value=calculate_mean(data)
median_value=calculate_median(data)
mode_value=calculate_mode(data)
varience_value=calculate_varience(data)
standard_deviation_value=calculate_standard_deviation(data)
print("dataset",data)
print("mean=",mean_value)
print("median=",median_value)
print("mode=",mode_value)
print("varience=",varience_value)
print("standard_deviation=",standard_deviation_value)

   
