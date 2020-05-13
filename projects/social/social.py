import random
import sys
sys.path.insert(0, '../graph')
from util import Queue

class User:
    def __init__(self, name):
        self.name = name

class SocialGraph:
    def __init__(self):
        self.last_id = 0
        self.users = {}
        self.friendships = {}

    def add_friendship(self, user_id, friend_id):
        """
        Creates a bi-directional friendship
        """
        if user_id == friend_id:
            print("WARNING: You cannot be friends with yourself")
        elif friend_id in self.friendships[user_id] or user_id in self.friendships[friend_id]:
            print("WARNING: Friendship already exists")
        else:
            self.friendships[user_id].add(friend_id)
            self.friendships[friend_id].add(user_id)

    def add_user(self, name):
        """
        Create a new user with a sequential integer ID
        """
        self.last_id += 1  # automatically increment the ID to assign the new user
        self.users[self.last_id] = User(name)
        self.friendships[self.last_id] = set()

    def populate_graph(self, num_users, avg_friendships):
        """
        Takes a number of users and an average number of friendships
        as arguments

        Creates that number of users and a randomly distributed friendships
        between those users.

        The number of users must be greater than the average number of friendships.
        """
        # Reset graph
        self.last_id = 0
        self.users = {}
        self.friendships = {}
        # !!!! IMPLEMENT ME

        # Add users
        for index in range(0, num_users):
            self.add_user(f"User {index}")

        # Create friendships
        possible_friendships = []

        # Avoid duplicates by ensuring the first number is smaller than the second
        for user_identifier in self.users:
            for friend_identifier in range(user_identifier + 1, self.last_id + 1):
                friends = (user_identifier, friend_identifier)
                possible_friendships.append(friends)
        # Shuffle the possible friendships
        random.shuffle(possible_friendships)
        # Create friendships for the first X pairs of the list
        # X is determined by the formula: num_users * avg_friendships // 2
        # Need to divide by 2 since each add_friendship() creates 2 friendships
        for index in range(num_users * avg_friendships // 2):
            friendship = possible_friendships[index]
            friend_one, friend_two = friendship
            self.add_friendship(friend_one, friend_two)

    def get_all_social_paths(self, user_id):
        """
        Takes a user's user_id as an argument

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        The key is the friend's ID and the value is the path.
        """
        visited = {}  # Note that this is a dictionary, not a set
        # !!!! IMPLEMENT ME
        # BFS
        queue = Queue()
        queue.enqueue([user_id])

        while queue.size() > 0:
            path = queue.dequeue()
            current_person = path[-1]
            print("current person: ", current_person)
            if current_person not in visited:
                print(f"this person {current_person} hasn't been visited")
                visited[current_person] = path
                for friend in self.friendships[current_person]:
                    print(f"friend of {current_person}: {friend}")
                    new_path = path + [friend]
                    queue.enqueue(new_path)
        return visited


if __name__ == '__main__':
    sg = SocialGraph()
    sg.populate_graph(100, 4)
    print(sg.friendships)
    print("-------------------------------------")
    connections = sg.get_all_social_paths(34)
    print(connections)
