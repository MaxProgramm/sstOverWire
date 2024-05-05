import time
import helper

helper.reset_round_counter()
helper.reset_win_counter()

def main():
    action = int(input("Please select action \n [1] Schere \n [2] Stein \n [3] Papier \n"))

    ac_list = ["", "Schere", "Stein", "Papier"]

    salt = helper.get_random_string(10)
    helper.write_own_salt(salt)

    helper.write_own_action(ac_list[action])
    helper.send_hashed(ac_list[action], salt)

    while not helper.received_hash():
        pass

    helper.send_choice_clear(ac_list[action], salt)

    print("reset Hash")
    helper.reset_hash()


if helper.get_round_counter() < 3:
    main()

if helper.get_win_counter() < 2:
    print("You lost the game!")

else:
    print("You won!")


helper.reset_win_counter()
helper.reset_round_counter()






