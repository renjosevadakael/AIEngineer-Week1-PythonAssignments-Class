from sklearn.preprocessing import LabelEncoder

# Create a LabelEncoder instance
le = LabelEncoder()

# Fit the encoder with a list of labels
le.fit(["Red", "Blue", "Green", "Yellow"])

# Blue - 0, Green - 1, Red - 2, Yellow - 3

# Transform the labels into numerical values
encoded_labels = le.transform(["Red", "Yellow", "Green"])
print(encoded_labels)  # Output: array([2,3,1])

# Inverse transform to get the original labels back
original_labels = le.inverse_transform([3, 0, 2])
print(original_labels)  # Output: ['Yellow' 'Blue' 'Red']

print("\n--- Using fit_transform (Combined approach) ---")
# Create a new LabelEncoder instance
le2 = LabelEncoder()

# Fit and transform in one step with the same data
encoded_colors = le2.fit_transform(["Red", "Blue", "Green", "Yellow"])
print(f"Encoded colors: {encoded_colors}")  # Output: [2 0 1 3]

# Now transform new data using the already fitted encoder
new_encoded = le2.transform(["Green", "Red", "Blue"])
print(f"New encoded values: {new_encoded}")  # Output: [1 2 0]

# Inverse transform
decoded_colors = le2.inverse_transform([2, 3, 1])
print(f"Decoded colors: {decoded_colors}")  # Output: ['Red' 'Yellow' 'Green']