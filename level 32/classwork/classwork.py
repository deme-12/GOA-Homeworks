# Sentence Smash
# Write a function that takes an array of words and smashes them together into a sentence and returns the sentence. You can ignore any need to sanitize words or add punctuation, but you should add spaces between each word. Be careful, there shouldn't be a space at the beginning or the end of the sentence!

def smash(words):
    return " ".join(words)
    
# Find Maximum and Minimum Values of a List

def minimum(arr):
    min = arr[0]
    for num in arr:
        if num < min:
            min = num
    return min

def maximum(arr):
    max = arr[0]
    for num in arr:
        if num > max:
            max = num
    return max


# Reversed sequence

def reverse_seq(n):
    result = []
    for i in range(1,n+1):
        result.append(i)
    return result[::-1]


