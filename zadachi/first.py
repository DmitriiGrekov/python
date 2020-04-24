


def search_dublicat(example_list):
    return (len(set(example_list)))  != len(example_list)


example_list = [1,3,5,1]
print(search_dublicat(example_list))
