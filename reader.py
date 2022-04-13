import collections
from itertools import islice


CHANNELS = [
    ("logic-world", 401255675264761868),
    ("builds", 901195561980543007),
    ("works-in-progress", 930935059886784532),
    ("questions", 901199821212352573),
    ("suggestions", 906825697190895646),
    ("bugs-and-issues", 901158328405729371),
    ("modding", 901659878869844048),
    ("thonk-topics", 631616731282014218),
    ("not-logic-world", 416276124977332226),
    ("also-not-logic-world", 631004929762525204),
    ("memes", 403343343775383552),
    ("spam", 428658408510455810),
    ("voice-chat", 903124059255078943),
]


def sliding_window(iterable, n):
    # sliding_window('ABCDEFG', 4) -> ABCD BCDE CDEF DEFG
    it = iter(iterable)
    window = collections.deque(islice(it, n), maxlen=n)
    if len(window) == n:
        yield tuple(window)
    for x in it:
        window.append(x)
        yield tuple(window)


def main():
    frequencies = {}
    for (name, _) in CHANNELS:
        with open(f"data/{name}.txt", "r") as f:
            lines = f.readlines()
            for line in lines:
                if line.startswith("Jimmy#8080:"):
                    sentence = line.replace(" <[newline]> ", "\n").replace(
                        "Jimmy#8080:", "").lower().split()
                    for chunk_size in range(1, 11):
                        for chunk in sliding_window(sentence, chunk_size):
                            s = ""
                            for word in chunk:
                                s += word + " "
                            chunk = s.strip()
                            if chunk not in frequencies:
                                frequencies[chunk] = 1
                            else:
                                frequencies[chunk] += 1

    with open("jimmy-frequencies.txt", "a+") as f:
        sorted_freqs = {k: frequencies[k]
                        for k in sorted(frequencies, key=frequencies.get)}

        for (k, v) in sorted_freqs.items().__reversed__():
            f.write(f"{k}: {v}\n")


if __name__ == "__main__":
    main()
