# A RouteTrieNode will be similar to our autocomplete TrieNode... with one additional element, a handler.
class RouteTrieNode:
    def __init__(self, handler=None):
        # Initialize the node with children as before, plus a handler
        self.handler = handler
        self.children = dict()

    def insert(self, sub_path, handler=None):
        # Insert the node as before
        self.children[sub_path] = RouteTrieNode(handler)


# A RouteTrie will store our routes and their associated handlers
class RouteTrie:
    def __init__(self, handler=None):
        # Initialize the trie with an root node and a handler, this is the root path or home page node
        self.root = RouteTrieNode(handler)

    def insert(self, provided_paths, handler):
        # Similar to our previous example you will want to recursively add nodes
        # Make sure you assign the handler to only the leaf (deepest) node of this path

        # Split the path into sub paths with "/"
        sub_paths = provided_paths.split("/")

        # Only process the path if there exist 1 or more sub-paths
        if len(sub_paths) <= 1:
            return

        node = self.root
        
        # Traverse the list while checking for sub path
        # Create a child node for each new sub path.
        for sub_path in sub_paths[1:]:     
            if sub_path in node.children:
                node = node.children[sub_path]
            else:
                child_node = RouteTrieNode()
                node.children[sub_path] = child_node
                node = child_node

        # node is now at the leaf node, update the handler attribute
        node.handler = handler

    def find(self, provided_paths):
        # Starting at the root, navigate the Trie to find a match for this path
        # Return the handler for a match, or None for no match

        node = self.root
        if len(provided_paths) == 1 and provided_paths[0] == '/':
            return node.handler

        # Trim the trailing "/"
        if provided_paths[-1] == "/":
            provided_paths = provided_paths[:-1]

        # Split the path into sub path by "/" and then Traverse on the list of paths
        sub_paths = provided_paths.split("/")

        for sub_path in sub_paths[1:]:
            if sub_path in node.children:
                node = node.children[sub_path]
            else:
                return

        return node.handler


# The Router class will wrap the Trie and handle
class Router:
    def __init__(self, root_handler=None, not_found_handler=None):
        # Create a new RouteTrie for holding our routes
        # You could also add a handler for 404 page not found responses as well!
        self.route_trie = RouteTrie(handler=root_handler)
        self.not_found_handler = not_found_handler

    def add_handler(self, provided_paths, handler):
        # Add a handler for a path
        # You will need to split the path and pass the pass parts
        # as a list to the RouteTrie
        self.route_trie.insert(provided_paths, handler)

    def lookup(self, provided_paths):
        # lookup path (by parts) and return the associated handler
        # you can return None if it's not found or
        # return the "not found" handler if you added one
        # bonus points if a path works with and without a trailing slash
        # e.g. /about and /about/ both return the /about handler
        handler = self.route_trie.find(provided_paths)

        if handler is None:
            return self.not_found_handler
        else:
            return handler


# create the router and add a route
router = Router("root handler", "not found handler")  # remove the 'not found handler' if you did not implement this
router.add_handler("/home/about", "about handler")  # add a route

# Test Case 1
print(router.lookup("/"))  # should print 'root handler'

# Test Case 2
print(router.lookup("/home"))  # should print 'not found handler'

# Test Case 3
print(router.lookup("/home/about"))  # should print 'about handler'
print(router.lookup("/home/about/"))  # should print 'about handler'

# Test Case 4
print(router.lookup("/home/about/me"))  # should print 'not found handler'

# Test Case 5 - Edge Case
print(router.lookup("/blabla"))  # should print 'not found handler'


