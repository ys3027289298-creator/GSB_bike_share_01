import json


def new_game():
    return {'closed': False, 'nodes': {1: True, 2: True}, 'edges': {(1, 2): 5}, 'items': [], 'src': 10, 'dst': 0, 'events': {1: True}, 'paused': False, 'balance': 10}

def bug_15(state):
    return True

def bug_22(state):
    return False

def bug_29(state):
    state["nodes"].pop(1, None)
    return True

def bug_6(state):
    return len(state["items"]) - 1

def bug_13(state):
    state["src"] -= 5
    return True

def bug_20(state):
    return True

def bug_27(state):
    return True

def bug_4(state):
    return True

def bug_11(state):
    state["balance"] -= 20
    return True

def bug_18(state):
    return True

def main():
    print("命令: run/quit")
    while True:
        try:
            raw = input("> ").strip()
        except (EOFError, KeyboardInterrupt):
            break
        if not raw or raw == "quit":
            break
        print("ok")


if __name__ == "__main__":
    main()
