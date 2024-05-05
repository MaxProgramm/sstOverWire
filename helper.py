import requests
import hashlib as hl
import random
import string

url = "http://192.168.179.92"

def write_hash(hashed_action_and_secret: str):
    with open("hashes.txt", "w") as file:
        file.write(hashed_action_and_secret)


def get_hash():
    with open("hashes.txt", "r") as file:
        res = file.read()
    return res


def send_hashed(action: str, salt: str):
    hs = generate_hash(action, salt)
    requests.get(f"{url}:5551/receive-hash", data=hs)

    pass


def get_random_string(length):
    # choose from all lowercase letter
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(length))
    return result_str






def generate_hash(action: str, salt: str):
    hs = hl.md5(f"{action}{salt}".encode("utf8"))
    return hs.hexdigest()


def check_hash(action: str, salt: str):
    own_hash = generate_hash(action, salt)
    guest_hash = get_hash()

    if (own_hash == guest_hash):
        return True
    return False


def ssp_check_round_if_won(own_choice: str, guest_choice: str):
    # -1 = Untentschieden
    # 0 = Lost
    # 1 = Won
    if own_choice == guest_choice:
        return -1

    if own_choice == "Schere" and guest_choice == "Papier":
        return 1

    if own_choice == "Papier" and guest_choice == "Stein":
        return 1

    if own_choice == "Stein" and guest_choice == "Schere":
        return 1

    return 0


def write_own_action(action: str):
    with open("own_action.txt", "w") as file:
        file.write(action)


def get_own_action():
    with open("own_action.txt", "r") as file:
        return file.read()


def get_round_counter():
    with open("round_counter.txt", "r") as file:
        return int(file.read())


def write_round_counter(number: int):
    with open("round_counter.txt", "w") as file:
        return file.write(str(number))


def add_round_counter():
    counter = get_round_counter()
    counter = counter + 1
    write_round_counter(counter)


def reset_round_counter():
    write_round_counter(0)


def received_hash():
    if get_hash() != "no":
        return True
    return False


def reset_hash():
    write_hash("no")


def write_own_salt(salt: str):
    with open("own_salt.txt", "w") as file:
        file.write(salt)


def get_own_salt():
    with open("own_salt.txt", "r") as file:
        return file.read()


def send_choice_clear(action, salt):
    requests.get(f"{url}:5551?action={action}&salt={salt}")













