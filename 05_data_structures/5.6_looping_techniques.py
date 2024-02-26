## 5.6. Looping Techniques

# Reference: https://docs.python.org/3.12/tutorial/datastructures.html#looping-techniques

import math

"""
When looping through dictionaries, the key and cprresponding value can be retrieved at the same time using the items() method.
"""

knights = { "gallahad": "the pure", "robin": "the brave" }
for key, value in knights.items():
  print(f"key: {key}, value: {value}")

"""
When looping through a sequence, the position index and corresponding value can be retrieved at the same time using the enumerate() function
"""

for index, value in enumerate(["tic", "tac", "toe"]):
  print(f"index: {index} value: {value}")

questions = ["name", "quest", "favorite color"]
answers = ["lancelot", "the holy grail", "blue"]
for question, answer in zip(questions, answers):
  print(f"What is your {question}? It is ${answer}")

"""
To loop over a sequence in reverse, first specify the sequence in a forward direction and then call the reverse() function
"""

for i in reversed(range(1, 10, 2)):
  print(i)

"""
To loop over a sequence in sorted order, use the sorted() function which returns a new sorted list while leaving the source unaltered.
"""

basket = ["apple", "orange", "apple", "pear", "orange", "banana"]
for i in sorted(basket):
  print(i)

"""
Using set() on a sequence eliminates duplicate elements.
The use of sorted in combination with set() over a sequence is an idiomatic way to loop over unique elements of the sequence in sorted order.
"""

basket = ["apple", "orange", "apple", "pear", "orange", "banana"]
for i in sorted(set(basket)):
  print(i)

"""
It is sometimes tempting to change a list while you are looping over it;
however it is often simpler and safe to create a new list instead.
"""

raw_data = [56.2, float("NaN"), 51.7, 55.3, 52.5, float("NaN"), 47.8]
print("raw_data:", raw_data)

filtered_data = []
for value in raw_data:
  if not math.isnan(value):
    filtered_data.append(value)
print("filtered_data:", filtered_data)
