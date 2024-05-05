import time

import helper

action = int(input("Please select action \n [1] Schere \n [2] Stein \n [3] Papier \n"))

ac_list = ["", "Schere", "Stein", "Papier"]

salt = helper.get_random_string(10)
helper.write_own_salt(salt)

helper.write_own_action(ac_list[action])
helper.send_hashed(ac_list[action], salt)

while not helper.received_hash():
    pass

helper.send_choice_clear(ac_list[action], salt)

time.sleep(5)
print("reset Hash")
helper.reset_hash()




