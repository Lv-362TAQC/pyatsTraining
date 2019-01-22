from pyats.aetest import Testcase, test, loop, main


@loop(a=[1, 2, 3])
class Test1(Testcase):

    @test.loop(b=['a', 'b', 'c'])
    def only_parameters(self, a, b):
        print(a, b)
        pass


class Uids(Testcase):

    @test.loop(uids=['l1', 'l2'],
               a=[1, 2, 3])
    def less_uids(self, a):
        print(a)

    @test.loop(uids=['e1', 'e2', 'e3'],
               a=[1, 2, 3])
    def equal_uids(self, a):
        print(a)

    @test.loop(uids=['m1', 'm2', 'm3', 'm4'],
               a=[1, 2, 3])
    def more_uids(self, a):
        print(a)


class Definitions(Testcase):

    @test.loop(a=[1, 2, 3],
               b=['a', 'b', 'c'])
    def per_parameter(self, a, b):
        print(a, b)
        pass

    @test.loop(args=['a33', 'b33'],
               argvs=[(1, 'a'), (2, 'b'), (3, 'c')])
    def groups(self, a33, b33):
        print(a33, b33)


if __name__ == '__main__':
    main()
