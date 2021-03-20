
 def getInput():
    input_file = []
    with open('/Users/ASUS/Desktop/goodie/sample_input.txt') as f:
        line = f.readline()
        while line:
            if(line == '\n'):
                line  = f.readline()
                continue
            input_file.append(line)
            line  = f.readline()
    return input_file

def getItems(input_):
    items = {} 
    for line in input_[2:]:
        item = line.split(':')
        #print(item)
        items[item[0]] = int(item[1])
    return items

def getSortedItems(items):
    sorted_tuples = sorted(items.items(), key=lambda item: item[1])
    sorted_dict = {k: v for k, v in sorted_tuples}
    return sorted_dict
   
def getminDiff(values):
    i, j = 0, n-1
    min_value = 9223372036854775807
    min_index = -1
    size = len(values)

    while j < size:
        diff = values[j] - values[i]
        #print(values[j], values[i], diff)
        if(diff < min_value):
            min_value = diff
            min_index = i
        i += 1
        j += 1
    return [min_index,min_value]

def writeOutput(sorted_items, min_index, min_value):
    with open('/Users/ASUS/Desktop/goodie/sample_output.txt', 'w') as f:
        f.write('Here the goodies that are selected for distribution are:\n\n')
        for i, (k, v) in enumerate(sorted_items.items()):
            if(i >= min_index and i <= (min_index+n-1)):
                line  = k + ': ' + str(v) + '\n'
                f.write(line)
        f.write('\nAnd the difference between the chosen goodie with highest price and the lowest price is' + str(min_value))


if __name__ == '__main__':
    input_ = getInput()
    items = getItems(input_)
    n = int(input_[0].split(':')[-1])

    sorted_items = getSortedItems(items)
    values = list(sorted_items.values())
    min_index,min_value = getminDiff(values)
    writeOutput(sorted_items, min_index,min_value)



