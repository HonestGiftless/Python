# best_sender()

from collections import defaultdict

def best_sender(messages, senders):
    chats = defaultdict(int)

    for i in range(len(messages)):
        chats[senders[i]] += len(messages[i].split())

    chats = sorted(chats.items(), key=lambda item: (item[1], item[0]), reverse=True)

    return chats[0][0]