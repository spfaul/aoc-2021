"""
See: https://adventofcode.com/2021/day/8
why is the question this long - its only day 8.
"""

def parse_input():
    data = []
    with open('input/8.txt', 'r') as file:
        lines = file.read().split('\n')
        for line in lines:
            digits, output = line.split('|')

            digits = digits.split(' ')
            digits = digits[:len(digits)-1] # slice off empty data
            output = output.split(' ')
            output = output[1:len(output)] # slice off empty data
            
            data.append( (digits, output) )
            
    return data

def part1() -> int:
    data = parse_input()
    count: int = 0
    
    for digits, output in data:
        for num in output:
            if len(num) in [2, 4, 3, 7]: # num of segments displayed to show digits [1, 4, 7, 8]
                count += 1   
    return count

def part2() -> int:
    def count_shared_chars(s_a, s_b):
        count = 0
        for char in s_a:
            count += s_b.count(char)
        return count

    data = parse_input()
    count = 0

    for digits, output in data:
        sorted_digits = {} # in a key-value pair X:Y, X is the sorted string representation of digit segments for digit Y
        unique_seg_to_dig = {2: 1, 4: 4, 3: 7, 7: 8} # we can identify these digits because they have unique repr lengths

        for d_repr in digits.copy():
            if len(d_repr) in unique_seg_to_dig.keys():
                corr_digit = unique_seg_to_dig[len(d_repr)]
                sorted_digits[corr_digit] = "".join(sorted(d_repr)) # store the str repr in a sorted way so it doesnt matter if the output is scrambled
                
                digits.remove(d_repr) # prevent unnecessary reiterations

        # now we can use the 4 digits we found to find the others
        for d_repr in digits:
            if len(d_repr) == 5: # either 2, 3, 5
                if count_shared_chars(d_repr, sorted_digits[1]) == 2:
                    corr_digit = 3
                elif count_shared_chars(d_repr, sorted_digits[4]) == 3:
                    corr_digit = 5
                else:
                    corr_digit = 2
            else: # either 0, 6, 9
                if count_shared_chars(d_repr, sorted_digits[1]) == 1:
                    corr_digit = 6
                elif count_shared_chars(d_repr, sorted_digits[4]) == 4:
                    corr_digit = 9
                else:
                    corr_digit = 0
            sorted_digits[corr_digit] = "".join(sorted(d_repr)) # store the str repr in a sorted way so it doesnt matter if the output is scrambled

        # find and add the output value using our sorted digit hashmap
        for idx, d in enumerate(output):
            sorted_d = "".join(sorted(d)) # sort output digits
            # my choice of data structures always come back to haunt me.
            # THE VARIABLE NAMES ARE LALKIUAYSDGFLAKSJHDFGAKSLDHFJLKASHJDFSADFLKJSAD
            for digit, digit_repr in sorted_digits.items():
                if sorted_d == digit_repr:
                    count += digit * (10 ** (3-idx))
                
    return count
    
if __name__ == '__main__':
    print(part2())