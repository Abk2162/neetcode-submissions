class Twitter:

    def __init__(self):
        self.users = {}
        self.posts = {}
        self.count = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId not in self.users:
            self.users[userId] = [userId]
        if userId not in self.posts:
            self.posts[userId] = []
            
        self.count -= 1
        self.posts[userId].append((self.count, tweetId))

 
    def getNewsFeed(self, userId: int) -> List[int]:
        temp = []
        res = []
        people = self.users.get(userId, [userId])
        for person in people:
            if person in self.posts:
                temp.extend(self.posts[person][-10:])
        heapq.heapify(temp)
        for i in range(10):
            if not temp:
                break
            mid = heapq.heappop(temp)
            res.append(mid[1])
        return res

        

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.users:
            self.users[followerId] = [followerId]
            
        if followerId != followeeId and followeeId not in self.users[followerId]:
            self.users[followerId].append(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.users and followeeId in self.users[followerId]:
            self.users[followerId].remove(followeeId)
        
