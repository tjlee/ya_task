import matplotlib.pyplot as plt
from ast import literal_eval
import os

#read file data
lines = []
with open("output", "r") as f:
    lines = f.readlines()

delete_classy_delimiter = "delete classy"
delete_custom_delimiter = "delete custom"
seq_classy_delimiter = "sequential classy"
seq_custom_delimiter = "sequential custom"
rand_classy_delimiter = "random classy"
rand_custom_delimiter = "random custom"

classy_delete_data = map(lambda x: literal_eval(x),
                         map(lambda x: x.strip(delete_classy_delimiter),
                             filter(lambda x: delete_classy_delimiter in x, lines)))
custom_delete_data = map(lambda x: literal_eval(x),
                         map(lambda x: x.strip(delete_custom_delimiter),
                             filter(lambda x: delete_custom_delimiter in x, lines)))
classy_seq_data = map(lambda x: literal_eval(x),
                      map(lambda x: x.strip(seq_classy_delimiter),
                          filter(lambda x: seq_classy_delimiter in x, lines)))
custom_seq_data = map(lambda x: literal_eval(x),
                      map(lambda x: x.strip(seq_custom_delimiter),
                          filter(lambda x: seq_custom_delimiter in x, lines)))
classy_rand_data = map(lambda x: literal_eval(x),
                       map(lambda x: x.strip(rand_classy_delimiter),
                           filter(lambda x: rand_classy_delimiter in x, lines)))
custom_rand_data = map(lambda x: literal_eval(x),
                       map(lambda x: x.strip(rand_custom_delimiter),
                           filter(lambda x: rand_custom_delimiter in x, lines)))


def make_lists(data):
    a, b = [], []
    for x, y in data:
        a.append(x)
        b.append(y)
    return a, b


def save_plot(path, ext='png', close=True):
    directory = os.path.split(path)[0]
    filename = "%s.%s" % (os.path.split(path)[1], ext)
    if directory == '':
        directory = '.'

    if not os.path.exists(directory):
        os.makedirs(directory)

    save_path = os.path.join(directory, filename)

    plt.savefig(save_path)

    if close:
        plt.close()


def build_and_save_plot(title, file_name, classy_data, custom_data):
    classy_x, classy_y = make_lists(classy_data)
    custom_x, custom_y = make_lists(custom_data)
    plt.ylabel('Time, sec')
    plt.xlabel('Number of entities in hash table')
    plt.title(title)
    plt.plot(classy_x, classy_y)
    plt.plot(custom_x, custom_y)
    plt.legend(('Python dictionary', 'Custom dictionary with "super_fast_hash"'))

    save_plot(file_name)


build_and_save_plot("Delete from hash table", "delete", classy_delete_data, custom_delete_data)
build_and_save_plot("Sequential insert to hash table", "seq", classy_seq_data, custom_seq_data)
build_and_save_plot("Random insert to hash table", "random", classy_rand_data, custom_rand_data)