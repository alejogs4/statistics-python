def classic_probability(cases, function):
  positive_cases = filter(function, cases)
  
  length = float(len(cases))
  positive_cases_length = float(len(positive_cases))
  
  return  positive_cases_length / length

def multiplication_rule(cases, function_a, function_b, independent = True):
  probability_a = classic_probability(cases, function_a)
  probability_b = classic_probability(cases, function_b)

  return probability_a * probability_b

def conditional_probability(cases, function_a, function_b, independent = True):
  intersection = multiplication_rule(cases, function_a, function_b, independent)
  probability_a = classic_probability(cases, function_a)

  return intersection / probability_a



cases = [1,2,3,4,5,6]
classic_probability(cases, lambda x: x % 2 == 0)