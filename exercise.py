emotions_dict = {'happy': 3, 'joy': 2, 'angry': 1}

class Person:
    def __init__(self, name, emotions):
        self.name = name
        self.emotions = emotions
    
    def __str__ (self):
        return "{} is {}.".format(self.name, self.emotions)

    def my_feeling(self):
        emotions_dict.update({'happy': "high", "joy": "medium", "angry": "low"})
        for emotion, stats in self.emotions.items():
            print("I am feeling a {} amount of {}.".format(stats, emotion))

judoboy = Person('Alex', emotions_dict)
print(judoboy)
print(judoboy.my_feeling())