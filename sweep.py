import random
import bandit
from inbounds import is_inbounds

# Generate Number of bogeys  
def sweep(bogeys):  
    # If there are no bogeys, generate some
    if bogeys is None or len(bogeys) == 0:
        num_bogeys = random.randrange(1, 4)
        for _ in range(num_bogeys):
            x = random.randrange(100, 700)
            y = random.randrange(150, 415)
            bogeys.append(bandit.Bandit(x, y))
    
    # If there are bogeys, move them. Delete those that go out of radar contact
    else:
        for idx, bogey in enumerate(bogeys):
            # Update previous position
            bogey.set_previous(bogey.get_position())
    
            # Change position
            x_shift = random.randrange(-(random.randrange(1, 10)), random.randrange(1, 10))
            y_shift = random.randrange(-(random.randrange(1)), random.randrange(1, 10))

            current_x, current_y = bogey.get_position()
            bogey.set_position(current_x + x_shift, current_y + y_shift)

            # if not inbounds, delete
            new_x, new_y = bogey.get_position()
            if is_inbounds(new_x, new_y) == False:
                del(bogeys[idx])

    return bogeys


# Test
# bogeys = []
# bandit_a = bandit.Bandit(130, 240)
# bandit_b = bandit.Bandit(340, 300)
# bandit_c = bandit.Bandit(490, 150)
# bogeys.append(bandit_a)
# bogeys.append(bandit_b)
# bogeys.append(bandit_c)

# bogeys = sweep(bogeys)
# for bogey in bogeys:
#     print(bogey)
