class AntiSpam:
    def __init__(self, threshold=5, interval=10):
        self.threshold = threshold
        self.interval = interval
        self.user_messages = {}

    def check_message(self, user_id, timestamp):
        if user_id not in self.user_messages:
            self.user_messages[user_id] = []
        self.user_messages[use        @echo off
        git add .
        git commit -m "Auto update"
        git push_id].append(timestamp)
        # Remove messages outside the interval
        self.user_messages[user_id] = [t for t in self.user_messages[user_id] if timestamp - t <= self.interval]
        if len(self.user_messages[user_id]) > self.threshold:
            return True  # Spam detected
        return False

# Example usage:
if __name__ == "__main__":
    import time
    antispam = AntiSpam(threshold=3, interval=5)
    user = "user123"
    now = int(time.time())
    print(antispam.check_message(user, now))
    print(antispam.check_message(user, now+1))
    print(antispam.check_message(user, now+2))
    print(antispam.check_message(user, now+3))  # Should return True (spam)
