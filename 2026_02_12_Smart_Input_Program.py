# Smart Input Program
name = input("Enter your name: ")
age = int(input("Enter your age: "))
hobby = input("Enter your hobby: ")

if age < 18:
    age_group = "Teenager"
elif age < 60:
    age_group = "Adult"
else:
    age_group = "Senior"

print(f"Hello {name}! You are a {age_group} and enjoy {hobby}.")