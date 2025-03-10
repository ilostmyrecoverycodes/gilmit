from friendsbalt.acs import OrderedMap, StringDiff, AVLTree

class file_version_system:
    def __init__(self):
        # Using OrderedMap to store files, and the versions as a list
        self.files = OrderedMap()

    def save(self, filename, new_text):
        
        # Check if the file already exists, if not, initialize a new list of versions
        if filename not in self.files:
            self.files[filename] = []

        # Get the previous version, if it exists, for diff comparison
        previous_version = self.files[filename][-1] if self.files[filename] else ""

        # Use StringDiff to generate a diff of the new content vs the previous version
        diff = StringDiff(previous_version, new_text)

        # Store the diff in an AVLTree to keep track of all diffs in an ordered manner
        diff_log = AVLTree()
        diff_log.insert(len(self.files[filename]), diff)

        # Add the new file version to the OrderedMap
        self.files[filename].append(new_text)

#objectives:
#store version of file
#store version history of multiple files
#restore prev. version
#see a log of changes

# x = OrderedMap()
# a = "apple"
# b = "apple!"

# 