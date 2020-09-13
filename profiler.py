# Profiling de tempo
import cProfile
import pstats
import io
import main

pr = cProfile.Profile()
pr.enable()

my_result = main.main()

pr.disable()
s = io.StringIO()
ps = pstats.Stats(pr, stream=s).sort_stats('tottime')
ps.print_stats()

with open('profile.txt', 'w+') as f:
    f.write(s.getvalue())

# # Profiling de memória
# from guppy import hpy
# h = hpy()
# my_result = h.heap()
# with open('profileMem.txt', 'w+') as f:
#     print(my_result, file=f)

# from memory_profiler import profile
# @profile
# def memoryMain():
#     main.main()

# if __name__ == '__main__':
#     memoryMain()