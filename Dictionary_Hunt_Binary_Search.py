words = ["Apple", "Ball", "Cat", "Dog", "Elephant", "Ephemeral", "Fish"]

search = "Ephemeral"

low = 0
high = len(words) - 1

while low <= high:
    mid = (low + high) // 2

    if words[mid] == search:
        print("Word Found")
        break

    elif search > words[mid]:
        low = mid + 1

    else:
        high = mid - 1

if low > high:
    print("Word Not Found")
