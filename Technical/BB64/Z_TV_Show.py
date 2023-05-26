from collections import defaultdict

class TVShow:
    def __init__(self, name):
        self.name = name
        self.episodes_watched = defaultdict(int)
        self.viewers_finished = defaultdict(int)
    
    def process_log(self, episode):
        self.episodes_watched[episode] += 1
        
        for ep in range(1, episode + 1):
            if self.episodes_watched[ep] == 0:
                return
            
        self.viewers_finished[episode] += 1
    
    def print_results(self):
        for episode in range(1, 11):
            viewers_watched = self.episodes_watched[episode]
            viewers_finished = self.viewers_finished[episode]
            
            if viewers_watched == 0:
                break
            
            if viewers_finished / viewers_watched >= 0.7:
                print(f"For show '{self.name}', x is {episode}.")
                break

# Example usage
log_entries = [
    ("Show A", 1),
    ("Show A", 1),
    ("Show A", 2),
    ("Show A", 2),
    ("Show A", 3),
    ("Show B", 1),
    ("Show B", 2),
    ("Show B", 3),
    ("Show B", 4),
    ("Show B", 5),
    ("Show B", 6),
    ("Show B", 7),
    ("Show B", 8),
    ("Show B", 9),
    ("Show B", 10)
]

shows = {}

def process_log(show, episode):
    if show not in shows:
        shows[show] = TVShow(show)
    shows[show].process_log(episode)

def print_results():
    for show in shows.values():
        show.print_results()

# Process log entries
for entry in log_entries:
    process_log(*entry)

# Print results
print_results()
