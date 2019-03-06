from descriptive import average
from functools import reduce
from math import pow

def anova(*samples):
  total_size = sum(list(map(lambda sample: len(sample), samples)))
  number_samples = len(samples)
  averages = list(map(lambda sample: average(sample), samples))

  great_average = get_great_average(samples, total_size)
  print(great_average)
  SCT = get_SCT(samples, great_average)
  SCTR = get_SCTR(averages, great_average, samples)
  SCE = get_SCE(samples, averages)

  CMT = SCT / (total_size - 1)
  CMTR = SCTR / (number_samples - 1)
  CME = SCE / (total_size - number_samples)
  F = CMTR /  CME

  return {
    'averages': averages,
    'great_average': great_average,
    'SCT': SCT,
    'SCTR': SCTR,
    'SCE': SCE,
    'CMT': CMT,
    'CMTR': CMTR,
    'CME': CME,
    'F': F
  }

def get_SCT(samples, great_average):
  SCT = 0
  for sample in samples:
    for x in sample:
      SCT += pow(x - great_average, 2)

  return SCT

def get_SCTR(averages, great_average, samples):
  SCTR = 0
  lens = list(map(lambda sample: len(sample), samples))

  for i in range(len(lens)):
    SCTR += lens[i] * pow(averages[i] - great_average, 2)

  return SCTR

def get_SCE(samples, averages):
  SCE = 0

  for i in range(len(samples)):
    for x in samples[i]:
      SCE = pow(x - averages[i], 2)
  return SCE

def get_great_average(samples, total):
  great_average = 0
  for sample in samples:
    for x in sample:
      great_average += x
  return great_average / total


