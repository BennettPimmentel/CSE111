import random

def get_determiner(quantity):
    determiners = {1: ["a", "one", "the"],
                   2: ["some", "many", "the"]}
    return random.choice(determiners[quantity])

def get_noun(quantity):
    nouns = {1: ["bird", "boy", "car", "cat", "dog", "girl", "rabbit", "child"],
             2: ["birds", "boys", "cars", "cats", "dogs", "girls", "rabbits", "children"]}
    return random.choice(nouns[quantity])

def get_verb(quantity, tense):
    verbs = {
        "past": {1: ["drank", "ate", "grew", "laughed", "thought", "ran", "slept", "talked", "walked", "wrote"],
                 2: ["drank", "ate", "grew", "laughed", "thought", "ran", "slept", "talked", "walked", "wrote"]},
        "present": {1: ["drinks", "eats", "grows", "laughs", "thinks", "runs", "sleeps", "talks", "walks", "writes"],
                    2: ["drink", "eat", "grow", "laugh", "think", "run", "sleep", "talk", "walk", "write"]},
        "future": {1: ["will drink", "will eat", "will grow", "will laugh", "will think", "will run", "will sleep", "will talk", "will walk", "will write"],
                    2: ["will drink", "will eat", "will grow", "will laugh", "will think", "will run", "will sleep", "will talk", "will walk", "will write"]}
    }
    return random.choice(verbs[tense][quantity])

def get_preposition():
    prepositions = ["about", "above", "across", "after", "along",
                    "around", "at", "before", "behind", "below",
                    "beyond", "by", "despite", "except", "for",
                    "from", "in", "into", "near", "of",
                    "off", "on", "onto", "out", "over",
                    "past", "to", "under", "with", "without"]
    return random.choice(prepositions)

def get_prepositional_phrase(quantity):
    return f"{get_preposition()} {get_determiner(quantity)} {get_noun(quantity)}"

def get_adjective():
    adjectives = ["happy", "sad", "bright", "dark", "small", "big", "fast", "slow", "young", "old"]
    return random.choice(adjectives)

def make_sentence(quantity, tense):
    determiner = get_determiner(quantity)
    adjective = get_adjective()
    noun = get_noun(quantity)
    verb = get_verb(quantity, tense)
    prepositional_phrase = get_prepositional_phrase(quantity)
    
    sentence = f"{determiner.capitalize()} {adjective} {noun} {verb} {prepositional_phrase}."
    return sentence

def main():
    print(make_sentence(1, "past"))
    print(make_sentence(1, "present"))
    print(make_sentence(1, "future"))
    print(make_sentence(2, "past"))
    print(make_sentence(2, "present"))
    print(make_sentence(2, "future"))

if __name__ == "__main__":
    main()

