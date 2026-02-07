import sqlite3

MOTIVATIONAL_QUOTES = [
    # Calming
    ("Breathe in peace, breathe out stress. You are exactly where you need to be.", "Calming"),
    ("The quieter you become, the more you can hear.", "Calming"),
    ("Almost everything will work again if you unplug it for a few minutes, including you.", "Calming"),
    ("In the middle of difficulty lies opportunity for calm.", "Calming"),
    ("Nature does not hurry, yet everything is accomplished.", "Calming"),
    # Empathetic
    ("It is okay to not be okay. What matters is that you keep going.", "Empathetic"),
    ("Your feelings are valid, even if others don't understand them.", "Empathetic"),
    ("You don't have to carry everything alone. It's okay to ask for help.", "Empathetic"),
    ("Sometimes the strongest thing you can do is let yourself feel.", "Empathetic"),
    ("Be gentle with yourself. You're doing the best you can.", "Empathetic"),
    # Encouraging
    ("You are capable of amazing things. Believe in yourself!", "Encouraging"),
    ("Every step forward, no matter how small, is progress.", "Encouraging"),
    ("You didn't come this far to only come this far.", "Encouraging"),
    ("Keep going. Everything you need will come to you at the perfect time.", "Encouraging"),
    ("You are stronger than you think and braver than you believe.", "Encouraging"),
    # General
    ("Today is a good day to have a good day.", "General"),
    ("Life is what happens when you're busy making other plans.", "General"),
    ("Be yourself; everyone else is already taken.", "General"),
    ("Every day is a fresh start.", "General"),
    ("The best time for new beginnings is now.", "General"),
    # Gratitude-Inspired
    ("Gratitude turns what we have into enough.", "Gratitude-Inspired"),
    ("Start each day with a grateful heart.", "Gratitude-Inspired"),
    ("The more you are thankful, the more you attract things to be thankful for.", "Gratitude-Inspired"),
    ("Gratitude is not only the greatest of virtues but the parent of all others.", "Gratitude-Inspired"),
    ("When you focus on the good, the good gets better.", "Gratitude-Inspired"),
    # Hopeful
    ("After every storm, there is a rainbow waiting to shine.", "Hopeful"),
    ("Hope is being able to see that there is light despite all of the darkness.", "Hopeful"),
    ("The sun will rise and we will try again.", "Hopeful"),
    ("Tomorrow is another chance to get it right.", "Hopeful"),
    ("Even the darkest night will end, and the sun will rise.", "Hopeful"),
    # Humorous
    ("I'm not lazy, I'm on energy-saving mode.", "Humorous"),
    ("Life is short. Smile while you still have teeth.", "Humorous"),
    ("I need a six-month vacation, twice a year.", "Humorous"),
    ("My bed is a magical place where I suddenly remember everything I forgot to do.", "Humorous"),
    ("Stressed spelled backwards is desserts. Coincidence? I think not.", "Humorous"),
    # Motivational
    ("The only way to do great work is to love what you do.", "Motivational"),
    ("Don't watch the clock; do what it does. Keep going.", "Motivational"),
    ("Success is not final, failure is not fatal: it is the courage to continue that counts.", "Motivational"),
    ("Dream big, start small, act now.", "Motivational"),
    ("Your limitation is only your imagination.", "Motivational"),
    # Overcoming Challenges
    ("The struggle you're in today is developing the strength you need for tomorrow.", "Overcoming Challenges"),
    ("A diamond is just a piece of charcoal that handled stress exceptionally well.", "Overcoming Challenges"),
    ("Difficult roads often lead to beautiful destinations.", "Overcoming Challenges"),
    ("You were given this life because you are strong enough to live it.", "Overcoming Challenges"),
    ("Rock bottom became the solid foundation on which I rebuilt my life.", "Overcoming Challenges"),
    # Reflective
    ("What you think, you become. What you feel, you attract. What you imagine, you create.", "Reflective"),
    ("Life isn't about finding yourself. Life is about creating yourself.", "Reflective"),
    ("In the end, we only regret the chances we didn't take.", "Reflective"),
    ("The only person you are destined to become is the person you decide to be.", "Reflective"),
    ("Sometimes you have to look back to understand what lies ahead.", "Reflective"),
    # Self-Love
    ("You are enough just as you are.", "Self-Love"),
    ("Talk to yourself like you would to someone you love.", "Self-Love"),
    ("You yourself, as much as anybody in the entire universe, deserve your love and affection.", "Self-Love"),
    ("Self-care is not selfish. You cannot serve from an empty vessel.", "Self-Love"),
    ("Be proud of who you are, not ashamed of how someone else sees you.", "Self-Love"),
    # Uplifting
    ("You make the world a better place just by being in it.", "Uplifting"),
    ("Your smile is a light in the window of your soul, showing people that your heart is at home.", "Uplifting"),
    ("You are a work of art. Not everyone will understand you, but the ones who do will never forget you.", "Uplifting"),
    ("Happiness looks gorgeous on you. Keep shining!", "Uplifting"),
    ("The world needs your light. Don't ever dim it.", "Uplifting"),
]

ANIMAL_INSPIRATIONS = [
    # Ape
    ("A young orangutan lost its mother but was adopted by a wildlife sanctuary. Over years of gentle care, it learned to climb, forage, and eventually returned to the wild — proving that love and patience can rebuild what was broken.", "ape"),
    ("Koko the gorilla learned sign language and could express emotions like love and sadness, reminding us that empathy knows no species boundaries.", "ape"),
    ("A group of chimpanzees was observed consoling a grieving member of their group, showing that compassion is deeply woven into nature.", "ape"),
    # Bear
    ("A mother bear carried her cubs across a rushing river, never once letting go. Her determination reminds us that love gives us the strength to overcome any obstacle.", "bear"),
    ("A bear cub orphaned in a forest fire was rescued and nursed back to health. It grew strong and was released back into the wild, thriving once again.", "bear"),
    ("Every winter, bears retreat into hibernation, trusting that spring will come. Sometimes resting is the bravest thing you can do.", "bear"),
    # Butterfly
    ("A butterfly struggles to emerge from its cocoon, but that struggle is what gives its wings the strength to fly. Your challenges are making you stronger.", "butterfly"),
    ("Butterflies can't see their own wings, but everyone else can see how beautiful they are. Sometimes you can't see your own beauty, but others can.", "butterfly"),
    ("The caterpillar thought the world was ending, but it was just becoming a butterfly. Change can be beautiful.", "butterfly"),
    # Camel
    ("A camel can walk hundreds of miles through scorching desert without giving up. It reminds us that endurance and resilience can carry us through the toughest journeys.", "camel"),
    ("Camels store reserves for the hardest parts of the journey. Like them, the strength you've built in good times will carry you through the tough times.", "camel"),
    ("A baby camel asked its mother why they have humps. She said, 'To store energy for when the journey gets hard.' Everything about you has a purpose.", "camel"),
    # Cat
    ("A stray cat wandered into an elderly woman's home and never left. They became each other's best companion, proving that love finds you when you least expect it.", "cat"),
    ("Cats always land on their feet. No matter how many times life flips you upside down, you have the instinct to find your balance again.", "cat"),
    ("A rescue cat who was once terrified of people slowly learned to trust again, eventually becoming the most affectionate companion. Healing takes time, but it's always possible.", "cat"),
    # Cheetah
    ("A cheetah is the fastest land animal, but it rests after every sprint. Even the fastest among us need to pause and recharge.", "cheetah"),
    ("A cheetah cub was paired with a puppy companion at a zoo to help with its anxiety. The unlikely friendship helped the cheetah thrive — sometimes help comes from unexpected places.", "cheetah"),
    ("The cheetah doesn't catch its prey every time, but it never stops trying. Persistence is more powerful than perfection.", "cheetah"),
    # Cow
    ("Cows have best friends and get stressed when separated from them. It reminds us how important our closest relationships are.", "cow"),
    ("A rescued dairy cow was brought to a sanctuary where she could live freely for the first time. She spent her first day running through green fields with pure joy.", "cow"),
    ("Cows have been observed mourning their companions, showing that deep bonds exist throughout the animal kingdom. Never underestimate the power of connection.", "cow"),
    # Dog
    ("Hachiko, the loyal dog, waited at the train station for his owner every day for nearly 10 years after his owner passed away. His loyalty reminds us of the power of unconditional love.", "dog"),
    ("A three-legged rescue dog learned to run, play, and live joyfully despite its disability. It reminds us that our limitations don't define us.", "dog"),
    ("A therapy dog visits hospital patients every week, bringing smiles and comfort. Sometimes a gentle presence is the most healing gift you can offer.", "dog"),
    # Dolphin
    ("Dolphins have been known to save humans from shark attacks by forming a protective circle around them. True courage is protecting others, even at risk to yourself.", "dolphin"),
    ("Dolphins sleep with one eye open, always looking out for their pod. Being there for your loved ones doesn't mean you can't rest.", "dolphin"),
    ("A stranded dolphin was guided back to the ocean by a group of beachgoers. Sometimes all you need is a little help from kind strangers.", "dolphin"),
    # Elephant
    ("Elephants never forget their loved ones. They have been seen mourning and even returning to the bones of their fallen family members. Love endures beyond all things.", "elephant"),
    ("A baby elephant that fell into a well was rescued by villagers who spent hours carefully lifting it out. The whole herd waited nearby and trumpeted with joy when the calf was safe.", "elephant"),
    ("Elephants walk long distances to find water, and when they do, they share it with the whole herd. Generosity in tough times is true strength.", "elephant"),
    # Lamb
    ("A little lamb rejected by its mother was hand-raised by a farmer. It grew up healthy and became the friendliest animal on the farm, greeting every visitor with joy.", "lamb"),
    ("Lambs bounce and leap when they're happy — it's called 'pronking.' Never be afraid to show your joy, even if it looks silly.", "lamb"),
    ("A lamb born during a snowstorm was kept warm by the farmer through the night. Small acts of care can save a life.", "lamb"),
    # Octopus
    ("An octopus can squeeze through the tiniest spaces, reminding us that flexibility and adaptability are superpowers in life.", "octopus"),
    ("A mother octopus guards her eggs for months without eating, sacrificing everything for the next generation. Selfless love is the most powerful force in nature.", "octopus"),
    ("Octopuses have three hearts and blue blood. Being different doesn't make you strange — it makes you extraordinary.", "octopus"),
    # Otter
    ("Sea otters hold hands while they sleep so they don't drift apart. It reminds us to hold onto the people who matter most.", "otter"),
    ("An orphaned otter pup was adopted by a surrogate mother at an aquarium. With patience and love, it learned to swim, float, and thrive. Family is whoever loves you.", "otter"),
    ("Otters wrap themselves in kelp to stay anchored while they rest. Find your anchor — the things that keep you grounded when life gets choppy.", "otter"),
    # Penguin
    ("Emperor penguins huddle together in freezing storms to keep each other warm. Community and togetherness can help us survive the coldest times.", "penguin"),
    ("A penguin named Grape-kun fell in love with a cardboard cutout at a zoo and stayed loyal to it. It reminds us that love is love, no matter how unusual.", "penguin"),
    ("Penguin parents take turns caring for their eggs in the harshest conditions on Earth. Dedication and teamwork make the impossible possible.", "penguin"),
    # Rat
    ("Rats have been shown to free trapped companions, even when offered chocolate instead. They choose friendship over treats, reminding us of the value of loyalty.", "rat"),
    ("Rats giggle when tickled! Finding joy in small moments is something even the tiniest creatures understand.", "rat"),
    ("Trained rats have detected landmines in war zones, saving countless human lives. Even the smallest among us can make the biggest difference.", "rat"),
    # Squirrel
    ("Squirrels plant thousands of trees every year by forgetting where they buried their acorns. Sometimes our forgetfulness leads to something beautiful growing.", "squirrel"),
    ("A squirrel prepares for winter by gathering food all autumn long. Planning ahead and working steadily makes even the harshest seasons survivable.", "squirrel"),
    ("A baby squirrel fell from a tree and was nursed back to health by a kind family. When released, it visited them every day for years. Kindness creates bonds that last.", "squirrel"),
    # Tiger
    ("A tiger walks alone through the jungle with quiet confidence. You don't need a crowd to be powerful — your strength comes from within.", "tiger"),
    ("A tigress adopted a litter of orphaned cubs alongside her own, raising them all with equal care. Compassion has no limits.", "tiger"),
    ("Tigers can swim for miles across rivers. When life throws deep water at you, remember — you were built to handle it.", "tiger"),
]


def seed_database(db_path):
    """Seed the database with initial data if tables are empty."""
    with sqlite3.connect(db_path) as con:
        cursor = con.cursor()

        cursor.execute("SELECT COUNT(*) FROM motivational_quotes")
        if cursor.fetchone()[0] == 0:
            cursor.executemany(
                "INSERT INTO motivational_quotes (text, category) VALUES (?, ?)",
                MOTIVATIONAL_QUOTES
            )

        cursor.execute("SELECT COUNT(*) FROM animal_inspirations")
        if cursor.fetchone()[0] == 0:
            cursor.executemany(
                "INSERT INTO animal_inspirations (story, animal_type) VALUES (?, ?)",
                ANIMAL_INSPIRATIONS
            )

        con.commit()
