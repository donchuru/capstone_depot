import random

adjectives = [
    'adventurous', 'mysterious', 'curious', 'playful', 'cheerful',
    'energetic', 'friendly', 'gentle', 'happy', 'jolly',
    'lively', 'merry', 'peaceful', 'quirky', 'silly',
    'thoughtful', 'vibrant', 'whimsical', 'zealous', 'bright',
    'creative', 'dazzling', 'eager', 'fantastic', 'graceful',
    'harmonious', 'inspiring', 'joyful', 'kind', 'magical',
    'noble', 'optimistic', 'radiant', 'serene', 'tranquil',
    'unique', 'wise', 'amazing', 'brilliant', 'charming'
]

nouns = [
    'panda', 'dolphin', 'unicorn', 'phoenix', 'dragon',
    'wizard', 'artist', 'dreamer', 'explorer', 'pioneer',
    'scholar', 'poet', 'dancer', 'singer', 'painter',
    'astronaut', 'inventor', 'scientist', 'writer', 'musician',
    'butterfly', 'eagle', 'lion', 'tiger', 'wolf',
    'bear', 'fox', 'owl', 'penguin', 'koala',
    'elephant', 'giraffe', 'kangaroo', 'dolphin', 'whale',
    'peacock', 'flamingo', 'parrot', 'hummingbird', 'swan'
]

def generate_username():
    """Generate a random username combining an adjective and a noun."""
    adj = random.choice(adjectives)
    noun = random.choice(nouns)
    return f"{adj}_{noun}"

def generate_unique_username(User):
    """Generate a unique username that doesn't exist in the database."""
    while True:
        username = generate_username()
        if not User.query.filter_by(username=username).first():
            return username
