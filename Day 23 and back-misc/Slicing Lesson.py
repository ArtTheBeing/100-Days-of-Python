#Slicing Lesson

piano_keys = ["a","b","c","d","e","f","g","h"]
end = len(piano_keys) - 1

print(piano_keys[0::2])
print(piano_keys[:])
print(piano_keys[end:1:-1])
print(piano_keys[-1:2:-1])