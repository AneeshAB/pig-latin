vowels = ['a', 'e', 'i', 'o', 'u']

# Main function
def main():
    # Get user input
    str_input = raw_input('Enter a string: ')

    # Modify string as necessary
    append = ''
    for c in str_input:
        if c in vowels:
            break
        append += c
    append += 'ay'
    str_output = str_input[(len(append) - 2):] + append

    # Print output
    print(str_output)

if __name__ == '__main__':
    main()