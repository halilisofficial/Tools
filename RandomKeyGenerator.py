class KeyGen():
  def __init__():

    pass

  def generate_key(length_of_key=256,start_point=0,jump=17,seed_of_random=42):
    from random import randint,seed
    seed(seed_of_random)
    key = ""
    binary_array = ""
    for _ in range(100000):
      binary_array += str(randint(0,1))
    for i in range(length_of_key):
      key += binary_array[start_point+(i*jump)]
    return key
#note: for better key; use all function parameters
generated_key = KeyGen.generate_key(length_of_key=128,start_point = 13,jump = 42,seed_of_random = 41)
print(generated_key)