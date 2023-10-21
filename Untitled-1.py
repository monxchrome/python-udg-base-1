def task1(num):
    arr = []
    for i in str(num):
        arr.append(int(i))
        if arr[0] * arr[-1] > sum(arr[1:-1]):
            return arr[0] * arr[-1]
        else:
            return sum(arr[1:-1])

print(task1(45356))

def task2(bcrypt):
    result = []
    for i in bcrypt:
        if i.isalpha():
            if i.isupper():
                result.append(i.lower())
            elif i.islower() :
                result.append(i.upper())
        if i.isdigit():
            result.append(i)
        else:
            continue
    string = ''.join(result)

    return string

print(task2("hj87VHj9^26gbhnUJ72'"))

def task3(arr):
    counter = 0

    for i in arr:
        if i < 0:
            counter += 1
        else:
            continue
    return counter

print(task3([1, 2, -1, 3, -3]))

def task4():
    i_country = input()
    min_num = None
    min_country = None

    with open("task4.txt", "r") as file:
        for line in file:
            part = line.strip().split(',')
        if len(part) == 3:
            country, city, num_min = part

            if country == i_country:
                num_min == min_num
                min_country = city
    
    if min_country is not None:
        print(f"{i_country} - {min_country}")
    else:
        print(f"put file {i_country}")
            

task4()

channel_arr = ['tetete']
class Tv:
    def __init__(self, num, name, channels, volume) -> None:
        self.num = num
        self.name = name
        self.channels = channels
        self.volume = volume
        pass

    def add_channel(self):
        c_name = input()
        channel_arr.append(c_name)
        return f"channel {c_name} has been added"
    
    def boost_tone(self):
        tone = self.volume
        if self:
            tone += 1
        return f"your tone is {tone}"
    
    def channel_name(self):
        for i in channel_arr:
            if i == self.name:
                return f"channel name is {self.name}"
            else:
                print("YOC: invalid index")

tv1 = Tv(1, 'tetete', 1, 10)
print(tv1.add_channel())
print(tv1.boost_tone())
print(tv1.channel_name())