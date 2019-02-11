from dane import us_state_abbrev
from dane import states_list

print(states_list[9], us_state_abbrev[states_list[9]])
element45 = {k for k, v in us_state_abbrev.items() if k == states_list[44]}
print(element45)
element27 = {v for k, v in us_state_abbrev.items() if k == states_list[26]}
print(element27)
