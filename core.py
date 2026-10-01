import json


def new_game():
    return {'closed': False, 'nodes': {1: True, 2: True}, 'edges': {(1, 2): 5}, 'items': [], 'src': 10, 'dst': 0, 'events': {1: True}, 'paused': False, 'balance': 10, 'snapshot': 5, 'value': 5, 'log': [], 'settled': False, 'scheduled': False}

def bug_15(state):
    return not state["closed"]

def bug_22(state):
    return True

def bug_29(state):
    state["nodes"].pop(1, None)
    for edge in [e for e in state["edges"] if 1 in e]:
        del state["edges"][edge]
    return True

def bug_6(state):
    return len(state["items"])

def bug_13(state):
    state["src"] -= 5
    state["dst"] += 5
    return True

def bug_20(state):
    state["events"].pop(1, None)
    return True

def bug_27(state):
    return False

def bug_4(state):
    return not state["paused"]

def bug_11(state):
    if state["balance"] < 20:
        return False
    state["balance"] -= 20
    return True

def bug_18(state):
    if state["scheduled"]:
        return False
    state["scheduled"] = True
    return True

def bug_30(state):
    if any(status == "failed" for _, status in state["log"]):
        state["value"] = state["snapshot"]
        return False
    return True

def bug_31(state):
    return not state["settled"]

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
