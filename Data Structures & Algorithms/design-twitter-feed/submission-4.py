import heapq
from collections import defaultdict
from typing import List

class Twitter:

    def __init__(self):
        # Maps userId -> set of followeeIds (O(1) lookups/removals)
        self.users = defaultdict(set)
        # Maps userId -> list of (-timestamp, tweetId)
        self.posts = defaultdict(list)
        self.count = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.count -= 1
        self.posts[userId].append((self.count, tweetId))

    def getNewsFeed(self, userId: int) -> List[int]:
        min_heap = []
        res = []

        # Everyone follows themselves implicitly for the feed
        followees = self.users[userId] | {userId}

        # Initialize the heap with only the most recent tweet from each followee
        # Format: (neg_time, tweetId, personId, next_index_in_person_posts)
        for person in followees:
            if self.posts[person]:
                last_idx = len(self.posts[person]) - 1
                neg_time, tweetId = self.posts[person][last_idx]
                min_heap.append((neg_time, tweetId, person, last_idx - 1))

        heapq.heapify(min_heap)

        # Pull up to 10 most recent tweets overall (K-way merge)
        while min_heap and len(res) < 10:
            neg_time, tweetId, person, next_idx = heapq.heappop(min_heap)
            res.append(tweetId)

            # If this user has an older tweet, push that into the heap next
            if next_idx >= 0:
                older_neg_time, older_tweetId = self.posts[person][next_idx]
                heapq.heappush(min_heap, (older_neg_time, older_tweetId, person, next_idx - 1))

        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            self.users[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        # discard does not throw KeyError or ValueError if followeeId is not present
        self.users[followerId].discard(followeeId)
