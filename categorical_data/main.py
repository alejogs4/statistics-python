from chi import Chi

values = [
    [15, 11, 10, 12],
    [12, 12, 12, 12]
]

chi_proof = Chi(values, 0)
print(chi_proof.goodness_proof_uniform().get('x2'))

bank = [
  [62, 10, 13],
  [0.6, 0.1, 0.3]
]

chi_proof_2 = Chi(bank, 0)
print(chi_proof_2.ajust_specific_parameter_proof().get('x2'))
