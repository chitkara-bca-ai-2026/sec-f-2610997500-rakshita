print("=" * 35)
print("       TEXT PROCESSING TOOL")
print("=" * 35)

sentence = input("Enter a sentence: ")

print("\n--- Processing Results ---")

index = int(input("Enter position for indexing: "))
print("Character at position", index, ":", repr(sentence[index]))

start = int(input("Enter start index for slicing: "))
end = int(input("Enter end index for slicing: "))
print("Sliced string [0:5]   :", repr(sentence[start:end]))

print("Uppercase              :", sentence.upper())
print("Lowercase              :", sentence.lower())

old_word = input("Enter word to replace   : ")
new_word = input("Enter replacement word  : ")

updated_sentence = sentence.replace(old_word, new_word)
print("After replace           :", updated_sentence)

print("Length of sentence      :", len(sentence))

print("\n" + "=" * 35)
print("Analysis Complete!")
print("=" * 35)