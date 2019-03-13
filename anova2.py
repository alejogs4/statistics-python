from ANOVA import get_SCT, get_SCTR, get_great_average
from math import pow

def anova_two_way():
  return NotImplemented


def get_SCBL(samples, great_average):
  SCBL = 0

  for sample in samples:
    for x in sample:
      SCBL += len(samples) * pow(x - great_average, 2)
    
  return SCBL

def get_SCE(samples, great_average, averages):
  SCT = get_SCT(samples, get_great_average)
  SCTR = get_SCTR(averages, great_average, samples)
  SCBL = get_SCBL(samples, great_average)

  return SCT - SCTR - SCBL


