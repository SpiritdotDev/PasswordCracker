import hashlib


#This allows for pseudo rainbow table operations, essentially a dictionary attack with hashes instead of plaintext
def generate_lookup_table(file_path, hash_algo="sha-256"):

    with open(file_path, 'r', encoding='latin-1') as file:
        for line in file:
            word = line.strip()

            # Create a hash object
            h = hashlib.new(hash_algo)
            # Update the hash object with the bytes of the word
            h.update(word.encode("utf-8"))
            # Get the hexadecimal representation of the hash
            hash_val = h.hexdigest()

            # Creates a new file holding the hashed values of the dictionary file
            with open("rainbowtable.txt", 'w', encoding="utf-8") as lookup:
                lookup.write(f"{hash_val}: {word}")

def RainbowTable(password, hash_algo="sha-256"):

    #turn the password into a hash
    h = hashlib.new(hash_algo)
    h.update(password.encode("utf-8"))
    hashed_password = h.hexdigest()


                

