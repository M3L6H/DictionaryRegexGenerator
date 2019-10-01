import re, sys

WORD = re.compile(r"[A-Za-z']+\n?")

class Tree:
    def __init__(self, key = "_root", children = {}):
        self.key = key
        self.children = children

    def setKey(self, key):
        self.key = key

    def getKey(self):
        return self.key

    def setChild(self, key, tree):
        self.children[key] = tree

    def addChild(self, key):
        self.setChild(key, Tree(key, {}))

    def getChild(self, key):
        try:
            return self.children[key]
        except KeyError as e:
            return None

    def getChildren(self):
        return self.children

    def removeChild(self, key):
        del self.children[key]

    def clearChildren(self):
        self.children.clear()

    def isLeaf(self):
        return not self.children

    def getCount(self):
        return len(self.children)

    def getRegex(self):
        if self.key == "_root":
            return "(?:" + "|".join([self.children[child].getRegex() for child in self.children]) + ")"
        escaped = self.key.replace(".", "\.")
        if self.isLeaf():
            return escaped
        return f"{ escaped }(?:" + "|".join([self.children[child].getRegex() for child in self.children]) + ")"

    def __str__(self, depth=0):
        returnVal = "  "*depth + (str(self.key) or "_null") +"\n"
        for child in self.children:
            returnVal += self.children[child].__str__(depth+1)
        return returnVal

def getDiff(a, b):
    return [i for i in range(min(len(a) + 1, len(b) + 1)) if len(a) == i or len(b) == i or a[i] != b[i]][0]

def insertWord(tree, word, depth = 0):
    # Look for a matching key
    for key in tree.getChildren():
        diff = getDiff(key, word)

        # We found a similar prefix
        if diff != 0:
            # How similar are we
            match, rest = word[:diff], word[diff:]

            # Does the prefix we are looking for already exist?
            if tree.getChild(match):
                return insertWord(tree.getChild(match), rest, depth + 1)

            # Otherwise we need to update the tree
            tree.setChild(match, tree.getChild(key))
            tree.removeChild(key)

            # Now we work with the subtree
            tree = tree.getChild(match)

            # Make a deep copy so we can edit the base
            children = tree.getChildren().copy()
            tree.clearChildren()

            # Get the rest of the key that got chopped off
            tree_rest = tree.getKey()[diff:]

            # Add that as a new subtree
            tree.setKey(match)
            tree.setChild(tree_rest, Tree(tree_rest, children))

            # Insert our abbreviation as a sibling
            tree.addChild(rest)
            return
    # If there are no matching keys, add a new child to this level of the tree
    if depth > 0:
        tree.addChild("")
    tree.addChild(word)

def main(args):
    insensitive = False
    wholeword = False

    while "-i" in args:
        insensitive = True
        args.remove("-i")

    while "--insensitive" in args:
        insensitive = True
        args.remove("--insensitive")

    while "-w" in args:
        wholeword = True
        args.remove("-w")

    while "--whole" in args:
        wholeword = True
        args.remove("--whole")

    words = [line.rstrip('\n') for line in open(args[1]) if WORD.match(line)]

    if insensitive:
        words = [word.lower() for word in words]

    words.sort()

    tree = Tree()

    for word in words:
        insertWord(tree, word)

    regex = tree.getRegex().replace("||", "|")

    if wholeword:
        regex = f"(?<!\w){ regex }(?!\w)"

    with open("out.txt", "w") as f:
        f.write(regex)


if __name__ == "__main__":
    main(sys.argv)
