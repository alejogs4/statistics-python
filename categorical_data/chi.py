from math import pow
'''
Class to make chi distribution analysis, for caregorical data
'''
class Chi:
  def __init__(self, values, number_params_stimate):

    self.values = values
    self.number_classes = len(values[0])
    self.number_params_stimate = number_params_stimate
    self.degree_free = self.number_classes - self.number_params_stimate - 1

  '''
   Given a values get the chi value with the observed values an hope values, compare that value with the chi table
  '''
  def goodness_proof_uniform(self):
    x2 = 0
    for i in range(0, len(self.values[0])):

      observed_value = self.values[0][i]
      hope_value = self.values[1][i]
      x2 += pow(observed_value - hope_value, 2) / hope_value
    

    return {
      'x2': x2,
      'degree_free': self.degree_free
    }

  '''
    Very useful when you want compare your data with a given pattern,
    for example: you want give credits 60% for bussiness 10% for natural people and 20% for goverment
    You have 85 credits when 63 are bussiness 10 are natural persons and 12 are goverment
    this data allow you to review that your hope pattern is ok?
    Ei = n * pi
         85* 0.6   
  '''
  def ajust_specific_parameter_proof(self):
    n = sum(self.values[0])
    hope_values = []
    x2 = 0

    for i in range(0, self.number_classes):

      hope_value = n * self.values[1][i]
      hope_values.append(hope_value)
    
    for i in range(0, self.number_classes):

      observed_value = self.values[0][i]
      hope_value = hope_values[i]
      x2 += pow(observed_value - hope_value, 2) / hope_value
    
    return {
      'x2': x2,
      'degree-free': self.degree_free
    }
    