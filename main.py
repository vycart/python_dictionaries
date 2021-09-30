from dis import dis
from timeit import timeit


if __name__ == '__main__':
    my_first_dict = {}
    print(my_first_dict)
    print(type(my_first_dict))

    my_second_dict = dict()
    print(my_second_dict)
    print(type(my_second_dict))

    # Creating empty dictionaries
    dis("{}")
    print("")
    dis("dict()")
    print("")

    # Creating dictionaries with one key:value pair
    dis("{\"One\":1}")
    print("")
    dis("dict(One=1)")
    print("")

    # Measuring how long does it take to create dictionaries in different ways
    print(timeit("{}", number=10**7))
    print(timeit("dict()", number=10**7))

    # Can pass Lists to dict constructor
    sample_list = [["One", 1], ["Four", 4], ["Six", 6]]
    my_dict_v1 = dict(sample_list)
    print(my_dict_v1)

    # The approach above is the same as
    my_dict_v2 = {}
    for key, value in sample_list:
        my_dict_v2[key] = value

    print(my_dict_v2)

    # Dictionary comprehension
    my_dict_v3 = {key: value for (key, value) in sample_list}
    print(my_dict_v3)

    # Creating dict using keyword arguments
    kwargs_dict = dict(position=4, name="Peter", Color="Blue", id=25663)
    print(kwargs_dict)
    print(type(kwargs_dict))

    # Dictionary methods
    example_dict = dict(position=4, name="Peter", Color="Blue", id=25663)
    print(example_dict)

    # keys()
    print(example_dict.keys())

    for key in example_dict.keys():
        print(f"key:{key}, value:{example_dict[key]}")

    # items()
    example_dict_v1 = {"Ticket-1": 8, "Ticket-2": 20, "Ticket-3": 36}
    print(example_dict_v1.values())

    for value in example_dict_v1.values():
        print(f"Hours spent:{value}")

    # get()
    # Uncomment line 70 and comment line 71 to see that accessing dictionary value by [] with a key
    # that is not present in a dictionary causes an exception
    # hours_on_issue = example_dict_v1["Ticket-6"]
    hours_on_issue = example_dict_v1.get("Ticket-6")
    print(hours_on_issue)

    # update()
    example_dict_v1.update({"Ticket-13": 48})
    example_dict_v1.update(Ticket16=28)
    print(example_dict_v1)

    # copy() and pop()
    example_dict_v1_copy = example_dict_v1
    print(hex(id(example_dict_v1)))
    print(hex(id(example_dict_v1_copy)))
    example_dict_v1_copy.pop("Ticket-13")
    print(example_dict_v1)
    print(example_dict_v1_copy)

    example_dict_v1_true_copy = example_dict_v1.copy()
    print(hex(id(example_dict_v1)))
    print(hex(id(example_dict_v1_true_copy)))
    example_dict_v1_true_copy.pop("Ticket-1")
    print(example_dict_v1)
    print(example_dict_v1_true_copy)

    help(dict)