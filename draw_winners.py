import numpy as np
np.random.seed(1676573610) # UNIX timestamp at moment of the draw

print("$HUAHUA $JUNO Slot spins giveaway Feb 15, 2023")

# Retweets
list_of_rter = []
with open('retweets', 'r') as f:
  lines = f.readlines()
  for l in lines:
    list_of_rter.append(l[:-1])
# No dupes
list_of_rter = list(set(list_of_rter))

# Comments
list_of_comments = []
with open('comments', 'r') as f:
  lines = f.readlines()
  for l in lines:
    list_of_comments.append(l[:-1])
# No dupes
list_of_comments = list(set(list_of_comments))

# Combine both list
combined_list = sorted(list_of_comments + list_of_rter)
print(f"Total tickets {len(combined_list)}")
print(f"Total players {len(set(combined_list))}")
np.random.shuffle(combined_list)

# Draw prizes: 1. 500k $HUAHUA, 2. 50 $JUNO 3. 1000 slot spins, 4. Participation: 100 $RAC
winner = np.random.choice(combined_list, 4, False)
print(f"Winners are: {winner}")
