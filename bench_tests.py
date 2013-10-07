import unittest
import timeit
from custom_dictionary import CustomDictionary


class BenchTests(unittest.TestCase):
    min_keys = 2 * 1000 * 100
    max_keys = 10 * 1000 * 100
    step = 2 * 1000 * 100
    repeat_time = 10 # repeat time to get average value

    isForFirstTime = False

    def setUp(self):
        if not self.isForFirstTime:
            self.setupClass()
            self.__class__.isForFirstTime = True

    def setupClass(self):
        self.delete_file_content("output")

    def test_sequential_insert(self):

        current_step = self.min_keys

        while current_step <= self.max_keys:
            setup_statement = "from custom_dictionary import CustomDictionary; l = [(str(x), x) for x in range(%d)]; d = {}; cd = CustomDictionary()" % current_step

            t = timeit.Timer("""
            for s, i in l:
                d[s] = i
            """, setup_statement)

            t2 = timeit.Timer("""
            for s, i in l:
                cd[s] = i
            """, setup_statement)

            tm1 = t.timeit(number=self.repeat_time)
            tm2 = t2.timeit(number=self.repeat_time)

            self.write_to_output("sequential classy", (current_step, tm1))
            self.write_to_output("sequential custom", (current_step, tm2))

            current_step += self.step

    def test_delete(self):
        current_step = self.min_keys
        while current_step <= self.max_keys:
            setup_statement = """from bench_tests import fill_dictionary;from bench_tests import fill_custom;rang=%d; d = fill_dictionary(rang);l = range(rang);cd=fill_custom(rang)""" % current_step

            t = timeit.Timer("""
            for i in l:
                d.pop(str(i), "default")
            """, setup_statement)

            t2 = timeit.Timer("""
            for i in l:
                cd.pop(str(i), "default")
            """, setup_statement)

            tm1 = t.timeit(number=self.repeat_time)
            tm2 = t2.timeit(number=self.repeat_time)

            self.write_to_output("delete classy", (current_step, tm1))
            self.write_to_output("delete custom", (current_step, tm2))

            current_step += self.step

    def test_random_insert(self):
        current_step = self.min_keys

        while current_step <= self.max_keys:
            setup_statement = "import random;from custom_dictionary import CustomDictionary; l = [(str(x), x) for x in range(%d)]; d = {}; cd = CustomDictionary();" % current_step

            t = timeit.Timer("""
            for s, i in l:
                d[str(random.randint(0, %d))] = i
            """ % current_step, setup_statement)

            t2 = timeit.Timer("""
            for s, i in l:
                cd[str(random.randint(0, %d))] = i
            """ % current_step, setup_statement)

            tm1 = t.timeit(number=self.repeat_time)
            tm2 = t2.timeit(number=self.repeat_time)

            self.write_to_output("random classy", (current_step, tm1))
            self.write_to_output("random custom", (current_step, tm2))

            current_step += self.step

    def write_to_output(self, description, data):
        outfile = open('output', 'a')
        print >> outfile, description, data
        outfile.close()

    def delete_file_content(self, fName):
        with open(fName, "w"):
            pass

#timeit import methods
def fill_dictionary(rang):
    d = {}
    for i in range(rang):
        d[str(i)] = i
    return d


def fill_custom(rang):
    cd = CustomDictionary()
    for i in range(rang):
        cd[str(i)] = i
    return cd