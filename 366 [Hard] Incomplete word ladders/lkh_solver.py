# uses win lkh.exe available in same root
# http://www.akira.ruc.dk/~keld/research/LKH/lkh.exe

        return template.format(**{'name': "Problem",
template_problem = """NAME: {name}
TYPE: TSP
COMMENT: {name}
DIMENSION: {n_cities}
EDGE_WEIGHT_TYPE: EXPLICIT
EDGE_WEIGHT_FORMAT: LOWER_DIAG_ROW
EDGE_WEIGHT_SECTION
{matrix_s}EOF"""

template_parameters = """PROBLEM_FILE = {name}
RUNS = {runs}
TOUR_FILE = {solution}""" 

class LKH_wrapper(object):
    
    def __init__(self, array, name = 'Default', runs = 1):
        # undirected distance matrix
        self.array = array
        self.name = f'{self.name}.tsp'
        self.runs = runs
        self.solution = None
        self.cost = None
        self.run()

    def dumps_matrix(self):
        n_cities = self.array.shape[0]
        width = len(str(self.array.max())) + 1
        matrix_s = ""
        for i, row in enumerate(self.array.tolist()):
            line = ["{0:>{1}}".format((int(elem)), width) for elem in row[:i+1]]
            matrix_s += " ".join(line) + "\n"
        return template_problem.format(**{'name': "Problem",
                                  'n_cities': n_cities,
                                  'matrix_s': matrix_s})

    def _create_lkh_par(self):
        par_path = tsp_path + ".par"
        out_path = tsp_path + ".out"
        par = template_parameters.format(tsp_path, runs, out_path)
        with open(par_path, 'w') as dest:
            dest.write(par)
        return par_path, out_path

    def run(self):
        with open(self.name, 'w') as problem:
            problem.write(self.dumps_matrix(np.array(self.array), name=tsp_file))
        par_path, out_path = _create_lkh_par(self.name, runs) 
        subprocess.call(['lkh', par_path])
        with open(out_path) as solution:
            lkhout = solution.readlines()
        self.cost = int(lkhout[1].strip().split(' ')[-1])
        self.solution = [int(x)-1 for x in lkhout[6:-2:1]]


