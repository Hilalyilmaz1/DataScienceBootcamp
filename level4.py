#level4
def control(arr):
    if len(arr)!=len(set(arr)):
        return "array repeats."
    else:
        return "array doesnt repeat."
arr=[23,56,76,44,23]
print(control(arr))    