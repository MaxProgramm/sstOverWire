from flask import Flask, request
import helper

app = Flask(__name__)

@app.route("/")
def receive_action():
    action = request.args.get("action")
    salt = request.args.get("salt")

    if helper.check_hash(action, salt):
        print("Hash check successful!")
        print(f"Guest chose: {action}")
        win_state = helper.ssp_check_round_if_won(helper.get_own_action(), action)
        if win_state == 1:
            print("You won this round!")
            helper.add_win_counter()
            helper.add_win_counter()
            helper.add_round_counter()

        if win_state == 0:
            print("You lost this round!")
            helper.add_round_counter()

        if win_state == -1:
            print("Tie")


    else:
        print("Hashes don't match! FAKE detected")

    return "<p>Works!</p>"





@app.route("/receive-hash")
def receive_hash():
    hashed_action = request.get_data(as_text=True)
    helper.write_hash(hashed_action)
    return "<p>WORKS!</p>"



app.run("0.0.0.0", 5551, debug=True)


